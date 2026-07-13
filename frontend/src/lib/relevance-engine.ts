/**
 * DealSignal AI — Relevance Engine
 *
 * Scores signals against a user's relevance profile (companies, themes, assumptions, thesis).
 * Returns relevance score, thesis impact, and reasons.
 */

import type { Signal, AnalystBrief } from "./types";

// ── Types ──────────────────────────────────────────────────────────────

export interface TrackedAssumption {
  company_ticker: string;
  assumption: string;
  importance: "low" | "medium" | "high";
}

export interface RelevanceProfile {
  tracked_companies: string[];
  tracked_themes: string[];
  tracked_assumptions: TrackedAssumption[];
  thesis_by_company: Record<string, string>;
}

export interface RelevanceResult {
  relevance_score: number;
  relevance_level: "low" | "medium" | "high" | "critical";
  relevance_reasons: string[];
  matched_companies: string[];
  matched_assumptions: string[];
  matched_themes: string[];
}

export type ThesisImpact = "supports" | "weakens" | "neutral" | "watch";

export interface ThesisImpactResult {
  thesis_impact: ThesisImpact;
  thesis_impact_reason: string;
}

// ── Default demo profile ───────────────────────────────────────────────

export const DEMO_PROFILE: RelevanceProfile = {
  tracked_companies: ["NVDA", "AAPL", "JPM"],
  tracked_themes: ["AI infrastructure", "regulation", "China exposure", "interest rates"],
  tracked_assumptions: [
    { company_ticker: "NVDA", assumption: "data center revenue growth", importance: "high" },
    { company_ticker: "NVDA", assumption: "gross margin", importance: "high" },
    { company_ticker: "AAPL", assumption: "App Store take-rate", importance: "high" },
    { company_ticker: "JPM", assumption: "net interest income", importance: "high" },
    { company_ticker: "JPM", assumption: "provision expense", importance: "medium" },
  ],
  thesis_by_company: {
    NVDA: "Data center revenue growth remains strong, gross margins stay elevated, and China restrictions remain manageable.",
    AAPL: "Services revenue remains resilient, and regulatory pressure does not materially damage App Store economics.",
    JPM: "Net interest income remains strong while credit losses stay manageable.",
  },
};

// ── Theme-to-keyword mappings ──────────────────────────────────────────

const THEME_KEYWORDS: Record<string, string[]> = {
  "AI infrastructure": ["ai", "gpu", "data center", "chip", "inference", "training", "blackwell", "hopper", "cuda", "h200", "b200"],
  regulation: ["regulation", "regulatory", "dma", "basel", "fca", "fed", "export control", "bis", "compliance", "capital requirement", "gsib"],
  "China exposure": ["china", "beijing", "huawei", "export", "sanction", "restriction", "secondary sanction", "biren"],
  "interest rates": ["interest rate", "fed", "fomc", "rate cut", "rate hike", "nii", "net interest", "yield", "monetary"],
  "cybersecurity": ["breach", "outage", "incident", "exploit", "vulnerability", "ransomware", "endpoint"],
  payments: ["payment", "take-rate", "transaction", "processing", "checkout", "acquiring"],
  enterprise: ["saas", "arr", "subscription", "seat", "renewal", "retention", "churn", "crm", "agent"],
  "consumer tech": ["iphone", "ios", "app store", "services", "wearables", "mac", "adoption"],
};

// ── Scoring ────────────────────────────────────────────────────────────

export function scoreRelevance(
  signal: Signal,
  profile: RelevanceProfile,
  brief?: Pick<AnalystBrief, "model_assumptions" | "what_happened" | "why_it_matters">
): RelevanceResult {
  const reasons: string[] = [];
  const matchedCompanies: string[] = [];
  const matchedAssumptions: string[] = [];
  const matchedThemes: string[] = [];
  let score = 0;

  // 1. Company match (+30)
  if (profile.tracked_companies.includes(signal.ticker)) {
    score += 30;
    matchedCompanies.push(signal.ticker);
    reasons.push(`Tracked company: $${signal.ticker}`);
  }

  // 2. Assumption match (+20 per match, max 2)
  const signalText = [signal.title, signal.summary, signal.tags?.join(" ") ?? ""].join(" ").toLowerCase();
  const briefText = brief ? [brief.what_happened ?? "", brief.why_it_matters ?? ""].join(" ").toLowerCase() : "";

  for (const ta of profile.tracked_assumptions) {
    if (ta.company_ticker !== signal.ticker) continue;
    const kw = ta.assumption.toLowerCase();
    const kwWords = kw.split(/\s+/);
    const relevance = matchScore(signalText + " " + briefText, kwWords);
    if (relevance > 0.5) {
      score += 20;
      matchedAssumptions.push(ta.assumption);
      reasons.push(`Affects tracked assumption: ${ta.assumption}`);
    }
    if (matchedAssumptions.length >= 2) break;
  }

  // 3. Theme match (+15 per match, max 2)
  for (const theme of profile.tracked_themes) {
    const keywords = THEME_KEYWORDS[theme] || [theme.toLowerCase()];
    const relevance = matchScore(signalText, keywords);
    if (relevance > 0.3) {
      score += 15;
      matchedThemes.push(theme);
      reasons.push(`Theme match: ${theme}`);
    }
    if (matchedThemes.length >= 2) break;
  }

  // 4. Severity bonus (+15 if high)
  if (signal.severity === "high") {
    score += 15;
    reasons.push("High-severity signal");
  }

  // 5. Evidence quality (+10 if historical_verified or strong source)
  if ((signal as any).evidence_class === "historical_verified") {
    score += 10;
    reasons.push("Historically verified source");
  }
  if ((signal as any).source_quality === "strong") {
    score += 10;
    reasons.push("Strong source quality");
  }

  // Cap at 100
  score = Math.min(score, 100);

  const level: RelevanceResult["relevance_level"] =
    score >= 80 ? "critical" :
    score >= 60 ? "high" :
    score >= 35 ? "medium" : "low";

  return {
    relevance_score: score,
    relevance_level: level,
    relevance_reasons: reasons,
    matched_companies: matchedCompanies,
    matched_assumptions: matchedAssumptions,
    matched_themes: matchedThemes,
  };
}

// ── Thesis Impact ──────────────────────────────────────────────────────

export function assessThesisImpact(
  signal: Signal,
  profile: RelevanceProfile,
  relevance: RelevanceResult,
  brief?: Pick<AnalystBrief, "model_assumptions" | "why_it_matters">
): ThesisImpactResult {
  const thesis = profile.thesis_by_company[signal.ticker];
  if (!thesis || !profile.tracked_companies.includes(signal.ticker)) {
    return { thesis_impact: "neutral", thesis_impact_reason: "Company is not tracked or thesis is not defined." };
  }

  const signalText = [signal.title, signal.summary, signal.category, brief?.why_it_matters ?? ""].join(" ").toLowerCase();
  const thesisLower = thesis.toLowerCase();

  // ── Threat detection (run BEFORE positive keyword matching) ────────
  const threatKeywords = [
    "competition", "competitive pressure", "custom chip", "in-house chip",
    "in-house silicon", "insourcing", "procurement shift", "replacement",
    "substitute", "pricing pressure", "margin pressure", "share loss",
    "reduced dependency", "customer concentration", "hyperscaler alternative",
    "demand risk", "reduce external", "procurement reduction", "displace",
  ];

  const threatScore = threatKeywords.reduce((s, kw) => s + (signalText.includes(kw) ? 1 : 0), 0);

  if (threatScore >= 1 && signal.severity === "high") {
    const matchedAssumption = relevance.matched_assumptions[0] || "";
    return {
      thesis_impact: "weakens",
      thesis_impact_reason: `Competitive or customer-insourcing pressure detected. ${matchedAssumption ? `May affect tracked assumption: ${matchedAssumption}.` : "May challenge thesis assumptions about market position or growth."}`,
    };
  }

  if (threatScore >= 1) {
    return {
      thesis_impact: "watch",
      thesis_impact_reason: "Competitive or insourcing signal detected. Impact on thesis is plausible but not yet confirmed by direct financial data.",
    };
  }

  // Keywords that suggest the signal weakens the thesis
  const weakenIndicators = [
    "restrict", "restriction", "sanction", "ban", "decline", "deceleration",
    "pressure", "compression", "loss", "provision", "breach", "outage", "crash",
    "probe", "investigation", "penalty", "fine", "forced", "mandate", "limit",
    "weakens", "threat", "risk", "headwind", "downside",
  ];

  // Keywords that suggest the signal supports the thesis
  const supportIndicators = [
    "record", "growth", "beat", "exceed", "expand", "expansion", "gains",
    "traction", "wins", "contract", "launch", "approval", "licence",
    "resilient", "strong", "accelerate", "upside", "momentum",
  ];

  const weakenScore = weakenIndicators.reduce((s, w) => s + (signalText.includes(w) ? 1 : 0), 0);
  const supportScore = supportIndicators.reduce((s, w) => s + (signalText.includes(w) ? 1 : 0), 0);

  // Check thesis mentions specific themes threatened by the signal
  if (thesisLower.includes("china") && signalText.includes("china")) {
    const chinaThreat = ["restrict", "sanction", "ban", "expire", "tight", "control"].some(w => signalText.includes(w));
    if (chinaThreat) {
      return {
        thesis_impact: "weakens",
        thesis_impact_reason: "Signal documents new restrictions on China access, conflicting with thesis assumption that restrictions remain manageable.",
      };
    }
  }

  if (thesisLower.includes("regulatory") || thesisLower.includes("regulation")) {
    const regThreat = ["mandate", "force", "fine", "penalty", "investigation", "probe"].some(w => signalText.includes(w));
    if (regThreat) {
      return {
        thesis_impact: "weakens",
        thesis_impact_reason: "Regulatory action may materially affect assumptions about regulatory resilience in thesis.",
      };
    }
    if (["regulation", "regulatory"].some(w => signal.category?.includes(w))) {
      return {
        thesis_impact: "watch",
        thesis_impact_reason: "Regulatory development requires monitoring but may not materially change thesis assumptions.",
      };
    }
  }

  if (thesisLower.includes("margin") && signalText.includes("margin")) {
    const marginThreat = ["pressur", "compress", "decline", "drop"].some(w => signalText.includes(w));
    if (marginThreat) {
      return { thesis_impact: "weakens", thesis_impact_reason: "Margin pressure conflicts with thesis assumption of stable or expanding margins." };
    }
    if (["growth", "expand", "record"].some(w => signalText.includes(w))) {
      return { thesis_impact: "supports", thesis_impact_reason: "Margin performance supports thesis assumptions." };
    }
  }

  if (thesisLower.includes("growth") || thesisLower.includes("revenue")) {
    const growthPos = ["record", "beat", "exceed", "expansion", "wins", "traction"].some(w => signalText.includes(w));
    if (growthPos) {
      return { thesis_impact: "supports", thesis_impact_reason: "Revenue growth trajectory supports thesis expectations." };
    }
    const growthNeg = ["deceleration", "decline", "drop", "below", "slow"].some(w => signalText.includes(w));
    if (growthNeg) {
      return { thesis_impact: "weakens", thesis_impact_reason: "Revenue deceleration conflicts with thesis growth assumptions." };
    }
  }

  if (thesisLower.includes("credit") || thesisLower.includes("loss")) {
    const creditNeg = ["provision", "increase", "write-off", "default"].some(w => signalText.includes(w));
    if (creditNeg) {
      return { thesis_impact: "weakens", thesis_impact_reason: "Increased credit provisions conflict with thesis assumption of manageable credit losses." };
    }
  }

  // Fall back to heuristic
  if (weakenScore > supportScore + 2) {
    return { thesis_impact: "weakens", thesis_impact_reason: "Multiple weakening indicators found in signal content." };
  }
  if (supportScore > weakenScore + 1) {
    return { thesis_impact: "supports", thesis_impact_reason: "Signal content aligns with thesis direction." };
  }

  return {
    thesis_impact: relevance.relevance_score >= 60 ? "watch" : "neutral",
    thesis_impact_reason: relevance.relevance_score >= 60
      ? "This signal is relevant to tracked assumptions and warrants monitoring."
      : "No strong alignment or conflict with thesis detected.",
  };
}

// ── Helpers ────────────────────────────────────────────────────────────

function matchScore(text: string, keywords: string[]): number {
  let hits = 0;
  for (const kw of keywords) {
    if (text.includes(kw)) hits++;
  }
  return keywords.length > 0 ? hits / keywords.length : 0;
}

/** Load profile from localStorage, fallback to demo */
export function loadProfile(): RelevanceProfile {
  if (typeof window === "undefined") return DEMO_PROFILE;
  try {
    const raw = localStorage.getItem("dealsignal_profile");
    if (raw) return JSON.parse(raw);
  } catch { /* ignore */ }
  return DEMO_PROFILE;
}

export function saveProfile(profile: RelevanceProfile): void {
  if (typeof window === "undefined") return;
  localStorage.setItem("dealsignal_profile", JSON.stringify(profile));
}

export interface Company {
  ticker: string;
  name: string;
  sector: string;
  industry: string;
  description: string;
  logo_url: string;
  founded: number | null;
  headquarters: string;
  employees: number | null;
  market_cap: string;
  signal_count: number;
}

export interface Signal {
  id: string;
  ticker: string;
  company_name: string;
  title: string;
  event_date: string;
  category: string;
  severity: "low" | "medium" | "high";
  confidence: number;
  confidence_rationale: string;
  source_name: string;
  source_url: string;
  source_type: string;
  source_status: string;
  source_note: string;
  source_depth: string;
  source_quality: string;
  evidence_class: string;
  summary: string;
  tags: string[];
}

export interface SignalFeed {
  signals: Signal[];
  total: number;
  page: number;
  page_size: number;
}

export interface FinancialArea {
  area: string;
  impact: string;
  detail: string;
}

export interface ModelAssumption {
  assumption: string;
  financial_area: string;
  possible_direction: string;
  timing: string;
  confidence: string;
  reasoning: string;
  evidence_gap: string;
}

export interface AnalystQuestion {
  question: string;
  urgency: string;
}

export interface AnalystBrief {
  signal: Signal;
  executive_summary: string;
  what_happened: string;
  why_it_matters: string;
  financial_areas: FinancialArea[];
  model_assumptions: ModelAssumption[];
  evidence: string;
  what_is_unknown: string;
  next_steps: string[];
  analyst_questions: AnalystQuestion[];
}

export interface CompanyDetail {
  company: Company;
  recent_signals: Signal[];
  category_breakdown: Record<string, number>;
  severity_breakdown: Record<string, number>;
}
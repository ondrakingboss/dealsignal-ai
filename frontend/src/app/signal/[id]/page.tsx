"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { motion } from "framer-motion";
import {
  ArrowLeft,
  ExternalLink,
  ShieldCheck,
  AlertTriangle,
  BarChart3,
  Lightbulb,
  ChevronRight,
  Target,
  FileText,
  TrendingUp,
  TrendingDown,
  Minus,
  HelpCircle,
} from "lucide-react";
import SeverityBadge, { CategoryBadge, ConfidenceBadge } from "@/components/severity-badge";
import type { AnalystBrief } from "@/lib/types";

const impactIcons: Record<string, React.ReactNode> = {
  positive: <TrendingUp className="w-3.5 h-3.5 text-green-400" />,
  negative: <TrendingDown className="w-3.5 h-3.5 text-red-400" />,
  neutral: <Minus className="w-3.5 h-3.5 text-zinc-500" />,
  uncertain: <HelpCircle className="w-3.5 h-3.5 text-yellow-400" />,
};

const magnitudeColors: Record<string, string> = {
  significant: "text-red-400 border-red-500/20 bg-red-500/10",
  moderate: "text-yellow-400 border-yellow-500/20 bg-yellow-500/10",
  minor: "text-blue-400 border-blue-500/20 bg-blue-500/10",
};

export default function SignalBriefPage() {
  const { id } = useParams<{ id: string }>();
  const [brief, setBrief] = useState<AnalystBrief | null>(null);
  const [loading, setLoading] = useState(true);
  const [notFound, setNotFound] = useState(false);

  useEffect(() => {
    if (!id) return;
    setLoading(true);
    fetch(`/api/brief/${id}`)
      .then((r) => {
        if (!r.ok) throw new Error("Not found");
        return r.json();
      })
      .then((d) => {
        setBrief(d);
        setLoading(false);
      })
      .catch(() => {
        setNotFound(true);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return (
      <div className="max-w-3xl mx-auto px-8 pt-12">
        <div className="animate-pulse space-y-4">
          <div className="h-6 bg-zinc-800 rounded w-32" />
          <div className="h-10 bg-zinc-800 rounded w-3/4" />
          <div className="h-4 bg-zinc-800 rounded w-full" />
          <div className="h-4 bg-zinc-800 rounded w-5/6" />
          <div className="h-4 bg-zinc-800 rounded w-4/6" />
        </div>
      </div>
    );
  }

  if (notFound || !brief) {
    return (
      <div className="max-w-3xl mx-auto px-8 pt-20 text-center">
        <h1 className="text-xl font-bold text-zinc-400">Brief not found</h1>
        <Link href="/signals" className="text-green-400 text-sm mt-4 inline-block">
          ← Back to signals
        </Link>
      </div>
    );
  }

  const { signal } = brief;

  return (
    <div className="min-h-screen">
      <div className="max-w-3xl mx-auto px-8 pt-12 pb-24">
        {/* Back nav */}
        <Link
          href="/signals"
          className="inline-flex items-center gap-2 text-xs text-zinc-500 hover:text-zinc-300 mb-6 transition-colors"
        >
          <ArrowLeft className="w-3 h-3" /> All Signals
        </Link>

        {/* Signal Header */}
        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-8"
        >
          <div className="flex items-center gap-3 mb-3">
            <Link
              href={`/company/${signal.ticker}`}
              className="text-xs font-mono text-green-400 hover:underline"
            >
              ${signal.ticker}
            </Link>
            <CategoryBadge category={signal.category} />
            <SeverityBadge severity={signal.severity} />
            <ConfidenceBadge confidence={signal.confidence} />
          </div>
          <h1 className="text-2xl font-bold leading-tight mb-3">{signal.title}</h1>
          <div className="flex items-center gap-3 text-xs text-zinc-500">
            <span>
              {new Date(signal.event_date).toLocaleDateString("en-US", {
                weekday: "long",
                month: "long",
                day: "numeric",
                year: "numeric",
              })}
            </span>
            <span>·</span>
            <a
              href={signal.source_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 text-green-400 hover:underline"
            >
              {signal.source_name} <ExternalLink className="w-3 h-3" />
            </a>
          </div>
        </motion.div>

        {/* Executive Summary */}
        <motion.section
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="glass-card p-6 mb-6 border-l-2 border-green-500"
        >
          <div className="flex items-center gap-2 mb-3">
            <FileText className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Executive Summary</h2>
          </div>
          <p className="text-sm text-zinc-300 leading-relaxed">{brief.executive_summary}</p>
        </motion.section>

        {/* What Happened + Why It Matters */}
        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.15 }}
          className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6"
        >
          <div className="glass-card p-5">
            <div className="flex items-center gap-2 mb-3">
              <AlertTriangle className="w-4 h-4 text-yellow-400" />
              <h2 className="text-sm font-semibold text-zinc-200">What Happened</h2>
            </div>
            <p className="text-xs text-zinc-400 leading-relaxed">{brief.what_happened}</p>
          </div>
          <div className="glass-card p-5">
            <div className="flex items-center gap-2 mb-3">
              <Lightbulb className="w-4 h-4 text-green-400" />
              <h2 className="text-sm font-semibold text-zinc-200">Why It Matters</h2>
            </div>
            <p className="text-xs text-zinc-400 leading-relaxed">{brief.why_it_matters}</p>
          </div>
        </motion.div>

        {/* Financial Areas Affected */}
        <motion.section
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mb-6"
        >
          <div className="flex items-center gap-2 mb-4">
            <BarChart3 className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Financial Areas Affected</h2>
          </div>
          <div className="space-y-2">
            {brief.financial_areas.map((area, i) => (
              <div key={i} className="glass-card p-4 flex items-start gap-3">
                <div className="mt-0.5">{impactIcons[area.impact] || impactIcons.neutral}</div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-0.5">
                    <h3 className="text-sm font-medium text-zinc-200">{area.area}</h3>
                    <span
                      className={`text-[0.6rem] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded ${
                        area.impact === "negative"
                          ? "text-red-400 bg-red-500/10"
                          : area.impact === "positive"
                          ? "text-green-400 bg-green-500/10"
                          : area.impact === "uncertain"
                          ? "text-yellow-400 bg-yellow-500/10"
                          : "text-zinc-400 bg-zinc-500/10"
                      }`}
                    >
                      {area.impact}
                    </span>
                  </div>
                  <p className="text-xs text-zinc-500">{area.detail}</p>
                </div>
              </div>
            ))}
          </div>
        </motion.section>

        {/* Model Impact Mapping */}
        <motion.section
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.25 }}
          className="mb-6"
        >
          <div className="flex items-center gap-2 mb-4">
            <Target className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Model Impact Mapping</h2>
          </div>
          <div className="space-y-3">
            {brief.model_assumptions.map((assumption, i) => (
              <div key={i} className="glass-card p-4">
                <div className="flex items-start justify-between gap-3 mb-2">
                  <div className="flex-1">
                    <h3 className="text-xs font-medium text-zinc-300 mb-1">
                      Current assumption:
                    </h3>
                    <p className="text-xs text-zinc-500 font-mono bg-[#ffffff05] rounded px-2 py-1">
                      {assumption.assumption}
                    </p>
                  </div>
                  <span
                    className={`text-[0.6rem] font-bold uppercase px-2 py-0.5 rounded border ${magnitudeColors[assumption.magnitude] || magnitudeColors.minor}`}
                  >
                    {assumption.magnitude}
                  </span>
                </div>
                <div>
                  <h3 className="text-xs font-medium text-green-400 mb-1">
                    Revised estimate:
                  </h3>
                  <p className="text-xs text-zinc-400 font-mono bg-[#22c55e05] rounded px-2 py-1 border border-green-500/10">
                    {assumption.change}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </motion.section>

        {/* Evidence */}
        <motion.section
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="mb-6"
        >
          <div className="flex items-center gap-2 mb-3">
            <ShieldCheck className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Evidence & Source</h2>
          </div>
          <div className="glass-card p-4">
            <p className="text-xs text-zinc-400 leading-relaxed mb-3">{brief.evidence}</p>
            <a
              href={signal.source_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 text-xs text-green-400 hover:underline"
            >
              <ExternalLink className="w-3 h-3" />
              View source: {signal.source_name}
            </a>
          </div>
        </motion.section>

        {/* Next Steps */}
        <motion.section
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.35 }}
          className="mb-6"
        >
          <div className="flex items-center gap-2 mb-3">
            <ChevronRight className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Suggested Next Steps</h2>
          </div>
          <div className="glass-card p-4">
            <ul className="space-y-2">
              {brief.next_steps.map((step, i) => (
                <li key={i} className="flex items-start gap-2 text-xs text-zinc-400">
                  <span className="text-green-400 mt-0.5 flex-shrink-0">▸</span>
                  {step}
                </li>
              ))}
            </ul>
          </div>
        </motion.section>

        {/* Analyst Questions */}
        <motion.section
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="mb-6"
        >
          <div className="flex items-center gap-2 mb-3">
            <HelpCircle className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Questions to Investigate</h2>
          </div>
          <div className="space-y-2">
            {brief.analyst_questions.map((q, i) => (
              <div key={i} className="glass-card p-4 flex items-start gap-3">
                <span
                  className={`text-[0.6rem] font-bold uppercase px-1.5 py-0.5 rounded flex-shrink-0 mt-0.5 ${
                    q.urgency === "high"
                      ? "text-red-400 bg-red-500/10"
                      : q.urgency === "medium"
                      ? "text-yellow-400 bg-yellow-500/10"
                      : "text-blue-400 bg-blue-500/10"
                  }`}
                >
                  {q.urgency}
                </span>
                <p className="text-xs text-zinc-300">{q.question}</p>
              </div>
            ))}
          </div>
        </motion.section>
      </div>
    </div>
  );
}
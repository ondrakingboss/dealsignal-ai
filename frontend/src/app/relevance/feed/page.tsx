"use client";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowUpRight, Target, AlertTriangle, CheckCircle2, Eye, Sliders } from "lucide-react";
import { loadProfile, scoreRelevance, assessThesisImpact, DEMO_PROFILE } from "@/lib/relevance-engine";
import SeverityBadge, { CategoryBadge, ConfidenceBadge } from "@/components/severity-badge";
import type { Signal, SignalFeed, AnalystBrief } from "@/lib/types";

const THESIS_COLORS: Record<string, string> = {
  supports: "text-green-400 bg-green-500/10 border-green-500/20",
  weakens: "text-red-400 bg-red-500/10 border-red-500/20",
  neutral: "text-zinc-500 bg-zinc-500/10 border-zinc-500/20",
  watch: "text-yellow-400 bg-yellow-500/10 border-yellow-500/20",
};

const RELEVANCE_COLORS: Record<string, string> = {
  critical: "text-red-400",
  high: "text-orange-400",
  medium: "text-yellow-400",
  low: "text-zinc-500",
};

export default function RelevanceFeedPage() {
  const [signals, setSignals] = useState<Signal[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/signals")
      .then(r => r.json())
      .then((d: SignalFeed) => {
        setSignals(d.signals);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const profile = typeof window !== "undefined" ? loadProfile() : DEMO_PROFILE;

  // Score and sort all signals
  const scored = signals
    .map(signal => {
      const relevance = scoreRelevance(signal, profile);
      const thesis = assessThesisImpact(signal, profile, relevance);
      return { signal, relevance, thesis };
    })
    .sort((a, b) => b.relevance.relevance_score - a.relevance.relevance_score);

  const topSignals = scored.filter(s => s.relevance.relevance_level !== "low");
  const lowSignals = scored.filter(s => s.relevance.relevance_level === "low");

  if (loading) {
    return (
      <div className="max-w-3xl mx-auto px-8 pt-12">
        <div className="animate-pulse space-y-4">
          <div className="h-6 bg-zinc-800 rounded w-40" />
          <div className="h-4 bg-zinc-800 rounded w-full" />
          <div className="h-32 bg-zinc-800 rounded w-full" />
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      <div className="max-w-3xl mx-auto px-8 pt-12 pb-24">
        {/* Header */}
        <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} className="mb-8">
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center gap-3">
              <Target className="w-5 h-5 text-green-400" />
              <h1 className="text-2xl font-bold tracking-tight">Personalized Feed</h1>
            </div>
            <Link href="/relevance" className="flex items-center gap-1 text-xs text-zinc-500 hover:text-zinc-300 transition-colors">
              <Sliders className="w-3 h-3" />
              Edit Profile
            </Link>
          </div>
          <p className="text-sm text-zinc-500">
            Signals scored against your {profile.tracked_companies.length} tracked companies,{" "}
            {profile.tracked_themes.length} themes, and {profile.tracked_assumptions.length} assumptions.
          </p>
        </motion.div>

        {/* Top Signals */}
        {topSignals.length === 0 && (
          <div className="glass-card p-8 text-center mb-8">
            <Target className="w-8 h-8 text-zinc-600 mx-auto mb-3" />
            <h3 className="text-sm font-semibold text-zinc-400 mb-1">No relevant signals</h3>
            <p className="text-xs text-zinc-600">
              Try adding more tracked companies, themes, or assumptions in your{" "}
              <Link href="/relevance" className="text-green-400 hover:underline">Relevance Profile</Link>.
            </p>
          </div>
        )}

        <div className="space-y-4">
          {topSignals.map(({ signal, relevance, thesis }, i) => (
            <motion.div
              key={signal.id}
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.04 }}
            >
              <Link href={`/signal/${signal.id}`}>
                <div className="glass-card p-4 hover:border-[#3f3f46] transition-all duration-200 cursor-pointer group">
                  {/* Header row */}
                  <div className="flex items-start justify-between gap-3 mb-2">
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2 mb-1 flex-wrap">
                        <span className="text-xs font-mono text-zinc-500">{signal.ticker}</span>
                        <CategoryBadge category={signal.category} />
                        <SeverityBadge severity={signal.severity} />
                      </div>
                      <h3 className="text-sm font-medium text-zinc-100 leading-snug group-hover:text-green-400 transition-colors">
                        {signal.title}
                      </h3>
                    </div>
                    <div className="flex items-center gap-2 flex-shrink-0">
                      {/* Thesis impact badge */}
                      {thesis.thesis_impact !== "neutral" && (
                        <span className={`text-[0.6rem] font-semibold uppercase px-1.5 py-0.5 rounded border ${THESIS_COLORS[thesis.thesis_impact]}`}>
                          {thesis.thesis_impact === "supports" && <CheckCircle2 className="w-2.5 h-2.5 inline mr-0.5" />}
                          {thesis.thesis_impact === "weakens" && <AlertTriangle className="w-2.5 h-2.5 inline mr-0.5" />}
                          {thesis.thesis_impact === "watch" && <Eye className="w-2.5 h-2.5 inline mr-0.5" />}
                          {thesis.thesis_impact}
                        </span>
                      )}
                      {/* Relevance score */}
                      <span className={`text-xs font-mono font-bold ${RELEVANCE_COLORS[relevance.relevance_level]}`}>
                        {relevance.relevance_score}
                      </span>
                      <ArrowUpRight className="w-4 h-4 text-zinc-600 group-hover:text-green-400 transition-colors" />
                    </div>
                  </div>

                  {/* Summary */}
                  <p className="text-xs text-zinc-500 leading-relaxed line-clamp-2 mb-2">{signal.summary}</p>

                  {/* Relevance reasons */}
                  <div className="flex flex-wrap gap-1.5 mb-2">
                    {relevance.relevance_reasons.slice(0, 3).map((r, i) => (
                      <span key={i} className="text-[0.6rem] text-zinc-600 bg-[#ffffff04] border border-[#27272a] rounded-full px-2 py-0.5">
                        {r}
                      </span>
                    ))}
                  </div>

                  {/* Thesis impact reason */}
                  {thesis.thesis_impact !== "neutral" && thesis.thesis_impact_reason && (
                    <p className="text-[0.6rem] text-zinc-600 italic mt-1">
                      {thesis.thesis_impact_reason.length > 120
                        ? thesis.thesis_impact_reason.slice(0, 120) + "..."
                        : thesis.thesis_impact_reason}
                    </p>
                  )}
                </div>
              </Link>
            </motion.div>
          ))}
        </div>

        {/* Low relevance */}
        {lowSignals.length > 0 && (
          <>
            <div className="flex items-center gap-2 my-6 pt-4 border-t border-[#27272a]">
              <span className="text-xs text-zinc-600">Lower relevance signals</span>
              <span className="text-[0.6rem] text-zinc-700 bg-[#ffffff04] rounded-full px-2 py-0.5">{lowSignals.length}</span>
            </div>
            <div className="space-y-2 opacity-60">
              {lowSignals.map(({ signal, relevance }) => (
                <Link key={signal.id} href={`/signal/${signal.id}`}>
                  <div className="glass-card p-3 hover:border-[#3f3f46] transition-all cursor-pointer flex items-center justify-between">
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-mono text-zinc-600">{signal.ticker}</span>
                        <span className="text-xs text-zinc-500 line-clamp-1">{signal.title}</span>
                      </div>
                    </div>
                    <span className="text-xs font-mono text-zinc-600 ml-2">{relevance.relevance_score}</span>
                  </div>
                </Link>
              ))}
            </div>
          </>
        )}

        {/* Trust copy */}
        <p className="text-xs text-zinc-700 mt-8 text-center italic">
          Relevance scoring is deterministic and based on your selected companies, themes, assumptions, and thesis keywords. It is not investment advice.
        </p>
      </div>
    </div>
  );
}
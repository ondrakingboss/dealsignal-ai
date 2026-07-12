"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowUpRight, ShieldCheck, FileText, Globe, CheckCircle, AlertCircle, Search } from "lucide-react";
import SeverityBadge, { CategoryBadge, ConfidenceBadge } from "./severity-badge";
import type { Signal } from "@/lib/types";

const sourceIcons: Record<string, React.ReactNode> = {
  "company-filing": <FileText className="w-3 h-3" />,
  "company-press-release": <Globe className="w-3 h-3" />,
  "regulator": <ShieldCheck className="w-3 h-3" />,
};

const sourceLabels: Record<string, string> = {
  "company-filing": "Filing",
  "company-press-release": "Official",
  "regulator": "Regulator",
  "financial-news": "News",
  "niche-financial": "Niche",
  "demo-only": "Demo",
};

const depthLabels: Record<string, { label: string; color: string }> = {
  "exact_document": { label: "Exact", color: "text-green-400 bg-green-500/10 border-green-500/20" },
  "relevant_page": { label: "Relevant", color: "text-blue-400 bg-blue-500/10 border-blue-500/20" },
  "base_page": { label: "Base", color: "text-zinc-500 bg-zinc-500/10 border-zinc-500/20" },
};

const qualityIcons: Record<string, React.ReactNode> = {
  "strong": <CheckCircle className="w-2.5 h-2.5 text-green-400" />,
  "acceptable": <AlertCircle className="w-2.5 h-2.5 text-blue-400" />,
  "weak": <Search className="w-2.5 h-2.5 text-zinc-500" />,
};

export default function SignalCard({ signal, index = 0 }: { signal: Signal; index?: number }) {
  const catClass = `cat-${signal.category}`;
  const sourceIcon = sourceIcons[signal.source_type];
  const sourceLabel = sourceLabels[signal.source_type] || "Source";
  const depth = depthLabels[signal.source_depth];
  const qualityIcon = qualityIcons[signal.source_quality];

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.05, duration: 0.3 }}
    >
      <Link href={`/signal/${signal.id}`}>
        <div
          className={`glass-card p-4 hover:border-[#3f3f46] transition-all duration-200 cursor-pointer group ${catClass}`}
        >
          <div className="flex items-start justify-between gap-3 mb-2">
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2 mb-1 flex-wrap">
                <span className="text-xs font-mono text-zinc-500">{signal.ticker}</span>
                <CategoryBadge category={signal.category} />
                <SeverityBadge severity={signal.severity} />
              </div>
              <h3 className="text-sm font-medium text-zinc-100 leading-snug line-clamp-2 group-hover:text-green-400 transition-colors">
                {signal.title}
              </h3>
            </div>
            <ArrowUpRight className="w-4 h-4 text-zinc-600 group-hover:text-green-400 transition-colors flex-shrink-0 mt-1" />
          </div>

          <p className="text-xs text-zinc-500 leading-relaxed line-clamp-2 mb-3">
            {signal.summary}
          </p>

          <div className="flex items-center justify-between gap-2 flex-wrap">
            <div className="flex items-center gap-2">
              <span className="text-xs text-zinc-600">
                {new Date(signal.event_date).toLocaleDateString("en-US", {
                  month: "short",
                  day: "numeric",
                  year: "numeric",
                })}
              </span>
              <span className="text-[0.6rem] uppercase tracking-wider text-zinc-600 bg-[#ffffff04] border border-[#27272a] rounded-full px-1.5 py-0.5 flex items-center gap-1">
                {sourceIcon}
                {sourceLabel}
              </span>
            </div>
            <ConfidenceBadge confidence={signal.confidence} />
          </div>

          {/* Source quality indicator */}
          <div className="mt-2 flex items-center gap-2">
            {depth && (
              <span className={`text-[0.6rem] rounded-full px-2 py-0.5 border ${depth.color}`}>
                {depth.label}
              </span>
            )}
            {qualityIcon && (
              <span className="flex items-center gap-1 text-[0.6rem] text-zinc-500">
                {qualityIcon}
                {signal.source_quality}
              </span>
            )}
            {signal.source_status === "demo_only" && (
              <span className="text-[0.6rem] text-zinc-600 italic ml-auto">
                {depth?.label || "Demo"} source
              </span>
            )}
          </div>
        </div>
      </Link>
    </motion.div>
  );
}
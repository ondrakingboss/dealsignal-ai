"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowUpRight } from "lucide-react";
import SeverityBadge, { CategoryBadge, ConfidenceBadge } from "./severity-badge";
import type { Signal } from "@/lib/types";

export default function SignalCard({ signal, index = 0 }: { signal: Signal; index?: number }) {
  const catClass = `cat-${signal.category}`;

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
              <div className="flex items-center gap-2 mb-1">
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

          <div className="flex items-center justify-between">
            <span className="text-xs text-zinc-600">
              {new Date(signal.event_date).toLocaleDateString("en-US", {
                month: "short",
                day: "numeric",
                year: "numeric",
              })}
            </span>
            <ConfidenceBadge confidence={signal.confidence} />
          </div>
        </div>
      </Link>
    </motion.div>
  );
}
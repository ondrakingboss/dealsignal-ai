"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import { motion } from "framer-motion";
import {
  Building2,
  MapPin,
  Users,
  TrendingUp,
  ArrowLeft,
  BarChart3,
} from "lucide-react";
import SignalCard from "@/components/signal-card";
import type { CompanyDetail } from "@/lib/types";

export default function CompanyPage() {
  const { ticker } = useParams<{ ticker: string }>();
  const [data, setData] = useState<CompanyDetail | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!ticker) return;
    setLoading(true);
    fetch(`/api/company/${ticker}`)
      .then((r) => r.json())
      .then((d) => {
        setData(d);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [ticker]);

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto px-8 pt-12">
        <div className="animate-pulse space-y-4">
          <div className="h-8 bg-zinc-800 rounded w-48" />
          <div className="h-4 bg-zinc-800 rounded w-96" />
          <div className="grid grid-cols-4 gap-4 mt-8">
            {[...Array(4)].map((_, i) => (
              <div key={i} className="h-24 bg-zinc-800 rounded-xl" />
            ))}
          </div>
        </div>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="max-w-4xl mx-auto px-8 pt-20 text-center">
        <h1 className="text-xl font-bold text-zinc-400">Company not found</h1>
        <Link href="/watchlist" className="text-green-400 text-sm mt-4 inline-block">
          ← Back to watchlist
        </Link>
      </div>
    );
  }

  const { company, recent_signals, category_breakdown, severity_breakdown } = data;

  return (
    <div className="min-h-screen">
      <div className="max-w-4xl mx-auto px-8 pt-12 pb-24">
        {/* Back */}
        <Link
          href="/watchlist"
          className="inline-flex items-center gap-2 text-xs text-zinc-500 hover:text-zinc-300 mb-8 transition-colors"
        >
          <ArrowLeft className="w-3 h-3" /> Watchlist
        </Link>

        {/* Company Header */}
        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          className="mb-10"
        >
          <div className="flex items-start gap-4 mb-4">
            <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-zinc-800 to-zinc-700 flex items-center justify-center border border-zinc-700 flex-shrink-0">
              <Building2 className="w-7 h-7 text-zinc-400" />
            </div>
            <div>
              <div className="flex items-center gap-3 mb-1">
                <h1 className="text-2xl font-bold">{company.name}</h1>
                <span className="text-sm font-mono text-zinc-500 bg-[#ffffff08] px-2 py-0.5 rounded">
                  ${company.ticker}
                </span>
              </div>
              <p className="text-sm text-zinc-500 leading-relaxed max-w-2xl">
                {company.description}
              </p>
            </div>
          </div>

          {/* Quick stats */}
          <div className="flex flex-wrap gap-4 text-xs text-zinc-500 mt-4">
            {company.headquarters && (
              <span className="flex items-center gap-1">
                <MapPin className="w-3 h-3" /> {company.headquarters}
              </span>
            )}
            {company.employees && (
              <span className="flex items-center gap-1">
                <Users className="w-3 h-3" /> {company.employees.toLocaleString()} employees
              </span>
            )}
            {company.founded && (
              <span className="flex items-center gap-1">
                <Building2 className="w-3 h-3" /> Founded {company.founded}
              </span>
            )}
            {company.market_cap && (
              <span className="flex items-center gap-1 font-mono text-green-400">
                <TrendingUp className="w-3 h-3" /> {company.market_cap}
              </span>
            )}
          </div>
        </motion.div>

        {/* Stats Cards */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-10">
          <div className="glass-card p-4">
            <div className="text-2xl font-bold text-green-400">{recent_signals.length}</div>
            <div className="text-xs text-zinc-500 mt-1">Signals</div>
          </div>
          <div className="glass-card p-4">
            <div className="text-2xl font-bold text-red-400">
              {severity_breakdown.high || 0}
            </div>
            <div className="text-xs text-zinc-500 mt-1">High Severity</div>
          </div>
          <div className="glass-card p-4">
            <div className="text-2xl font-bold text-yellow-400">
              {severity_breakdown.medium || 0}
            </div>
            <div className="text-xs text-zinc-500 mt-1">Medium</div>
          </div>
          <div className="glass-card p-4">
            <div className="text-2xl font-bold text-blue-400">
              {severity_breakdown.low || 0}
            </div>
            <div className="text-xs text-zinc-500 mt-1">Low</div>
          </div>
        </div>

        {/* Category Breakdown */}
        {Object.keys(category_breakdown).length > 0 && (
          <div className="mb-10">
            <h2 className="text-xs font-semibold text-zinc-500 uppercase tracking-wider mb-3">
              Categories
            </h2>
            <div className="flex flex-wrap gap-2">
              {Object.entries(category_breakdown).map(([cat, count]) => (
                <span
                  key={cat}
                  className="px-3 py-1.5 rounded-lg bg-[#ffffff05] border border-[#27272a] text-xs text-zinc-400"
                >
                  {cat.replace("-", " ")} × {count}
                </span>
              ))}
            </div>
          </div>
        )}

        {/* Signals */}
        <div className="mb-6">
          <div className="flex items-center gap-2 mb-4">
            <BarChart3 className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-300">
              Recent Signals ({recent_signals.length})
            </h2>
          </div>
        </div>

        <div className="space-y-3">
          {recent_signals.map((s, i) => (
            <SignalCard key={s.id} signal={s} index={i} />
          ))}
        </div>
      </div>
    </div>
  );
}
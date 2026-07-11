"use client";

import { useEffect, useState } from "react";
import { Radio, Filter } from "lucide-react";
import SignalCard from "@/components/signal-card";
import type { Signal, SignalFeed } from "@/lib/types";

const CATEGORIES = [
  "all",
  "revenue",
  "margin",
  "balance-sheet",
  "regulation",
  "competition",
  "management",
  "macro",
  "ma",
  "sentiment",
];

const SEVERITIES = ["all", "high", "medium", "low"];

export default function SignalsPage() {
  const [data, setData] = useState<SignalFeed | null>(null);
  const [loading, setLoading] = useState(true);
  const [category, setCategory] = useState("all");
  const [severity, setSeverity] = useState("all");

  useEffect(() => {
    setLoading(true);
    const params = new URLSearchParams();
    if (category !== "all") params.set("category", category);
    if (severity !== "all") params.set("severity", severity);

    fetch(`/api/signals?${params.toString()}`)
      .then((r) => r.json())
      .then((d) => {
        setData(d);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, [category, severity]);

  return (
    <div className="min-h-screen">
      <div className="max-w-3xl mx-auto px-8 pt-12 pb-24">
        {/* Header */}
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-2">
            <Radio className="w-5 h-5 text-green-400" />
            <h1 className="text-2xl font-bold tracking-tight">Signal Feed</h1>
          </div>
          <p className="text-sm text-zinc-500">
            {data ? `${data.total} signals` : "Loading..."}{" "}
            across 8 companies. Filter by category and severity.
          </p>
        </div>

        {/* Filters */}
        <div className="flex flex-wrap items-center gap-2 mb-6">
          <Filter className="w-4 h-4 text-zinc-500" />
          <span className="text-xs text-zinc-600 mr-1">Category:</span>
          {CATEGORIES.map((cat) => (
            <button
              key={cat}
              onClick={() => setCategory(cat)}
              className={`px-2.5 py-1 rounded-full text-xs transition-all ${
                category === cat
                  ? "bg-green-500/20 text-green-400 border border-green-500/30"
                  : "bg-[#ffffff05] border border-[#27272a] text-zinc-500 hover:text-zinc-300"
              }`}
            >
              {cat === "all" ? "All" : cat.replace("-", " ")}
            </button>
          ))}
        </div>

        <div className="flex flex-wrap items-center gap-2 mb-8">
          <span className="text-xs text-zinc-600 mr-1">Severity:</span>
          {SEVERITIES.map((sev) => (
            <button
              key={sev}
              onClick={() => setSeverity(sev)}
              className={`px-2.5 py-1 rounded-full text-xs font-medium transition-all ${
                severity === sev
                  ? sev === "high"
                    ? "bg-red-500/20 text-red-400 border border-red-500/30"
                    : sev === "medium"
                    ? "bg-yellow-500/20 text-yellow-400 border border-yellow-500/30"
                    : sev === "low"
                    ? "bg-blue-500/20 text-blue-400 border border-blue-500/30"
                    : "bg-green-500/20 text-green-400 border border-green-500/30"
                  : "bg-[#ffffff05] border border-[#27272a] text-zinc-500 hover:text-zinc-300"
              }`}
            >
              {sev}
            </button>
          ))}
        </div>

        {/* Signal List */}
        {loading ? (
          <div className="space-y-3">
            {[...Array(6)].map((_, i) => (
              <div key={i} className="glass-card p-4 animate-pulse">
                <div className="flex gap-2 mb-2">
                  <div className="h-4 bg-zinc-800 rounded w-12" />
                  <div className="h-4 bg-zinc-800 rounded w-20" />
                  <div className="h-4 bg-zinc-800 rounded w-14" />
                </div>
                <div className="h-4 bg-zinc-800 rounded w-3/4 mb-2" />
                <div className="h-3 bg-zinc-800 rounded w-full mb-2" />
                <div className="flex justify-between">
                  <div className="h-3 bg-zinc-800 rounded w-20" />
                  <div className="h-3 bg-zinc-800 rounded w-14" />
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="space-y-3">
            {data?.signals.map((s, i) => (
              <SignalCard key={s.id} signal={s} index={i} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
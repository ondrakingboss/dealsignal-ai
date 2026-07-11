"use client";

import { useEffect, useState } from "react";
import { Radio, Search, Filter } from "lucide-react";
import CompanyCard from "@/components/company-card";
import type { Company } from "@/lib/types";

export default function WatchlistPage() {
  const [companies, setCompanies] = useState<Company[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/companies")
      .then((r) => r.json())
      .then((data) => {
        setCompanies(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen">
      <div className="max-w-5xl mx-auto px-8 pt-12 pb-24">
        {/* Header */}
        <div className="mb-10">
          <div className="flex items-center gap-3 mb-2">
            <Radio className="w-5 h-5 text-green-400" />
            <h1 className="text-2xl font-bold tracking-tight">Watchlist</h1>
          </div>
          <p className="text-sm text-zinc-500">
            Monitor 8 companies across technology and financial services. Click a card to see signals and analyst briefs.
          </p>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-4 mb-8">
          {[
            { label: "Companies", value: "8" },
            { label: "Signals", value: "18" },
            { label: "Sectors", value: "Tech, Fin Svc" },
          ].map((stat) => (
            <div key={stat.label} className="glass-card p-4 text-center">
              <div className="text-2xl font-bold text-green-400">{stat.value}</div>
              <div className="text-xs text-zinc-500 mt-1">{stat.label}</div>
            </div>
          ))}
        </div>

        {/* Grid */}
        {loading ? (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {[...Array(8)].map((_, i) => (
              <div key={i} className="glass-card p-5 animate-pulse">
                <div className="flex items-center gap-3 mb-3">
                  <div className="w-10 h-10 rounded-lg bg-zinc-800" />
                  <div className="flex-1">
                    <div className="h-4 bg-zinc-800 rounded w-32 mb-1" />
                    <div className="h-3 bg-zinc-800 rounded w-16" />
                  </div>
                </div>
                <div className="h-3 bg-zinc-800 rounded w-full mb-2" />
                <div className="h-3 bg-zinc-800 rounded w-3/4" />
              </div>
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {companies.map((c, i) => (
              <CompanyCard key={c.ticker} company={c} index={i} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import { Building2, ArrowUpRight } from "lucide-react";
import type { Company } from "@/lib/types";

export default function CompanyCard({
  company,
  index = 0,
}: {
  company: Company;
  index?: number;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.06, duration: 0.3 }}
    >
      <Link href={`/company/${company.ticker}`}>
        <div className="glass-card p-5 hover:border-[#3f3f46] transition-all duration-200 cursor-pointer group">
          <div className="flex items-start justify-between mb-3">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-zinc-800 to-zinc-700 flex items-center justify-center border border-zinc-700">
                <Building2 className="w-5 h-5 text-zinc-400" />
              </div>
              <div>
                <h3 className="text-sm font-semibold text-zinc-100 group-hover:text-green-400 transition-colors">
                  {company.name}
                </h3>
                <p className="text-xs text-zinc-500 font-mono">{company.ticker}</p>
              </div>
            </div>
            <ArrowUpRight className="w-4 h-4 text-zinc-600 group-hover:text-green-400 transition-colors" />
          </div>

          <p className="text-xs text-zinc-500 leading-relaxed line-clamp-2 mb-3">
            {company.description}
          </p>

          <div className="flex items-center gap-4 text-xs text-zinc-600">
            <span>{company.sector}</span>
            <span>{company.market_cap}</span>
            {company.signal_count > 0 && (
              <span className="text-green-400 font-medium">
                {company.signal_count} signal{company.signal_count !== 1 ? "s" : ""}
              </span>
            )}
          </div>
        </div>
      </Link>
    </motion.div>
  );
}
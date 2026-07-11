"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import {
  Radio,
  BarChart3,
  ShieldCheck,
  ArrowRight,
  TrendingUp,
  GitCompare,
  FileSearch,
} from "lucide-react";

const features = [
  {
    icon: Radio,
    title: "Real-Time Signal Detection",
    desc: "Monitor market-moving events across 8 companies with AI-powered classification and severity scoring.",
  },
  {
    icon: BarChart3,
    title: "Analyst-Grade Briefs",
    desc: "Every signal includes an executive summary, what happened, why it matters, and financial impact analysis.",
  },
  {
    icon: GitCompare,
    title: "Model Impact Mapping",
    desc: "See exactly how each event affects your financial model assumptions — revenue, margin, balance sheet.",
  },
  {
    icon: FileSearch,
    title: "Source Traceability",
    desc: "Every signal links to original sources with confidence scores. No black-box AI — full provenance.",
  },
  {
    icon: ShieldCheck,
    title: "Demo Ready",
    desc: "Works without API keys. Curated demo data with realistic financial events for portfolio demonstration.",
  },
  {
    icon: TrendingUp,
    title: "Complementary to ModelGuard",
    desc: "ModelGuard answers 'Is the model trustworthy?' DealSignal answers 'What new information could change it?'",
  },
];

const companies = ["NVDA", "AAPL", "JPM", "ADYEN", "CRM", "CRWD"];

export default function LandingPage() {
  return (
    <div className="min-h-screen">
      {/* Hero */}
      <section className="relative overflow-hidden hero-grid">
        <div className="absolute inset-0 bg-gradient-to-b from-[#09090b] via-transparent to-[#09090b]" />
        <div className="absolute top-20 left-1/4 w-96 h-96 bg-green-500/5 rounded-full blur-3xl" />
        <div className="absolute bottom-20 right-1/4 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl" />

        <div className="relative max-w-5xl mx-auto px-8 pt-32 pb-24 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full glass border border-[#27272a] text-xs text-zinc-400 mb-6">
              <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
              Demo Mode — No API Keys Required
            </div>

            <h1 className="text-5xl md:text-6xl font-bold tracking-tight leading-tight mb-6">
              Market Intelligence
              <br />
              <span className="gradient-text">That Moves With You</span>
            </h1>

            <p className="text-lg text-zinc-400 max-w-2xl mx-auto mb-10 leading-relaxed">
              DealSignal AI monitors company events, classifies financial impact,
              and maps how new information could change your financial model assumptions.
              Built for analysts who need to move fast.
            </p>

            <div className="flex items-center justify-center gap-4">
              <Link
                href="/watchlist"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-green-500 text-black font-semibold text-sm hover:bg-green-400 transition-all"
              >
                View Watchlist
                <ArrowRight className="w-4 h-4" />
              </Link>
              <Link
                href="/signals"
                className="inline-flex items-center gap-2 px-6 py-3 rounded-xl glass text-zinc-300 font-semibold text-sm hover:border-zinc-600 transition-all"
              >
                Browse Signals
              </Link>
            </div>

            {/* Ticker strip */}
            <div className="mt-12 flex items-center justify-center gap-3 flex-wrap">
              {companies.map((t) => (
                <Link
                  key={t}
                  href={`/company/${t}`}
                  className="px-3 py-1.5 rounded-lg bg-[#ffffff05] border border-[#27272a] text-xs font-mono text-zinc-500 hover:text-green-400 hover:border-green-500/30 transition-all"
                >
                  ${t}
                </Link>
              ))}
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features */}
      <section className="max-w-5xl mx-auto px-8 py-24">
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
        >
          <h2 className="text-2xl font-bold text-center mb-3">
            Analyst-Ready Intelligence
          </h2>
          <p className="text-zinc-500 text-center mb-12 max-w-lg mx-auto text-sm">
            Every feature is designed for the way financial analysts actually work.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {features.map((f, i) => (
            <motion.div
              key={f.title}
              initial={{ opacity: 0, y: 12 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: i * 0.08 }}
              className="glass-card p-5"
            >
              <f.icon className="w-8 h-8 text-green-400 mb-4" />
              <h3 className="text-sm font-semibold text-zinc-100 mb-2">{f.title}</h3>
              <p className="text-xs text-zinc-500 leading-relaxed">{f.desc}</p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="border-t border-[#27272a]">
        <div className="max-w-5xl mx-auto px-8 py-20 text-center">
          <h2 className="text-2xl font-bold mb-4">
            Ready to analyze?
          </h2>
          <p className="text-zinc-500 mb-8 text-sm">
            Explore 18 curated signals across 8 companies. No signup required.
          </p>
          <Link
            href="/signals"
            className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-green-500 text-black font-semibold text-sm hover:bg-green-400 transition-all"
          >
            Start Monitoring
            <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </section>
    </div>
  );
}
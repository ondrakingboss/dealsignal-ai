"use client";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import {
  Target, Sliders, Save, RotateCcw, Building2, Lightbulb, FileText,
} from "lucide-react";
import {
  loadProfile, saveProfile, DEMO_PROFILE,
  type RelevanceProfile, type TrackedAssumption,
} from "@/lib/relevance-engine";

const ALL_TICKERS = ["NVDA", "AAPL", "WISE", "REVOLUT", "ADYEN", "JPM", "CRM", "CRWD"];
const ALL_THEMES = [
  "AI infrastructure", "regulation", "China exposure", "interest rates",
  "cybersecurity", "payments", "enterprise", "consumer tech",
];

export default function RelevancePage() {
  const [profile, setProfile] = useState<RelevanceProfile>(DEMO_PROFILE);
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    setProfile(loadProfile());
  }, []);

  const toggleCompany = (ticker: string) => {
    setProfile(p => ({
      ...p,
      tracked_companies: p.tracked_companies.includes(ticker)
        ? p.tracked_companies.filter(t => t !== ticker)
        : [...p.tracked_companies, ticker],
    }));
  };

  const toggleTheme = (theme: string) => {
    setProfile(p => ({
      ...p,
      tracked_themes: p.tracked_themes.includes(theme)
        ? p.tracked_themes.filter(t => t !== theme)
        : [...p.tracked_themes, theme],
    }));
  };

  const addAssumption = () => {
    setProfile(p => ({
      ...p,
      tracked_assumptions: [
        ...p.tracked_assumptions,
        { company_ticker: p.tracked_companies[0] || "NVDA", assumption: "", importance: "medium" },
      ],
    }));
  };

  const updateAssumption = (idx: number, field: string, value: string) => {
    setProfile(p => {
      const a = [...p.tracked_assumptions];
      a[idx] = { ...a[idx], [field]: value };
      return { ...p, tracked_assumptions: a };
    });
  };

  const removeAssumption = (idx: number) => {
    setProfile(p => ({
      ...p,
      tracked_assumptions: p.tracked_assumptions.filter((_, i) => i !== idx),
    }));
  };

  const updateThesis = (ticker: string, text: string) => {
    setProfile(p => ({
      ...p,
      thesis_by_company: { ...p.thesis_by_company, [ticker]: text },
    }));
  };

  const handleSave = () => {
    saveProfile(profile);
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  };

  const handleReset = () => {
    setProfile(DEMO_PROFILE);
  };

  return (
    <div className="min-h-screen">
      <div className="max-w-3xl mx-auto px-8 pt-12 pb-24">
        <motion.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}>
          <div className="flex items-center gap-3 mb-2">
            <Target className="w-5 h-5 text-green-400" />
            <h1 className="text-2xl font-bold tracking-tight">Relevance Profile</h1>
          </div>
          <p className="text-sm text-zinc-500 mb-8">
            Tell DealSignal what matters to you. Signals are scored against your tracked companies, themes, assumptions, and thesis.
          </p>
        </motion.div>

        {/* Tracked Companies */}
        <section className="mb-8">
          <div className="flex items-center gap-2 mb-4">
            <Building2 className="w-4 h-4 text-green-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Tracked Companies</h2>
          </div>
          <div className="flex flex-wrap gap-2">
            {ALL_TICKERS.map(t => (
              <button
                key={t}
                onClick={() => toggleCompany(t)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  profile.tracked_companies.includes(t)
                    ? "bg-green-500/20 text-green-400 border border-green-500/30"
                    : "bg-[#ffffff05] border border-[#27272a] text-zinc-500 hover:text-zinc-300"
                }`}
              >
                ${t}
              </button>
            ))}
          </div>
        </section>

        {/* Tracked Themes */}
        <section className="mb-8">
          <div className="flex items-center gap-2 mb-4">
            <Lightbulb className="w-4 h-4 text-yellow-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Tracked Themes</h2>
          </div>
          <div className="flex flex-wrap gap-2">
            {ALL_THEMES.map(th => (
              <button
                key={th}
                onClick={() => toggleTheme(th)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  profile.tracked_themes.includes(th)
                    ? "bg-blue-500/20 text-blue-400 border border-blue-500/30"
                    : "bg-[#ffffff05] border border-[#27272a] text-zinc-500 hover:text-zinc-300"
                }`}
              >
                {th}
              </button>
            ))}
          </div>
        </section>

        {/* Tracked Assumptions */}
        <section className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <FileText className="w-4 h-4 text-purple-400" />
              <h2 className="text-sm font-semibold text-zinc-200">Tracked Assumptions</h2>
            </div>
            <button
              onClick={addAssumption}
              className="text-xs text-green-400 hover:underline"
            >
              + Add assumption
            </button>
          </div>
          <div className="space-y-2">
            {profile.tracked_assumptions.map((a, i) => (
              <div key={i} className="glass-card p-3 flex items-center gap-3 flex-wrap">
                <select
                  value={a.company_ticker}
                  onChange={e => updateAssumption(i, "company_ticker", e.target.value)}
                  className="text-xs bg-[#ffffff08] border border-[#27272a] rounded px-2 py-1 text-zinc-300"
                >
                  {ALL_TICKERS.map(t => (
                    <option key={t} value={t}>${t}</option>
                  ))}
                </select>
                <input
                  value={a.assumption}
                  onChange={e => updateAssumption(i, "assumption", e.target.value)}
                  placeholder="e.g. data center revenue growth"
                  className="flex-1 min-w-[160px] text-xs bg-[#ffffff08] border border-[#27272a] rounded px-2 py-1 text-zinc-300 placeholder-zinc-600"
                />
                <select
                  value={a.importance}
                  onChange={e => updateAssumption(i, "importance", e.target.value)}
                  className="text-xs bg-[#ffffff08] border border-[#27272a] rounded px-2 py-1 text-zinc-300"
                >
                  <option value="high">High</option>
                  <option value="medium">Medium</option>
                  <option value="low">Low</option>
                </select>
                <button
                  onClick={() => removeAssumption(i)}
                  className="text-xs text-red-400 hover:text-red-300"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>
        </section>

        {/* Thesis */}
        <section className="mb-8">
          <div className="flex items-center gap-2 mb-4">
            <Sliders className="w-4 h-4 text-orange-400" />
            <h2 className="text-sm font-semibold text-zinc-200">Investment Thesis</h2>
          </div>
          {profile.tracked_companies.map(ticker => (
            <div key={ticker} className="mb-3">
              <label className="text-xs font-semibold text-zinc-400 mb-1 block">${ticker}</label>
              <textarea
                value={profile.thesis_by_company[ticker] || ""}
                onChange={e => updateThesis(ticker, e.target.value)}
                rows={2}
                className="w-full text-xs bg-[#ffffff05] border border-[#27272a] rounded-lg px-3 py-2 text-zinc-300 placeholder-zinc-600 resize-none focus:outline-none focus:border-green-500/30"
                placeholder={`Your thesis for ${ticker}...`}
              />
            </div>
          ))}
        </section>

        {/* Actions */}
        <div className="flex items-center gap-3">
          <button
            onClick={handleSave}
            className="flex items-center gap-2 px-4 py-2 rounded-lg bg-green-500/20 text-green-400 text-sm font-medium hover:bg-green-500/30 transition-all"
          >
            <Save className="w-4 h-4" />
            {saved ? "Saved!" : "Save Profile"}
          </button>
          <button
            onClick={handleReset}
            className="flex items-center gap-2 px-4 py-2 rounded-lg bg-[#ffffff05] border border-[#27272a] text-zinc-500 text-sm hover:text-zinc-300 transition-all"
          >
            <RotateCcw className="w-4 h-4" />
            Reset to Demo
          </button>
        </div>

        {/* Trust copy */}
        <p className="text-xs text-zinc-600 mt-6 italic">
          Relevance scoring is deterministic and based on your selected companies, themes, assumptions, and thesis keywords. It is not investment advice. Profile stored locally in your browser.
        </p>
      </div>
    </div>
  );
}
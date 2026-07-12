/**
 * Centralized API configuration for DealSignal AI.
 *
 * In development, API calls go through Next.js rewrites to 127.0.0.1:8001.
 * In production, set NEXT_PUBLIC_API_BASE_URL to the deployed backend URL.
 */

export const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8001";

export function apiUrl(path: string): string {
  const cleanPath = path.startsWith("/") ? path : `/${path}`;
  return `${API_BASE_URL}${cleanPath}`;
}

// ── Type-safe API fetchers ──────────────────────────────────────────

import type { Company, Signal, SignalFeed, AnalystBrief, CompanyDetail } from "./types";

export async function fetchCompanies(): Promise<Company[]> {
  const res = await fetch(apiUrl("/api/companies"), { cache: "no-store" });
  return res.json();
}

export async function fetchSignals(params?: {
  ticker?: string;
  category?: string;
  severity?: string;
}): Promise<SignalFeed> {
  const url = new URL(apiUrl("/api/signals"));
  if (params?.ticker) url.searchParams.set("ticker", params.ticker);
  if (params?.category) url.searchParams.set("category", params.category);
  if (params?.severity) url.searchParams.set("severity", params.severity);
  const res = await fetch(url.toString(), { cache: "no-store" });
  return res.json();
}

export async function fetchSignal(id: string): Promise<Signal> {
  const res = await fetch(apiUrl(`/api/signals/${id}`), { cache: "no-store" });
  return res.json();
}

export async function fetchCompany(ticker: string): Promise<CompanyDetail> {
  const res = await fetch(apiUrl(`/api/company/${ticker}`), { cache: "no-store" });
  return res.json();
}

export async function fetchBrief(signalId: string): Promise<AnalystBrief> {
  const res = await fetch(apiUrl(`/api/brief/${signalId}`), { cache: "no-store" });
  return res.json();
}
import type { Company, Signal, SignalFeed, AnalystBrief, CompanyDetail } from "./types";

const API = "http://localhost:8000";

export async function fetchCompanies(): Promise<Company[]> {
  const res = await fetch(`${API}/api/companies`, { cache: "no-store" });
  return res.json();
}

export async function fetchSignals(params?: {
  ticker?: string;
  category?: string;
  severity?: string;
}): Promise<SignalFeed> {
  const url = new URL(`${API}/api/signals`);
  if (params?.ticker) url.searchParams.set("ticker", params.ticker);
  if (params?.category) url.searchParams.set("category", params.category);
  if (params?.severity) url.searchParams.set("severity", params.severity);
  const res = await fetch(url.toString(), { cache: "no-store" });
  return res.json();
}

export async function fetchSignal(id: string): Promise<Signal> {
  const res = await fetch(`${API}/api/signals/${id}`, { cache: "no-store" });
  return res.json();
}

export async function fetchCompany(ticker: string): Promise<CompanyDetail> {
  const res = await fetch(`${API}/api/company/${ticker}`, { cache: "no-store" });
  return res.json();
}

export async function fetchBrief(signalId: string): Promise<AnalystBrief> {
  const res = await fetch(`${API}/api/brief/${signalId}`, { cache: "no-store" });
  return res.json();
}
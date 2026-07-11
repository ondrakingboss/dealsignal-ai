"""
DealSignal AI — Pydantic Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


# ── Enums as string literals ──────────────────────────────────────────

Severity = str  # "low" | "medium" | "high"
EventCategory = str  # "revenue" | "margin" | "balance-sheet" | "regulation" | "competition" | "management" | "macro" | "ma" | "sentiment"


# ── Company ────────────────────────────────────────────────────────────

class Company(BaseModel):
    ticker: str
    name: str
    sector: str
    industry: str
    description: str
    logo_url: str = ""
    founded: Optional[int] = None
    headquarters: str = ""
    employees: Optional[int] = None
    market_cap: str = ""  # e.g. "$3.2T"
    signal_count: int = 0


# ── Financial Area ─────────────────────────────────────────────────────

class FinancialArea(BaseModel):
    area: str  # e.g. "Revenue", "EBITDA Margin", "Operating Expenses"
    impact: str  # "positive" | "negative" | "neutral" | "uncertain"
    detail: str


# ── Model Assumption ───────────────────────────────────────────────────

class ModelAssumption(BaseModel):
    assumption: str  # e.g. "Revenue take-rate assumed at 2.9%"
    change: str  # e.g. "Take-rate may compress to 2.4% under new regulation"
    magnitude: str  # "minor" | "moderate" | "significant"


# ── Analyst Question ───────────────────────────────────────────────────

class AnalystQuestion(BaseModel):
    question: str
    urgency: str = "medium"  # "low" | "medium" | "high"


# ── Signal / Event ─────────────────────────────────────────────────────

class Signal(BaseModel):
    id: str
    ticker: str
    company_name: str
    title: str
    event_date: str  # ISO date
    category: EventCategory
    severity: Severity
    confidence: float  # 0.0–1.0
    source_name: str
    source_url: str
    summary: str
    tags: list[str] = []


# ── Analyst Brief ──────────────────────────────────────────────────────

class AnalystBrief(BaseModel):
    signal: Signal
    executive_summary: str
    what_happened: str
    why_it_matters: str
    financial_areas: list[FinancialArea]
    model_assumptions: list[ModelAssumption]
    evidence: str
    next_steps: list[str]
    analyst_questions: list[AnalystQuestion]


# ── API Responses ──────────────────────────────────────────────────────

class HealthCheck(BaseModel):
    status: str = "ok"
    version: str = "1.0.0"
    companies: int
    signals: int


class CompanyDetail(BaseModel):
    company: Company
    recent_signals: list[Signal]
    category_breakdown: dict[str, int]
    severity_breakdown: dict[str, int]


class SignalFeed(BaseModel):
    signals: list[Signal]
    total: int
    page: int = 1
    page_size: int = 20
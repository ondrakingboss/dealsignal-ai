"""
DealSignal AI — Pydantic Models
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


# ── Enums as string literals ──────────────────────────────────────────

Severity = str  # "low" | "medium" | "high"
EventCategory = str
SourceType = str  # "company-filing" | "company-press-release" | "regulator" | "financial-news" | "niche-financial" | "demo-only"


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
    market_cap: str = ""
    signal_count: int = 0


# ── Financial Area ─────────────────────────────────────────────────────

class FinancialArea(BaseModel):
    area: str
    impact: str  # "positive" | "negative" | "neutral" | "uncertain"
    detail: str


# ── Model Assumption ───────────────────────────────────────────────────

class ModelAssumption(BaseModel):
    assumption: str
    financial_area: str = ""  # "Income Statement" | "Balance Sheet" | "Cash Flow" | "Valuation"
    possible_direction: str = ""  # "up" | "down" | "uncertain"
    confidence: str = "medium"  # "low" | "medium" | "high"
    reasoning: str = ""
    evidence_gap: str = ""


# ── Analyst Question ───────────────────────────────────────────────────

class AnalystQuestion(BaseModel):
    question: str
    urgency: str = "medium"


# ── Signal / Event ─────────────────────────────────────────────────────

class Signal(BaseModel):
    id: str
    ticker: str
    company_name: str
    title: str
    event_date: str
    category: EventCategory
    severity: Severity
    confidence: float
    confidence_rationale: str = ""
    source_name: str
    source_url: str
    source_type: SourceType = "demo-only"
    source_status: str = "demo_only"  # "verified" | "demo_only" | "unavailable"
    source_note: str = ""
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
    what_is_unknown: str = ""
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
"""
DealSignal AI — FastAPI Backend
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from mock import BRIEFS, COMPANIES, SIGNALS
from models import CompanyDetail, HealthCheck, SignalFeed

app = FastAPI(title="DealSignal AI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.vercel.app",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Health ─────────────────────────────────────────────────────────────

@app.get("/api/health", response_model=HealthCheck)
def health():
    return HealthCheck(companies=len(COMPANIES), signals=len(SIGNALS))


# ── Companies ──────────────────────────────────────────────────────────

@app.get("/api/companies")
def list_companies():
    companies = []
    for c in COMPANIES:
        count = len([s for s in SIGNALS if s.ticker == c.ticker])
        c.signal_count = count
        companies.append(c.model_dump())
    return companies


# ── Company Detail ─────────────────────────────────────────────────────

@app.get("/api/company/{ticker}")
@app.get("/api/companies/{ticker}")
def get_company(ticker: str):
    ticker_upper = ticker.upper()
    company = next((c for c in COMPANIES if c.ticker == ticker_upper), None)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    company_signals = [s for s in SIGNALS if s.ticker == ticker_upper]
    company.signal_count = len(company_signals)

    category_breakdown: dict[str, int] = {}
    severity_breakdown: dict[str, int] = {}
    for s in company_signals:
        category_breakdown[s.category] = category_breakdown.get(s.category, 0) + 1
        severity_breakdown[s.severity] = severity_breakdown.get(s.severity, 0) + 1

    recent = sorted(company_signals, key=lambda s: s.event_date, reverse=True)[:10]

    return CompanyDetail(
        company=company,
        recent_signals=[s.model_dump() for s in recent],
        category_breakdown=category_breakdown,
        severity_breakdown=severity_breakdown,
    ).model_dump()


# ── Company Signals ────────────────────────────────────────────────────

@app.get("/api/company/{ticker}/signals")
def get_company_signals(ticker: str, category: str | None = None, severity: str | None = None):
    ticker_upper = ticker.upper()
    company = next((c for c in COMPANIES if c.ticker == ticker_upper), None)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    filtered = [s for s in SIGNALS if s.ticker == ticker_upper]
    if category:
        filtered = [s for s in filtered if s.category == category]
    if severity:
        filtered = [s for s in filtered if s.severity == severity]

    filtered = sorted(filtered, key=lambda s: s.event_date, reverse=True)
    return [s.model_dump() for s in filtered]


# ── All Signals ────────────────────────────────────────────────────────

@app.get("/api/signals")
def list_signals(
    ticker: str | None = None,
    category: str | None = None,
    severity: str | None = None,
    page: int = 1,
    page_size: int = 20,
):
    filtered = list(SIGNALS)
    if ticker:
        filtered = [s for s in filtered if s.ticker == ticker.upper()]
    if category:
        filtered = [s for s in filtered if s.category == category]
    if severity:
        filtered = [s for s in filtered if s.severity == severity]

    filtered = sorted(filtered, key=lambda s: s.event_date, reverse=True)
    total = len(filtered)
    start = (page - 1) * page_size
    page_signals = filtered[start : start + page_size]

    return SignalFeed(
        signals=[s.model_dump() for s in page_signals],
        total=total,
        page=page,
        page_size=page_size,
    ).model_dump()


# ── Signal Detail ──────────────────────────────────────────────────────

@app.get("/api/signals/{signal_id}")
def get_signal(signal_id: str):
    signal = next((s for s in SIGNALS if s.id == signal_id), None)
    if not signal:
        raise HTTPException(status_code=404, detail="Signal not found")
    return signal.model_dump()


# ── Analyst Brief ──────────────────────────────────────────────────────

@app.get("/api/brief/{signal_id}")
def get_brief(signal_id: str):
    brief = BRIEFS.get(signal_id)
    if not brief:
        raise HTTPException(status_code=404, detail="Brief not found")
    return brief.model_dump()


# ── Categories ──────────────────────────────────────────────────────────

@app.get("/api/categories")
def get_categories():
    """Return all unique signal categories with counts."""
    from collections import Counter
    cat_counts = Counter(s.category for s in SIGNALS)
    return [
        {"category": cat, "label": _cat_label(cat), "count": count}
        for cat, count in cat_counts.most_common()
    ]


def _cat_label(cat: str) -> str:
    labels = {
        "revenue": "Revenue",
        "margin": "Margin",
        "balance-sheet": "Balance Sheet",
        "regulation": "Regulation",
        "competition": "Competition",
        "management": "Management",
        "macro": "Macro",
        "ma": "M&A",
        "sentiment": "Sentiment",
    }
    return labels.get(cat, cat.title())


# ── Run ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# DealSignal AI

**AI-powered market and company event monitor for finance analysts.**

DealSignal identifies business events, classifies their financial impact, and explains how they may affect assumptions in a financial model.

> **ModelGuard answers:** "Is the model trustworthy?"  
> **DealSignal answers:** "What new information could change the model?"

## Demo

Live demo — no API keys or signup required. Curated events for 8 companies across tech and financial services.

| Company | Ticker | Signals |
|---------|--------|---------|
| Nvidia | NVDA | 3 |
| Apple | AAPL | 2 |
| Wise | WISE | 2 |
| Revolut | REVOLUT | 2 |
| Adyen | ADYEN | 2 |
| JPMorgan | JPM | 3 |
| Salesforce | CRM | 2 |
| CrowdStrike | CRWD | 2 |

## Architecture

```
┌─────────────────────────────────────────────┐
│                 Next.js 16                   │
│  ┌───────────────────────────────────────┐  │
│  │  Pages: /  /watchlist  /signals       │  │
│  │         /company/[ticker]             │  │
│  │         /signal/[id]                  │  │
│  └──────────────┬────────────────────────┘  │
│                 │ API Proxy                  │
└─────────────────┼───────────────────────────┘
                  │
┌─────────────────┼───────────────────────────┐
│                 ▼                            │
│            FastAPI Backend                   │
│  ┌───────────────────────────────────────┐  │
│  │  /api/health                          │  │
│  │  /api/companies                       │  │
│  │  /api/signals?ticker=&category=&sev=  │  │
│  │  /api/signals/{id}                    │  │
│  │  /api/company/{ticker}                │  │
│  │  /api/company/{ticker}/signals        │  │
│  │  /api/brief/{signal_id}              │  │
│  └───────────────────────────────────────┘  │
│            Demo Data (JSON in-memory)         │
└──────────────────────────────────────────────┘
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 16, TypeScript, Tailwind CSS v4 |
| UI Components | shadcn/ui (badge, card, dialog, table, tabs, skeleton) |
| Animation | Framer Motion |
| Charts | Recharts |
| Icons | Lucide React |
| Backend | FastAPI, Python 3.11 |
| Data | In-memory JSON seed data |
| Font | Inter (next/font) |

## Design

Dark fintech aesthetic inspired by Bloomberg Terminal, Linear, and Mercury.

- Background: `#09090b`
- Cards: `#18181b` with glass morphism
- Primary: `#22c55e` (green)
- Accent: `#3b82f6` (blue)

## Event Categories

| Category | Description |
|----------|------------|
| Revenue | Revenue impact events |
| Margin | Margin/cost structure events |
| Balance Sheet | Asset/liability/credit events |
| Regulation | Regulatory and legal events |
| Competition | Competitive dynamics |
| Management | Leadership and governance |
| Macro | Macroeconomic events |
| M&A | Mergers and acquisitions |
| Sentiment | Market sentiment signals |

## Signal Severity & Confidence

Each signal includes:
- **Severity:** low | medium | high
- **Confidence score:** 0.0–1.0
- **Source URL** with traceability
- **Event date**
- **Tags** for filtering

## Analyst Brief Format

Each signal produces a detailed brief with:

1. Executive summary
2. What happened
3. Why it matters
4. Financial areas affected (with directional impact)
5. Model assumption impact mapping (current → revised estimates)
6. Evidence and source traceability
7. Suggested next steps
8. Analyst questions to investigate (with urgency)

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- npm

### Backend

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Verify:
```bash
curl http://localhost:8000/api/health
# {"status":"ok","version":"1.0.0","companies":8,"signals":18}
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000

### Build for Production

```bash
cd frontend
npm run build
npm start
```

## Portfolio Highlights

- 🔬 **18 analyst-grade briefs** with financial reasoning
- 🎯 **Model impact mapping** — maps events to model assumptions
- 📊 **9 event categories** with severity classification
- 🔗 **Source traceability** — every signal links to original sources
- ⚡ **Zero API keys required** — demo mode with curated data
- 🎨 **Premium dark fintech UI** — glass morphism, animated cards
- 🏗️ **Contract-first development** — API defined before implementation
- 📦 **Production build passes** — zero TypeScript errors

## CV Bullet Points

- Built DealSignal AI, a full-stack market intelligence platform that monitors company events and maps their impact to financial model assumptions
- Designed and implemented analyst-grade signal briefs with executive summaries, financial impact analysis, and model assumption mapping
- Developed FastAPI backend serving 18 curated signals across 8 companies with RESTful endpoints and Pydantic validation
- Engineered premium dark-themed Next.js 16 frontend with shadcn/ui components, Framer Motion animations, and glass-morphism design
- Implemented contract-first API design ensuring full-stack type safety with TypeScript and Python type hints
- Created demo mode requiring zero API keys while demonstrating production-ready architecture patterns

## License

MIT
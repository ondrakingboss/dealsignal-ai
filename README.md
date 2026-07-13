# DealSignal AI

**AI-assisted analyst relevance engine for tracking company events, evidence quality, and financial model assumption impact.**

> **ModelGuard answers:** "Is the model trustworthy?"  
> **DealSignal answers:** "What new information could change the model?"

## Live Demo

**Frontend:** [deal-signal-ai.vercel.app](https://deal-signal-ai.vercel.app)  
**Backend API:** [dealsignal-ai.onrender.com](https://dealsignal-ai.onrender.com)

## What It Does

Finance users do not need more news. They need to know which events matter to their assumptions.

DealSignal AI:

- Tracks company and market signals across 8 companies
- **Classifies evidence quality** — separates historical facts, analyst estimates, mixed evidence, and synthetic scenarios
- **Maps signals to financial model assumptions** with direction, timing, confidence, and evidence gaps
- **Scores relevance** based on user-selected companies, themes, tracked assumptions, and investment thesis
- **Classifies thesis impact** as supports, weakens, watch, or neutral — using deterministic logic, not AI
- Persists user profiles locally in the browser (no accounts, no backend storage)

## Core Features

| Feature | Description |
|---------|-------------|
| Watchlist | 8 companies across tech and financial services |
| Signal Feed | 18 curated signals with category and severity filters |
| Signal Detail | Analyst briefs with executive summary, financial areas, model impact |
| Evidence Classification | historical_verified, analyst_estimate, mixed_evidence, synthetic_scenario |
| Source Quality/Depth | strong/acceptable/weak, exact_document/relevant_page/base_page |
| Model Impact Mapping | Table with assumption, financial area, direction, timing, confidence, evidence gap |
| Relevance Engine | Deterministic scoring (0–100) against user profile |
| Thesis Impact | supports / weakens / watch / neutral with explanation |
| Local Profile | Tracked companies, themes, assumptions, thesis per company — localStorage |
| Trust Copy | "Not investment advice" disclaimer on every signal detail page |
| Mobile | Sidebar drawer, hamburger menu, responsive layout |

## Tech Stack

- **Frontend:** Next.js 16, TypeScript, Tailwind, shadcn/ui, Framer Motion
- **Backend:** Python, FastAPI, Pydantic
- **Deployment:** Vercel (frontend), Render (backend)

## Architecture

```
┌─────────────────────────────────────────────┐
│                 Vercel                       │
│  Next.js 16 — 8 routes                       │
│  /  /watchlist  /signals  /relevance         │
│  /relevance/feed  /signal/[id]               │
│  /company/[ticker]                           │
└──────────────┬──────────────────────────────┘
               │ NEXT_PUBLIC_API_BASE_URL
┌──────────────▼──────────────────────────────┐
│                 Render                       │
│  FastAPI — 9 endpoints                       │
│  /api/health  /api/companies                 │
│  /api/signals  /api/categories               │
│  /api/company/{ticker}                       │
│  /api/signals/{id}  /api/brief/{id}          │
└─────────────────────────────────────────────┘
```

## Verification

All endpoints return 200. 16/18 signals use verified historical sources with real company IR pages, regulator publications, and SEC filings. 2 remain demo_only or synthetic_scenario where sources could not be verified.

## Limitations

This is a **curated demo**, not a live market data product.

- 18 curated signals across 8 companies — not a live feed
- Relevance scoring is **deterministic keyword-based**, not machine learning
- Source URLs point to real company/regulator pages, but not to specific filings (deep-linking requires JavaScript on most IR sites)
- **Not investment advice** — clearly labeled throughout
- No real-time ingestion, no Bloomberg/Reuters API integration
- Claim-level source extraction is future work (currently signal-level)

## Future Roadmap

- Asset universe expansion (more companies, sectors, geographies)
- Real source ingestion (RSS, SEC EDGAR, press release monitoring)
- Claim-level provenance (individual facts linked to specific source paragraphs)
- Analyst memo export (PDF reports with evidence trail)
- ModelGuard integration — DealSignal feeds events into ModelGuard's scenario impact analysis
- AI-assisted signal summarization (opt-in, clearly labeled)

## Local Development

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001

# Frontend
cd frontend
npm install
npm run dev
```

## License

MIT — use freely for portfolio, learning, and educational purposes.

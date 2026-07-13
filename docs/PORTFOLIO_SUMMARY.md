# DealSignal AI — Portfolio Summary

## Project Description

DealSignal AI is a full-stack fintech portfolio project that demonstrates how financial analysts can prioritize company events by relevance to their model assumptions — rather than drowning in news feeds. It classifies evidence quality, maps events to financial statement assumptions, and scores relevance deterministically against a user's investment thesis.

Built as a complement to [ModelGuard AI](https://modelguard-ai.vercel.app) (Excel model auditing), DealSignal answers: "What new information could change the model?"

## Best Demo Flow

1. Open [deal-signal-ai.vercel.app](https://deal-signal-ai.vercel.app)
2. Navigate to **Signals** — show the 18 curated signals with evidence classes
3. Open sig-001 (NVDA export controls) — show the analyst brief with model impact mapping table
4. Point out: observed facts vs analyst interpretation vs scenario assumptions
5. Navigate to **Relevance Profile** — show the preloaded demo profile
6. Navigate to **Relevance Feed** — show personalized ranking:
   - sig-001 (NVDA export controls) **weakens** NVDA thesis
   - sig-003 (NVDA record DC revenue) **supports** NVDA thesis
   - sig-002 (hyperscaler competition) shows **watch** on threat detection
7. Explain: deterministic scoring, not AI — honest about limitations

## Strongest Talking Points

- **Evidence classification** — historical_verified, analyst_estimate, mixed_evidence, synthetic_scenario — not "all verified" or "all fake"
- **Source credibility** — exact_document deep links to real SEC filings and company press releases (5 confirmed 200 OK)
- **Model impact mapping** — every signal maps to specific financial statement assumptions with direction, timing, confidence, and evidence gaps
- **Relevance engine** — deterministic scoring against user's thesis, not a black-box recommendation algorithm
- **Honest about limitations** — "not investment advice" on every page, demo-only sources clearly labeled

## Known Limitations

- 18 curated signals, not a live feed
- Deterministic keyword-based relevance, not ML
- Source URLs are real but not deep-linked to specific paragraphs
- No real-time data ingestion
- No Bloomberg/Reuters integration

## CV Bullet — Short

> Built DealSignal AI, a full-stack financial event intelligence platform that classifies evidence quality, maps company events to financial model assumptions, and deterministically scores signal relevance against user-defined investment thesis. (Next.js, FastAPI, TypeScript, Python, Vercel, Render)

## CV Bullet — Technical

> Engineered DealSignal AI, a full-stack analyst relevance platform with evidence classification (historical/estimate/mixed/synthetic), source credibility depth scoring, and a deterministic thesis-impact engine. Built with Next.js 16 + TypeScript frontend, FastAPI + Python backend, deployed on Vercel and Render with CORS, rate limiting, and security headers.

## CV Bullet — Finance-Focused

> Designed DealSignal AI to solve the analyst signal-to-noise problem: which events actually matter to financial model assumptions? Built evidence classification, model impact mapping (direction/timing/confidence/evidence gaps), and a deterministic relevance engine that scores signals against user-defined thesis and tracked assumptions. Complements ModelGuard AI (Excel model auditing) in a fintech portfolio.

## LinkedIn Post Draft

> I built DealSignal AI because analysts don't need more news — they need to know which events actually matter to their assumptions.
>
> It's a full-stack financial event intelligence platform that:
> • Classifies evidence quality (historical, estimate, mixed, synthetic)
> • Maps events to specific financial model assumptions
> • Deterministically scores relevance against your thesis
> • Tells you whether a signal supports or weakens your assumptions
>
> Tech: Next.js 16, FastAPI, Python, TypeScript, Vercel, Render.
> Live at deal-signal-ai.vercel.app — no signup, no API keys.
>
> This is the companion to ModelGuard AI (Excel model auditing).
> Together: "Is the model trustworthy?" and "What could change the model?"
>
> Curated demo dataset. Honest about limitations. Not investment advice.
> Built to show how analyst workflows could work — not to pretend it's Bloomberg.

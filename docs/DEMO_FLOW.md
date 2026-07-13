# DealSignal AI — Demo Flow

Best demo path for portfolio presentations, interviews, or sharing.

## Flow (5-7 minutes)

### 1. Landing Page (30s)
Open [deal-signal-ai.vercel.app](https://deal-signal-ai.vercel.app)

> "This is not a news dashboard. It ranks events by relevance to financial assumptions."

Show the hero, feature cards, and ticker strip. Note: demo-only, no API keys required.

### 2. Watchlist (30s)
Navigate to `/watchlist`

> "8 companies across tech and financial services. Nvidia, Apple, JPMorgan, Adyen, Salesforce, CrowdStrike, Wise, Revolut."

Show company cards with signal counts and high-severity counts.

### 3. Signal Feed (45s)
Navigate to `/signals`

> "18 curated signals. Each has an evidence class — historical_verified, analyst_estimate, mixed_evidence, synthetic_scenario."

Show filter by category (e.g., "Regulation") and severity. Point out source quality badges (Exact/Relevant/Base).

### 4. Signal Detail — The Core Product (90s)
Open `/signal/sig-001` (NVDA export controls)

Walk through:
1. **Header** — title, date, severity, confidence, source link, source depth badge
2. **Executive Summary** — concise analyst-grade summary
3. **Why This Signal** — Trigger, Financial Relevance, Confidence Rationale, What Is Unknown, Suggested Follow-Up
4. **Financial Areas Affected** — Data Center Revenue, Gross Margin, R&D, Geographic Mix
5. **Model Impact Mapping Table** — Assumption | Area | Direction | Confidence | Evidence Gap
6. **Evidence** — what the source proves, separated from estimates
7. **Disclaimer** — "This is not investment advice"

> "Every signal maps to specific financial statement assumptions. Not vague 'revenue may change' — specific: 'China revenue contribution modeled at 17% of DC revenue.'"

### 5. Relevance Profile (45s)
Navigate to `/relevance`

> "You tell DealSignal what matters to you. Tracked companies, themes, specific assumptions, and an investment thesis per company. All stored locally in your browser — no accounts, no backend storage."

Show the demo profile: NVDA, AAPL, JPM with tracked assumptions and thesis text.

### 6. Relevance Feed — The Payoff (90s)
Navigate to `/relevance/feed`

> "Now signals are ranked by relevance to YOUR assumptions."

Show the top-ranked signals:
1. **sig-001 (NVDA export controls)** — score 75, **weakens** thesis: "Signal documents new restrictions on China access, conflicting with thesis assumption that restrictions remain manageable."
2. **sig-003 (NVDA record DC revenue)** — score 90, **supports** thesis: "Margin performance supports thesis assumptions."
3. **sig-002 (hyperscaler competition)** — score 45, **watch**: "Competitive or insourcing signal detected. Impact on thesis is plausible but not yet confirmed."

Point out relevance reasons, matched assumptions, and thesis impact badges.

### 7. Honest Limitations (30s)

> "This is deterministic keyword-based scoring, not AI. I'm honest about limitations: 18 curated signals, not a live feed. Real source URLs but not deep-linked to specific paragraphs. Not investment advice — labeled everywhere. This shows how the workflow could work, not pretending it's Bloomberg."

## Key Transitions

- "This is not a news dashboard. It ranks events by relevance to assumptions."
- "Every signal maps to specific financial statement assumptions."
- "You tell it what matters. It scores everything against your thesis."
- "Not AI — deterministic logic. Honest about what it knows and doesn't know."

## Screenshots Needed

1. Landing page hero
2. Signal feed with filters
3. Signal detail — model impact table
4. Signal detail — Why This Signal section
5. Relevance profile page
6. Relevance feed with thesis impact badges
7. Mobile view of signal detail

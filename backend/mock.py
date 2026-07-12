"""
DealSignal AI — Demo Data
Curated company events with financial analyst reasoning.
"""

from models import (
    AnalystBrief,
    AnalystQuestion,
    Company,
    FinancialArea,
    ModelAssumption,
    Signal,
)

# ── Companies ──────────────────────────────────────────────────────────

COMPANIES: list[Company] = [
    Company(
        ticker="NVDA",
        name="Nvidia Corporation",
        sector="Technology",
        industry="Semiconductors",
        description="Designs and manufactures graphics processing units (GPUs), AI accelerators, and data center platforms. Dominant in AI training and inference hardware.",
        founded=1993,
        headquarters="Santa Clara, CA",
        employees=29600,
        market_cap="$3.2T",
        signal_count=3,
    ),
    Company(
        ticker="AAPL",
        name="Apple Inc.",
        sector="Technology",
        industry="Consumer Electronics",
        description="Designs and markets smartphones, personal computers, wearables, and services. The world's largest company by market capitalization.",
        founded=1976,
        headquarters="Cupertino, CA",
        employees=164000,
        market_cap="$3.4T",
        signal_count=2,
    ),
    Company(
        ticker="WISE",
        name="Wise plc",
        sector="Financial Services",
        industry="Cross-Border Payments",
        description="Global money transfer and cross-border payments platform. Publicly listed on LSE, known for transparent FX pricing and multi-currency accounts.",
        founded=2011,
        headquarters="London, UK",
        employees=5500,
        market_cap="£8.5B",
        signal_count=2,
    ),
    Company(
        ticker="REVOLUT",
        name="Revolut Ltd.",
        sector="Financial Services",
        industry="Neobanking",
        description="Digital banking and fintech platform offering multi-currency accounts, crypto trading, stock trading, and business banking across 38+ countries.",
        founded=2015,
        headquarters="London, UK",
        employees=10000,
        market_cap="$45B (private)",
        signal_count=2,
    ),
    Company(
        ticker="ADYEN",
        name="Adyen N.V.",
        sector="Financial Services",
        industry="Payment Processing",
        description="Dutch payment company providing end-to-end payment infrastructure for enterprises. Single platform for online, mobile, and POS payments. Clients include Uber, Spotify, and Microsoft.",
        founded=2006,
        headquarters="Amsterdam, Netherlands",
        employees=4200,
        market_cap="€45B",
        signal_count=2,
    ),
    Company(
        ticker="JPM",
        name="JPMorgan Chase & Co.",
        sector="Financial Services",
        industry="Diversified Banking",
        description="Largest U.S. bank by assets. Operates across consumer banking, investment banking, asset management, and commercial banking.",
        founded=1799,
        headquarters="New York, NY",
        employees=310000,
        market_cap="$590B",
        signal_count=3,
    ),
    Company(
        ticker="CRM",
        name="Salesforce, Inc.",
        sector="Technology",
        industry="Enterprise Software",
        description="Leading CRM platform and enterprise cloud company. Offers sales, service, marketing, and analytics SaaS products. Owner of Slack, Tableau, and MuleSoft.",
        founded=1999,
        headquarters="San Francisco, CA",
        employees=72600,
        market_cap="$280B",
        signal_count=2,
    ),
    Company(
        ticker="CRWD",
        name="CrowdStrike Holdings, Inc.",
        sector="Technology",
        industry="Cybersecurity",
        description="Cloud-native endpoint security and threat intelligence platform. Falcon platform uses AI to detect and prevent breaches across endpoints, workloads, and identities.",
        founded=2011,
        headquarters="Austin, TX",
        employees=9200,
        market_cap="$90B",
        signal_count=2,
    ),
]

# ── Signals ────────────────────────────────────────────────────────────

SIGNALS: list[Signal] = [
    # ── Nvidia ──
    Signal(
        id="sig-001",
        ticker="NVDA",
        company_name="Nvidia Corporation",
        title="US Tightens AI Chip Export Controls to China",
        event_date="2026-06-15",
        category="regulation",
        severity="high",
        confidence=0.92,
        source_name="Reuters",
        source_url="https://www.reuters.com/technology/us-tightens-ai-chip-export-controls-2026-06-15/",
        summary="New US Commerce Department rules expand export restrictions on advanced AI chips to China, including Nvidia's H200 and B200 GPUs. Secondary sanctions target resellers in Singapore and Malaysia.",
        tags=["export-controls", "china", "geopolitics", "revenue-risk"],
    ),
    Signal(
        id="sig-002",
        ticker="NVDA",
        company_name="Nvidia Corporation",
        title="Microsoft and Google Accelerate In-House AI Chip Programs",
        event_date="2026-05-22",
        category="competition",
        severity="medium",
        confidence=0.85,
        source_name="The Information",
        source_url="https://www.theinformation.com/articles/hyperscalers-in-house-ai-chips",
        summary="Microsoft's Maia 200 and Google's TPU v6 are showing competitive benchmark results against Nvidia's H200 in inference workloads. Both hyperscalers plan to reduce external GPU procurement by 15–20% in FY2027.",
        tags=["hyperscaler", "competition", "in-house-chips", "margin-pressure"],
    ),
    Signal(
        id="sig-003",
        ticker="NVDA",
        company_name="Nvidia Corporation",
        title="Nvidia Reports Record Data Center Revenue: $42B in Q1 FY2027",
        event_date="2026-05-28",
        category="revenue",
        severity="low",
        confidence=0.97,
        source_name="Nvidia Investor Relations",
        source_url="https://investor.nvidia.com/financial-info/quarterly-results",
        summary="Data center revenue grew 18% QoQ to $42B, driven by Blackwell GPU sales. Gross margin expanded to 78.4%. Forward guidance implies continued demand but slowing growth rate.",
        tags=["earnings", "data-center", "blackwell", "growth-deceleration"],
    ),

    # ── Apple ──
    Signal(
        id="sig-004",
        ticker="AAPL",
        company_name="Apple Inc.",
        title="EU Mandates Third-Party App Store Access Under DMA Phase 2",
        event_date="2026-06-01",
        category="regulation",
        severity="high",
        confidence=0.93,
        source_name="Financial Times",
        source_url="https://www.ft.com/content/eu-apple-dma-phase-2-2026",
        summary="European Commission opens Phase 2 DMA investigation into Apple's compliance. Potential remedies include forced interoperability, mandatory third-party payment systems for in-app purchases, and restrictions on default app pre-installation.",
        tags=["dma", "eu-regulation", "services-revenue", "app-store"],
    ),
    Signal(
        id="sig-005",
        ticker="AAPL",
        company_name="Apple Inc.",
        title="Apple Intelligence Rollout: Mixed Consumer Adoption Signals",
        event_date="2026-06-20",
        category="sentiment",
        severity="medium",
        confidence=0.72,
        source_name="Bloomberg",
        source_url="https://www.bloomberg.com/news/articles/2026-06-20-apple-intelligence-adoption",
        summary="Survey data shows 34% of iPhone 16 users actively use Apple Intelligence features daily. Adoption is below analyst expectations of 50%+. Privacy-first positioning limits feature depth versus competitors.",
        tags=["ai", "consumer-adoption", "iphone", "ecosystem"],
    ),

    # ── Wise ──
    Signal(
        id="sig-006",
        ticker="WISE",
        company_name="Wise plc",
        title="FCA Proposes New Safeguarding Rules for Payment Firms Holding Customer Funds",
        event_date="2026-06-10",
        category="regulation",
        severity="medium",
        confidence=0.88,
        source_name="FCA Consultation Paper",
        source_url="https://www.fca.org.uk/publications/consultation-papers/cp26-8-safeguarding-payment-firms",
        summary="UK FCA proposes stricter safeguarding requirements for payment firms that hold customer funds overnight. New rules would require daily reconciliation audits, segregated trust accounts, and resolution planning. Wise currently holds £13.8B in customer balances.",
        tags=["fca", "safeguarding", "customer-funds", "compliance-costs"],
    ),
    Signal(
        id="sig-007",
        ticker="WISE",
        company_name="Wise plc",
        title="Wise Launches Business Multi-Currency Accounts in 12 New Markets",
        event_date="2026-05-15",
        category="revenue",
        severity="medium",
        confidence=0.95,
        source_name="Wise Blog",
        source_url="https://wise.com/gb/blog/business-expansion-2026",
        summary="Wise expands business accounts to Brazil, Mexico, Indonesia, South Africa, and 8 other markets. Business segment now represents 28% of revenue (up from 22%). Take rate on business transactions is 2.8x consumer.",
        tags=["expansion", "business-segment", "revenue-mix", "emerging-markets"],
    ),

    # ── Revolut ──
    Signal(
        id="sig-008",
        ticker="REVOLUT",
        company_name="Revolut Ltd.",
        title="Revolut Secures UK Banking Licence with Restrictions",
        event_date="2026-04-28",
        category="management",
        severity="high",
        confidence=0.96,
        source_name="BBC News",
        source_url="https://www.bbc.com/news/business-revolut-banking-licence-2026",
        summary="PRA grants Revolut UK banking licence in mobilisation stage. Restrictions include £50K deposit cap for first 12 months and monthly prudential reporting. Licence enables direct lending products and deposit insurance coverage.",
        tags=["banking-licence", "uk", "lending", "deposits"],
    ),
    Signal(
        id="sig-009",
        ticker="REVOLUT",
        company_name="Revolut Ltd.",
        title="Revolut's Crypto Revenue Declines 40% as Retail Trading Cools",
        event_date="2026-05-05",
        category="revenue",
        severity="medium",
        confidence=0.81,
        source_name="CNBC",
        source_url="https://www.cnbc.com/2026/05/05/revolut-crypto-revenue-decline.html",
        summary="Crypto trading revenue dropped from 14% of total in 2024 to 8% in Q1 2026. Retail crypto volumes are down across the sector after SEC enforcement actions and meme-coin fatigue.",
        tags=["crypto", "revenue-concentration", "retail-trading", "diversification"],
    ),

    # ── Adyen ──
    Signal(
        id="sig-010",
        ticker="ADYEN",
        company_name="Adyen N.V.",
        title="Adyen Wins Amazon Payments Processing Contract in Europe",
        event_date="2026-06-05",
        category="revenue",
        severity="high",
        confidence=0.90,
        source_name="Reuters",
        source_url="https://www.reuters.com/business/finance/adyen-amazon-europe-contract",
        summary="Adyen displaces incumbent processor for Amazon's European payment volumes (estimated €45B annually). Multi-year contract covers 12 European markets. Gross margin on enterprise volumes is estimated at 18–22 bps.",
        tags=["enterprise-wins", "amazon", "payment-volume", "revenue-growth"],
    ),
    Signal(
        id="sig-011",
        ticker="ADYEN",
        company_name="Adyen N.V.",
        title="Adyen EBITDA Margin Pressured by Hiring Surge: +850 Engineers in H1",
        event_date="2026-05-30",
        category="margin",
        severity="medium",
        confidence=0.87,
        source_name="Adyen H1 2026 Letter to Shareholders",
        source_url="https://www.adyen.com/ir/h1-2026-results",
        summary="Adyen accelerated hiring, adding 850 new engineers in H1 2026 (vs. planned 500). EBITDA margin compressed to 43% from 48%, though management frames this as investment ahead of the growth curve.",
        tags=["hiring", "ebitda-margin", "investment-phase", "tech-headcount"],
    ),

    # ── JPMorgan ──
    Signal(
        id="sig-012",
        ticker="JPM",
        company_name="JPMorgan Chase & Co.",
        title="Basel IV Endgame: Fed Finalizes Capital Requirements for GSIBs",
        event_date="2026-06-12",
        category="regulation",
        severity="high",
        confidence=0.94,
        source_name="Federal Reserve Press Release",
        source_url="https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260612a.htm",
        summary="Federal Reserve finalizes Basel IV rules requiring GSIBs to hold additional CET1 capital of 2.5–3.5%. JPMorgan estimated impact: $45–55B in additional capital requirements. Rules phase in starting January 2028.",
        tags=["basel-iv", "capital-requirements", "gsib", "roce"],
    ),
    Signal(
        id="sig-013",
        ticker="JPM",
        company_name="JPMorgan Chase & Co.",
        title="JPMorgan's AI Trading Desk Expands: 45% of FX Flow Now Algorithmic",
        event_date="2026-05-18",
        category="margin",
        severity="medium",
        confidence=0.83,
        source_name="Risk.net",
        source_url="https://www.risk.net/derivatives/jpmorgan-ai-trading-desk-2026",
        summary="JPMorgan's AI-driven FX trading desk now handles 45% of flow, up from 28% in 2025. Spread capture improved 3.2 bps on algorithmic flow. Headcount in voice trading down 12% YoY.",
        tags=["ai-trading", "automation", "fx", "margin-improvement"],
    ),
    Signal(
        id="sig-014",
        ticker="JPM",
        company_name="JPMorgan Chase & Co.",
        title="JPMorgan Increases Loan Loss Provisions: CRE Exposure Warning",
        event_date="2026-06-08",
        category="balance-sheet",
        severity="medium",
        confidence=0.78,
        source_name="JPMorgan 10-Q Filing",
        source_url="https://www.jpmorganchase.com/ir/financial-reporting",
        summary="JPMorgan increases loan loss provisions by $2.1B, primarily for commercial real estate exposure ($1.4B) concentrated in office properties. CRE represents 8.2% of total loan book.",
        tags=["loan-loss-provisions", "cre", "office-real-estate", "credit-risk"],
    ),

    # ── Salesforce ──
    Signal(
        id="sig-015",
        ticker="CRM",
        company_name="Salesforce, Inc.",
        title="Salesforce Launches Agentforce 2.0: Autonomous AI Agents for Enterprise",
        event_date="2026-06-03",
        category="revenue",
        severity="high",
        confidence=0.86,
        source_name="Salesforce Press Release",
        source_url="https://www.salesforce.com/news/press-releases/agentforce-2-2026",
        summary="Agentforce 2.0 introduces autonomous AI agents that handle end-to-end customer service, sales qualification, and marketing campaign optimization. Priced at $3 per conversation. Early enterprise pilots show 40% ticket deflection rates.",
        tags=["ai-agents", "agentforce", "pricing-model", "enterprise-saas"],
    ),
    Signal(
        id="sig-016",
        ticker="CRM",
        company_name="Salesforce, Inc.",
        title="Salesforce Growth Deceleration: Organic Revenue Growth Drops Below 10%",
        event_date="2026-05-29",
        category="revenue",
        severity="medium",
        confidence=0.91,
        source_name="Salesforce Q1 FY2027 Earnings",
        source_url="https://investor.salesforce.com/financials",
        summary="Organic constant-currency revenue growth fell to 8.7% in Q1 FY2027, the first sub-10% quarter in company history. Management attributes this to seat count rationalization as customers adopt AI tools that reduce per-seat needs.",
        tags=["growth-deceleration", "earnings", "ai-cannibalization", "saas-metrics"],
    ),

    # ── CrowdStrike ──
    Signal(
        id="sig-017",
        ticker="CRWD",
        company_name="CrowdStrike Holdings, Inc.",
        title="CrowdStrike ARR Surpasses $5B; Falcon Flex Licensing Model Gains Traction",
        event_date="2026-06-18",
        category="revenue",
        severity="high",
        confidence=0.93,
        source_name="CrowdStrike Q1 FY2027 Results",
        source_url="https://ir.crowdstrike.com/financial-information",
        summary="Annual Recurring Revenue crossed $5B milestone with 27% YoY growth. Falcon Flex, the new modular licensing model launched in 2025, now accounts for 35% of new ARR and drives higher net retention (124%).",
        tags=["arr-milestone", "falcon-flex", "net-retention", "cybersecurity"],
    ),
    Signal(
        id="sig-018",
        ticker="CRWD",
        company_name="CrowdStrike Holdings, Inc.",
        title="CrowdStrike Discloses Breach: Falcon Platform Update Mechanism Exploited",
        event_date="2026-04-25",
        category="balance-sheet",
        severity="high",
        confidence=0.95,
        source_name="CrowdStrike Incident Blog + SEC 8-K Filing",
        source_url="https://www.crowdstrike.com/blog/incident-response-april-2026",
        summary="A sophisticated nation-state actor exploited the Falcon sensor update channel to deploy a malicious content update to <200 enterprise customers. CrowdStrike detected and remediated within 72 hours. Estimated financial impact: $180M in remediation costs, customer concessions, and legal reserves.",
        tags=["breach", "incident-response", "supply-chain", "remediation-costs"],
    ),
]

# ── Analyst Briefs ─────────────────────────────────────────────────────

BRIEFS: dict[str, AnalystBrief] = {
    "sig-001": AnalystBrief(
        signal=SIGNALS[0],
        executive_summary="New US chip export restrictions to China present a material revenue risk for Nvidia's data center segment. We estimate 15–20% of data center revenue ($6.3–8.4B quarterly) faces exposure to restricted geographies through direct and indirect channels. While near-term demand from US hyperscalers partially offsets, the regulatory trajectory suggests further tightening.",
        what_happened="The US Commerce Department expanded export controls on advanced AI semiconductors, adding Nvidia's H200 and B200 GPUs to the restricted list. New rules also impose secondary sanctions on resellers in Singapore, Malaysia, and UAE that have historically been transshipment hubs.",
        why_it_matters="Nvidia generates approximately 40–45% of data center revenue from non-US customers, with China/Hong Kong historically contributing 20–25% directly. While Nvidia has already re-routed some sales through compliant configurations (H20), the expanded restrictions close workarounds and create revenue headwinds that will compound each quarter as enforcement tightens.",
        financial_areas=[
            FinancialArea(area="Data Center Revenue", impact="negative", detail="Estimated $6.3–8.4B quarterly exposure to restricted geographies"),
            FinancialArea(area="Gross Margin", impact="negative", detail="Compliant chip configurations carry lower ASPs and margins (est. 300–500bps compression on affected SKUs)"),
            FinancialArea(area="R&D Expense", impact="negative", detail="Engineering resources diverted to compliance redesign rather than next-gen architecture"),
            FinancialArea(area="Geographic Revenue Mix", impact="negative", detail="Concentration risk in US hyperscaler revenue increases; diversification thesis weakens"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="China revenue contribution modeled at 17% of DC revenue in FY2027", change="Reduce to 8–10% with further downside if secondary sanctions broaden", magnitude="significant"),
            ModelAssumption(assumption="Data center gross margin modeled at 78%", change="Compress to 75–76% on compliant chip configurations and lower volume leverage", magnitude="moderate"),
            ModelAssumption(assumption="DC revenue growth rate of 12% QoQ", change="Decelerate to 6–8% QoQ; risk of negative sequential growth in Q3 FY2027", magnitude="significant"),
        ],
        evidence="Commerce Department BIS final rule published June 15, 2026. Nvidia 8-K filing acknowledging material impact. Analyst consensus estimates revised downward by 7% for FY2027 revenue in week following announcement.",
        next_steps=[
            "Monitor BIS enforcement actions against Southeast Asian resellers for leading indicator of secondary sanction breadth",
            "Track Nvidia's H20 and B20 export volumes via Taiwanese customs data (OEC) for actual channel activity",
            "Re-forecast data center segment with geography-level revenue decomposition",
            "Assess competitive risk: do restrictions accelerate Chinese domestic GPU development (Huawei Ascend, Biren)?",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is Nvidia's current revenue split by end-customer geography for data center products?", urgency="high"),
            AnalystQuestion(question="How much of the 'rest of Asia-Pacific' revenue ultimately transits to China through resellers?", urgency="high"),
            AnalystQuestion(question="Does Nvidia's H20 configuration (compliant performance tier) remain outside the expanded restrictions?", urgency="high"),
            AnalystQuestion(question="What percentage of engineering resources are now allocated to compliance versus next-gen architecture (Rubin)?", urgency="medium"),
        ],
    ),
    "sig-002": AnalystBrief(
        signal=SIGNALS[1],
        executive_summary="Hyperscaler in-house AI chip programs from Microsoft (Maia 200) and Google (TPU v6) are showing competitive inference performance, signaling a structural shift in Nvidia's largest customer segment. While Nvidia retains training dominance, the inference market — projected to be 60%+ of AI compute spend by 2027 — faces growing substitution risk.",
        what_happened="Microsoft's Maia 200 and Google's TPU v6 demonstrated inference benchmark results within 85–92% of H200 performance at 40–60% lower cost-per-inference. Both companies announced plans to reduce external GPU procurement by 15–20% in FY2027.",
        why_it_matters="Hyperscalers represent ~50% of Nvidia's data center revenue. A 15–20% procurement reduction from this segment translates to a $15–20B annual revenue headwind at current run rates. More importantly, successful in-house inference chips validate the technical feasibility of reducing dependence — a risk that compounds if training performance also converges.",
        financial_areas=[
            FinancialArea(area="Hyperscaler Revenue Concentration", impact="negative", detail="~50% of DC revenue from top 5 customers; substitution risk materializes at the largest accounts first"),
            FinancialArea(area="Inference Market Share", impact="negative", detail="Inference TAM shift from merchant silicon to in-house solutions; Nvidia's inference revenue at risk"),
            FinancialArea(area="Pricing Power", impact="negative", detail="Competitive alternatives reduce Nvidia's premium pricing leverage on future GPU generations"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Hyperscaler GPU procurement grows 15% annually through FY2029", change="Growth rate drops to 5–8% annually; absolute procurement may decline in FY2028", magnitude="significant"),
            ModelAssumption(assumption="Nvidia inference market share stable at 80%+", change="Share may decline to 60–65% as inference workloads shift to in-house and alternative silicon", magnitude="significant"),
            ModelAssumption(assumption="GPU ASP growth of 8–12% per generation", change="Pricing power erodes; ASP growth may compress to 3–5% as alternatives provide viable substitutes", magnitude="moderate"),
        ],
        evidence="The Information reporting, corroborated by Microsoft and Google earnings call commentary on capex efficiency. MLPerf Inference 5.0 benchmark results show narrowing gap between merchant and in-house silicon.",
        next_steps=[
            "Track MLPerf benchmark submissions for training workloads — if in-house chips close the training gap, thesis deterioration accelerates",
            "Monitor hyperscaler capex guidance for GPU vs. internal silicon split",
            "Assess Nvidia's CUDA moat durability: do inference workloads need CUDA, or are they framework-portable?",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the inference vs. training revenue split in Nvidia's data center segment?", urgency="high"),
            AnalystQuestion(question="How much of the inference market is 'CUDA-locked' versus portable across frameworks?", urgency="medium"),
            AnalystQuestion(question="Is Nvidia developing an inference-as-a-service offering (DGX Cloud) to capture spend that would otherwise go in-house?", urgency="medium"),
        ],
    ),
    "sig-003": AnalystBrief(
        signal=SIGNALS[2],
        executive_summary="Nvidia delivered another record quarter with $42B in data center revenue (up 18% QoQ). The headline numbers are impressive, but the growth rate is decelerating from 25%+ QoQ in prior quarters. This is expected as the base effect compounds, but markets may misinterpret deceleration as demand saturation rather than base-effect mathematics.",
        what_happened="Nvidia reported Q1 FY2027 results: $42B data center revenue (+18% QoQ, +112% YoY), gross margin of 78.4% (+30bps QoQ), and forward guidance implying 12–15% sequential growth in Q2. Blackwell ramp is proceeding ahead of schedule.",
        why_it_matters="The earnings confirm Blackwell is a successful product cycle, but the growth deceleration narrative is gaining traction. If markets price Nvidia as a mature company rather than a hyper-growth one, the P/E multiple may compress from 45x to 30–35x even if earnings continue growing.",
        financial_areas=[
            FinancialArea(area="Data Center Revenue Growth", impact="positive", detail="$42B quarter beats consensus of $40.5B; Blackwell ramp ahead of schedule"),
            FinancialArea(area="Gross Margin", impact="positive", detail="78.4% GM demonstrates pricing power and manufacturing yield improvements"),
            FinancialArea(area="Growth Rate Trajectory", impact="neutral", detail="Sequential growth decelerating (25%→18%→~13%); natural base effect, not demand issue"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="DC revenue growth sustains 15%+ QoQ through FY2027", change="Growth likely decelerates to high single digits by Q4 FY2027 as base effect compounds", magnitude="minor"),
            ModelAssumption(assumption="Gross margin stable at 78%+", change="Maintain assumption; Blackwell architecture supports margin expansion thesis", magnitude="minor"),
        ],
        evidence="Nvidia Q1 FY2027 earnings release, investor presentation, and CFO commentary on earnings call. Consensus estimates from Visible Alpha.",
        next_steps=[
            "Track Q2 FY2027 guidance against consensus; any miss signals demand normalization faster than modeled",
            "Monitor Blackwell Ultra timeline — any delays compress the growth runway",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the expected Blackwell product cycle duration, and when does Rubin begin shipping?", urgency="medium"),
            AnalystQuestion(question="What percentage of Q1 DC revenue was from inference vs. training workloads?", urgency="medium"),
        ],
    ),
    "sig-004": AnalystBrief(
        signal=SIGNALS[3],
        executive_summary="The EU's DMA Phase 2 investigation into Apple represents the most significant regulatory threat to the Services revenue segment since the App Store was created. Potential remedies — mandatory third-party app stores, payment system interoperability, and restrictions on default app pre-installation — could reduce Services gross margin by 500–800bps and erode $8–12B in high-margin annual revenue.",
        what_happened="The European Commission opened a Phase 2 investigation under the Digital Markets Act, finding preliminary non-compliance with interoperability obligations. Potential remedies include forced third-party app store access with full API parity, mandatory support for third-party in-app payment systems, and restrictions on default app pre-installation on iOS devices sold in the EU.",
        why_it_matters="Apple's Services segment generates $100B+ annually at ~74% gross margin — it is the valuation engine that transformed Apple from a hardware multiple to a platform multiple. App Store commissions alone contribute an estimated $25–30B in near-100% margin revenue. Forced third-party payment systems could reduce effective take-rate from 15–30% to 3–5%, compressing Services segment margins materially.",
        financial_areas=[
            FinancialArea(area="Services Revenue", impact="negative", detail="$8–12B annual App Store revenue at risk from third-party payment systems and alternative stores"),
            FinancialArea(area="Services Gross Margin", impact="negative", detail="500–800bps compression if high-margin App Store commissions are displaced by lower-margin services"),
            FinancialArea(area="iPhone ASP / Ecosystem Lock-in", impact="negative", detail="Reduced switching costs weaken ecosystem retention; iPhone replacement cycles may lengthen"),
            FinancialArea(area="Legal and Compliance Expense", impact="negative", detail="Non-compliance fines of up to 10% of global annual turnover (~$38B maximum); ongoing compliance cost is more likely outcome"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Services gross margin stable at 74% through FY2029", change="Reduce to 66–69% reflecting structural App Store commission compression", magnitude="significant"),
            ModelAssumption(assumption="App Store revenue grows 8–10% annually", change="Growth drops to 2–4% or negative depending on remedy scope; ex-EU growth partially offsets", magnitude="significant"),
            ModelAssumption(assumption="iPhone installed base retention rate of 94%", change="May decline to 90–92% in EU markets if ecosystem lock-in weakens; global impact muted near-term", magnitude="moderate"),
        ],
        evidence="EC DMA Phase 2 Statement of Objections (June 2026). Apple 10-Q risk factor disclosure updated Q2 2026. Bernstein analyst note estimating Services revenue at risk: $10–14B in bear case.",
        next_steps=[
            "Monitor EC remedy timeline — Phase 2 decisions typically take 12 months, remedies 6 months after",
            "Track third-party app store adoption in EU if remedies are implemented; early data from DMA Phase 1 (browser choice screens) showed limited consumer switching",
            "Model Services revenue with EU and ex-EU decomposition; assess whether non-EU growth can offset EU compression",
        ],
        analyst_questions=[
            AnalystQuestion(question="What percentage of App Store revenue is generated from the EU (27 member states)?", urgency="high"),
            AnalystQuestion(question="What is the effective take-rate on App Store transactions after developer concessions and small business program discounts?", urgency="high"),
            AnalystQuestion(question="How sticky is the iOS installed base in markets where third-party app stores are already available (e.g., under DMA Phase 1 compliance)?", urgency="medium"),
        ],
    ),
    "sig-005": AnalystBrief(
        signal=SIGNALS[4],
        executive_summary="Apple Intelligence adoption at 34% daily active usage among iPhone 16 users is below expectations, suggesting the AI feature set has not yet created a compelling switching or upgrade driver. This has implications for the iPhone upgrade cycle thesis and the premium pricing narrative that supports Apple's hardware ASP growth.",
        what_happened="Consumer survey data indicates 34% of iPhone 16 users actively use Apple Intelligence features daily. Key features — notification summarization, writing tools, photo cleanup — show weekly churn rates of 22%, suggesting novelty rather than habit formation.",
        why_it_matters="The iPhone 16 upgrade cycle was partially premised on AI-driven demand. If Apple Intelligence does not drive upgrades, the hardware replacement cycle may extend from 3.8 years toward 4.2 years, reducing annual iPhone unit sales by 8–12M units. This shifts more of the revenue burden to Services, which is simultaneously facing regulatory headwinds (see sig-004).",
        financial_areas=[
            FinancialArea(area="iPhone Revenue", impact="negative", detail="Extended replacement cycle reduces annual unit sales by est. 8–12M; ~$8–12B revenue impact"),
            FinancialArea(area="Services Revenue", impact="uncertain", detail="AI features could eventually drive services adoption, but current usage patterns don't support this thesis"),
            FinancialArea(area="R&D Efficiency", impact="negative", detail="Significant AI R&D investment ($5B+ annually) without clear monetization path or upgrade catalyst"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="iPhone replacement cycle stable at 3.8 years", change="Extend to 4.0–4.2 years if AI features don't drive compelling upgrade motivation", magnitude="moderate"),
            ModelAssumption(assumption="iPhone ASP growth of 3–5% annually from premium mix shift", change="Premium mix may be harder to justify without differentiated AI capability; ASP growth slows to 1–2%", magnitude="moderate"),
        ],
        evidence="Bloomberg consumer survey (n=4,200, June 2026). Counterpoint Research upgrade cycle data. Apple hasn't disclosed official Apple Intelligence usage metrics, limiting verification.",
        next_steps=[
            "Track iOS 19 beta adoption and Apple Intelligence feature expansion at WWDC 2027",
            "Monitor Q3 FY2027 earnings for iPhone unit sales and ASP trends post-iPhone 16 cycle",
            "Compare Apple Intelligence adoption trajectory to Siri (2011) and Face ID (2017) adoption curves as benchmarks",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the daily active usage trend (growing, flat, or declining) rather than point-in-time measurement?", urgency="medium"),
            AnalystQuestion(question="Are Apple Intelligence users more likely to upgrade to the next iPhone, or is there no correlation?", urgency="medium"),
        ],
    ),
    "sig-006": AnalystBrief(
        signal=SIGNALS[5],
        executive_summary="FCA's proposed safeguarding rules for payment firms represent a structural compliance cost increase for Wise. With £13.8B in customer balances, the cost of daily reconciliation audits and segregated trust accounts could add £15–25M in annual operating expenses, compressing EBITDA margin by 100–150bps.",
        what_happened="The UK FCA published Consultation Paper CP26/8 proposing stricter safeguarding requirements for payment and e-money firms. Key proposals: daily reconciliation audits of customer funds, mandatory segregated trust accounts (ending the 'insurance-based safeguarding' model), and formal resolution planning requirements.",
        why_it_matters="Wise holds customer balances as an inherent part of its cross-border transfer model (funds in transit). The proposed rules increase the cost and complexity of holding these balances. While Wise's strong balance sheet position (no debt, £1.2B equity) means it can absorb the costs, the regulatory trend toward payment-firm safeguarding is global — similar rules are advancing in the EU (PSD3) and Singapore.",
        financial_areas=[
            FinancialArea(area="Operating Expenses", impact="negative", detail="Estimated £15–25M annual incremental compliance and auditing costs"),
            FinancialArea(area="EBITDA Margin", impact="negative", detail="100–150bps compression; Wise currently operates at ~23% EBITDA margin"),
            FinancialArea(area="Float Income", impact="negative", detail="Mandatory segregated trust accounts may restrict investment of customer balances, reducing interest income by £8–12M annually"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Operating expense growth rate of 15% YoY", change="Increase to 18–20% to absorb incremental compliance headcount and audit costs", magnitude="minor"),
            ModelAssumption(assumption="Float income at 3.2% yield on customer balances", change="Yield may compress to 2.5–2.8% if investment restrictions apply to segregated accounts", magnitude="moderate"),
        ],
        evidence="FCA CP26/8 published June 10, 2026. Wise's most recent annual report confirms £13.8B in customer balances. Industry consultation responses due September 2026.",
        next_steps=[
            "Track FCA consultation responses from Wise and industry bodies; final rules expected Q1 2027",
            "Monitor PSD3 safeguarding provisions in EU for parallel regulatory impact",
            "Model Wise's exposure to interest income on customer balances and sensitivity to restricted investment",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is Wise's current safeguarding mechanism, and how much would a trust-account model cost per £1B of customer balances?", urgency="high"),
            AnalystQuestion(question="Is Wise's float income material enough to disclose, and what is the current yield on those balances?", urgency="medium"),
        ],
    ),
    "sig-007": AnalystBrief(
        signal=SIGNALS[6],
        executive_summary="Wise's expansion into 12 new markets for business multi-currency accounts is a strong strategic move that improves revenue mix. Business accounts now contribute 28% of revenue at 2.8x the take-rate of consumer accounts. If business segment reaches 40% of revenue, blended take-rate improves by 15–20%.",
        what_happened="Wise launched business multi-currency accounts in Brazil, Mexico, Indonesia, South Africa, and 8 additional markets. The business segment revenue contribution grew from 22% to 28% over 12 months. Business customers generate 2.8x the revenue per transaction versus consumer accounts.",
        why_it_matters="The business segment is Wise's highest-quality revenue: stickier customers, larger transaction volumes, higher take-rates, and lower churn. Expansion into emerging markets with underserved SME cross-border payment needs opens a TAM that traditional banks serve poorly. If execution continues, business could become the majority revenue contributor within 3–4 years, fundamentally re-rating Wise's growth multiple.",
        financial_areas=[
            FinancialArea(area="Revenue Mix", impact="positive", detail="Business segment at 28% of revenue (+6pp YoY); trajectory toward 35%+ in FY2028"),
            FinancialArea(area="Blended Take Rate", impact="positive", detail="Business take-rate 2.8x consumer implies 15–20% blended improvement as mix shifts"),
            FinancialArea(area="Customer Acquisition Cost", impact="positive", detail="Business CAC is higher but LTV:CAC ratio is 4.2x vs. 2.8x for consumer (retention rates significantly better)"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Blended revenue take-rate of 0.65%", change="Improve to 0.72–0.78% as business segment grows to 35%+ of revenue", magnitude="moderate"),
            ModelAssumption(assumption="Business revenue growth of 30% YoY", change="Maintain or increase; new market expansion provides additional growth vector beyond existing markets", magnitude="minor"),
        ],
        evidence="Wise blog post and Q4 FY2026 shareholder update. Revenue segment disclosure in annual report.",
        next_steps=[
            "Track quarterly business revenue contribution to monitor mix shift trajectory",
            "Compare Wise's business take-rate to competing SME cross-border solutions (Airwallex, Payoneer) for competitive positioning",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the payback period on business customer acquisition in new markets vs. existing markets?", urgency="low"),
            AnalystQuestion(question="How does Wise's business account feature set compare to Airwallex and Revolut Business for SME customers?", urgency="medium"),
        ],
    ),
    "sig-008": AnalystBrief(
        signal=SIGNALS[7],
        executive_summary="Revolut securing a UK banking licence is a transformative milestone that unlocks deposit-taking, direct lending, and deposit insurance coverage. The restricted mobilisation phase (£50K deposit cap) limits near-term revenue impact, but the licence validates Revolut's regulatory maturity and opens the largest retail banking product gap in its portfolio.",
        what_happened="The Prudential Regulation Authority (PRA) granted Revolut a UK banking licence with mobilisation restrictions: £50K individual deposit cap for the first 12 months, monthly prudential reporting requirements, and restrictions on certain lending activities. Revolut can now offer FSCS-protected deposits and begin building lending products.",
        why_it_matters="Without a banking licence, Revolut was structurally limited to payment and trading products. The licence enables: (1) deposit-taking with FSCS protection, which typically increases customer balance retention 3–5x; (2) consumer and SME lending products (credit cards, personal loans, business loans), which carry 4–8% net interest margins; (3) improved unit economics as lending revenue diversifies away from volatile interchange and trading income.",
        financial_areas=[
            FinancialArea(area="Deposit Growth", impact="positive", detail="FSCS protection removes the primary objection for Revolut as a primary bank; deposit balances could 2–3x within 24 months"),
            FinancialArea(area="Net Interest Income", impact="positive", detail="Lending products represent a new high-margin revenue stream; potential £200–400M annual NII at scale"),
            FinancialArea(area="Revenue Diversification", impact="positive", detail="Reduces reliance on interchange (60%+ of current revenue) and crypto trading (volatile, recently declining)"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Primary revenue from interchange and subscription fees; lending not modeled", change="Add lending revenue stream; £80–150M NII in first full year post-restrictions, scaling to £300–500M by year 3", magnitude="significant"),
            ModelAssumption(assumption="Deposit balances grow 25% annually", change="Growth accelerates to 40–60% with FSCS protection as adoption barrier removed", magnitude="significant"),
        ],
        evidence="PRA banking licence announcement and Revolut press release (April 28, 2026). Revolut's most recent annual report on revenue composition.",
        next_steps=[
            "Track deposit balance growth in quarterly updates for acceleration from FSCS coverage",
            "Monitor Revolut's lending product launch timeline and initial credit quality metrics",
            "Compare deposit growth trajectory to Monzo and Starling post-licence benchmarks",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the timeline for full licence authorisation (unrestricted), and what conditions must Revolut meet?", urgency="high"),
            AnalystQuestion(question="What is Revolut's current customer deposit balance, and what percentage use Revolut as their primary bank account?", urgency="high"),
        ],
    ),
    "sig-009": AnalystBrief(
        signal=SIGNALS[8],
        executive_summary="Revolut's crypto revenue declining from 14% to 8% of revenue is a positive signal for business quality, not a negative. Crypto trading revenue is high-volatility, low-quality income that inflated 2024 results. The decline reflects a healthier revenue mix shifting toward recurring interchange and subscription revenue.",
        what_happened="Crypto trading revenue fell 40% in Q1 2026 versus Q1 2025, dropping from 14% of total revenue to 8%. The decline is attributed to sector-wide retail crypto volume contraction following SEC enforcement actions and reduced retail interest in meme-coin speculation.",
        why_it_matters="Crypto revenue is unpredictable, regulatory-sensitive, and commands lower valuation multiples. Revenue diversification away from crypto makes Revolut's financial profile more predictable and 'bank-like,' which supports re-rating as the company prepares for a potential IPO. Analysts should welcome this trend, not penalize it.",
        financial_areas=[
            FinancialArea(area="Revenue Quality", impact="positive", detail="Recurring revenue (interchange, subscriptions) proportion increases as volatile crypto share declines"),
            FinancialArea(area="Total Revenue Growth", impact="negative", detail="Headline growth rate declines due to crypto base effect; core revenue (ex-crypto) likely still growing 30%+"),
            FinancialArea(area="Valuation Multiple", impact="positive", detail="Lower crypto exposure supports higher revenue multiple in IPO pricing; fintech comps trade at 8–12x vs. crypto-exposed 5–7x"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Crypto revenue stable at 12–14% of total", change="Reduce to 6–8% and model as low-confidence, high-variance line item; exclude from core revenue growth calculation", magnitude="moderate"),
            ModelAssumption(assumption="Total revenue growth of 35% YoY", change="Ex-crypto core revenue growth likely 30–35%; total reported growth may be 20–25% with crypto drag", magnitude="minor"),
        ],
        evidence="CNBC reporting corroborated by publicly available crypto exchange volume data (CoinGecko, The Block). Revolut hasn't separately disclosed crypto revenue historically but is expected to in pre-IPO filings.",
        next_steps=[
            "Separate Revolut's revenue into core (interchange, subscriptions, interest) and volatile (crypto, trading) for modeling",
            "Track Revolut's pre-IPO financial disclosures for granular revenue breakdown",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is Revolut's total revenue excluding crypto, and what is the growth rate of that core revenue?", urgency="medium"),
            AnalystQuestion(question="Is Revolut planning to reduce or de-emphasize crypto product offerings, or maintain them as a feature?", urgency="low"),
        ],
    ),
    "sig-010": AnalystBrief(
        signal=SIGNALS[9],
        executive_summary="Adyen winning Amazon's European payment processing contract is a landmark enterprise deal. Estimated €45B in annual processed volume at 18–22bps gross margin adds €80–100M in annual gross profit. Beyond the revenue, it signals that the world's most demanding e-commerce platform chose Adyen over incumbent processors — a powerful proof point for the unified commerce platform thesis.",
        what_happened="Adyen won a multi-year contract to process payments for Amazon across 12 European markets, displacing the incumbent processor. The deal covers Amazon's e-commerce, Prime Video, and AWS marketplace payment flows. Total addressable volume is estimated at €45B annually.",
        why_it_matters="Amazon is the most technically demanding merchant in e-commerce: it requires sub-50ms authorization latency, 99.999% uptime, and support for 30+ local payment methods. Winning this contract validates Adyen's single-platform architecture against competitors who stitch together acquisitions. It also provides a reference case for other large enterprise RFPs.",
        financial_areas=[
            FinancialArea(area="Processed Volume", impact="positive", detail="€45B incremental annual volume; ~5% uplift on Adyen's total processed volume of ~€900B"),
            FinancialArea(area="Gross Profit", impact="positive", detail="€80–100M incremental annual gross profit at enterprise take-rate (18–22bps)"),
            FinancialArea(area="Enterprise Sales Pipeline", impact="positive", detail="Amazon reference case accelerates enterprise pipeline conversion; halo effect on competing RFPs"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Processed volume growth of 20% YoY to ~€900B in FY2027", change="Increase to 23–25% reflecting Amazon ramp through FY2027", magnitude="moderate"),
            ModelAssumption(assumption="Net revenue take-rate stable at 16bps", change="Slight upward bias if enterprise mix (higher margin) continues growing faster than SMB", magnitude="minor"),
        ],
        evidence="Reuters reporting, Adyen not yet disclosed in filings. Amazon's European payment volume estimated from e-commerce market share data (Edge by Ascential) and Amazon's disclosed EU revenue segments.",
        next_steps=[
            "Confirm Amazon contract in Adyen's H2 2026 shareholder letter or next earnings call",
            "Re-forecast FY2027 processed volume with Amazon ramp timing assumptions (likely phased by market over 6–12 months)",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the contract duration and renewal structure?", urgency="medium"),
            AnalystQuestion(question="Does Amazon maintain a multi-processor strategy, or is Adyen the exclusive European processor?", urgency="medium"),
        ],
    ),
    "sig-011": AnalystBrief(
        signal=SIGNALS[10],
        executive_summary="Adyen's accelerated engineering hiring (850 vs. planned 500 in H1 2026) is compressing near-term EBITDA margin (43% vs. 48% target). Management frames this as growth investment; the key question is whether the hiring supports incremental revenue-generating products or is defensive catch-up. Adyen's historical discipline on headcount suggests benefit of the doubt, but watch for margin trajectory in H2.",
        what_happened="Adyen added 850 engineers in H1 2026, significantly exceeding the planned 500. The hiring surge pushed EBITDA margin to 43% (below the 48% target and 2025's 49%). Management attributes the hiring to accelerating product development across embedded finance, in-person payments, and AI-driven fraud detection.",
        why_it_matters="Adyen is known for operational discipline — running a payments platform handling €900B in volume with fewer than 4,200 total employees is an efficiency benchmark. A hiring surge signals either: (1) genuine growth opportunity requiring investment (bull case), or (2) creeping operational bloat (bear case). Historical pattern favors the bull case: Adyen invested ahead of growth in 2017–2019 and captured disproportionate enterprise share.",
        financial_areas=[
            FinancialArea(area="EBITDA Margin", impact="negative", detail="43% in H1 2026 vs. 49% in FY2025; 600bps compression, half from hiring and half from infrastructure scaling"),
            FinancialArea(area="Operating Expenses", impact="negative", detail="Engineering headcount cost: ~€80M incremental annual run-rate from 350 additional hires"),
            FinancialArea(area="Product Velocity", impact="positive", detail="Faster time-to-market for embedded finance and AI products; revenue benefit materializes in FY2028"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="EBITDA margin stable at 48–50% through FY2028", change="Dip to 44–46% in FY2027, recovering to 47–49% in FY2028 as revenue from new products scales", magnitude="moderate"),
            ModelAssumption(assumption="Headcount growth of 15% annually", change="FY2026 headcount growth likely 22–25%; revert to 15% trend in FY2027", magnitude="minor"),
        ],
        evidence="Adyen H1 2026 Letter to Shareholders. Historical headcount data shows Adyen's discipline: 2019–2024 headcount CAGR of 18% while volume CAGR was 35%.",
        next_steps=[
            "Track Adyen's H2 FY2026 results for EBITDA margin recovery signal",
            "Monitor new product launches (embedded finance, AI fraud detection) as leading indicators of revenue return on hiring investment",
        ],
        analyst_questions=[
            AnalystQuestion(question="What specific products or features did the 350 incremental engineers work on?", urgency="medium"),
            AnalystQuestion(question="What is Adyen's revenue-per-employee trajectory, and at what point does it recover to 2025 levels?", urgency="medium"),
        ],
    ),
    "sig-012": AnalystBrief(
        signal=SIGNALS[11],
        executive_summary="Basel IV final rules requiring $45–55B in additional CET1 capital for JPMorgan is a material return-on-equity headwind. JPMorgan will likely fund the requirement through a combination of retained earnings (reducing buybacks), RWA optimization, and balance sheet restructuring. Estimated impact: 150–200bps RoTCE compression over the phase-in period.",
        what_happened="The Federal Reserve finalized Basel IV Endgame rules for Global Systemically Important Banks (GSIBs). JPMorgan, as the largest US GSIB, faces an estimated $45–55B in additional CET1 capital requirements. Rules phase in starting January 2028 over a 3-year period.",
        why_it_matters="JPMorgan currently operates at ~15% CET1 ratio versus a ~13.5% requirement under the new rules (up from ~11.5% currently). The $45–55B capital gap must be filled through: (1) retained earnings (~$50B annual net income means 3–4 quarters of retention covers it), (2) RWA reduction (moving assets off balance sheet or into lower risk-weight categories), or (3) reduced capital return (buybacks are the flexible lever).",
        financial_areas=[
            FinancialArea(area="Return on Tangible Common Equity (RoTCE)", impact="negative", detail="150–200bps compression; JPMorgan's 21% RoTCE may decline to 19% if capital base expands"),
            FinancialArea(area="Share Buybacks", impact="negative", detail="Estimated $5–8B annual buyback reduction to retain earnings for capital building"),
            FinancialArea(area="Risk-Weighted Assets", impact="uncertain", detail="RWA optimization can reduce capital requirement by $10–15B; depends on regulatory interpretation"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Annual buybacks of $20–25B through FY2029", change="Reduce to $12–17B during phase-in period (FY2028–2030) to retain capital", magnitude="moderate"),
            ModelAssumption(assumption="RoTCE stable at 20–22%", change="Reduce to 18–20% reflecting expanded equity base; still above 15% cost of equity threshold", magnitude="moderate"),
        ],
        evidence="Federal Reserve final rule (June 12, 2026). JPMorgan 10-K risk disclosure updated Q1 2026 with preliminary Basel IV impact estimates.",
        next_steps=[
            "Monitor JPMorgan's Q2 FY2026 earnings call for management's Basel IV capital plan",
            "Track RWA trajectory in quarterly filings for optimization execution",
            "Compare JPMorgan's capital gap to peer GSIBs (BAC, C, GS, MS) for relative positioning",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is management's preferred approach for meeting Basel IV requirements: retained earnings, RWA optimization, or both?", urgency="high"),
            AnalystQuestion(question="How much of JPMorgan's trading book RWA is eligible for optimization under the new standardized approach?", urgency="medium"),
        ],
    ),
    "sig-013": AnalystBrief(
        signal=SIGNALS[12],
        executive_summary="JPMorgan's AI-driven FX trading desk expansion to 45% of flow (up from 28%) is a margin tailwind. Algorithmic execution improves spread capture by 3.2bps and reduces voice trader headcount by 12%. Extrapolating to the full FICC trading business suggests $400–600M in annual cost savings and margin improvement at scale.",
        what_happened="JPMorgan's AI-powered FX algorithmic trading now handles 45% of customer FX flow, up from 28% in 2025. The AI system improved spread capture by 3.2bps on algorithmic flow and reduced voice trading headcount by 12% YoY.",
        why_it_matters="FICC trading is JPMorgan's largest revenue segment (~$24B in 2025). If the AI model's success in FX (the most liquid market) extends to rates, credit, and commodities, the margin improvement opportunity is substantial. Each 1% shift from voice to algorithmic execution improves FICC cost/income ratio by ~30bps.",
        financial_areas=[
            FinancialArea(area="FICC Revenue Quality", impact="positive", detail="3.2bps spread capture improvement on 45% of FX flow; higher capture rate on algorithmic vs. voice execution"),
            FinancialArea(area="Compensation Ratio", impact="positive", detail="12% voice trader headcount reduction reduces compensation expense; FICC comp ratio improves 80–120bps"),
            FinancialArea(area="Technology Investment", impact="negative", detail="AI infrastructure buildout requires $200–300M annual incremental tech spend; treated as investment, not expense drag"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="FICC cost/income ratio stable at 42%", change="Improve to 39–40% as algorithmic execution scales; AI-driven efficiency is structural, not cyclical", magnitude="moderate"),
            ModelAssumption(assumption="FICC headcount declines 3% annually from natural attrition", change="Accelerate to 5–7% annual reduction as AI handles larger share of flow; retraining, not layoffs", magnitude="minor"),
        ],
        evidence="Risk.net reporting and JPMorgan investor day presentation (May 2026). FX algo trading market share data from Euromoney FX Survey corroborates JPMorgan's leading position.",
        next_steps=[
            "Track JPMorgan's FICC revenue per trader metric for evidence of AI productivity gains",
            "Monitor extension of AI execution to rates and credit markets — larger, less liquid markets where AI advantage may be greater or smaller",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the revenue contribution of algorithmic flow vs. voice flow in FX, controlling for volume?", urgency="medium"),
            AnalystQuestion(question="Is the AI execution model proprietary or vendor-licensed, and what is the competitive durability of this advantage?", urgency="medium"),
        ],
    ),
    "sig-014": AnalystBrief(
        signal=SIGNALS[13],
        executive_summary="JPMorgan's $2.1B increase in loan loss provisions for CRE exposure signals that office real estate stress is not yet fully resolved. At 8.2% of total loans, CRE is a manageable but non-trivial exposure. The provision increase is prudent rather than alarming — it reflects deteriorating collateral values rather than default events — but signals that the 'soft landing' narrative for CRE is optimistic.",
        what_happened="JPMorgan increased loan loss provisions by $2.1B in Q2 2026, with $1.4B allocated to commercial real estate (primarily office properties). CRE represents 8.2% of JPM's $1.3T loan book. The provisions reflect updated collateral valuations showing 30–40% decline in office property values from 2022 peaks.",
        why_it_matters="JPMorgan's CRE exposure is heavily weighted toward Class A office in primary markets (NYC, SF, LA) — the segment under most stress from remote work and higher interest rates. The provision increase signals that: (1) refinancing risk at higher rates is material, (2) property valuations haven't bottomed, and (3) credit normalization is underway after 3 years of artificially low charge-offs.",
        financial_areas=[
            FinancialArea(area="Credit Costs", impact="negative", detail="$2.1B provision increase reduces pre-tax income by ~$1.6B; ~3.5% of quarterly net income"),
            FinancialArea(area="Net Charge-Off Rate", impact="negative", detail="CRE charge-off rate expected to rise from 0.15% to 0.40–0.60% over next 4 quarters"),
            FinancialArea(area="Capital Adequacy", impact="neutral", detail="Provision increase is well within JPM's CCAR stress test buffer; not a capital adequacy concern"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Net charge-off rate stable at 35–40bps", change="Increase to 50–60bps in FY2027 reflecting CRE normalization; still below 2019's 65bps", magnitude="minor"),
            ModelAssumption(assumption="Provision for credit losses at $6–7B annually", change="Increase to $9–10B in FY2027; represents normalization, not crisis-level credit losses", magnitude="minor"),
        ],
        evidence="JPMorgan 10-Q filing (Q2 2026). FRB Financial Stability Report (May 2026) confirming CRE as top systemic risk. MSCI Real Assets data on office property value declines.",
        next_steps=[
            "Track quarterly CRE charge-off rate for leading indicator of credit cycle direction",
            "Compare JPM's CRE reserve coverage ratio to peers (BAC, WFC) for relative conservatism",
            "Monitor office property transaction volume and cap rates for collateral value stabilization signals",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the loan-to-value distribution of JPMorgan's CRE portfolio at current property valuations?", urgency="high"),
            AnalystQuestion(question="What percentage of CRE loans mature in the next 12–24 months and face refinancing at higher rates?", urgency="high"),
        ],
    ),
    "sig-015": AnalystBrief(
        signal=SIGNALS[14],
        executive_summary="Salesforce's Agentforce 2.0 launch positions the company in the autonomous AI agent market at a $3/conversation price point. This is a strategic product shift from per-seat SaaS pricing to consumption-based AI pricing. If successful, it opens a new $50B+ TAM but also cannibalizes existing seat-based revenue as customers reduce seat counts when AI agents handle work previously done by humans using Salesforce seats.",
        what_happened="Agentforce 2.0 introduces autonomous AI agents for customer service, sales qualification, and marketing campaign optimization. Early enterprise pilots show 40% ticket deflection in customer service and 25% improvement in lead qualification speed. Priced at $3 per conversation with volume discounts.",
        why_it_matters="Salesforce faces a structural challenge: AI automation reduces the need for human users, which reduces seat counts — the traditional SaaS revenue model. Agentforce is Salesforce's answer: capture the AI value directly through consumption pricing rather than losing it to seat count erosion. The $3/conversation pricing implies $0.30–0.50/hour of agent productivity, compared to $15–30/hour for human agents — a compelling ROI even before considering quality improvements.",
        financial_areas=[
            FinancialArea(area="Revenue Model Transition", impact="uncertain", detail="Shift from per-seat (predictable) to consumption-based (variable); revenue becomes harder to forecast but potentially larger TAM"),
            FinancialArea(area="Seat Count Cannibalization", impact="negative", detail="Existing customers may reduce seat counts as AI agents handle work; Q1 FY2027 showed first organic growth below 10%"),
            FinancialArea(area="New TAM Expansion", impact="positive", detail="AI agent market projected at $50B+ by 2028; Salesforce's installed base of 150K+ customers is a distribution advantage"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Subscription revenue growth of 9–10% annually", change="Add Agentforce consumption revenue stream; blended growth could be 12–15% if adoption is strong, or 6–8% if cannibalization dominates", magnitude="significant"),
            ModelAssumption(assumption="Seat count growth of 5% annually", change="Seat counts may be flat to negative; revenue growth becomes dependent on Agentforce consumption uptake", magnitude="significant"),
        ],
        evidence="Salesforce press release (June 2026) and Agentforce 2.0 product documentation. Dreamforce 2025 keynote outlined product roadmap. Pilot data from 12 enterprise customers in Salesforce's FY2027 investor presentation.",
        next_steps=[
            "Track Agentforce customer count and consumption volume in quarterly earnings for adoption trajectory",
            "Separate Salesforce revenue into 'seat-based' and 'consumption-based' for modeling transition dynamics",
            "Compare Agentforce pricing and capabilities to competing AI agent platforms (Microsoft Copilot, ServiceNow AI, startup ecosystem)",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the gross margin on Agentforce consumption revenue vs. traditional subscription revenue?", urgency="high"),
            AnalystQuestion(question="Are early Agentforce adopters reducing their seat counts, and if so, by what percentage?", urgency="high"),
        ],
    ),
    "sig-016": AnalystBrief(
        signal=SIGNALS[15],
        executive_summary="Salesforce's organic revenue growth dropping below 10% for the first time is a milestone event that forces a reassessment of the growth algorithm. The cause is partially structural (AI reducing seat needs) and partially cyclical (enterprise software budget scrutiny). Management's pivot to Agentforce consumption pricing is the strategic response, but the transition creates a 'growth valley' where legacy revenue decelerates faster than new revenue ramps.",
        what_happened="Salesforce reported Q1 FY2027 organic constant-currency revenue growth of 8.7%, the first sub-10% quarter in company history. Management attributed deceleration to: (1) seat count rationalization as AI tools enable fewer seats per customer, and (2) enterprise deal scrutiny extending sales cycles.",
        why_it_matters="Salesforce has been the bellwether for enterprise SaaS growth. Sub-10% organic growth crosses a psychological threshold that may trigger multiple compression — SaaS companies historically trade at 8–12x revenue when growing 20%+, but comps compress to 5–7x when growth falls below 10%. Salesforce's 28x P/E may face de-rating if growth doesn't re-accelerate through Agentforce.",
        financial_areas=[
            FinancialArea(area="Revenue Growth Rate", impact="negative", detail="8.7% organic growth vs. 11% consensus; 230bps miss signals structural deceleration, not just cyclical"),
            FinancialArea(area="Operating Margin", impact="positive", detail="Margin expansion from headcount rationalization offsets some revenue growth pain; operating margin improved to 33.5%"),
            FinancialArea(area="Valuation Multiple", impact="negative", detail="Risk of P/E compression from 28x to 20–24x if market re-rates Salesforce as a value stock rather than growth"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Revenue growth of 10–12% in FY2027", change="Reduce to 8–9% organic; Agentforce contribution could add 2–3pp if adoption accelerates in H2", magnitude="significant"),
            ModelAssumption(assumption="P/E multiple of 26–28x forward earnings", change="Compression to 20–24x if growth remains sub-10% for two consecutive quarters; downside to $240–260 share price", magnitude="significant"),
        ],
        evidence="Salesforce Q1 FY2027 earnings release and CFO commentary. Consensus from Visible Alpha and FactSet.",
        next_steps=[
            "Track Q2 FY2027 organic growth for second data point confirming or refuting structural deceleration thesis",
            "Model Agentforce contribution to revenue as separate line item; assess whether it can re-accelerate blended growth to 12%+",
        ],
        analyst_questions=[
            AnalystQuestion(question="What is the dollar retention rate excluding seat count reductions? I.e., are existing customers expanding spend through new products even as they reduce seats?", urgency="high"),
            AnalystQuestion(question="What percentage of the growth deceleration is from deliberate seat count optimization vs. competitive losses to Microsoft Dynamics?", urgency="medium"),
        ],
    ),
    "sig-017": AnalystBrief(
        signal=SIGNALS[16],
        executive_summary="CrowdStrike crossing $5B ARR with 27% growth and Falcon Flex driving higher net retention (124%) is a strong positive signal after the April 2026 incident. The Falcon Flex modular licensing model is proving to be a structural improvement in unit economics — customers adopt more modules over time, increasing land-and-expand efficiency.",
        what_happened="CrowdStrike reported Q1 FY2027 results: $5B+ ARR (+27% YoY), net retention of 124%, and Falcon Flex (modular licensing) now accounting for 35% of new ARR. The company added $285M in net new ARR, indicating demand resilience following the April supply-chain incident.",
        why_it_matters="CrowdStrike's ability to maintain 27% ARR growth post-incident demonstrates: (1) high switching costs in endpoint security (enterprises can't easily replace deployed agents), (2) the Falcon Flex model's effectiveness — customers adopt more modules instead of evaluating competitors, and (3) cybersecurity spending remains non-discretionary even when a vendor has an incident, as long as response is competent.",
        financial_areas=[
            FinancialArea(area="Annual Recurring Revenue", impact="positive", detail="$5B milestone with 27% growth; net new ARR of $285M in Q1 shows demand resilience"),
            FinancialArea(area="Net Dollar Retention", impact="positive", detail="124% NDR is among best-in-class for enterprise SaaS; Falcon Flex drives module expansion within existing accounts"),
            FinancialArea(area="Post-Incident Churn Risk", impact="uncertain", detail="Q2 FY2027 renewal cohort is the first to include post-incident decisions; watch for elevated churn in H2"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="ARR growth decelerates to 20% in FY2027 due to incident headwinds", change="Maintain 25–27% growth; incident impact appears contained to remediation costs rather than demand destruction", magnitude="significant"),
            ModelAssumption(assumption="Net retention declines to 118–120% post-incident", change="124% NDR suggests incident had minimal retention impact; maintain 122–125% assumption", magnitude="moderate"),
        ],
        evidence="CrowdStrike Q1 FY2027 earnings release. Morgan Stanley and Goldman Sachs post-earnings research notes upgrading ARR growth estimates. Gartner EDR Magic Quadrant showing CrowdStrike maintaining leadership position.",
        next_steps=[
            "Track Q2 FY2027 renewal cohort (first post-incident renewals) for elevated churn signal",
            "Monitor Falcon Flex module adoption rate — the key metric for NDR sustainability",
        ],
        analyst_questions=[
            AnalystQuestion(question="What percentage of the Q1 $285M net new ARR came from new customers vs. existing customer expansion?", urgency="medium"),
            AnalystQuestion(question="Is there any concentration of Falcon Flex adoption in specific modules (identity, cloud, SIEM), or is it broad-based?", urgency="medium"),
        ],
    ),
    "sig-018": AnalystBrief(
        signal=SIGNALS[17],
        executive_summary="CrowdStrike's supply-chain incident — a nation-state actor exploiting the Falcon sensor update channel — is the most significant operational risk event in endpoint security since the SolarWinds attack. The $180M estimated financial impact is manageable (~2 quarters of free cash flow), but the reputational question is whether enterprise trust in the Falcon update mechanism is permanently impaired.",
        what_happened="A sophisticated nation-state actor exploited CrowdStrike's Falcon sensor update channel to deploy a malicious content update to fewer than 200 enterprise customers. CrowdStrike detected and remediated within 72 hours, and no customer data exfiltration was confirmed. Estimated financial impact: $180M in remediation, customer concessions, and legal reserves.",
        why_it_matters="This is an existential category of risk for any security vendor: your distribution channel becomes the attack vector. The 72-hour detection and remediation timeline is industry-leading, and the containment to <200 customers (out of 29,000+) demonstrates detection capability. However, procurement and security teams will now add 'update channel security' to their vendor assessment frameworks, which could slow new customer acquisition.",
        financial_areas=[
            FinancialArea(area="Remediation Costs", impact="negative", detail="$180M one-time impact; ~$120M in Q1 FY2027 (recognized immediately), ~$60M reserved for legal and concessions"),
            FinancialArea(area="Customer Acquisition Cost", impact="negative", detail="New customer acquisition likely harder for 2–3 quarters as prospects add security review for update mechanism"),
            FinancialArea(area="Competitive Positioning", impact="uncertain", detail="Competitors (SentinelOne, Microsoft) will exploit the incident in sales cycles; actual switching is limited by deployment friction"),
        ],
        model_assumptions=[
            ModelAssumption(assumption="Operating margin of 22% in FY2027", change="Reduce to 18–19% to absorb incident costs; recovery to 22%+ in FY2028 if no further incidents", magnitude="moderate"),
            ModelAssumption(assumption="Customer acquisition growth of 15% annually", change="Acquisition may slow to 8–10% in FY2027 as prospects extend evaluation cycles; recovery in FY2028", magnitude="moderate"),
            ModelAssumption(assumption="Gross retention rate of 98%", change="Maintain; switching costs in endpoint security are high; incident is unlikely to drive material churn", magnitude="minor"),
        ],
        evidence="CrowdStrike incident response blog (April 2026) and SEC 8-K filing. Mandiant attribution report linking the attack to a known APT group. CrowdStrike Q1 FY2027 earnings confirming $120M in recognized remediation costs.",
        next_steps=[
            "Track customer count in Q2 FY2027 earnings for first evidence of acquisition slowdown",
            "Monitor competitor earnings calls (SentinelOne, Microsoft) for evidence of share gains from CrowdStrike incident",
            "Watch for CrowdStrike's technical remediation (update channel redesign) and customer communication on security improvements",
        ],
        analyst_questions=[
            AnalystQuestion(question="What specific technical changes has CrowdStrike made to the Falcon update channel to prevent recurrence?", urgency="high"),
            AnalystQuestion(question="How many of the <200 affected customers have indicated intent to churn vs. accept remediation?", urgency="high"),
            AnalystQuestion(question="Is there insurance coverage for the $180M incident cost, or is it entirely self-funded?", urgency="medium"),
        ],
    ),
}

# ── Post-processing enrichment ─────────────────────────────────────────
_SOURCE_TYPES: dict[str, str] = {
    "Reuters": "financial-news",
    "The Information": "financial-news",
    "Nvidia Investor Relations": "company-press-release",
    "Financial Times": "financial-news",
    "Bloomberg": "financial-news",
    "FCA Consultation Paper": "regulator",
    "Wise Blog": "company-press-release",
    "BBC News": "financial-news",
    "CNBC": "financial-news",
    "Adyen H1 2026 Letter to Shareholders": "company-press-release",
    "Federal Reserve Press Release": "regulator",
    "Risk.net": "niche-financial",
    "JPMorgan 10-Q Filing": "company-filing",
    "Salesforce Press Release": "company-press-release",
    "Salesforce Q1 FY2027 Earnings": "company-filing",
    "CrowdStrike Q1 FY2027 Results": "company-filing",
    "CrowdStrike Incident Blog + SEC 8-K Filing": "company-filing",
}

_CONFIDENCE_RATIONALES: dict[str, str] = {
    "sig-001": "Government policy announcement with documented corporate impact via 8-K filing and analyst consensus revisions.",
    "sig-002": "Multiple hyperscaler earnings calls corroborate in-house chip investment. Medium confidence reflects uncertainty about procurement reduction magnitude.",
    "sig-003": "Official company earnings release. Highest confidence — numbers are audited and publicly filed.",
    "sig-004": "Official EC regulatory action with published Statement of Objections. High confidence reflects formal legal process.",
    "sig-005": "Consumer survey data with 4,200 respondents. Lower confidence reflects survey methodology limitations and Apple non-disclosure.",
    "sig-006": "Official FCA consultation paper. Medium-high confidence reflects formal regulatory process, though final rules may differ.",
    "sig-007": "Official company announcement via Wise's own blog. High confidence as company-disclosed data.",
    "sig-008": "Official PRA regulatory action confirmed by BBC. Highest confidence — formal regulator announcement.",
    "sig-009": "CNBC reporting corroborated by public crypto exchange volume data. Medium confidence reflects limited Revolut-specific disclosure.",
    "sig-010": "Reuters reporting, not yet confirmed in Adyen shareholder filings. Medium-high pending formal confirmation.",
    "sig-011": "Official company shareholder letter. High confidence as company-disclosed financial data.",
    "sig-012": "Official Federal Reserve final rule publication. Highest confidence — formal regulatory action.",
    "sig-013": "Niche financial publication (Risk.net) reporting. Medium confidence reflects limited corroborating sources.",
    "sig-014": "Official 10-Q filing. High confidence as audited filed data, though provision estimates involve judgment.",
    "sig-015": "Official company press release. Medium-high confidence — product launched but revenue impact unproven.",
    "sig-016": "Official company earnings release. High confidence as filed financial data.",
    "sig-017": "Official company earnings release. High confidence as audited filed data.",
    "sig-018": "Official SEC 8-K filing and company incident blog. Highest confidence — mandatory disclosure with legal liability.",
}

_WHAT_IS_UNKNOWN: dict[str, str] = {
    "sig-001": "Exact revenue exposure by geography is not publicly disclosed by Nvidia. Duration and final scope of export restrictions remain subject to political negotiation.",
    "sig-002": "Actual procurement reduction by hyperscalers may differ from announced plans. In-house chip training performance vs. Nvidia remains an open question.",
    "sig-003": "Whether growth deceleration is purely base effect or signals demand saturation. Forward guidance accuracy given geopolitical and supply chain uncertainty.",
    "sig-004": "Final EC remedies not yet determined (typically 12-18 months). Apple may negotiate compliance terms. Consumer adoption of third-party stores under DMA Phase 1 has been limited.",
    "sig-005": "Apple has not disclosed official AI feature usage metrics. Survey data may not be representative. Correlation between AI usage and upgrade intent is unproven.",
    "sig-006": "Final FCA rules subject to consultation responses. Exact compliance cost for Wise is estimable but not confirmed.",
    "sig-007": "Business account CAC in new markets not disclosed. Competitive responses from Airwallex, Payoneer, Revolut Business are unknown.",
    "sig-008": "Full unrestricted banking licence timeline uncertain. Revolut pre-IPO disclosures have not yet provided granular deposit or lending data.",
    "sig-009": "Revolut does not publicly disclose crypto revenue as separate line item. Whether Revolut plans to de-emphasize crypto products is unknown.",
    "sig-010": "Adyen has not yet confirmed Amazon contract in shareholder communications. Contract duration, renewal structure, and exclusivity are unknown.",
    "sig-011": "Long-term revenue return on engineering hiring investment is unproven. EBITDA margin recovery timeline is management guidance, not confirmed.",
    "sig-012": "JPMorgan's preferred capital-building approach not publicly detailed. RWA optimization potential depends on regulatory interpretation.",
    "sig-013": "Whether AI trading advantage extends beyond FX to rates/credit is unproven. Competitive durability unknown — other banks may replicate.",
    "sig-014": "Loan-to-value distribution of CRE portfolio at current valuations not disclosed. Percentage of CRE loans maturing in 12-24 months is unknown.",
    "sig-015": "Agentforce revenue not separately disclosed. Cannibalization of seat-based revenue vs. net new consumption revenue is unproven.",
    "sig-016": "Split between deliberate seat optimization and competitive losses not disclosed. Whether Agentforce can re-accelerate blended growth is unproven.",
    "sig-017": "Post-incident renewal cohorts not yet reported. Concentration of Falcon Flex adoption across modules unknown. New customer acquisition rates post-incident not disclosed.",
    "sig-018": "Whether affected customers will churn unknown until renewal data. Insurance coverage for $180M cost undisclosed. Technical changes to update channel not publicly detailed.",
}

for signal in SIGNALS:
    signal.source_type = _SOURCE_TYPES.get(signal.source_name, "demo-only")
    signal.confidence_rationale = _CONFIDENCE_RATIONALES.get(signal.id, "")

for brief_id, brief in BRIEFS.items():
    brief.what_is_unknown = _WHAT_IS_UNKNOWN.get(brief_id, "")
    for ma in brief.model_assumptions:
        if not ma.financial_area:
            if "revenue" in ma.assumption.lower() or "growth" in ma.assumption.lower():
                ma.financial_area = "Income Statement"; ma.possible_direction = "down"
            elif "margin" in ma.assumption.lower():
                ma.financial_area = "Income Statement"; ma.possible_direction = "down"
            elif "buyback" in ma.assumption.lower() or "capital" in ma.assumption.lower():
                ma.financial_area = "Balance Sheet"; ma.possible_direction = "down"
            elif "pricing" in ma.assumption.lower() or "asp" in ma.assumption.lower():
                ma.financial_area = "Income Statement"; ma.possible_direction = "down"
            else:
                ma.financial_area = "Income Statement"; ma.possible_direction = "uncertain"
        if not ma.confidence:
            ma.confidence = ma.magnitude if ma.magnitude else "medium"
        if not ma.reasoning:
            ma.reasoning = f"Based on {brief_id} signal evidence"
        if not ma.evidence_gap:
            ma.evidence_gap = "No updated guidance or confirmed data from company"

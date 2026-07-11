#!/bin/bash
# DealSignal AI — 60-Second Demo Script
# Run from project root: bash scripts/demo.sh

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'
API="http://localhost:8000"

echo -e "${GREEN}DealSignal AI — Demo${NC}"
echo "=============================="
echo ""

# 1. Health check
echo -e "${BLUE}[1/7] Backend Health${NC}"
curl -s "$API/api/health" | jq '.'
echo ""

# 2. Companies
echo -e "${BLUE}[2/7] Company Watchlist${NC}"
curl -s "$API/api/companies" | jq -r '.[] | "  ${\(.ticker)}\t\(.name)\t\(.signal_count) signals"' | column -t -s $'\t'
echo ""

# 3. Signals feed
echo -e "${BLUE}[3/7] Signal Feed${NC}"
curl -s "$API/api/signals?page_size=18" | jq -r '.signals[] | "  [\(.severity)] \(.ticker) — \(.title)"'
echo ""

# 4. Nvidia company detail
echo -e "${BLUE}[4/7] Company Detail — Nvidia (NVDA)${NC}"
curl -s "$API/api/company/NVDA" | jq '{name: .company.name, ticker: .company.ticker, market_cap: .company.market_cap, signals: (.recent_signals | length), categories: .category_breakdown}'
echo ""

# 5. Analyst brief preview
echo -e "${BLUE}[5/7] Analyst Brief — sig-001 (NVDA Export Controls)${NC}"
curl -s "$API/api/brief/sig-001" | jq '{title: .signal.title, severity: .signal.severity, confidence: .signal.confidence, summary: (.executive_summary[:120] + "..."), financial_areas: (.financial_areas | length), model_assumptions: (.model_assumptions | length), analyst_questions: (.analyst_questions | length)}'
echo ""

# 6. Filter: high severity
echo -e "${BLUE}[6/7] High Severity Signals${NC}"
curl -s "$API/api/signals?severity=high" | jq -r '.signals[] | "  \(.ticker) — \(.title)"'
echo ""

# 7. Filter: regulation
echo -e "${BLUE}[7/7] Regulation Signals${NC}"
curl -s "$API/api/signals?category=regulation" | jq -r '.signals[] | "  \(.ticker) — \(.title)"'
echo ""

echo -e "${GREEN}Demo complete. Visit http://localhost:3000 for the full UI.${NC}"
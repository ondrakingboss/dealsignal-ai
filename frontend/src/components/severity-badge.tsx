type Severity = "low" | "medium" | "high";

export default function SeverityBadge({ severity }: { severity: Severity }) {
  return <span className={`severity-${severity}`}>{severity}</span>;
}

export function CategoryBadge({ category }: { category: string }) {
  const labels: Record<string, string> = {
    revenue: "Revenue",
    margin: "Margin",
    "balance-sheet": "Balance Sheet",
    regulation: "Regulation",
    competition: "Competition",
    management: "Management",
    macro: "Macro",
    ma: "M&A",
    sentiment: "Sentiment",
  };
  return <span className="category-badge">{labels[category] || category}</span>;
}

export function ConfidenceBadge({ confidence }: { confidence: number }) {
  const pct = Math.round(confidence * 100);
  const color = pct >= 90 ? "text-green-400" : pct >= 80 ? "text-yellow-400" : "text-red-400";
  return (
    <span className={`text-xs font-mono ${color}`}>
      {pct}% conf.
    </span>
  );
}
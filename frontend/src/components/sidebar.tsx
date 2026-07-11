"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  BarChart3,
  Radio,
  Search,
  Zap,
} from "lucide-react";

const navItems = [
  { href: "/", label: "Home", icon: Zap },
  { href: "/watchlist", label: "Watchlist", icon: LayoutDashboard },
  { href: "/signals", label: "Signals", icon: Radio },
  { href: "/company/NVDA", label: "Research", icon: Search },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="fixed left-0 top-0 h-full w-56 glass border-r border-[#27272a] flex flex-col z-50">
      {/* Logo */}
      <div className="px-5 py-5 border-b border-[#27272a]">
        <Link href="/" className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-green-500 to-emerald-700 flex items-center justify-center">
            <Radio className="w-4 h-4 text-white" />
          </div>
          <span className="font-bold text-sm tracking-tight">
            Deal<span className="text-green-400">Signal</span>
          </span>
        </Link>
      </div>

      {/* Nav */}
      <nav className="flex-1 px-3 py-4 space-y-1">
        {navItems.map((item) => {
          const isActive = pathname === item.href || 
            (item.href !== "/" && pathname.startsWith(item.href));
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-all duration-200 ${
                isActive
                  ? "bg-[#22c55e15] text-green-400 font-medium"
                  : "text-zinc-400 hover:text-zinc-200 hover:bg-[#ffffff08]"
              }`}
            >
              <item.icon className="w-4 h-4" />
              {item.label}
            </Link>
          );
        })}
      </nav>

      {/* Footer */}
      <div className="px-5 py-4 border-t border-[#27272a]">
        <div className="flex items-center gap-2 text-xs text-zinc-600">
          <div className="w-1.5 h-1.5 rounded-full bg-green-500" />
          Live Demo
        </div>
      </div>
    </aside>
  );
}
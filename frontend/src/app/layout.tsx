import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Sidebar from "@/components/sidebar";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "DealSignal AI — Market Intelligence",
  description:
    "AI-powered market and company event monitor. Identify business events, classify financial impact, and map signals to model assumptions.",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={`${inter.variable} dark h-full`}>
      <body className="min-h-full bg-[#09090b] text-[#fafafa] antialiased">
        <Sidebar />
        <main className="min-h-screen lg:ml-56">{children}</main>
      </body>
    </html>
  );
}
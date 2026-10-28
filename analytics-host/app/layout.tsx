import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {title: "偶然的数学 · 作者工作台",description: "Private author analytics for The Mathematics of Chance"};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body className="antialiased">{children}</body>
    </html>
  );
}

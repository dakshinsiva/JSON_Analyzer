import React from 'react'
import './globals.css'
import type { Metadata } from 'next'
import { type ReactNode } from 'react'
import { ThemeProvider } from "@/components/theme-provider"

export const metadata: Metadata = {
  title: 'Cybersecurity Assessment',
  description: 'Assessment tool for cybersecurity practices',
}

export default function RootLayout({
  children,
}: {
  children: ReactNode
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}

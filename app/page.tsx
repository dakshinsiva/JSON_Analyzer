import React from 'react'
import Link from 'next/link'
import CybersecurityAssessment from '../components/cybersecurity-assessment'
import type { LinkProps } from 'next/link'

export default function Home() {
  return (
    <main className="p-4">
      <h1>JSON Analyzer</h1>
      <Link href="/cybersecurity" className="text-blue-500 hover:underline">
        Go to Cybersecurity Assessment
      </Link>
    </main>
  )
}

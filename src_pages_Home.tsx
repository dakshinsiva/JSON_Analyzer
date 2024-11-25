import React from 'react'
import MainLayout from '../layouts/MainLayout'
import Card from '../components/Card'
import Button from '../components/Button'

export default function Home() {
  return (
    <MainLayout>
      <h1 className="text-4xl font-bold mb-6">Welcome to Our Website</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card title="Feature 1" content="Description of feature 1" />
        <Card title="Feature 2" content="Description of feature 2" />
        <Card title="Feature 3" content="Description of feature 3" />
      </div>
      <div className="mt-8 text-center">
        <Button onClick={() => console.log('Learn More clicked')}>
          Learn More
        </Button>
      </div>
    </MainLayout>
  )
}
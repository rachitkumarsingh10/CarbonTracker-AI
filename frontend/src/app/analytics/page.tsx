'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'

interface AnalyticsData {
  summary: any
  trends: any
  breakdown: any
  comparison: any
}

export default function AnalyticsPage() {
  const router = useRouter()
  const [loading, setLoading] = useState(true)
  const [data, setData] = useState<AnalyticsData | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchAnalytics()
  }, [])

  const fetchAnalytics = async () => {
    try {
      const [summary, trends, breakdown, comparison] = await Promise.all([
        fetch('http://localhost:8000/api/analytics/summary').then(r => r.json()),
        fetch('http://localhost:8000/api/analytics/trends').then(r => r.json()),
        fetch('http://localhost:8000/api/analytics/breakdown').then(r => r.json()),
        fetch('http://localhost:8000/api/analytics/comparison').then(r => r.json())
      ])

      setData({ summary, trends, breakdown, comparison })
    } catch (err) {
      setError('Failed to load analytics data')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-blue-50 flex items-center justify-center">
        <div className="text-2xl font-bold text-emerald-700">Loading Analytics...</div>
      </div>
    )
  }

  if (error || !data) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-blue-50 flex items-center justify-center">
        <div className="text-xl text-red-600">{error || 'No data available'}</div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-blue-50 py-8 px-4">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <button
            onClick={() => router.push('/')}
            className="text-emerald-700 hover:text-emerald-800 mb-4 font-semibold text-lg"
          >
            ← Back to Home
          </button>
          <h1 className="text-4xl font-bold text-emerald-700 mb-2">
            📊 Analytics Dashboard
          </h1>
          <p className="text-gray-700 font-medium">
            Track your carbon footprint trends and progress
          </p>
        </div>

        {/* Summary Cards */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          {/* Current Month */}
          <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-emerald-300">
            <div className="text-sm font-bold text-gray-600 mb-2">CURRENT MONTH</div>
            <div className="text-3xl font-bold text-emerald-700 mb-1">
              {data.summary.current_month.total_co2_kg} kg
            </div>
            <div className="text-sm text-gray-700 font-medium">
              CO₂ Emissions
            </div>
            <div className={`text-sm font-bold mt-2 ${data.summary.current_month.vs_last_month < 0 ? 'text-green-600' : 'text-red-600'}`}>
              {data.summary.current_month.vs_last_month > 0 ? '+' : ''}{data.summary.current_month.vs_last_month}% vs last month
            </div>
          </div>

          {/* Sustainability Score */}
          <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-blue-300">
            <div className="text-sm font-bold text-gray-600 mb-2">SUSTAINABILITY SCORE</div>
            <div className="text-3xl font-bold text-blue-700 mb-1">
              {data.summary.current_month.sustainability_score}/100
            </div>
            <div className="text-sm text-gray-700 font-medium">
              Your Rating
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2 mt-3">
              <div 
                className="bg-blue-600 h-2 rounded-full" 
                style={{ width: `${data.summary.current_month.sustainability_score}%` }}
              ></div>
            </div>
          </div>

          {/* Yearly Total */}
          <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-purple-300">
            <div className="text-sm font-bold text-gray-600 mb-2">YEARLY TOTAL</div>
            <div className="text-3xl font-bold text-purple-700 mb-1">
              {data.summary.yearly_total.co2_kg} kg
            </div>
            <div className="text-sm text-gray-700 font-medium">
              Target: {data.summary.yearly_total.target_kg} kg
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2 mt-3">
              <div 
                className="bg-purple-600 h-2 rounded-full" 
                style={{ width: `${data.summary.yearly_total.progress_percentage}%` }}
              ></div>
            </div>
          </div>

          {/* vs Average */}
          <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-amber-300">
            <div className="text-sm font-bold text-gray-600 mb-2">VS AVERAGE</div>
            <div className="text-3xl font-bold text-amber-700 mb-1">
              {Math.abs(data.summary.current_month.vs_average)}%
            </div>
            <div className="text-sm text-gray-700 font-medium">
              {data.summary.current_month.vs_average < 0 ? 'Below' : 'Above'} Average
            </div>
            <div className={`text-sm font-bold mt-2 ${data.summary.current_month.vs_average < 0 ? 'text-green-600' : 'text-red-600'}`}>
              {data.summary.current_month.vs_average < 0 ? '🌟 Great job!' : '⚠️ Room for improvement'}
            </div>
          </div>
        </div>

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          {/* Monthly Trends */}
          <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-emerald-300">
            <h2 className="text-xl font-bold text-emerald-700 mb-4">📈 Monthly Trends</h2>
            <div className="space-y-3">
              {data.trends.months.map((month: any, index: number) => (
                <div key={index}>
                  <div className="flex justify-between items-center mb-1">
                    <span className="text-sm font-bold text-gray-800">{month.month}</span>
                    <span className="text-sm font-bold text-gray-900">{month.total_co2} kg</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-3">
                    <div 
                      className="bg-gradient-to-r from-emerald-500 to-blue-500 h-3 rounded-full transition-all" 
                      style={{ width: `${(month.total_co2 / 500) * 100}%` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
            <div className="mt-4 p-3 bg-emerald-50 rounded-lg border border-emerald-200">
              <p className="text-sm font-semibold text-emerald-800">
                Trend: {data.trends.trend === 'decreasing' ? '📉 Decreasing' : data.trends.trend === 'increasing' ? '📈 Increasing' : '➡️ Stable'}
              </p>
            </div>
          </div>

          {/* Category Breakdown */}
          <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-blue-300">
            <h2 className="text-xl font-bold text-blue-700 mb-4">🎯 Category Breakdown</h2>
            <div className="space-y-4">
              {data.breakdown.categories.map((category: any, index: number) => (
                <div key={index} className="border-l-4 pl-4" style={{ borderColor: category.color }}>
                  <div className="flex justify-between items-center mb-2">
                    <span className="font-bold text-gray-800">
                      {category.icon} {category.name}
                    </span>
                    <span className="font-bold text-gray-900">{category.co2_kg} kg</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <div className="flex-1 bg-gray-200 rounded-full h-2">
                      <div 
                        className="h-2 rounded-full" 
                        style={{ 
                          width: `${category.percentage}%`,
                          backgroundColor: category.color
                        }}
                      ></div>
                    </div>
                    <span className="text-sm font-semibold text-gray-600">{category.percentage}%</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Comparison Section */}
        <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-purple-300 mb-8">
          <h2 className="text-xl font-bold text-purple-700 mb-4">🏆 How You Compare</h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="text-3xl font-bold text-emerald-600 mb-1">{data.comparison.your_footprint}</div>
              <div className="text-sm font-semibold text-gray-700">Your Footprint</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-blue-600 mb-1">{data.comparison.national_average}</div>
              <div className="text-sm font-semibold text-gray-700">National Average</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-purple-600 mb-1">{data.comparison.global_average}</div>
              <div className="text-sm font-semibold text-gray-700">Global Average</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-amber-600 mb-1">{data.comparison.target}</div>
              <div className="text-sm font-semibold text-gray-700">Target</div>
            </div>
          </div>
          <div className="mt-6 p-4 bg-emerald-50 rounded-lg border-2 border-emerald-300">
            <p className="text-center font-bold text-emerald-800 text-lg">
              {data.comparison.message}
            </p>
            <p className="text-center text-sm text-gray-700 mt-2 font-medium">
              You're in the top {100 - data.comparison.percentile}% of users! 🌟
            </p>
          </div>
        </div>

        {/* Top Categories */}
        <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-amber-300">
          <h2 className="text-xl font-bold text-amber-700 mb-4">🔝 Top Emission Sources</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {data.summary.top_categories.map((category: any, index: number) => (
              <div key={index} className="p-4 bg-gradient-to-br from-amber-50 to-orange-50 rounded-lg border-2 border-amber-200">
                <div className="text-2xl font-bold text-amber-700 mb-1">{category.co2_kg} kg</div>
                <div className="text-sm font-bold text-gray-800">{category.name}</div>
                <div className="text-xs text-gray-600 font-medium mt-1">{category.percentage}% of total</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

// Made with Bob

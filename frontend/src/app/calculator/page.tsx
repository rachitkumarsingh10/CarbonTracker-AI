'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

interface CalculationResult {
  total_co2_kg: number
  sustainability_score: number
  breakdown: {
    [key: string]: number
  }
  recommendations: string[]
}

export default function CalculatorPage() {
  const router = useRouter()
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<CalculationResult | null>(null)
  const [error, setError] = useState<string | null>(null)

  const [formData, setFormData] = useState({
    electricity_kwh: 0,
    car_km: 0,
    bike_km: 0,
    public_transport_km: 0,
    flight_km: 0,
    water_liters: 0,
    food_type: 'mixed'
  })

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      const response = await fetch('http://localhost:8000/api/carbon/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
      })

      if (!response.ok) {
        throw new Error('Failed to calculate carbon footprint')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: name === 'food_type' ? value : parseFloat(value) || 0
    }))
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-blue-50 py-8 px-4">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <button
            onClick={() => router.push('/')}
            className="text-emerald-700 hover:text-emerald-800 mb-4 font-semibold text-lg"
          >
            ← Back to Home
          </button>
          <h1 className="text-4xl font-bold text-emerald-700 mb-2">
            🧮 Carbon Footprint Calculator
          </h1>
          <p className="text-gray-700 font-medium">
            Calculate your monthly carbon emissions and get personalized recommendations
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Form */}
          <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-emerald-200">
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Energy Section */}
              <div>
                <h2 className="text-xl font-bold mb-4 text-emerald-700">⚡ Energy</h2>
                <div>
                  <label className="block text-sm font-bold text-gray-800 mb-2">
                    Monthly Electricity Usage (kWh)
                  </label>
                  <input
                    type="number"
                    name="electricity_kwh"
                    value={formData.electricity_kwh}
                    onChange={handleChange}
                    min="0"
                    step="0.1"
                    className="w-full px-4 py-2 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 text-gray-900 font-medium"
                    placeholder="e.g., 300"
                  />
                </div>
              </div>

              {/* Transportation Section */}
              <div>
                <h2 className="text-xl font-bold mb-4 text-blue-700">🚗 Transportation</h2>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-bold text-gray-800 mb-2">
                      Car Distance (km/month)
                    </label>
                    <input
                      type="number"
                      name="car_km"
                      value={formData.car_km}
                      onChange={handleChange}
                      min="0"
                      step="0.1"
                      className="w-full px-4 py-2 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 text-gray-900 font-medium"
                      placeholder="e.g., 500"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Bike Distance (km/month)
                    </label>
                    <input
                      type="number"
                      name="bike_km"
                      value={formData.bike_km}
                      onChange={handleChange}
                      min="0"
                      step="0.1"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      placeholder="e.g., 50"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Public Transport (km/month)
                    </label>
                    <input
                      type="number"
                      name="public_transport_km"
                      value={formData.public_transport_km}
                      onChange={handleChange}
                      min="0"
                      step="0.1"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      placeholder="e.g., 100"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Flight Distance (km/month)
                    </label>
                    <input
                      type="number"
                      name="flight_km"
                      value={formData.flight_km}
                      onChange={handleChange}
                      min="0"
                      step="0.1"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      placeholder="e.g., 0"
                    />
                  </div>
                </div>
              </div>

              {/* Lifestyle Section */}
              <div>
                <h2 className="text-xl font-bold mb-4 text-green-700">🌱 Lifestyle</h2>
                <div className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Daily Water Usage (liters)
                    </label>
                    <input
                      type="number"
                      name="water_liters"
                      value={formData.water_liters}
                      onChange={handleChange}
                      min="0"
                      step="0.1"
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      placeholder="e.g., 150"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Diet Type
                    </label>
                    <select
                      name="food_type"
                      value={formData.food_type}
                      onChange={handleChange}
                      className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                    >
                      <option value="vegan">Vegan</option>
                      <option value="vegetarian">Vegetarian</option>
                      <option value="mixed">Mixed</option>
                      <option value="meat">Meat-heavy</option>
                    </select>
                  </div>
                </div>
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                disabled={loading}
                className="w-full bg-emerald-600 text-white py-3 px-6 rounded-lg hover:bg-emerald-700 transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed font-bold text-lg shadow-md hover:shadow-lg"
              >
                {loading ? 'Calculating...' : '🧮 Calculate Carbon Footprint'}
              </button>

              {error && (
                <div className="bg-red-50 border-2 border-red-300 text-red-800 px-4 py-3 rounded-lg font-semibold">
                  {error}
                </div>
              )}
            </form>
          </div>

          {/* Results */}
          <div className="space-y-6">
            {result ? (
              <>
                {/* Total CO2 */}
                <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-emerald-300">
                  <h2 className="text-xl font-bold mb-4 text-emerald-700">📊 Your Results</h2>
                  <div className="text-center">
                    <div className="text-5xl font-bold text-emerald-600 mb-2">
                      {result.total_co2_kg.toFixed(1)}
                    </div>
                    <div className="text-gray-700 mb-4 font-semibold">kg CO₂ per month</div>
                    <div className="text-2xl font-bold text-blue-600">
                      Score: {result.sustainability_score}/100
                    </div>
                  </div>
                </div>

                {/* Breakdown */}
                <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-blue-300">
                  <h3 className="text-lg font-bold mb-4 text-blue-700">Breakdown</h3>
                  <div className="space-y-2">
                    {Object.entries(result.breakdown).map(([category, value]) => (
                      <div key={category} className="flex justify-between items-center">
                        <span className="text-gray-800 capitalize font-semibold">{category}</span>
                        <span className="font-bold text-gray-900">{value.toFixed(1)} kg</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Recommendations */}
                <div className="bg-white rounded-xl shadow-lg p-6 border-2 border-amber-300">
                  <h3 className="text-lg font-bold mb-4 text-amber-700">💡 Recommendations</h3>
                  <ul className="space-y-3">
                    {result.recommendations.map((rec, index) => (
                      <li key={index} className="flex items-start">
                        <span className="text-emerald-600 mr-2 font-bold">•</span>
                        <span className="text-gray-800 font-medium">{rec}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              </>
            ) : (
              <div className="bg-white rounded-xl shadow-lg p-6 text-center border-2 border-gray-300">
                <p className="text-lg mb-2 font-bold text-gray-700">👈 Fill in the form</p>
                <p className="text-gray-600 font-medium">Enter your monthly usage data to calculate your carbon footprint</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

// Made with Bob

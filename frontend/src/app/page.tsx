'use client'

import { useState, useEffect } from 'react'

export default function Home() {
  const [backendStatus, setBackendStatus] = useState<string>('checking...')
  const [apiInfo, setApiInfo] = useState<any>(null)

  useEffect(() => {
    // Check backend connection
    fetch('http://localhost:8000/health')
      .then(res => res.json())
      .then(data => {
        setBackendStatus('connected ✅')
        return fetch('http://localhost:8000/api/v1/info')
      })
      .then(res => res.json())
      .then(data => setApiInfo(data))
      .catch(() => setBackendStatus('disconnected ❌'))
  }, [])

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8 md:p-24 bg-gradient-to-br from-emerald-50 to-blue-50">
      <div className="z-10 max-w-5xl w-full">
        <h1 className="text-4xl md:text-5xl font-bold text-center mb-4 text-emerald-700">
          🌍 CarbonTracker AI
        </h1>
        <p className="text-center text-lg md:text-xl mb-8 text-gray-700 font-medium">
          Track, Analyze, and Reduce Your Carbon Footprint with AI
        </p>

        {/* Backend Status */}
        <div className="bg-white border-2 border-blue-300 rounded-xl p-4 mb-8 shadow-md">
          <p className="text-center text-gray-800">
            <span className="font-bold text-blue-700">Backend Status:</span> <span className="font-semibold">{backendStatus}</span>
          </p>
          {apiInfo && (
            <p className="text-center text-sm mt-2 text-gray-600">
              Version: {apiInfo.version} | LLM: {apiInfo.llm_provider}
            </p>
          )}
        </div>

        {/* Current Status */}
        <div className="bg-white border-2 border-amber-300 rounded-xl p-6 mb-8 shadow-md">
          <h2 className="text-xl font-bold mb-3 text-center text-amber-700">🚧 Project Status</h2>
          <div className="space-y-2 text-sm text-gray-800">
            <p>✅ <strong className="text-emerald-700">Frontend:</strong> Next.js 14 + TypeScript + Tailwind CSS</p>
            <p>✅ <strong className="text-emerald-700">Backend:</strong> FastAPI + SQLite running on port 8000</p>
            <p>✅ <strong className="text-emerald-700">Database:</strong> SQLite initialized and connected</p>
            <p>✅ <strong className="text-emerald-700">Calculator:</strong> Fully functional carbon calculator</p>
          </div>
        </div>
        
        {/* Feature Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <a href="/calculator" className="p-6 border-2 border-emerald-400 rounded-xl bg-white shadow-lg hover:shadow-xl transition-all hover:scale-105">
            <h2 className="text-xl font-bold mb-2 text-emerald-700">🧮 Calculate</h2>
            <p className="text-gray-700 mb-3 font-medium">
              Track your carbon emissions from electricity, transportation, and more
            </p>
            <p className="text-sm text-emerald-600 font-bold">✅ Available Now →</p>
          </a>
          
          <a href="/analytics" className="p-6 border-2 border-blue-400 rounded-xl bg-white shadow-lg hover:shadow-xl transition-all hover:scale-105">
            <h2 className="text-xl font-bold mb-2 text-blue-700">📊 Analyze</h2>
            <p className="text-gray-700 mb-3 font-medium">
              Visualize your carbon footprint with interactive charts and insights
            </p>
            <p className="text-sm text-blue-600 font-bold">✅ Available Now →</p>
          </a>
          
          <div className="p-6 border-2 border-gray-300 rounded-xl bg-white shadow-lg opacity-75">
            <h2 className="text-xl font-bold mb-2 text-gray-700">🤖 AI Coach</h2>
            <p className="text-gray-600 mb-3 font-medium">
              Get personalized recommendations powered by IBM Granite AI
            </p>
            <p className="text-sm text-orange-600 font-bold">⏳ Coming Soon</p>
          </div>
        </div>

        {/* API Links */}
        <div className="bg-white border-2 border-emerald-300 rounded-xl p-6 shadow-md">
          <h2 className="text-xl font-bold mb-3 text-center text-emerald-700">🔗 Developer Tools</h2>
          <div className="flex flex-col md:flex-row gap-4 justify-center">
            <a
              href="http://localhost:8000/docs"
              target="_blank"
              className="px-6 py-3 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700 transition-colors text-center font-semibold shadow-md hover:shadow-lg"
            >
              📚 API Documentation
            </a>
            <a
              href="http://localhost:8000/health"
              target="_blank"
              className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors text-center font-semibold shadow-md hover:shadow-lg"
            >
              ❤️ Health Check
            </a>
          </div>
        </div>

        {/* Footer */}
        <div className="text-center mt-8">
          <p className="text-sm text-gray-700 font-medium">
            Aligned with UN SDGs 11, 12, and 13
          </p>
          <p className="text-xs text-gray-500 mt-2">
            Build complete • Ready for feature development
          </p>
        </div>
      </div>
    </main>
  )
}

// Made with Bob

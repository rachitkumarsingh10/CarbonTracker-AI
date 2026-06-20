"""
Analytics API Endpoints
"""

from fastapi import APIRouter
from datetime import datetime, timedelta
from typing import List, Dict

router = APIRouter()


@router.get("/summary")
async def get_analytics_summary():
    """
    Get analytics summary with sample data
    
    Returns overview statistics for the dashboard
    """
    return {
        "current_month": {
            "total_co2_kg": 385.5,
            "sustainability_score": 72,
            "vs_last_month": -12.3,  # Percentage change
            "vs_average": -8.5  # Percentage vs average user
        },
        "yearly_total": {
            "co2_kg": 4626.0,
            "target_kg": 2000.0,
            "progress_percentage": 43.2
        },
        "top_categories": [
            {"name": "Electricity", "co2_kg": 138.0, "percentage": 35.8},
            {"name": "Transportation", "co2_kg": 121.6, "percentage": 31.5},
            {"name": "Food", "co2_kg": 86.4, "percentage": 22.4},
            {"name": "Water", "co2_kg": 39.5, "percentage": 10.3}
        ]
    }


@router.get("/trends")
async def get_trends():
    """
    Get monthly trends data for charts
    
    Returns last 6 months of carbon footprint data
    """
    # Generate sample data for last 6 months
    months = []
    current_date = datetime.now()
    
    for i in range(5, -1, -1):
        month_date = current_date - timedelta(days=30 * i)
        month_name = month_date.strftime("%b")
        
        # Sample data with slight variations
        base_co2 = 400
        variation = (i - 3) * 15  # Creates a trend
        
        months.append({
            "month": month_name,
            "total_co2": base_co2 + variation,
            "electricity": 140 + (i - 3) * 5,
            "transportation": 120 + (i - 3) * 8,
            "food": 90 + (i - 3) * 2,
            "water": 50
        })
    
    return {
        "months": months,
        "average_monthly": 385.5,
        "trend": "decreasing"  # or "increasing" or "stable"
    }


@router.get("/breakdown")
async def get_category_breakdown():
    """
    Get detailed breakdown by category
    
    Returns CO2 emissions breakdown for pie/bar charts
    """
    return {
        "categories": [
            {
                "name": "Electricity",
                "co2_kg": 138.0,
                "percentage": 35.8,
                "color": "#10b981",
                "icon": "⚡"
            },
            {
                "name": "Car",
                "co2_kg": 101.0,
                "percentage": 26.2,
                "color": "#3b82f6",
                "icon": "🚗"
            },
            {
                "name": "Food",
                "co2_kg": 86.4,
                "percentage": 22.4,
                "color": "#f59e0b",
                "icon": "🍽️"
            },
            {
                "name": "Public Transport",
                "co2_kg": 20.6,
                "percentage": 5.3,
                "color": "#8b5cf6",
                "icon": "🚌"
            },
            {
                "name": "Water",
                "co2_kg": 39.5,
                "percentage": 10.3,
                "color": "#06b6d4",
                "icon": "💧"
            }
        ],
        "total_co2_kg": 385.5
    }


@router.get("/comparison")
async def get_comparison():
    """
    Get comparison with averages
    
    Returns comparison data for benchmarking
    """
    return {
        "your_footprint": 385.5,
        "national_average": 420.0,
        "global_average": 333.0,
        "target": 200.0,
        "percentile": 68,  # You're better than 68% of users
        "message": "You're doing better than the national average! Keep it up!"
    }


@router.get("/goals")
async def get_goals():
    """
    Get carbon reduction goals and progress
    
    Returns goals and achievement status
    """
    return {
        "active_goals": [
            {
                "id": 1,
                "title": "Reduce car usage by 20%",
                "target_reduction_kg": 20.0,
                "current_reduction_kg": 12.3,
                "progress_percentage": 61.5,
                "deadline": "2026-07-31",
                "status": "in_progress"
            },
            {
                "id": 2,
                "title": "Switch to renewable energy",
                "target_reduction_kg": 50.0,
                "current_reduction_kg": 0.0,
                "progress_percentage": 0.0,
                "deadline": "2026-12-31",
                "status": "not_started"
            }
        ],
        "completed_goals": [
            {
                "id": 3,
                "title": "Reduce electricity by 10%",
                "target_reduction_kg": 15.0,
                "achieved_reduction_kg": 16.2,
                "completed_date": "2026-05-15",
                "status": "completed"
            }
        ]
    }

# Made with Bob

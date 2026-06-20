"""
Carbon Calculator API Endpoints
"""

from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.carbon import (
    CarbonCalculationRequest,
    CarbonCalculationResponse
)
from app.services.carbon_calculator import carbon_calculator

router = APIRouter()


@router.post("/calculate", response_model=CarbonCalculationResponse)
async def calculate_carbon_footprint(request: CarbonCalculationRequest):
    """
    Calculate carbon footprint based on user inputs
    
    This endpoint calculates the total CO2 emissions and provides:
    - Total CO2 in kg
    - Sustainability score (0-100)
    - Breakdown by category
    - Personalized recommendations
    """
    try:
        result = carbon_calculator.calculate_carbon_footprint(
            electricity_kwh=request.electricity_kwh,
            car_km=request.car_km,
            bike_km=request.bike_km,
            public_transport_km=request.public_transport_km,
            flight_km=request.flight_km,
            water_liters=request.water_liters,
            food_type=request.food_type
        )
        
        return CarbonCalculationResponse(**result)
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating carbon footprint: {str(e)}"
        )


@router.get("/emission-factors")
async def get_emission_factors():
    """
    Get current emission factors used in calculations
    
    Returns the CO2 emission factors for different activities
    """
    return {
        "electricity_kwh": carbon_calculator.electricity_factor,
        "car_km": carbon_calculator.car_factor,
        "public_transport_km": carbon_calculator.public_transport_factor,
        "flight_km": carbon_calculator.flight_factor,
        "water_liter_daily": carbon_calculator.water_factor,
        "food_daily": carbon_calculator.food_factors,
        "units": {
            "electricity": "kg CO2 per kWh",
            "transportation": "kg CO2 per km",
            "water": "kg CO2 per liter per day",
            "food": "kg CO2 per day"
        }
    }


@router.get("/average-footprint")
async def get_average_footprint():
    """
    Get average carbon footprint statistics
    
    Returns average monthly CO2 emissions for comparison
    """
    return {
        "average_monthly_kg": 400,
        "average_yearly_kg": 4800,
        "global_average_yearly_kg": 4000,
        "target_yearly_kg": 2000,
        "description": "Average carbon footprint for a person in developed countries"
    }

# Made with Bob

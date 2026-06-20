"""
Carbon Footprint Schemas
Pydantic models for API request/response validation
"""

from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class CarbonCalculationRequest(BaseModel):
    """Request model for carbon calculation"""
    
    electricity_kwh: float = Field(default=0.0, ge=0, description="Monthly electricity usage in kWh")
    car_km: float = Field(default=0.0, ge=0, description="Monthly car distance in km")
    bike_km: float = Field(default=0.0, ge=0, description="Monthly bike distance in km")
    public_transport_km: float = Field(default=0.0, ge=0, description="Monthly public transport distance in km")
    flight_km: float = Field(default=0.0, ge=0, description="Monthly flight distance in km")
    water_liters: float = Field(default=0.0, ge=0, description="Daily water usage in liters")
    food_type: str = Field(default="mixed", description="Diet type: vegetarian, vegan, or meat")
    
    class Config:
        json_schema_extra = {
            "example": {
                "electricity_kwh": 300,
                "car_km": 500,
                "bike_km": 50,
                "public_transport_km": 100,
                "flight_km": 0,
                "water_liters": 150,
                "food_type": "mixed"
            }
        }


class CarbonCalculationResponse(BaseModel):
    """Response model for carbon calculation"""
    
    total_co2_kg: float = Field(description="Total CO2 emissions in kg")
    sustainability_score: int = Field(description="Sustainability score (0-100)")
    breakdown: dict = Field(description="CO2 breakdown by category")
    recommendations: list[str] = Field(description="Quick recommendations")
    
    class Config:
        json_schema_extra = {
            "example": {
                "total_co2_kg": 450.5,
                "sustainability_score": 65,
                "breakdown": {
                    "electricity": 276.0,
                    "car": 202.0,
                    "public_transport": 8.9,
                    "food": 216.0,
                    "water": 13.5
                },
                "recommendations": [
                    "Reduce car usage by 20% to save 40kg CO2/month",
                    "Switch to renewable energy to reduce electricity emissions"
                ]
            }
        }


class CarbonEntryResponse(BaseModel):
    """Response model for carbon entry"""
    
    id: int
    entry_date: date
    electricity_kwh: float
    car_km: float
    bike_km: float
    public_transport_km: float
    flight_km: float
    water_liters: float
    food_type: str
    total_co2_kg: float
    sustainability_score: int
    
    class Config:
        from_attributes = True

# Made with Bob

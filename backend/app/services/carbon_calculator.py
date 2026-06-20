"""
Carbon Calculator Service
Business logic for carbon footprint calculations
"""

from app.core.config import settings


class CarbonCalculatorService:
    """Service for calculating carbon footprints"""
    
    def __init__(self):
        """Initialize with emission factors from settings"""
        self.electricity_factor = settings.ELECTRICITY_FACTOR
        self.car_factor = settings.CAR_FACTOR
        self.public_transport_factor = settings.PUBLIC_TRANSPORT_FACTOR
        self.flight_factor = settings.FLIGHT_FACTOR
        self.water_factor = settings.WATER_FACTOR
        
        # Food factors (kg CO2 per day)
        self.food_factors = {
            "vegan": settings.VEGAN_DIET_FACTOR,
            "vegetarian": settings.VEGETARIAN_DIET_FACTOR,
            "meat": settings.MEAT_DIET_FACTOR,
            "mixed": (settings.MEAT_DIET_FACTOR + settings.VEGETARIAN_DIET_FACTOR) / 2
        }
    
    def calculate_carbon_footprint(
        self,
        electricity_kwh: float = 0.0,
        car_km: float = 0.0,
        bike_km: float = 0.0,
        public_transport_km: float = 0.0,
        flight_km: float = 0.0,
        water_liters: float = 0.0,
        food_type: str = "mixed"
    ) -> dict:
        """
        Calculate total carbon footprint and breakdown
        
        Args:
            electricity_kwh: Monthly electricity usage in kWh
            car_km: Monthly car distance in km
            bike_km: Monthly bike distance in km (zero emissions)
            public_transport_km: Monthly public transport distance in km
            flight_km: Monthly flight distance in km
            water_liters: Daily water usage in liters
            food_type: Diet type (vegan, vegetarian, meat, mixed)
        
        Returns:
            Dictionary with total CO2, breakdown, score, and recommendations
        """
        
        # Calculate emissions by category (in kg CO2)
        electricity_co2 = electricity_kwh * self.electricity_factor
        car_co2 = car_km * self.car_factor
        public_transport_co2 = public_transport_km * self.public_transport_factor
        flight_co2 = flight_km * self.flight_factor
        water_co2 = water_liters * 30 * self.water_factor  # Monthly water usage
        food_co2 = self.food_factors.get(food_type, self.food_factors["mixed"]) * 30  # Monthly food
        
        # Total CO2
        total_co2 = (
            electricity_co2 +
            car_co2 +
            public_transport_co2 +
            flight_co2 +
            water_co2 +
            food_co2
        )
        
        # Calculate sustainability score (0-100, higher is better)
        # Average person emits ~400kg CO2/month
        # Score: 100 - (actual / 400 * 100), capped at 0-100
        average_monthly_co2 = 400
        score = max(0, min(100, int(100 - (total_co2 / average_monthly_co2 * 100))))
        
        # Breakdown
        breakdown = {
            "electricity": round(electricity_co2, 2),
            "car": round(car_co2, 2),
            "public_transport": round(public_transport_co2, 2),
            "flight": round(flight_co2, 2),
            "water": round(water_co2, 2),
            "food": round(food_co2, 2),
            "bike": 0.0  # Zero emissions
        }
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            electricity_kwh, car_km, public_transport_km, 
            flight_km, water_liters, food_type, total_co2
        )
        
        return {
            "total_co2_kg": round(total_co2, 2),
            "sustainability_score": score,
            "breakdown": breakdown,
            "recommendations": recommendations
        }
    
    def _generate_recommendations(
        self,
        electricity_kwh: float,
        car_km: float,
        public_transport_km: float,
        flight_km: float,
        water_liters: float,
        food_type: str,
        total_co2: float
    ) -> list[str]:
        """Generate personalized recommendations based on usage"""
        
        recommendations = []
        
        # Electricity recommendations
        if electricity_kwh > 300:
            savings = (electricity_kwh - 300) * self.electricity_factor
            recommendations.append(
                f"💡 Reduce electricity usage by {int(electricity_kwh - 300)} kWh to save {savings:.1f}kg CO2/month"
            )
        
        # Car recommendations
        if car_km > 400:
            savings = (car_km - 400) * self.car_factor
            recommendations.append(
                f"🚗 Reduce car usage by {int(car_km - 400)} km to save {savings:.1f}kg CO2/month"
            )
        elif car_km > 0:
            recommendations.append(
                "🚗 Consider carpooling or using public transport to reduce car emissions"
            )
        
        # Flight recommendations
        if flight_km > 0:
            recommendations.append(
                f"✈️ Flights contribute {flight_km * self.flight_factor:.1f}kg CO2. Consider train travel for shorter distances"
            )
        
        # Food recommendations
        if food_type == "meat":
            savings = (self.food_factors["meat"] - self.food_factors["vegetarian"]) * 30
            recommendations.append(
                f"🥗 Reducing meat consumption could save {savings:.1f}kg CO2/month"
            )
        
        # Water recommendations
        if water_liters > 150:
            recommendations.append(
                "💧 Reduce water usage with shorter showers and fixing leaks"
            )
        
        # General recommendations
        if total_co2 > 400:
            recommendations.append(
                "🌱 Your carbon footprint is above average. Focus on the biggest contributors first"
            )
        elif total_co2 < 200:
            recommendations.append(
                "🌟 Great job! Your carbon footprint is below average. Keep it up!"
            )
        
        # If no specific recommendations, add general ones
        if not recommendations:
            recommendations.append("🌍 You're doing well! Consider renewable energy and public transport")
        
        return recommendations[:5]  # Return top 5 recommendations


# Create singleton instance
carbon_calculator = CarbonCalculatorService()

# Made with Bob

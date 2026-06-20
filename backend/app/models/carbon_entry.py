"""
Carbon Entry Model
Database model for carbon footprint entries
"""

from sqlalchemy import Column, Integer, Float, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class CarbonEntry(Base):
    """Carbon footprint entry model"""
    
    __tablename__ = "carbon_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    entry_date = Column(Date, nullable=False, default=datetime.utcnow().date)
    
    # Energy consumption
    electricity_kwh = Column(Float, default=0.0)
    
    # Transportation
    car_km = Column(Float, default=0.0)
    bike_km = Column(Float, default=0.0)
    public_transport_km = Column(Float, default=0.0)
    flight_km = Column(Float, default=0.0)
    
    # Other
    water_liters = Column(Float, default=0.0)
    food_type = Column(String, default="mixed")  # vegetarian, vegan, meat
    
    # Calculated values
    total_co2_kg = Column(Float, nullable=False)
    sustainability_score = Column(Integer, default=50)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="carbon_entries")
    
    def __repr__(self):
        return f"<CarbonEntry {self.id} - {self.total_co2_kg}kg CO2>"

# Made with Bob

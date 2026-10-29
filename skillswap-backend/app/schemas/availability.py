
from datetime import date
from pydantic import BaseModel


# =====================================
# Create Availability
# =====================================

class AvailabilityCreate(BaseModel):

    day: str

    availability_date: date

    start_time: str

    end_time: str


# =====================================
# Update Availability
# =====================================

class UpdateAvailability(BaseModel):

    day: str

    availability_date: date

    start_time: str

    end_time: str
from pydantic import BaseModel, Field, root_validator
from typing import Literal, Optional
import math

class CustomerData(BaseModel):
    Age: int = Field(description="Customer's age", ge=18, le=100)
    EstimatedSalary: float = Field(ge=0, description="Estimated annual salary")
    Balance: float = Field(ge=0, description="Account balance")
    CreditScore: int = Field(description="Credit score of the customer")
    NumOfProducts: int = Field(ge=1, le=4, description="Number of bank products (1-4)")
    Tenure: int = Field(ge=0, le=10, description="Years as a customer (0-10)")
    IsActiveMember: Literal[0, 1] = Field(description="Active member status (0=No, 1=Yes)")
    Geography: Literal["France", "Germany", "Spain"] = Field(description="Customer's country")
    Gender: Literal["Male", "Female"] = Field(description="Customer's gender")
    HasCrCard: Literal[0, 1] = Field(description="Has credit card (0=No, 1=Yes)")

    # Derived and one-hot fields
    Age_log: Optional[float] = None
    Geography_Germany: Optional[int] = None
    Geography_Spain: Optional[int] = None
    Gender_Male: Optional[int] = None

    @root_validator(pre=True)
    def compute_derived_fields(cls, values):
        # Age_log
        age = values.get("Age")
        if age:
            values["Age_log"] = round(math.log(age), 6)

        # One-hot Geography
        geography = values.get("Geography")
        values["Geography_Germany"] = 1 if geography == "Germany" else 0
        values["Geography_Spain"] = 1 if geography == "Spain" else 0

        # One-hot Gender
        gender = values.get("Gender")
        values["Gender_Male"] = 1 if gender == "Male" else 0

        return values

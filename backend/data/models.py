from typing import List
from pydantic import BaseModel

class PowerSystemRightNowRecords(BaseModel):
    Minutes1UTC: str
    Minutes1DK: str
    CO2Emission: float
    ProductionGe100MW: float
    ProductionLt100MW: float
    SolarPower: float
    OffshoreWindPower: float
    OnshoreWindPower: float
    Exchange_Sum: float
    Exchange_DK1_DE: float
    Exchange_DK1_NL: float
    Exchange_DK1_GB: float
    Exchange_DK1_NO: float
    Exchange_DK1_SE: float
    Exchange_DK1_DK2: float
    Exchange_DK2_DE: float
    Exchange_DK2_SE: float
    Exchange_Bornholm_SE: float
    aFRR_ActivatedDK1: float
    aFRR_ActivatedDK2: float
    mFRR_ActivatedDK1: float
    mFRR_ActivatedDK2: float
    ImbalanceDK1: float
    ImbalanceDK2: float

class PowerSystemRightNowModel(BaseModel):
    """
    Represents the API response containing power system data.
    """
    total: int
    limit: int
    dataset: str
    records: List[PowerSystemRightNowRecords]

# Example usage:
response_data = {
    "total": 2959035,
    "limit": 4,
    "dataset": "PowerSystemRightNow",
    "records": [
        {
            "Minutes1UTC": "2024-07-05T13:54:00",
            "Minutes1DK": "2024-07-05T15:54:00",
            "CO2Emission": 36.959999,
            "ProductionGe100MW": 129.830002,
            "ProductionLt100MW": 332.970001,
            "SolarPower": 1455.709961,
            "OffshoreWindPower": 937.859985,
            "OnshoreWindPower": 2877.889893,
            "Exchange_Sum": -822.900024,
            "Exchange_DK1_DE": 1472.209961,
            "Exchange_DK1_NL": -188.830002,
            "Exchange_DK1_GB": -1000.77002,
            "Exchange_DK1_NO": -1371.0,
            "Exchange_DK1_SE": -535.0,
            "Exchange_DK1_DK2": 0.0,
            "Exchange_DK2_DE": 484.829987,
            "Exchange_DK2_SE": 321.390015,
            "Exchange_Bornholm_SE": -5.73,
            "aFRR_ActivatedDK1": -29.379999,
            "aFRR_ActivatedDK2": 0.0,
            "mFRR_ActivatedDK1": 83.199997,
            "mFRR_ActivatedDK2": -83.199997,
            "ImbalanceDK1": 64.870003,
            "ImbalanceDK2": -248.050003
        },
        # Add more records here as needed
    ]
}

# Parsing the API response into Pydantic model
parsed_response = APIResponseModel(**response_data)

# Accessing fields
print(parsed_response.total)
print(parsed_response.records[0].Minutes1UTC)
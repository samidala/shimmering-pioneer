from pydantic import BaseModel, Field
from typing import List, Optional

class FinancialMetric(BaseModel):
    label: str = Field(..., description="The name of the metric (e.g., P/E Ratio)")
    value: str = Field(..., description="The value of the metric")
    analysis: str = Field(..., description="A brief analysis of what this value means for the stock")

class InvestmentRecommendation(BaseModel):
    stock_symbol: str = Field(..., description="The ticker symbol of the stock")
    rating: str = Field(..., description="Buy, Sell, or Hold")
    confidence_score: float = Field(..., ge=0, le=1, description="Confidence score from 0 to 1")
    key_reasons: List[str] = Field(..., description="Top 3-5 reasons for the recommendation")
    risks: List[str] = Field(..., description="Potential risks identified")
    summary: str = Field(..., description="A detailed executive summary of the committee's findings")

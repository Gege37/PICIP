from pydantic import BaseModel
from typing import List


class ArticleAnalysis(BaseModel):

    summary: str

    sentiment: str

    sentiment_score: int

    classifications: List[str]

    topics: List[str]

    risk_level: str

    risk_indicators: List[str]

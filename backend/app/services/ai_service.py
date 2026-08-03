"""
AI Service
"""

from intelligence.pipeline import pipeline


class AIService:

    def analyze_article(self, article):

        return pipeline.process(article)


ai_service = AIService()

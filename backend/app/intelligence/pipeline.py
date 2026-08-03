"""
PICIP Intelligence Pipeline
"""

from .summarizer import summarizer
from .sentiment import sentiment
from .classifier import classifier
from .topic_detector import topic_detector
from .risk_analyzer import risk_analyzer


class IntelligencePipeline:

    def process(self, article: dict):

        text = article.get("text", "")

        return {
            "summary": summarizer.process(text).data,
            "sentiment": sentiment.process(text).data,
            "classification": classifier.process(text).data,
            "topics": topic_detector.process(text).data,
            "risk": risk_analyzer.process(text).data,
        }


pipeline = IntelligencePipeline()

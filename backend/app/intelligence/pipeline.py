"""
PICIP Intelligence Pipeline
"""

from .summarizer import summarizer
from .sentiment import sentiment
from .classifier import classifier
from .topic_detector import topic_detector
from .impact_analyzer import impact_analyzer


class IntelligencePipeline:

    def process(self, article):

        text = article.get("text","")

        return {

            "summary":
                summarizer.process(text).data,

            "sentiment":
                sentiment.process(text).data,

            "category":
                classifier.process(text).data,

            "impact":
                impact_analyzer.process(text).data,

            "topics":
                topic_detector.process(text).data

        }


pipeline = IntelligencePipeline()

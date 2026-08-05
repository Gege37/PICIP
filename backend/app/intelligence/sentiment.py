"""
PICIP Sentiment Analysis Engine

Determines the tone of a news event.
"""


from .base_ai import AIEngine, AIResult


class SentimentAnalyzer(AIEngine):

    name = "sentiment"


    positive_words = [

        "success",
        "growth",
        "positive",
        "agreement",
        "investment",
        "development",
        "achievement",
        "improvement"

    ]


    negative_words = [

        "crisis",
        "failure",
        "risk",
        "conflict",
        "loss",
        "attack",
        "armed",
        "war",
        "violence",
        "death",
        "emergency",
        "threat",
        "shortage",
        "outbreak",
        "instability"

    ]


    def process(self,text):

        text = text.lower()


        score = 0


        for word in self.positive_words:

            if word in text:

                score += 1



        for word in self.negative_words:

            if word in text:

                score -= 1



        if score > 0:

            label = "positive"


        elif score < 0:

            label = "negative"


        else:

            label = "neutral"



        return AIResult(

            data={

                "sentiment": label,

                "score": score

            }

        )


sentiment = SentimentAnalyzer()

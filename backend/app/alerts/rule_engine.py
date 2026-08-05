"""
PICIP Alert Rule Engine

Generates alert classification
from intelligence assessment.

Phase 5
"""


class AlertRuleEngine:


    def evaluate(self, analysis):


        impact = analysis.get(
            "impact",
            {}
        )


        sentiment = analysis.get(
            "sentiment",
            {}
        )


        category = analysis.get(
            "category",
            {}
        )


        impact_value = impact.get(
            "impact",
            "Local"
        )


        sentiment_value = sentiment.get(
            "sentiment",
            "neutral"
        ).lower()


        category_value = category.get(
            "category",
            "General"
        )


        #
        # Level 5 - Critical
        #

        if (
            impact_value == "National"
            and sentiment_value == "negative"
            and category_value == "Security"
        ):

            return {

                "alert_level": 5,

                "alert_type": "Critical",

                "message":
                "National impact negative event detected."

            }


        #
        # Level 4 - Warning
        #

        elif impact_value in [
            "National",
            "Continental",
            "International"
        ]:

            return {

                "alert_level": 4,

                "alert_type": "Warning",

                "message":
                "High impact event detected."

            }


        #
        # Level 3 - Watch
        #

        elif sentiment_value == "Negative":

            return {

                "alert_level": 3,

                "alert_type": "Watch",

                "message":
                "Negative media event requires monitoring."

            }


        #
        # Level 2 - Advisory
        #

        elif category_value != "General":

            return {

                "alert_level": 2,

                "alert_type": "Advisory",

                "message":
                "Relevant monitored event detected."

            }


        #
        # Level 1 - Information
        #

        else:

            return {

                "alert_level": 1,

                "alert_type": "Information",

                "message":
                "Routine monitored information."

            }



rule_engine = AlertRuleEngine()

"""
PICIP Impact Analyzer

Determines geographic scope of an event.
"""


from .base_ai import AIEngine, AIResult


class ImpactAnalyzer(AIEngine):

    name = "impact_analyzer"


    national = [
        "government",
        "president",
        "parliament",
        "cabinet",
        "angola",
        "national",
        "security",
        "armed",
        "attack",
        "crisis"
    ]


    continental = [
        "african union",
        " au ",
        "sadc"
    ]


    international = [
        "united nations",
        "imf",
        "world bank",
        "european union"
    ]


    def process(self,text):

        text = " " + text.lower() + " "


        impact = "Local"


        #
        # National priority
        #

        if any(
            word in text
            for word in self.national
        ):

            impact = "National"


        #
        # Only if not national
        #

        elif any(
            word in text
            for word in self.continental
        ):

            impact = "Continental"


        elif any(
            word in text
            for word in self.international
        ):

            impact = "International"



        return AIResult(
            data={
                "impact": impact
            }
        )


impact_analyzer = ImpactAnalyzer()

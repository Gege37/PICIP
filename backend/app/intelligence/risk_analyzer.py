"""
PICIP Risk Analysis Engine
"""

from .base_ai import AIEngine,AIResult



class RiskAnalyzer(AIEngine):

    name="risk_analyzer"


    risk_words=[
        "crisis",
        "war",
        "failure",
        "collapse",
        "sanction",
        "shortage"
    ]


    def process(self,text):

        text=text.lower()

        risks=[]


        for word in self.risk_words:

            if word in text:
                risks.append(word)



        level="low"


        if len(risks)>=3:
            level="high"

        elif len(risks)>0:
            level="medium"



        return AIResult(
            data={
                "risk_level":level,
                "indicators":risks
            }
        )


risk_analyzer=RiskAnalyzer()

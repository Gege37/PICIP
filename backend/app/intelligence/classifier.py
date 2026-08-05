"""
PICIP Category Classifier
"""


from .base_ai import AIEngine, AIResult


class Classifier(AIEngine):


    name = "classifier"



    categories = {


        "Security":[
            "police",
            "crime",
            "attack",
            "war",
            "armed",
            "security"
        ],


        "Politics":[
            "government",
            "president",
            "parliament",
            "minister"
        ],


        "Economy":[
            "market",
            "investment",
            "business",
            "inflation"
        ],


        "Health":[
            "hospital",
            "cholera",
            "health",
            "outbreak"
        ],


        "Diplomacy":[
            "embassy",
            "summit",
            "african union"
        ],


        "Mining":[
            "mine",
            "diamond",
            "gold",
            "drilling"
        ]


    }



    def process(self,text):

        text=text.lower()


        category="General"


        for name, words in self.categories.items():

            if any(
                word in text
                for word in words
            ):

                category=name
                break


        return AIResult(
            data={
                "category":category
            }
        )



classifier=Classifier()

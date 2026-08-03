"""
PICIP Article Classification
"""

from .base_ai import AIEngine,AIResult



class Classifier(AIEngine):

    name="classifier"


    categories={

        "politics":[
            "government",
            "president",
            "minister"
        ],

        "economy":[
            "market",
            "investment",
            "business"
        ],

        "mining":[
            "diamond",
            "gold",
            "mine",
            "drilling"
        ],

        "security":[
            "police",
            "crime",
            "attack"
        ]

    }



    def process(self,text):

        text=text.lower()

        result=[]


        for category,keywords in self.categories.items():

            for keyword in keywords:

                if keyword in text:
                    result.append(category)
                    break


        return AIResult(
            data={
                "classification":result
            }
        )


classifier=Classifier()

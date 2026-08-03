"""
PICIP Topic Detection
"""

from .base_ai import AIEngine,AIResult



class TopicDetector(AIEngine):

    name="topic_detector"


    def process(self,text):

        topics=[]

        words=text.lower().split()


        for word in words:

            if word not in topics:
                topics.append(word)


        return AIResult(
            data={
                "topics":topics[:10]
            }
        )


topic_detector=TopicDetector()

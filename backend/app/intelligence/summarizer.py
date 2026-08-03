"""
PICIP AI Summary Engine
"""

from .base_ai import AIEngine, AIResult


class Summarizer(AIEngine):

    name = "summarizer"


    def process(self, text):

        if not text:
            return AIResult(
                success=False,
                data={"summary": ""}
            )


        words = text.split()

        summary = " ".join(
            words[:50]
        )


        return AIResult(
            data={
                "summary": summary
            }
        )


summarizer = Summarizer()

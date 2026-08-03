"""
PICIP Phase 4
AI Processing Base Engine
"""

from datetime import datetime


class AIResult:

    def __init__(
        self,
        success=True,
        data=None,
        engine="rule-based"
    ):
        self.success = success
        self.data = data or {}
        self.engine = engine
        self.timestamp = datetime.utcnow().isoformat()


class AIEngine:

    name = "base"

    def process(self, text: str):

        raise NotImplementedError(
            "AI processors must implement process()"
        )

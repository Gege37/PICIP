"""
PICIP Intelligence Storage Layer

Stores AI analysis using an existing database transaction.
"""


def save_analysis(conn, article_id, analysis):

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO ai_analysis
        (
            article_id,
            summary,
            sentiment,
            sentiment_score,
            classification,
            topics,
            risk_level,
            risk_indicators,
            engine
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        RETURNING id;
        """,
        (
            article_id,

            analysis["summary"].get(
                "summary",
                ""
            ),

            analysis["sentiment"].get(
                "sentiment",
                "unknown"
            ),

            analysis["sentiment"].get(
                "score",
                0
            ),

            ",".join(
                analysis["classification"].get(
                    "classification",
                    []
                )
            ),

            ",".join(
                analysis["topics"].get(
                    "topics",
                    []
                )
            ),

            analysis["risk"].get(
                "risk_level",
                "low"
            ),

            ",".join(
                analysis["risk"].get(
                    "indicators",
                    []
                )
            ),

            "rule-based"
        )
    )

    analysis_id = cur.fetchone()[0]

    cur.close()

    print(
        "Saved AI analysis:",
        analysis_id
    )

    return analysis_id

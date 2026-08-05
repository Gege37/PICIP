"""
PICIP Intelligence Storage

Stores AI assessment results.
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
            category,
            impact,
            topics,
            engine
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s
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
                "Neutral"
            ),

            analysis["sentiment"].get(
                "score",
                0
            ),

            analysis["category"].get(
                "category",
                "General"
            ),

            analysis["impact"].get(
                "impact",
                "Local"
            ),

            ",".join(
                analysis["topics"].get(
                    "topics",
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

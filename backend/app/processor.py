from database import get_connection

from services.ai_service import ai_service

from intelligence.storage import save_analysis

from alerts.rule_engine import rule_engine
from alerts.storage import save_alert


def save_article(article, source_id=None):

    conn = get_connection()
    cur = conn.cursor()

    try:

        #
        # Duplicate check
        #

        cur.execute(
            """
            SELECT id
            FROM articles
            WHERE url=%s;
            """,
            (
                article["url"],
            )
        )

        existing=cur.fetchone()

        if existing:

            print(
                "Duplicate skipped:",
                article["title"]
            )

            return existing[0]

        #
        # Save article
        #

        cur.execute(
            """
            INSERT INTO articles
            (
                source_id,
                title,
                content,
                url,
                language
            )
            VALUES
            (
                %s,%s,%s,%s,%s
            )
            RETURNING id;
            """,
            (
                source_id,
                article["title"],
                article["content"],
                article["url"],
                "unknown"
            )
        )

        article_id=cur.fetchone()[0]

        print(
            "Saved article:",
            article_id,
            article["title"]
        )

        #
        # AI
        #

        analysis=ai_service.analyze_article(
            {
                "text":article["content"]
            }
        )

        save_analysis(
            conn,
            article_id,
            analysis
        )

        #
        # Alert Engine
        #

        alert=rule_engine.evaluate(
            analysis
        )

        save_alert(
            conn,
            article_id,
            alert
        )

        conn.commit()

        return article_id

    except Exception as e:

        conn.rollback()

        print(
            "Transaction rolled back:",
            e
        )

        raise

    finally:

        cur.close()
        conn.close()

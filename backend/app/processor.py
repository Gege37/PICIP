from database import get_connection


def save_article(article, source_id=None):

    conn = get_connection()
    cur = conn.cursor()


    cur.execute(
        """
        SELECT id
        FROM articles
        WHERE url = %s;
        """,
        (
            article["url"],
        )
    )


    existing = cur.fetchone()


    if existing:

        cur.close()
        conn.close()

        print(
            "Duplicate skipped:",
            article["title"]
        )

        return existing[0]


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


    article_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()


    print(
        "Saved article:",
        article_id,
        article["title"]
    )


    return article_id

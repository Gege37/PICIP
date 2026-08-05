"""
PICIP Alert Storage
"""


def save_alert(conn, article_id, alert):

    cur = conn.cursor()


    cur.execute(
        """
        INSERT INTO alerts
        (
            article_id,
            alert_level,
            alert_type,
            message
        )
        VALUES
        (
            %s,%s,%s,%s
        )
        RETURNING id;
        """,
        (

            article_id,

            alert["alert_level"],

            alert["alert_type"],

            alert["message"]

        )
    )


    alert_id = cur.fetchone()[0]


    cur.close()


    print(
        "Saved alert:",
        alert_id
    )


    return alert_id

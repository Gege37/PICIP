from database import get_connection


def log_change(
    source_id,
    old_type,
    new_type,
    reason,
    status
):
    """
    Store every automatic source decision.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO source_health_history
        (
            source_id,
            old_type,
            new_type,
            reason,
            status
        )
        VALUES
        (
            %s,%s,%s,%s,%s
        );
        """,
        (
            source_id,
            old_type,
            new_type,
            reason,
            status
        )
    )

    conn.commit()

    cur.close()
    conn.close()


def update_source_type(
    source_id,
    new_type
):
    """
    Update the preferred collection method.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT type
        FROM media_sources
        WHERE id=%s;
        """,
        (
            source_id,
        )
    )

    row = cur.fetchone()

    if row is None:

        cur.close()
        conn.close()

        return

    old_type = row[0]

    if old_type == new_type:

        cur.close()
        conn.close()

        return

    cur.execute(
        """
        UPDATE media_sources
        SET type=%s
        WHERE id=%s;
        """,
        (
            new_type,
            source_id
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    log_change(
        source_id,
        old_type,
        new_type,
        "Automatic source optimization",
        "AUTO_SWITCH"
    )

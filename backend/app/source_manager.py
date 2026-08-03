from database import get_connection


def get_active_sources():
    """
    Return all active media sources configured in PICIP.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            id,
            name,
            type,
            url,
            country
        FROM media_sources
        WHERE active = TRUE
        ORDER BY id;
        """
    )

    sources = cur.fetchall()

    cur.close()
    conn.close()

    return sources


def get_source_id(url):
    """
    Find source ID using RSS URL.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id
        FROM media_sources
        WHERE url = %s;
        """,
        (url,)
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return result[0]

    return None


def add_source(name, source_type, url, country):
    """
    Add a new media source.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO media_sources
        (
            name,
            type,
            url,
            country
        )
        VALUES
        (
            %s,%s,%s,%s
        )
        RETURNING id;
        """,
        (
            name,
            source_type,
            url,
            country
        )
    )

    source_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return source_id

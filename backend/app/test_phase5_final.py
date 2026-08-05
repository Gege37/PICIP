from processor import save_article


article = {

    "title":
    "National Security Alert Test",

    "content":
    """
    A security incident was reported involving armed conflict.
    The government announced emergency measures to protect national stability.
    """,

    "url":
    "https://test.local/security-national-alert"

}


save_article(
    article,
    source_id=1
)

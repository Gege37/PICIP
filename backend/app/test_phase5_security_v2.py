from processor import save_article


article = {

    "title":
    "National Security Incident Assessment Test",

    "content":
    """
    The government announced emergency measures after an armed security attack.
    The President addressed the nation regarding national stability.
    """,

    "url":
    "https://test.local/security-national-alert-v2"

}


save_article(
    article,
    source_id=1
)

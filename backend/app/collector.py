import feedparser


def collect_rss(url):

    feed = feedparser.parse(url)

    articles = []

    for item in feed.entries:

        articles.append({

            "title": item.title,

            "url": item.link,

            "content": item.get(
                "summary",
                ""
            )

        })

    return articles

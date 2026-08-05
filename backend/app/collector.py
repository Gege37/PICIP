import requests
import feedparser


HEADERS = {
    "User-Agent": "PICIP-Media-Monitor/1.0"
}


def collect_rss(url):

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        response.raise_for_status()


        feed = feedparser.parse(
            response.text
        )


    except Exception as e:

        print(
            f"RSS collection failed: {e}"
        )

        return []


    articles = []


    for item in feed.entries:

        articles.append({

            "title": item.get(
                "title",
                ""
            ),

            "url": item.get(
                "link",
                ""
            ),

            "content": item.get(
                "summary",
                ""
            )

        })


    return articles

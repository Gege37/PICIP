import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin


HEADERS = {
    "User-Agent":
        "Mozilla/5.0 PICIP Intelligence Platform"
}


def collect_angop(url):

    articles = []

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        seen = set()


        #
        # ANGOP article discovery
        #

        for link in soup.find_all(
            "a",
            href=True
        ):

            href = urljoin(
                url,
                link["href"]
            )

            title = link.get_text(
                " ",
                strip=True
            )


            if len(title) < 20:
                continue


            if href in seen:
                continue


            #
            # avoid menus
            #

            if "/noticias/" not in href.lower():

                continue


            seen.add(href)


            articles.append(
                {
                    "title": title,
                    "content": "",
                    "url": href
                }
            )


        print(
            f"ANGOP parser discovered {len(articles)} articles."
        )


        return articles


    except Exception as e:

        print(
            f"ANGOP parser failed: {e}"
        )

        return []

from website_detector import detect_website
from angop_parser import collect_angop


import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin


HEADERS = {
    "User-Agent":
        "Mozilla/5.0 PICIP Intelligence Platform"
}



def collect_web(url):

    website = detect_website(url)


    print(
        f"WEB detector: {website}"
    )


    if website == "ANGOP":

        return collect_angop(url)



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


            if len(title) < 25:
                continue


            if href in seen:
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
            f"Generic WEB parser discovered {len(articles)} articles."
        )


        return articles


    except Exception as e:

        print(
            f"WEB collector failed: {e}"
        )

        return []

"""
PICIP Phase 4
End-to-End Pipeline Test

Source
 -> Dispatcher
 -> Collector
 -> Processor
 -> Intelligence
 -> Database
 -> Alerts
"""

import sys

sys.path.append("/app/app")

from source_dispatcher import collect_source


def main():

    print("=" * 60)
    print("PICIP END TO END PIPELINE TEST")
    print("=" * 60)


    source = (
        1,
        "ANGOP",
        "RSS",
        "https://www.angop.ao/rss"
    )


    articles, engine, status = collect_source(source)


    print()
    print("SOURCE:")
    print(source[1])

    print()
    print("ENGINE:")
    print(engine)

    print()
    print("STATUS:")
    print(status)

    print()
    print("ARTICLES:")
    print(len(articles))


    if articles:
        print()
        print("FIRST ARTICLE")
        print(articles[0])


if __name__ == "__main__":
    main()

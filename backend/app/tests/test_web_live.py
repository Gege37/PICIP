"""
Temporary live WEB validation.
Delete before commit.
"""

from source_manager import get_active_sources
from source_dispatcher import collect_source


sources = get_active_sources()


for source in sources:

    if source[2] == "WEB":

        print()
        print("=" * 60)
        print(source)
        print("=" * 60)

        articles, source_type, status = collect_source(source)

        print("TYPE:", source_type)
        print("STATUS:", status)
        print("COUNT:", len(articles))

        for a in articles[:3]:
            print()
            print(a["title"])
            print(a["url"])

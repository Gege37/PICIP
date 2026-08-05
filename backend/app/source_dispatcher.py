from collector import collect_rss
from web_collector import collect_web
from youtube_collector import collect_youtube

def collect_source(source):

    source_name = source[1]
    source_type = source[2].upper()
    source_url = source[3]

    print(
        f"Collecting from: {source_name} ({source_type})"
    )

    if source_type == "API":

        return [], "API", "NO_API"

    elif source_type == "RSS":

        articles = collect_rss(source_url)

        if articles:

            return articles, "RSS", "OK"

        print("RSS unavailable, trying WEB...")

        articles = collect_web(source_url)

        return articles, "WEB", "RSS_DOWN"

    elif source_type == "WEB":

        articles = collect_web(source_url)

        if articles:

            return articles, "WEB", "OK"

        print("WEB unavailable.")

        return [], "WEB", "FAILED"

    elif source_type == "YOUTUBE":

        articles = collect_youtube(source_url)

        return articles, "YOUTUBE", "OK"

    elif source_type == "TELEGRAM":

        return [], "TELEGRAM", "NOT_IMPLEMENTED"

    elif source_type == "FACEBOOK":

        return [], "FACEBOOK", "NOT_IMPLEMENTED"

    elif source_type == "X":

        return [], "X", "NOT_IMPLEMENTED"

    elif source_type == "LINKEDIN":

        return [], "LINKEDIN", "NOT_IMPLEMENTED"

    elif source_type == "INSTAGRAM":

        return [], "INSTAGRAM", "NOT_IMPLEMENTED"

    elif source_type == "TIKTOK":

        return [], "TIKTOK", "NOT_IMPLEMENTED"

    elif source_type == "SOCIAL":

        return [], "SOCIAL", "NOT_IMPLEMENTED"

    return [], source_type, "UNKNOWN"

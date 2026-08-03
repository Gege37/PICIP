from urllib.parse import urlparse


def detect_website(url):

    domain = urlparse(url).netloc.lower()

    if "angop.ao" in domain:
        return "ANGOP"

    if "bbc." in domain:
        return "BBC"

    if "cnn." in domain:
        return "CNN"

    if "miningweekly." in domain:
        return "MINING_WEEKLY"

    return "GENERIC"

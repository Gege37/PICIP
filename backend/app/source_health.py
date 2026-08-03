import socket
import requests


# Highest -> Lowest reliability
PRIORITY = [
    "API",
    "RSS",
    "TELEGRAM",
    "YOUTUBE",
    "WEB",
    "FACEBOOK",
    "X",
    "LINKEDIN",
    "INSTAGRAM",
    "TIKTOK",
    "SOCIAL"
]


def check_url(url, timeout=10):
    """
    Simple availability test.
    Returns True if the endpoint is reachable.
    """

    try:

        response = requests.get(
            url,
            timeout=timeout,
            headers={
                "User-Agent": "PICIP/1.0"
            }
        )

        return response.status_code < 500

    except (
        requests.RequestException,
        socket.timeout
    ):

        return False


def next_method(current_method):

    current_method = current_method.upper()

    if current_method not in PRIORITY:
        return None

    index = PRIORITY.index(current_method)

    if index >= len(PRIORITY) - 1:
        return None

    return PRIORITY[index + 1]


def best_method():

    return PRIORITY[0]

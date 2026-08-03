import time

from source_manager import get_active_sources
from source_dispatcher import collect_source
from processor import save_article
from source_health_manager import log_change


print("PICIP Python Monitoring Engine Starting")


SLEEP_TIME = 900   # 15 minutes


def monitoring_cycle():

    print("\nLoading active sources...")

    sources = get_active_sources()

    print(
        f"Active sources found: {len(sources)}"
    )


    for source in sources:

        source_id = source[0]
        source_name = source[1]
        current_type = source[2].upper()


        print(
            f"\nProcessing source: {source_name} ({current_type})"
        )


        try:

            articles, used_type, status = collect_source(
                source
            )


            print(
                f"{source_name}: "
                f"{len(articles)} articles collected "
                f"using {used_type}"
            )


            #
            # Record automatic fallback/recovery
            #

            if used_type != current_type:

                log_change(
                    source_id,
                    current_type,
                    used_type,
                    "Automatic collector fallback/recovery",
                    status
                )


            #
            # Save articles
            #

            for article in articles:

                save_article(
                    article,
                    source_id
                )


        except Exception as e:

            print(
                f"{source_name} failed: {e}"
            )


    print(
        "\nPICIP Monitoring Cycle Completed"
    )



while True:

    try:

        monitoring_cycle()


    except Exception as e:

        print(
            f"Monitoring error: {e}"
        )


    print(
        f"\nWaiting {SLEEP_TIME} seconds..."
    )


    time.sleep(SLEEP_TIME)

import psycopg2
import os


def get_connection():

    return psycopg2.connect(

        host="postgres",

        database=os.getenv(
            "POSTGRES_DB",
            "picip"
        ),

        user=os.getenv(
            "POSTGRES_USER",
            "picip_admin"
        ),

        password=os.getenv(
            "POSTGRES_PASSWORD",
            "picip_password"
        )

    )

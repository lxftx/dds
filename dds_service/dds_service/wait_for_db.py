import os
import time

import psycopg2
from psycopg2 import OperationalError


def wait_for_db():
    db_ready = False
    while not db_ready:
        try:
            conn = psycopg2.connect(
                dbname=os.environ.get("DDS_DB_NAME"),
                user=os.environ.get("DDS_DB_USER"),
                password=os.environ.get("DDS_DB_PASS"),
                host=os.environ.get("DDS_DB_HOST"),
                port=os.environ.get("DDS_DB_PORT")
            )
            db_ready = True
        except OperationalError:
            print("Ждем готовности базы данных...")
            time.sleep(2)

if __name__ == '__main__':
    wait_for_db()
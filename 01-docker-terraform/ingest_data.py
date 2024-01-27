#!/usr/bin/env python
# coding: utf-8

import os
import argparse
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = 'output.parquet'

    os.system(f'wget -O {parquet_name} {url}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    parquet_file = pq.ParquetFile(parquet_name)
    df = parquet_file.read_row_group(0).to_pandas()

    df.to_sql(name=table_name, con=engine, if_exists='append')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest Parquet data to Postgres')

    # user
    # password
    # host
    # port
    # database name
    # table name
    # url of the parquet
    parser.add_argument('--user', help='user name for Postgres')
    parser.add_argument('--password', help='password for Postgres')
    parser.add_argument('--host', help='host for Postgres')
    parser.add_argument('--port', help='port for Postgres')
    parser.add_argument('--db', help='database name for Postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the parquet file')

    args = parser.parse_args()
    main(args)
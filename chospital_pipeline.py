#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import sqlalchemy as sa
from urllib.parse import quote
import datetime

cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M%S')
print('Current Time : ',cur_time)

## 1. Extract from 202.44.12.115
conn_str = f"mysql+pymysql://testuser:{quote('P@ssw0rd')}@202.44.12.115:3306/de_inter"
engine = sa.create_engine(conn_str)
conn = engine.connect()
chospital = pd.read_sql("chospital", conn)
conn.close()

## 2. Load to Localhost
conn_str = f"mysql+pymysql://root:@localhost:3306/de_inter"
engine = sa.create_engine(conn_str)
conn = engine.connect()
chospital.to_sql("chospital", conn, index=None, if_exists="replace")
conn.close()



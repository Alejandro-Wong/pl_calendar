import os
import datetime
import logging
from dotenv import load_dotenv
import pandas as pd

import schwabdev

from funcs import *

"""
Retrieve order data from Charles Schwab API for all accounts, extract relevant data, combine all data into one DataFrame
"""

# Load environment variables
load_dotenv()

# Console logger
logging.basicConfig(level=logging.INFO)

# Client
client = schwabdev.Client(os.getenv('app_key'), os.getenv('app_secret'), os.getenv('callback_url'))

# Accounts
linked_accounts = client.account_linked().json()
cash_account = linked_accounts[0].get('hashValue')
margin_account = linked_accounts[1].get('hashValue') 

# Orders by account
cash_acct_orders = client.account_orders(cash_account, datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=65), datetime.datetime.now(datetime.timezone.utc)).json()
margin_acct_orders = client.account_orders(margin_account, datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=65), datetime.datetime.now(datetime.timezone.utc)).json() 

# Account DataFrames
cash_df = extract_orders(cash_acct_orders)
margin_df = extract_orders(margin_acct_orders)

# Combined DataFrame
orders_df = pd.concat([cash_df, margin_df])
orders_df = orders_df.sort_values(by=['date','time'])
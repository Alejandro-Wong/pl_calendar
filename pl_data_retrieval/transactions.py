import os
import datetime
import logging
from dotenv import load_dotenv
import pandas as pd

import schwabdev

from funcs import *

"""
Retrieve transactions data from Charles Schwab API for all accounts, extract relevant data, combine all data into one DataFrame
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

# Transactions by account
cash_acct_trans = client.transactions(cash_account, datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=65), datetime.datetime.now(datetime.timezone.utc), "TRADE").json()
margin_acct_trans = client.transactions(margin_account, datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=65), datetime.datetime.now(datetime.timezone.utc), "TRADE").json()

# Account DataFrames
cash_df = extract_transactions(cash_acct_trans)
margin_df = extract_transactions(margin_acct_trans)

# Combined DataFrame
transactions_df = pd.concat([cash_df, margin_df])
transactions_df = transactions_df.sort_values(by=['date','time'])
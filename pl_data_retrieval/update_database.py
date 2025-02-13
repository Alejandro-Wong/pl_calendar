import pandas as pd
import os
from profit_loss import profit_loss
from orders import orders_df
from transactions import transactions_df
from dotenv import load_dotenv
import psycopg2

"""
Creates two DataFrames: one of the daily profit/loss data for the latest 65 days, and
one of of the latest profit/loss data saved to the PostgreSQL server. The two DataFrames
are compared and the PostgreSQL database is updated with any rows it does not yet have.
"""

# Load in environment variables
load_dotenv()

database = os.getenv("database")
# user = os.getenv("user")
# password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")


def update_database():
    # Merge transactions and orders DataFrames
    df = pd.merge(transactions_df, orders_df, how='right')
    df = df.set_index('date')


    # Create Profit/Loss DataFrame
    profit_loss_dict = profit_loss(df)
    pl = pd.DataFrame(profit_loss_dict, index=['profit_loss']).T
    pl.index.name = 'date'
    pl = pl.reset_index()
    pl = pl.reset_index(drop=True)
    pl['profit_loss'] = pl['profit_loss'].astype(str)
    pl['date'] = pl['date'].astype(str)


    # Retrieve PostgreSQL Database
    conn = psycopg2.connect(database=database, host=host, port=port)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute('''SELECT * from pl_calendar''')
    fetch_pg_pl = cursor.fetchall()


    # Create DataFrame from PostgreSQL Database
    pg_df = pd.DataFrame(fetch_pg_pl)
    pg_df = pg_df.rename(columns={0:'date', 1:'profit_loss'})
    pg_df['profit_loss'] = pg_df['profit_loss'].astype(str)
    pg_df['date'] = pg_df['date'].astype(str)


    # Find difference between Profit/Loss DataFrame and Postgres DataFrame
    diff = pd.merge(pg_df.tail(10), pl.tail(10), how='right', indicator=True)
    diff = diff[diff['_merge'] == 'right_only']
    diff = diff.drop(columns=['_merge']).reset_index(drop=True)


    # Append new entries to Postgres DataFrame
    if len(diff) > 0:
        for i, row in diff.iterrows():
            cursor.execute(f"INSERT INTO pl_calendar(date, profit_loss) VALUES('{row['date']}', '{row['profit_loss']}')")


if __name__ == "__main__":
    update_database()
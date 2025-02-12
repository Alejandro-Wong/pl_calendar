import pandas as pd
from decimal import Decimal, ROUND_UP


def profit_loss(df:pd.DataFrame) -> dict:

    """

    Function for calculating daily profit/loss. Takes in DataFrame created from combining relevant data from 
    orders and transactions data and returns dictionary with dates as keys and $ profit/loss as values

    
    Profit/Loss Algorithm:

    'entry' dictionary tracks both total debit/credit, and quantity of shares long/short for each position.
    'exit' dictionary tracks both total return, and quantity of shares sold/covered for each position.
    When 'entry' and 'exit' quantities match, the trade for that symbol/contract is complete. Total gain/loss 
    for each trade is tracked by 'trade' dictionary. When trade is complete, total gain/loss value is added to 
    corresponding date's profit/loss in 'pl' dictionary. Symbol/contract is then deleted from 'entry', 'exit', 
    and 'trade' keys to prevent possible calculation errors in cases where the same symbol/contract is traded
    more than once.

    """
    
    # Dictionaries
    pl = {}                 # Profit/Loss - Date : Calculated Profit/Loss (initialized to 0)
    for date in df.index:
        pl[date] = 0

    entry = {}              # Entry - Symbol/Contract : [Debit/Credit , Quantity]
    exit = {}               # Exit - Symbol/Contract : [Return , Quantity]
    trade = {}              # Trade - Symbol/Contract : Entry[Debit/Credit] + Exit[Return]

    # Iterrate through rows of DataFrame
    for i, row in df.iterrows():
        
        # Columns variables
        symbol = row['symbol']
        net_amount = row['net_amount']
        quantity = row['quantity']
        instruction = row['instruction']

        # Profit/Loss Calculation Algorithm:
        if (
            'BUY_TO_OPEN' in instruction or
            'SELL_TO_OPEN' in instruction or
            'BUY' in instruction
        ):  
            if symbol not in entry.keys():
                entry[symbol] = [net_amount, quantity]
            else:
                entry[symbol][0] += net_amount
                entry[symbol][1] += quantity
        
        elif (
            'SELL_TO_CLOSE' in instruction or
            'BUY_TO_CLOSE' in instruction or
            'SELL' in instruction
        ):
            if symbol not in exit.keys():
                exit[symbol] = [net_amount, quantity]
            else:
                exit[symbol][0] += net_amount
                exit[symbol][1] += quantity

        if symbol in entry.keys() and symbol in exit.keys():

            if entry[symbol][1] == exit[symbol][1]:
                trade[symbol] = (entry[symbol][0] + exit[symbol][0])
                pl[i] += Decimal(trade[symbol]).quantize(Decimal('0.01'), rounding=ROUND_UP)
                del entry[symbol]
                del exit[symbol]
                del trade[symbol]

    return pl
    

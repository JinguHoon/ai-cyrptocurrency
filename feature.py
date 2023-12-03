import pandas as pd
import math


def cal_mid_price (gr_bid_level, gr_ask_level):

    if len(gr_bid_level) > 0 and len(gr_ask_level) > 0:
        bid_top_price = gr_bid_level.iloc[0].price
        ask_top_price = gr_ask_level.iloc[0].price
        mid_price = (bid_top_price + ask_top_price) * 0.5 #what is mid price?

        return (mid_price)

    else:
        print ('Error: serious cal_mid_price')
        return (-1)
    
def cal_book_balance(gr_bid_level, gr_ask_level, mid_price):
    ratio = 0.2
    level = 5
    interval = 1
    bidPx = 0.0
    askPx = 0.0
    bidQty = 0.0
    askQty = 0.0
    keys = gr_bid_level.keys()
    if len(gr_bid_level) > 0 and len(gr_ask_level) > 0:
        for i in keys:
            print(keys)
            #cal_bidQty = pow(gr_bid_level.loc[i].quantity, ratio)
            #cal_askQty = pow(gr_ask_level.loc[i].quantity, ratio)
            #bidQty += cal_bidQty 
            #askQty += cal_askQty
            #bidPx += cal_bidQty * gr_bid_level.loc[i].price
            #askPx += cal_askQty * gr_ask_level.loc[i].price

        #book_price = (((askQty*bidPx)/bidQty) + ((bidQty*askPx)/askQty)) / (bidQty+askQty)

        #book_balance = (book_price-mid_price) / interval
        #return (book_balance)

    else:
        print ('Error: serious cal_book_balance')
        return (-1)    


df = pd.read_csv('2023-12-03-bithumb-btc-orderbook.csv').apply(pd.to_numeric,errors='ignore')
groups = df.groupby('timestamp')

keys = groups.groups.keys()

for i in keys:
    select_gr = groups.get_group(i)
    
    gr_bid_level = select_gr[(select_gr.type==0)]
    gr_ask_level = select_gr[(select_gr.type==1)]

    mid_price = cal_mid_price(gr_bid_level, gr_ask_level) 
    book_balance = cal_book_balance(gr_bid_level, gr_ask_level, mid_price)
    print(i, mid_price, book_balance)
    


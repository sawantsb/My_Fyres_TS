# from RivCls import *
from datetime import *
import calendar
#import goto
from fyers_api import accessToken, fyersModel
import webbrowser
import requests as requests
import numpy as np
import csv
import json
from types import SimpleNamespace
import os
import math
import time
import sys

# Login function
# def RivLogin():

# RivWeekKey = '22APR'
# RivWeekKey= '22505'
# RivWeekKey= '22512'
# RivWeekKey = '22519'
# RivWeekKey = '22MAY'
# RivWeekKey = '22623'
#RivWeekKey = '22JUN'
#RivWeekKey = '22721'
#RivWeekKey = '22922'
#RivWeekKey = '22JUL'

print('Function-Login process Started')

print('Reading Input file')
Settings_Jfname = 'home/InputSettings.json'

with open(Settings_Jfname, 'r') as Settings_Jason_Read:
        JfileContent = (Settings_Jason_Read.read())
        if JfileContent != '':
            print(Settings_Jason_Read.name)
            data = JfileContent
            Setting_Jobject = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
            RivWeekKey = str(Setting_Jobject.RivWeekKey)
            RivST1_Qty = int(Setting_Jobject.RivST1QTY)

            print(RivWeekKey)
        else:
            print('Jason file is empty')

print('Reading Input file complete')


redirect_uri = "https://127.0.0.1"
client_id = "J1FYPHMZMF-100"
secret_key = "72RNWQQY61"
grant_type = "authorization_code"
response_type = "code"
state = "sample"
### Connect to the sessionModel object here with the required input parameters
appSession = accessToken.SessionModel(client_id=client_id, redirect_uri=redirect_uri, response_type=response_type,
                                      state=state, secret_key=secret_key, grant_type=grant_type)

# Make  a request to generate_authcode object this will return a login url which you need to open in your browser
# from where you can get the generated auth_code
generateTokenUrl = appSession.generate_authcode()
print((generateTokenUrl))
webbrowser.open(generateTokenUrl, new=1)

# ## After succesfull login the user can copy the generated auth_code over here and make the request to generate the
# accessToken
print("Paste the auth_code generated from the first request : ")
auth_code = input()
appSession.set_token(auth_code)
response = appSession.generate_token()

# ## There can be two cases over here you can successfully get the acccessToken over the request or you might get
# some error over here. so to avoid that have this in try except block
try:
    access_token = response["access_token"]
    print(access_token)
except Exception as e:
    print(e,
          response)  # # This will help you in debugging then and there itself like what was the error and also you
    # would be able to see the value you got in response variable. instead of getting key_error for unsuccessfull
    # response.

    # # Once you have generated accessToken now we can call multiple trading related or data related apis after that
    # in order to do so we need to first initialize the fyerModel object with all the requried params.
    """
    fyerModel object takes following values as arguments
    1. accessToken : this is the one which you received from above 
    2. client_id : this is basically the app_id for the particular app you logged into
    """
fyers = fyersModel.FyersModel(token=access_token, is_async=False, client_id=client_id, log_path="home/downloads/")

### After this point you can call the relevant apis and get started with

####################################################################################################################
"""
  1. User Apis : This includes (Profile,Funds,Holdings)
"""

print(fyers.get_profile())  ## This will provide us with the user related data

print(fyers.funds())  ## This will provide us with the funds the user has

print(fyers.holdings())  ## This will provide the available holdings the user has
####################################################################################################################
"""
  2. Transaction Apis : This includes (Tradebook,Orderbook,Positions)
"""

print(fyers.tradebook())  ## This will provide all the trade related information

print(fyers.orderbook())  ## This will provide the user with all the order realted information

print(fyers.positions())  ## This will provide the user with all the positions the user has on his end

######################################################################################################################
"""
  3. Download Symbol List
"""
req = requests.get('https://public.fyers.in/sym_details/NSE_FO.csv')
url_content = req.content
csv_file = open('home/downloads/NFO_Symbol.csv', 'wb')
csv_file.write(url_content)
csv_file.close()
######################################################################################################################
print('Function-Login process Successful !!!')


# return fyers

######################################################################################################################


class RivStraddleStrategyDetails:
    def __init__(self):
        self.Entered = ""
        self.Exited = ""
        self.date_num = ""
        self.Strategy = 'Straddle2'
        self.Entry_Time = ''
        self.CE_Symbol = ''
        self.PE_Symbol = ''
        self.CE_Entry_Price = ''
        self.PE_Entry_Price = ''
        self.CE_SL = ''
        self.PE_SL = ''
        self.CE_Exit_Price = ''
        self.PE_Exit_Price = ''
        self.CE_Exit_Time = ''
        self.PE_Exit_Time = ''
        self.CE_Oder_ID = ''
        self.PE_Oder_ID = ''
        self.CE_Oder_ID_Status = ''
        self.PE_Oder_ID_Status = ''
        self.CE_SL_Oder_ID = ''
        self.PE_SL_Oder_ID = ''
        self.CE_SL_Oder_ID_Status = ''
        self.PE_SL_Oder_ID_Status = ''
        self.Number_Of_Leg_In = ''

    def __del__(self):
        print('Inside destructor')
        print('Riv Straddle Details-Destroyed')


class RivDirectionalStrangle:
    def __init__(self):
        self.Symbol = ''
        self.Big_Leg_Main = ''
        self.Big_Leg_Main_Status = ''
        self.Big_Leg_TGT = ''
        self.Big_Leg_TGT_Status = ''
        self.Big_Leg_SL = ''
        self.Big_Leg_SL_Status = ''
        self.Sml_Leg_Main = ''
        self.Sml_Leg_Main_Status = ''
        self.Sml_Leg_TGT = ''
        self.Sml_Leg_TGT_Status = ''
        self.Sml_Leg_SL = ''
        self.Sml_Leg_SL_Status = ''
        self.Big_Leg_Symbol = ''
        self.SML_Leg_Symbol = ''
        self.Big_Leg_Entry_Price = ''
        self.Sml_Leg_Entry_Price = ''
        self.Big_Leg_SL_Price = ''
        self.Sml_Leg_SL_Price = ''
        self.date_num = ''
        self.In_Trade = ''
        self.Out_Trade = ''
        self.In_Ami = ''
        self.Order_Type = ''
        self.All_Legs_In = ''

    def ST3_Check_Ami(self):
        openPosition = ''
        with open("C:/Program Files (x86)/ATS/ATS_INT_5MIN_BN_V10/ORB_Input.csv") as file_name:
            file_read = csv.reader(file_name)
            array = list(file_read)
            my_array = np.asarray(array)
            self.In_Ami = False
            try:
                for x in my_array:
                    fullstring = x[1]
                    if fullstring != None:
                        self.In_Ami = True
                        self.Order_Type = fullstring
                        break
            except Exception:
                print('Error in reading ami Results')

    def ST3_Check_Orderbook(self):
        print('Test')

    def ST3_Check_Strange_Exceuted(self):
        print('test')

    def ST3_Get_All_Order_Staus(ST3):
        ST3.Big_Leg_Main = Order_Status(ST3.Big_Leg_Main)
        ST3.Big_Leg_TGT = Order_Status(ST3.Big_Leg_TGT)
        ST3.Big_Leg_SL = Order_Status(ST3.Big_Leg_SL)
        ST3.Sml_Leg_Main = Order_Status(ST3.Sml_Leg_Main)
        ST3.Sml_Leg_TGT = Order_Status(ST3.Sml_Leg_TGT)
        ST3.Sml_Leg_SL = Order_Status(ST3.Sml_Leg_SL)
        # 1 = > Canceled
        # 2 = > Traded / Filled
        # 3 = > (Not used currently)
        # 4 = > Transit
        # 5 = > Rejected
        # 6 = > Pending
        # 7 = > Expired

    def ST3_Strangle_Status(ST3):
        print('Checking ST3_Strangle_Status')
        Strangle_Staus = False
        if (ST3.Big_Leg_Main == 2 and ST3.ST3.Big_Leg_TGT == 6 and ST3.ST3.Big_Leg_SL == 6) and (
                ST3.Sml_Leg_Main == 2 and ST3.ST3.Sml_Leg_TGT == 6 and ST3.ST3.Sml_Leg_SL == 6):
            Strangle_Status = True

        return Strangle_Staus

        # 1 = > Canceled
        # 2 = > Traded / Filled
        # 3 = > (Not used currently)
        # 4 = > Transit
        # 5 = > Rejected
        # 6 = > Pending
        # 7 = > Expired

    def ST3_Close_All_Order(ST3):
        ExitPosition(ST3.Big_Leg_Main)
        ExitPosition(ST3.Sml_Leg_Main)
        CancelOrder(ST3.Big_Leg_TGT)
        CancelOrder(ST3.Big_Leg_SL)
        CancelOrder(ST3.Sml_Leg_TGT)
        CancelOrder(ST3.Sml_Leg_SL)
        ST3.Out_Trade = True


class RivSingleStatDetails:
    def __init__(self):
        self.Entered = ""
        self.Exited = ""
        self.date_num = ""
        self.Strategy = 'Single_Leg'
        self.Entry_Time = ''
        self.Stock = ''
        self.Entry_Price = ''
        self.SL = ''
        self.NTrade = 0
        self.InSignalType = ''

    def __del__(self):
        print('Inside destructor')
        print('RivSingleStatDetails-Destroyed')


class RivTime:
    def __init__(self):
        self.dt_string = ''
        self.datetime_num = ''
        self.datetime_num_Str = ''
        self.date_num = ''
        self.time_num = ''
        self.time_min = ''
        self.time_sec = ''
        self.time_datetime_num_Str = ''
        self.day = ''

    def RivTimeNow(self):
        # print('Running RivTime Function')
        now = datetime.now()
        curr_date = date.today()
        self.dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.datetime_num = int(now.strftime("%d%m%Y_%H%M%S"))
        self.date_num = int(now.strftime("%d%m%Y"))
        self.day = str(calendar.day_name[curr_date.weekday()])
        self.datetime_num_Str = now.strftime("%d%m%Y_%H%M%S")
        self.time_num = int(now.strftime("%H%M%S"))
        self.time_min = int(now.strftime("%M"))
        self.time_sec = int(now.strftime("%S"))
        self.time_datetime_num_Str = (now.strftime("%d%m%Y_%H%M%S"))


def RivWriteJasonAsfile(JObj_name, Jfname):
    # print('In RivWriteJasonAsfile')
    jobj = JObj_name
    # print('Converting Jbonj')
    # convert to JSON string
    jsonStr = json.dumps(jobj.__dict__)

    with open(Jfname, 'r+') as ST1_Jason_Write:
        ST1_Jason_Write.write(str(jsonStr))


def RivReadJasonAsObject(Jfname):
    print('In RivReadJasonAsObject')
    with open(Jfname, 'r') as ST1_Jason_Read:
        JfileContent = (ST1_Jason_Read.read())
        if JfileContent != '':
            print(ST1_Jason_Read.name)
            # Raw_data = str(json.load(JfileContent))
            # Raw_data = str(json.load(ST1_Jason_Read))
            # data = Raw_data.replace("'", '"')
            data = JfileContent
            Jobject = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
            print(Jobject.Strategy)  # Strategy
            return Jobject
        else:
            print('Jason file is empty')
            return ''


def RivReadDateFromRaw(Jfname):
    print('In RivReadJasonAsObject')
    with open(Jfname, 'r') as ST1_Jason_Read:
        JfileContent = (ST1_Jason_Read.read())
        if JfileContent != '':
            print(ST1_Jason_Read.name)
            # Raw_data = str(json.load(JfileContent))
            # Raw_data = str(json.load(ST1_Jason_Read))
            # data = Raw_data.replace("'", '"')
            data = JfileContent
            Jobject = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
            print(Jobject.Strategy)  # Strategy
            return Jobject
        else:
            print('Jason file is empty')
            return ''


def RivQuote(Symbol):
    # data1 = {"symbols": "NSE:NIFTYBANK-INDEX"}
    data = {"symbols": Symbol}
    RivQuoteRaw = str(fyers.quotes(data))
    RivQuote = RivQuoteRaw.replace("'", '"')
    RivQuoteJason = json.loads(RivQuote)
    return RivQuoteJason


def RivLtp(Symbol):
    data = {"symbols": Symbol}
    RivQuoteRaw = str(fyers.quotes(data))
    RivQuote = RivQuoteRaw.replace("'", '"')
    RivQuoteJason = json.loads(RivQuote)
    # LTP from Quote
    RivLtp = RivQuoteJason["d"][0]["v"]["lp"]
    print(RivLtp)
    return RivLtp


def RivAsk(Symbol):
    data = {"symbols": Symbol}
    RivQuoteRaw = str(fyers.quotes(data))
    RivQuote = RivQuoteRaw.replace("'", '"')
    RivQuoteJason = json.loads(RivQuote)
    # Ask from Quote
    RivAsk = RivQuoteJason["d"][0]["v"]["ask"]
    print(RivAsk)
    return RivAsk


def RivBid(Symbol):
    data = {"symbols": Symbol}
    RivQuoteRaw = str(fyers.quotes(data))
    RivQuote = RivQuoteRaw.replace("'", '"')
    RivQuoteJason = json.loads(RivQuote)
    # Bid from Quote
    RivBid = RivQuoteJason["d"][0]["v"]["bid"]
    print(RivBid)
    return RivBid


# Main function  for  Running
def RivSellStraddleBN_Main(ST1):
    print('In RivSellStraddleBN_Main')


def RivSellStraddleBN(ST1, RivTime, qty, SL_Points):
    try:
        print('Entering in BN Strategy Straddle sell')
        # Call Straddle at specified Time
        ####################################################################
        ST1.date_num = RivTime.date_num
        Input_Symbol = 'NSE:NIFTYBANK-INDEX'
        ltp = RivLtp(Input_Symbol)
        # NSE:BANKNIFTY2231716550CE
        RivLtp_Round = int(round(ltp / 100, 0) * 100)
        print(RivLtp_Round)
        RivSymbolPref = 'NSE:BANKNIFTY'
        # RivWeekStr = '22324'
        # RivWeekStr = '22MAR'
        # RivWeekKey = '22APR'
        RivWeekStr = RivWeekKey
        # NSE:BANKNIFTY2241334500CE

        # if RivTime.day=='Thursday':
        StraddleCE = RivSymbolPref + RivWeekStr + str(RivLtp_Round - 100) + 'CE'
        StraddlePE = RivSymbolPref + RivWeekStr + str(RivLtp_Round + 100) + 'PE'
        # else:
        # StraddleCE = RivSymbolPref + RivWeekStr + str(RivLtp_Round) + 'CE'
        # StraddlePE = RivSymbolPref + RivWeekStr + str(RivLtp_Round) + 'PE'
        # Get Symbol
        print(StraddleCE)
        print(StraddlePE)
        ST1.CE_Symbol = StraddleCE
        ST1.PE_Symbol = StraddlePE
        # Get Prices
        ST1.CE_Price = (RivLtp(StraddleCE))
        ST1.PE_Price = (RivLtp(StraddlePE))

        # Updated the Entry Prices
        ST1.CE_Entry_Price = ST1.CE_Price
        ST1.PE_Entry_Price = ST1.PE_Price

        ST1.Entered = 'Yes'
        ST1.Entry_Time = RivTime.time_num

        # Capture  stop-loss Information
        # 20% SL System
        # ST1.CE_SL = round(float(ST1.CE_Entry_Price) * 1.2, 1)
        # ST1.PE_SL = round(float(ST1.PE_Entry_Price) * 1.2, 1)
        # 100 RS Max SL System
        ST1.CE_SL = round(float(ST1.CE_Entry_Price) + float(SL_Points) - 1, 1)
        ST1.PE_SL = round(float(ST1.PE_Entry_Price) + float(SL_Points) - 1, 1)

        # Order Placement
        ST1.CE_Oder_ID = PlaceOrder(ST1.CE_Symbol, qty, -1, 2)
        ST1.PE_Oder_ID = PlaceOrder(ST1.PE_Symbol, qty, -1, 2)
        ST1.CE_Oder_ID_Status = Order_Status(ST1.CE_Oder_ID)
        ST1.PE_Oder_ID_Status = Order_Status(ST1.PE_Oder_ID)

        # Placing SL Orders
        ST1.CE_SL_Oder_ID = PlaceOrder(ST1.CE_Symbol, qty, 1, 4, ST1.CE_SL)
        ST1.PE_SL_Oder_ID = PlaceOrder(ST1.PE_Symbol, qty, 1, 4, ST1.PE_SL)
        ST1.CE_SL_Oder_ID_Status = Order_Status(ST1.CE_SL_Oder_ID)
        ST1.PE_SL_Oder_ID_Status = Order_Status(ST1.PE_SL_Oder_ID)

        print('Initial SL for CE ' + str(ST1.CE_SL))
        print('Initial SL for PE ' + str(ST1.PE_SL))

        # Number of leg In
        ST1.Number_Of_Leg_In = 2

        print('Sell BN Straddle Entry Complete')

    except:
        print("An exception occurred while Running RivSellStraddleBN ")
    ####################################################################


def RivSellStraddleBN_Validate(ST1, RivTime, qty):
    # print(RivLtp(ST1.CE_Symbol))
    # print(RivLtp(ST1.PE_Symbol))
    ST1.CE_SL_Oder_ID_Status = Order_Status(ST1.CE_SL_Oder_ID)
    ST1.PE_SL_Oder_ID_Status = Order_Status(ST1.PE_SL_Oder_ID)

    if int(ST1.CE_SL_Oder_ID_Status) == 2 and (ST1.Number_Of_Leg_In == 2):
        print('Stop-loss hit on CE Side - Exit CE Leg')
        ST1.CE_Exit_Price = ST1.CE_SL
        ST1.CE_Exit_Time = RivTime.time_num
        # Revise PE Leg SL to cst to cost
        print('Revising PE Side SL')
        ST1.PE_SL = ST1.PE_Price + 15
        ModifyOrder(ST1.PE_SL_Oder_ID, ST1.PE_SL, qty, 'SL', 1)
        ST1.Number_Of_Leg_In = 1

    elif int(ST1.PE_SL_Oder_ID_Status) == 2 and (ST1.Number_Of_Leg_In == 2):
        print('Stop-loss hit on PE Side - Exit PE Leg')
        ST1.PE_Exit_Price = ST1.PE_SL
        ST1.PE_Exit_Time = RivTime.time_num
        print('Revising CE Side SL')
        ST1.CE_SL = ST1.CE_Price + 15
        ModifyOrder(ST1.CE_SL_Oder_ID, ST1.CE_SL, qty, 'SL', 1)
        ST1.Number_Of_Leg_In = 1

    elif int(ST1.CE_SL_Oder_ID_Status) == 2 and (ST1.Number_Of_Leg_In == 1) and (ST1.CE_Exit_Time == ''):
        print('Stop-loss hit on CE Side, PE leg was Already Closed # Exit CE Leg')
        ST1.CE_Exit_Price = ST1.CE_SL
        ST1.CE_Exit_Time = RivTime.time_num
        # Set All Leg Closed
        ST1.Number_Of_Leg_In = 0
        # Set Strategy Closed
        print('Marking Strategy as Closed')
        ST1.Exited = 'Yes'

    elif int(ST1.PE_SL_Oder_ID_Status) == 2 and (ST1.Number_Of_Leg_In == 1) and (ST1.PE_Exit_Time == ''):
        print('Stop-loss hit on PE Side, CE leg was Already Closed # Exit PE Leg')
        ST1.PE_Exit_Price = ST1.PE_SL
        ST1.PE_Exit_Time = RivTime.time_num
        # Set All Leg Closed
        ST1.Number_Of_Leg_In = 0
        # Set Strategy Closed
        print('Marking Strategy as Closed')
        ST1.Exited = 'Yes'


###################################################################
def RivSellStraddleBN_ExitAll(ST1, RivTime):
    print('In Exit all')
    ce_ltp = RivLtp(ST1.CE_Symbol)
    pe_ltp = RivLtp(ST1.PE_Symbol)

    if (ST1.CE_Exit_Price == '' or ST1.PE_Exit_Price == ''):
        # Exit CE Leg
        if ST1.CE_Exit_Price == '':
            ST1.CE_Exit_Price = ce_ltp
            ExitPosition(ST1.CE_Oder_ID)
            CancelOrder(ST1.CE_SL_Oder_ID)
            ST1.CE_Exit_Time = RivTime.time_num
        # Exit CE Leg
        if ST1.PE_Exit_Price == '':
            ST1.PE_Exit_Price = pe_ltp
            ExitPosition(ST1.PE_Oder_ID)
            CancelOrder(ST1.PE_SL_Oder_ID)
            ST1.PE_Exit_Time = RivTime.time_num
    else:
        print('Position was already Closed before 3:10')

    ST1.Number_Of_Leg_In = 0
    ST1.Exited = 'Yes'


###################################################################
def Fun_Run_Analysis_1min_maruti():
    try:
        os.system("wscript C:\PROGRA~2\ATS\ATS_INT_1MIN_MARUTI_V10\JavaScr\Trig_Run_Ami_Scan.js")
    except:
        print("An exception occurred while Running java Script ")


###################################################################
def RivRead_Maruti_ORB():  # Returns 'Open Long'
    openPosition = ''
    with open("C:/Program Files (x86)/ATS/ATS_INT_1MIN_MARUTI_V10/ORB_Input.csv") as file_name:
        file_read = csv.reader(file_name)
        array = list(file_read)
        my_array = np.asarray(array)

        try:
            for x in my_array:
                fullstring = x[1]
                substring = "Open"

                if fullstring != None and substring in fullstring:
                    # print("Found!")
                    # print(fullstring)
                    openPosition = fullstring
                    break
        except Exception:
            print('Error in reading ami Results')

    return openPosition


###################################################################
def RivSingleLegOrder(Signal, ST2):
    symbol = "NSE:MARUTI-EQ"
    QTY = 2
    # "type": 1   2 => Market Order
    # side
    # 1 = > Buy
    # -1 = > Sell
    if Signal == 'Open Long':
        print('Open Long')
        ST2.Entered = 'Yes'
        ST2.InSignalType = 'Open Long'
        ST2.NTrade = int(ST2.NTrade) + 1
        Response = PlaceOrder(symbol, QTY, 1)
        print(Response)
    elif Signal == 'Open Short':
        print('Open Short')
        ST2.Entered = 'Yes'
        ST2.InSignalType = 'Open Short'
        ST2.NTrade = int(ST2.NTrade) + 1
        Response = PlaceOrder(symbol, QTY, -1)
        print(Response)
    elif Signal == '':
        ST2.Entered = ''
        if ST2.InSignalType == 'Open Short':
            print('Exiting Open Short')
            Response = PlaceOrder(symbol, QTY, 1)
            print(Response)
            ST2.InSignalType = ''
            print('Closed open Short')
        elif ST2.InSignalType == 'Open Long':
            print('Exiting Open Short')
            Response = PlaceOrder(symbol, QTY, -1)
            print(Response)
            ST2.InSignalType = ''
            print('Closed Open Long')


###################################################################
def PlaceOrder(symbol, qty, side, Order_type, stopPrice=0):
    # 1 = > Limit     Order
    # 2 = > Market    Order
    # 3 = > Stop    Order(SL - M)
    # 4 = > Stoplimit    Order(SL - L)
    # -1    = Buy side Position , SL Should be Lower than buy Price
    # 1     = Sell side Position , SL Should be Lower than Sell Price
    # productType='INTRADAY'
    # productType='CO'
    limitPrice = 0
    if Order_type == 4:
        limitPrice = round(stopPrice, 1) + 1

    print('Running Place Order')
    Order_ID = ''
    try:
        data = {
            "symbol": symbol,
            "qty": qty,
            "type": Order_type,
            "side": side,
            "productType": "INTRADAY",
            "limitPrice": limitPrice,
            "stopPrice": round(stopPrice, 1),
            "validity": "DAY",
            "disclosedQty": 0,
            "offlineOrder": "False",
            "stopLoss": 0,
            "takeProfit": 0
        }
        # Response = fyers.place_order(data)
        Response = str(fyers.place_order(data))
        Response_Formatted = Response.replace("'", '"')
        Response_Jason = json.loads(Response_Formatted)
        Response_Status = str(Response_Jason["s"])
        Order_msg = Response_Jason["message"]
        print(Order_msg)
        if Response_Status == 'ok':
            Order_ID = Response_Jason["id"]

    except:
        print("Oops!", sys.exc_info()[0], "occurred while Placing Order")

    return Order_ID


###################################################################
def ModifyOrder(orderId, stopPrice, qty, order_type_to_Modify, side):
    # order_type='Normal'
    # order_type='SL'
    # side = 1 for buy
    # side =-1 for Sell

    print('Running Modify Order')
    Response_Status = ''
    limitPrice = 0
    if order_type_to_Modify == 'SL' and side == 1:
        limitPrice = round(stopPrice, 1) + 1
    elif order_type_to_Modify == 'SL' and side == -1:
        limitPrice = round(stopPrice, 1) - 1

    try:
        data = {
            "id": orderId,
            "type": 1,
            "limitPrice": limitPrice,
            "stopPrice": stopPrice,
            "qty": qty
        }
        Response = str(fyers.modify_order(data))
        Response_Formatted = Response.replace("'", '"')
        Response_Jason = json.loads(Response_Formatted)
        Response_Status = str(Response_Jason["s"])
        Order_msg = Response_Jason["message"]
        print(Order_msg)

    except:
        print("Oops!", sys.exc_info()[0], "occurred while Modifying Order")

    return Response_Status


###################################################################
def ExitPosition(orderId):
    print('Running Exit Position')
    Response_Status = ''
    try:
        data = [{
            "id": orderId,
        }]
        # Response = fyers.place_order(data)
        Response = str(fyers.exit_positions(data))
        Response_Formatted = Response.replace("'", '"')
        Response_Jason = json.loads(Response_Formatted)
        Response_Status = str(Response_Jason["s"])
        Order_msg = Response_Jason["message"]
        print(Order_msg)

    except:
        print("Oops!", sys.exc_info()[0], "occurred while Exiting Order")

    return Response_Status


###################################################################
def CancelOrder(orderId):
    print('Running Exit Position')
    Response_Status = ''
    try:
        data = {"id": orderId}
        # Response = fyers.place_order(data)
        Response = str(fyers.cancel_order(data))
        Response_Formatted = Response.replace("'", '"')
        Response_Jason = json.loads(Response_Formatted)
        Response_Status = str(Response_Jason["s"])
        Order_msg = Response_Jason["message"]
        print(Order_msg)

    except:
        print("Oops!", sys.exc_info()[0], "occurred while Canceling Order")

    return Response_Status


###################################################################
def Order_Status(orderId):
    # 1 = > Canceled
    # 2 = > Traded / Filled
    # 3 = > (Not used currently)
    # 4 = > Transit
    # 5 = > Rejected
    # 6 = > Pending
    # 7 = > Expired
    print('Running get order status')
    O_Status = ''
    Response_Status = ''
    try:
        data = {"id": orderId}
        orderbook_raw = str(fyers.orderbook(data=data))  ## This will provide all the trade related information

        orderbook_Formatted_Binary = orderbook_raw.replace("False", '0')
        orderbook_Formatted = orderbook_Formatted_Binary.replace("'", '"')
        tradebook_json = json.loads(orderbook_Formatted)
        Response_Status = str(tradebook_json["s"])
        if Response_Status != 'error':
            O_Status = str(tradebook_json["orderBook"][0]["status"])
    except:
        print("Oops!", sys.exc_info()[0], "occurred while retrieving Order Status")
    return O_Status


###################################################################

def ST3_Place_Order(ST3, ST3_Jfname):
    lable = ''
    # lable.begin

    Order_STKSymbol_PE_Price = ''
    Order_STKSymbol_CE_Price = ''

    Dic_PE, Dic_CE = ST3_Get_Latest_Price_In_DIC()

    if ST3.Order_Type == 'Open Long':
        # Select PE
        for Select_PE in Dic_PE:
            print('Select PE')
            if (Select_PE.Value < 74.5) and (Select_PE.Value > 62.5):
                Order_STKSymbol_PE = Select_PE.Key
                Order_STKSymbol_PE_Price = Select_PE.Value
                break

        for Select_CE in Dic_CE:
            print('Select CE')
            if (Select_CE.Value < 38.5) and (Select_CE.Value > 32):
                Order_STKSymbol_CE = Select_CE.Key
                Order_STKSymbol_CE_Price = Select_CE.Value
                break

        Big_Leg_SL = round(Order_STKSymbol_PE_Price * 1.7, 2) - Order_STKSymbol_PE_Price
        Big_Leg_TGT = Order_STKSymbol_PE_Price - round(
            ((Order_STKSymbol_PE_Price + Order_STKSymbol_CE_Price) * 0.88) / 2, 2) - 1
        Sml_Leg_SL = math.Round(((Order_STKSymbol_PE_Price + Order_STKSymbol_CE_Price) * 0.88) / 2,
                                2) - Order_STKSymbol_CE_Price + 1
        Sml_Leg_TGT = Order_STKSymbol_CE_Price - round(Order_STKSymbol_CE_Price * 0.15, 2)
        if Order_STKSymbol_CE_Price == 0.0 or Order_STKSymbol_PE_Price == 0.0:
            print('ST3-Matching Price range not found-Iterating again')
            time.sleep(15)
            ST3_Place_Order(ST3, ST3_Jfname)
        Big_Leg_Sml_Leg_ratio = Order_STKSymbol_PE_Price / Order_STKSymbol_CE_Price
        if Big_Leg_Sml_Leg_ratio < 1.8:
            print('Price Ratio below 1.8=' + Big_Leg_Sml_Leg_ratio)
            time.sleep(15)
            ST3_Place_Order(ST3, ST3_Jfname)

        ST3.Big_Leg_Main = PlaceBOOrder_KT_OPT(Order_STKSymbol_PE, Order_STKSymbol_PE_Price, Big_Leg_SL,
                                               Big_Leg_TGT)
        ST3.Big_Leg_Symbol = Order_STKSymbol_PE
        ST3.Big_Leg_Entry_Price = Order_STKSymbol_PE_Price
        ST3.Big_Leg_SL_Price = Order_STKSymbol_PE_Price + Big_Leg_SL

        ST3.Sml_Leg_Main = PlaceBOOrder_KT_OPT(Order_STKSymbol_CE, Order_STKSymbol_CE_Price, Sml_Leg_SL,
                                               Sml_Leg_TGT)
        ST3.SML_Leg_Symbol = Order_STKSymbol_CE
        ST3.Sml_Leg_Entry_Price = Order_STKSymbol_CE_Price
        ST3.Sml_Leg_SL_Price = Order_STKSymbol_CE_Price + Sml_Leg_SL

        ST3.ExDate = RivTime.date_num

    elif ST3.Order_Type == 'Open Short':
        # Select CE
        for Select_CE in Dic_CE:
            print('Select CE')
            if (Select_CE.Value < 74.5) and (Select_CE.Value > 62.5):
                Order_STKSymbol_CE = Select_CE.Key
                Order_STKSymbol_CE_Price = Select_CE.Value
                break

        for Select_PE in Dic_PE:
            print('Select PE')
            if (Select_PE.Value < 38.5) and (Select_PE.Value > 32):
                Order_STKSymbol_PE = Select_PE.Key
                Order_STKSymbol_PE_Price = Select_PE.Value
                break

        Big_Leg_SL = round(Order_STKSymbol_CE_Price * 1.7, 2) - Order_STKSymbol_CE_Price
        Big_Leg_TGT = Order_STKSymbol_CE_Price - round(
            ((Order_STKSymbol_CE_Price + Order_STKSymbol_PE_Price) * 0.88) / 2, 2) - 1
        Sml_Leg_SL = round(((Order_STKSymbol_CE_Price + Order_STKSymbol_PE_Price) * 0.88) / 2,
                           2) - Order_STKSymbol_PE_Price + 1
        Sml_Leg_TGT = Order_STKSymbol_PE_Price - round(Order_STKSymbol_PE_Price * 0.15, 2)
        if Order_STKSymbol_PE_Price == 0.0 or Order_STKSymbol_CE_Price == 0.0:
            print('ST3-Matching Price range not found-Iterating again')
            time.sleep(15)
            ST3_Place_Order(ST3, ST3_Jfname)
        Big_Leg_Sml_Leg_ratio = Order_STKSymbol_CE_Price / Order_STKSymbol_PE_Price
        if Big_Leg_Sml_Leg_ratio < 1.8:
            print('Price Ratio below 1.8=' + Big_Leg_Sml_Leg_ratio)
            time.sleep(15)
            ST3_Place_Order(ST3, ST3_Jfname)

        ST3.Big_Leg_Main = PlaceBOOrder_KT_OPT(Order_STKSymbol_CE, Order_STKSymbol_CE_Price, Big_Leg_SL,
                                               Big_Leg_TGT)
        ST3.Big_Leg_Symbol = Order_STKSymbol_CE
        ST3.Big_Leg_Entry_Price = Order_STKSymbol_CE_Price
        ST3.Big_Leg_SL_Price = Order_STKSymbol_CE_Price + Big_Leg_SL

        ST3.Sml_Leg_Main = PlaceBOOrder_KT_OPT(Order_STKSymbol_PE, Order_STKSymbol_PE_Price, Sml_Leg_SL,
                                               Sml_Leg_TGT)
        ST3.SML_Leg_Symbol = Order_STKSymbol_PE
        ST3.Sml_Leg_Entry_Price = Order_STKSymbol_PE_Price
        ST3.Sml_Leg_SL_Price = Order_STKSymbol_PE_Price + Sml_Leg_SL

        ST3.ExDate = RivTime.date_num

    RivWriteJasonAsfile(ST3, ST3_Jfname)


def ST3_Get_Latest_Price_In_DIC():
    print('IN-Get_Latest_Price_In_DIC')
    Input_Symbol = 'NSE:NIFTYBANK-INDEX'
    OPT_Symbol = 'NSE:BANKNIFTY'
    ltp = RivLtp(Input_Symbol)
    RivLtp_Round = int(round(ltp / 100, 0) * 100)
    STRIKE_Price_PE = RivLtp_Round
    STRIKE_Price_CE = RivLtp_Round
    Dic_PE = {'Symbom': 0}
    Dic_CE = {'Symbom': 0}
    try:
        for CNT in range(1, 80, 2):
            STRIKE_Price_PE -= 100
            STRIKE_Price_CE += 100
            STRIKE_Price_PE_Code = "NFO:" & OPT_Symbol & STRIKE_Price_PE & "PE"
            STRIKE_Price_CE_Code = "NFO:" & OPT_Symbol & STRIKE_Price_CE & "CE"

            STRIKE_Price_PE_Code_Price = RivLtp(STRIKE_Price_PE_Code)
            STRIKE_Price_CE_Code_Price = RivLtp(STRIKE_Price_CE_Code)

            # add item
            Dic_PE[STRIKE_Price_PE_Code] = STRIKE_Price_PE_Code_Price
            Dic_CE[STRIKE_Price_CE_Code] = STRIKE_Price_CE_Code_Price

    except:
        print("Oops!", sys.exc_info()[0], "occurred while trying strategy 1.")

    print(RivTime.date_num + 'OUT-Get_Latest_Price_In_DIC')
    return Dic_PE, Dic_CE


def PlaceBOOrder_KT_OPT(Order_STKSymbol_PE, Order_STKSymbol_PE_Price, Sml_Leg_SL,
                        Sml_Leg_TGT):
    print('True')

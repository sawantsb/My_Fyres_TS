# from main import *
import sys
from RivFun import *
import time
import shutil


#############################################################################################################
def strategy1_1(RivTime):
    print('strategy-1 Started ')
    qty = RivST1_Qty
    print('ST1 Quantitiy set to ' + str(qty))
    SL_Points = 76
    FirstPass = True
    while True:
        # print('strategy 1 Loop')
        RivTime.RivTimeNow()
        #
        Entry_Time_RivSellStraddleBN = 92800
        #Entry_Time_RivSellStraddleBN = 102400 #RBI Policy on 10 am
        Max_Entry_Time_RivSellStraddleBN = 150800
        Exit_Time_RivSellStraddleBN = 150800
        try:

            if FirstPass:
                # Define the jason file for this strategy
                ST1_Jfname = 'home/Statergy_Json/ST_SellStraddleBN.json'

                # Create ST1 object of class RivStraddleStrategyDetails
                ST1 = RivStraddleStrategyDetails()

                # Update object for this strategy from jason file
                if RivReadJasonAsObject(ST1_Jfname) != '':
                    print('Checking if the Input file is not for today and then File is being primed / updated')
                    ST1 = RivReadJasonAsObject(ST1_Jfname)
                    today_datenum = int(datetime.now().strftime("%d%m%Y"))
                    if ST1.date_num != '':
                        file_datenum = int(ST1.date_num)

                    # If the file read is old then Clear Jason
                    if ST1.date_num != '':
                        if file_datenum != today_datenum and file_datenum != '':
                            del ST1
                            # copy the file as backup
                            original = r'home/Statergy_Json/ST_SellStraddleBN.json'
                            target = r'home/Statergy_Json/ST_SellStraddleBN_' + str(file_datenum) + '.json'
                            shutil.copyfile(original, target)

                            # Make the file Empty
                            open(ST1_Jfname, 'w').close()

                            # Then Write New Object
                            ST1 = RivStraddleStrategyDetails()
                            ST1.date_num = today_datenum
                            RivWriteJasonAsfile(ST1, ST1_Jfname)
                    else:
                        del ST1
                        # Make the file Empty
                        open(ST1_Jfname, 'w').close()

                        # Then Write New Object
                        ST1 = RivStraddleStrategyDetails()
                        ST1.date_num = today_datenum
                        RivWriteJasonAsfile(ST1, ST1_Jfname)

                else:
                    # Write the JObject to jason file for this strategy
                    print('Strategy file was empty and its primed from ST1 Object waiting for Start time')
                    # ST1.date_num = today_datenum
                    RivWriteJasonAsfile(ST1, ST1_Jfname)
                FirstPass = False

            # Checker after every 5 if the strategy is exited and stop the thread if so
            if ST1.Exited != '':
                print('strategy-1 Running -', RivTime.time_num)
                print('Checker after every 5 if the strategy 1 is exited and stop the thread if so ')
                sys.exit()
                # thread.exit()
                break

            # Checker after every 5 min
            if (int(RivTime.time_num) > Entry_Time_RivSellStraddleBN) and ST1.Entered == '' and (
                    int(RivTime.time_num) < Max_Entry_Time_RivSellStraddleBN):
                print('strategy-1 Entry Running -', RivTime.time_num)
                # Wait for 5 seconds
                time.sleep(1)
                print("time_num =", RivTime.time_num)
                RivSellStraddleBN(ST1, RivTime, qty, SL_Points)
                # Write the Jason to CSV
                RivWriteJasonAsfile(ST1, ST1_Jfname)

            # Checker after every 5 min after Entry
            if (int(RivTime.time_min) % 1 == 0) and (
                    int(RivTime.time_sec) == 5) and ST1.Entered == 'Yes' and ST1.Exited == '':
                # Wait for 5 seconds
                time.sleep(5)
                print('strategy-1 Validation Running -', RivTime.time_num)
                # Check if the SL is hit on CE
                RivSellStraddleBN_Validate(ST1, RivTime, qty)
                # Write the Jason to CSV
                RivWriteJasonAsfile(ST1, ST1_Jfname)
                if ST1.Exited == 'Yes':
                    break

            # the below condition will tell the loop to stop time_num == 151045:
            if (int(RivTime.time_num) > Exit_Time_RivSellStraddleBN) == True and ST1.Exited == '':
                print('strategy-1 Exiting on time stop -', RivTime.time_num)
                RivSellStraddleBN_ExitAll(ST1, RivTime)
                # Write the Jason to CSV
                RivWriteJasonAsfile(ST1, ST1_Jfname)
                break
            # time.sleep(10)
        except:
            print("Oops!", sys.exc_info()[0], "occurred while trying strategy 1.")


#############################################################################################################
def strategy2_1(RivTime):
    print('strategy-2 Started ')
    FirstPass = True
    while True:
        RivTime.RivTimeNow()
        Entry_Time_Strategy2 = 93500
        Max_Entry_Time_Strategy2 = 151500
        Exit_Time_Strategy2 = 151400
        # Checker after every 5 min after Entry
        if (int(RivTime.time_min) % 1 == 0) and (int(RivTime.time_sec) == 0) and (
                int(RivTime.time_num) < Max_Entry_Time_Strategy2):
            print('strategy-2 Running -', RivTime.time_num)
            try:
                # Wait for 5 seconds
                time.sleep(6)
                if FirstPass:
                    ST2_Jfname = 'home/Statergy_Json/ST2_1MIN_Stock.json'  # Define the jason file for this strategy
                    # Create ST1 object of class RivStraddleStrategyDetails
                    ST2 = RivSingleStatDetails()
                    # Update object for this strategy from jason file
                    if RivReadJasonAsObject(ST2_Jfname) != '':
                        print('File is being primed / updated')
                        ST2 = RivReadJasonAsObject(ST2_Jfname)
                        today_datenum = int(datetime.now().strftime("%d%m%Y"))

                        if ST2.date_num != '':
                            file_datenum = int(ST2.date_num)
                            # If the file read is old then Clear Jason
                            if file_datenum != today_datenum and file_datenum != '':
                                del ST2
                                # copy the file as backup
                                original = r'home/Statergy_Json/ST2_1MIN_Stock.json'
                                target = r'home/Statergy_Json/ST2_1MIN_Stock_' + str(file_datenum) + '.json'
                                shutil.copyfile(original, target)
                                # Make the file Empty
                                open(ST2_Jfname, 'w').close()
                                # Then Write New Object
                                ST2 = RivSingleStatDetails()
                                ST2.date_num = today_datenum
                                RivWriteJasonAsfile(ST2, ST2_Jfname)
                        else:
                            del ST2
                            # Make the file Empty
                            open(ST2_Jfname, 'w').close()
                            # Then Write New Object
                            ST2 = RivSingleStatDetails()
                            ST2.date_num = today_datenum
                            RivWriteJasonAsfile(ST2, ST2_Jfname)

                    else:
                        # Write the JObject to jason file for this strategy
                        print('Strategy-2 file was empty and its primed from ST2 Object')
                        ST2 = RivSingleStatDetails()
                        # ST2.date_num = today_datenum
                        RivWriteJasonAsfile(ST2, ST2_Jfname)
                    FirstPass = False

                # print('Running Ami to scan')
                Fun_Run_Analysis_1min_maruti()
                Signal = RivRead_Maruti_ORB()
                if Signal == 'Open Long' and ST2.Entered != 'Yes' and ST2.NTrade < 8:
                    print(RivTime.time_num)
                    ST2.date_num = RivTime.date_num
                    RivSingleLegOrder(Signal, ST2)
                    RivWriteJasonAsfile(ST2, ST2_Jfname)
                elif Signal == 'Open Short' and ST2.Entered != 'Yes' and ST2.NTrade < 10:
                    print(RivTime.time_num)
                    ST2.date_num = RivTime.date_num
                    RivSingleLegOrder(Signal, ST2)
                    RivWriteJasonAsfile(ST2, ST2_Jfname)
                elif Signal == '' and ST2.Entered == 'Yes':
                    print(RivTime.time_num)
                    RivSingleLegOrder(Signal, ST2)
                    RivWriteJasonAsfile(ST2, ST2_Jfname)
                # Exit if Entry Exit Signal Come at the Same Point
                elif Signal != ST2.InSignalType and ST2.Entered == 'Yes':
                    print(RivTime.time_num)
                    # Compensate order counter for Multi order
                    ST2.NTrade = int(ST2.NTrade) - 1
                    # First Exit the Old Position
                    RivSingleLegOrder(Signal, ST2)
                    RivWriteJasonAsfile(ST2, ST2_Jfname)
                    # Second Enter the New Position
                    RivSingleLegOrder(Signal, ST2)
                    RivWriteJasonAsfile(ST2, ST2_Jfname)

                # the below condition will tell the loop to stop time_num == 151045:
                if (int(RivTime.time_num) > Exit_Time_Strategy2) == True and ST2.InSignalType != '':
                    print('strategy 2 Loop Exiting on time stop')
                    RivSingleLegOrder(Signal, ST2)
                    RivWriteJasonAsfile(ST2, ST2_Jfname)
                    break
                    # time.sleep(10)
            except:
                print("Oops!", sys.exc_info()[0], "occurred while trying strategy 2.")


#############################################################################################################
def strategy3_1(RivTime):
    print('strategy-3 Started ')
    FirstPass = True
    while True:
        RivTime.RivTimeNow()
        Entry_Time_ST3 = 94400
        Max_Entry_Time_ST3 = 150900
        Exit_Time_ST3 = 150900
        try:
            # Activate Strategy
            if (int(RivTime.time_min) % 5 == 0) and (int(RivTime.time_sec) == 30) and (
                    int(RivTime.time_num) < Max_Entry_Time_ST3):
                print('strategy-3 Running -', RivTime.time_num)
                try:
                    # Wait for 5 seconds
                    time.sleep(10)
                    if FirstPass:
                        # Define the jason file for this strategy
                        ST3_Jfname = 'home/Statergy_Json/ST_SellDirectionalStrangle.json'

                        # Create ST3 object of class RivStraddleStrategyDetails
                        ST3 = RivDirectionalStrangle

                    # Update object for this strategy from jason file
                    if RivReadJasonAsObject(ST3_Jfname) != '':
                        print('File is being primed / updated')
                        ST3 = RivReadJasonAsObject(ST3_Jfname)
                        today_datenum = int(datetime.now().strftime("%d%m%Y"))
                        file_datenum = int(ST3.date_num)
                        # If the file read is old then Clear Jason
                        if file_datenum != today_datenum and file_datenum != '':
                            ST3 = RivStraddleStrategyDetails()
                            RivWriteJasonAsfile(ST3, ST3_Jfname)
                    else:
                        # Write the JObject to jason file for this strategy
                        print('File is being primed from empty')
                        RivWriteJasonAsfile(ST3, ST3_Jfname)
                    FirstPass = False

                    # 1   # Run Analysis after every 5 min
                    ST3.ST3_Check_Ami()

                    # '======================================================================================
                    # 2 Enter in the Trade if the signal is generated in the Ami
                    # '======================================================================================

                    if ST3.In_Ami == True and ST3.In_Trade == False:
                        print(RivTime.time_num + '-Signal is generated in Ami So Initiating Create Strangle')

                        if ST3.Order_Type == 'Open Long' or ST3.Order_Type == 'Open Buy' or ST3.Order_Type == 'Open Short':
                            print("ST3-New Position Open")
                            ST3_Place_Order()
                            print(RivTime.time_num + '-Sleeping app for 120 Sec after placing order')
                            time.sleep(10)
                            print(RivTime.time_num + '-Completed Create Strangle')
                    # 3 Keep Validating if the order is in
                    elif ST3.In_Ami == True and ST3.In_Trade == True and ST3.Out_Trade == False:
                        if ST3.Order_Type == 'Long' or ST3.Order_Type == 'Long (trail)' or ST3.Order_Type == 'Buy' or ST3.Order_Type == 'Short' or ST3.Order_Type == 'Buy (trail)' or ST3.Order_Type == 'Short (trail)':
                            print(RivTime.time_num + '-Signal is Closed in Ami So closing Strangle')
                            # Fun_Close_In_KT()

                            print(RivTime.time_num + '-Completed-Signal Closed in Ami So Initiating Close Strangle')
                            RivWriteJasonAsfile(ST3, ST3_Jfname)
                except:
                    print("Oops!", sys.exc_info()[0], "occurred while trying strategy 2.")
            # '======================================================================================
            # 3 Keep Validating every min if both the legs are present each Min
            # '======================================================================================
            # 'Run Check for Strangle is IN after every 60 Sec
            if ST3.In_Trade == True and ST3.Out_Trade == False and (int(RivTime.time_sec) % 45 == 0):
                ST3.ST3_Get_All_Order_Staus()
                print('Checking if any leg is closed or if SL/TGT hit')
                if ST3.ST3_Strangle_Status() == False:
                    ST3.ST3_Close_All_Order
            # ST3.ST_Get_All_Order_Staus #This is to update latest status of SL and TGT order
                    ST3.ST3_Get_All_Order_Staus()
            # 'Exiting Timeout based
            if (int(RivTime.time_num) > Exit_Time_ST3) == True and ST3.Out_Trade == '':
                print('strategy-3 Exiting on time stop -', RivTime.time_num)
                ST3.ST3_Close_All_Order
                ST3.ST3_Get_All_Order_Staus()
                # Write the Jason to CSV
                RivWriteJasonAsfile(ST3, ST3_Jfname)
                break
            ####################################################################


        except:
            print("Oops!", sys.exc_info()[0], "occurred while trying strategy 2.")

#############################################################################################################

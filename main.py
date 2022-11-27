from RivStrategy import *
from RivFun import *
import sys
import threading
import time

# from RivStrategy import strategy1

# XS41508 Test_Commit
# ====================================================================================================
# 1.1-Log File Section
RivTime = RivTime()
RivTime.RivTimeNow()
#############################################################################################################
# 2.1-Log File Section
print('Login Process Completed')


#############################################################################################################
# 3.1-Strategy Section
#############################################################################################################
def strategy1():
    print('strategy-1 Started -', RivTime.time_num)
    strategy1_1(RivTime)

#############################################################################################################
def strategy2():
    print('strategy-2 Started -', RivTime.time_num)
    strategy2_1(RivTime)

##############################################################################################################
def strategy3():
    print('strategy-3 Started -', RivTime.time_num)
    strategy3_1(RivTime)


##############################################################################################################
# Multithreading

thread1 = threading.Thread(target=strategy1)
thread1.start()

thread2 = threading.Thread(target=strategy2)
#thread2.start()

thread3 = threading.Thread(target=strategy3)
#thread3.start()

#############################################################################################################
# 4.1-Completion Section Test Change worked Successfully11
print('Started all threads Successfully !!')

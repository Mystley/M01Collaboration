import multiprocessing
import os
import time

def presence(intro):
    now = time.time()
    o = time.ctime(now)
    atime = time.strftime("%I:%M:%S %p")

    print("I am process %s, %s and time is %s" %(os.getpid(), intro, atime))
    
if __name__ == "__main__":
    presence("the main program")
    for n in range(2):
        p = multiprocessing.Process(target=presence,
                                    args=("function %s" % n,))
        
        time.sleep(0.5)
        p.start()
        
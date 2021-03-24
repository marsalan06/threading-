import threading
import time

class myThread(threading.Thread): #subclass
    def __init__ (self,threadId,name,count,delay): #int_id,str_name, int_count_down_time
        threading.Thread.__init__(self) #super class used to avoid creating arguments 
        self.threadID=threadId
        self.name=name
        self.count=count
        self.delay=delay
    
    def run(self):
        print("Starting: "+ self.name) #\n new line
        print_time(self.name,self.delay,self.count) #fuction defined ahead, 1 is the delay of time or variable delay
        print("Exiting: "+self.name + "\n")


def print_time(name,delay,count):
    while count: #true till not 0
        print(name +" going to sleep") #executes first 
        time.sleep(delay) #delay specified when called func called, puts thread to sleep, and start other thread
        print(name+" after sleep") #indicates thread's waking up
        print("%s: %s %s" %(name,time.ctime(time.time()),count)+"\n") #ctime is current time 
        count -= 1 #reduce count


thread_1=myThread(1,"Thread1",10,0.5)
thread_2=myThread(2,"Thread2",5,1) #instance created 

thread_1.start() # function of threading module 
thread_2.start()
thread_1.join() # verifys that thread_1 is terminated or is waiting for event exeception
thread_2.join()

print("Done main thread") # the main thread in which these two threads are running and switching,
#the above code is executed when all threads within the main thread are executed 




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
        thread_lock.acquire() #any object of myThread class will ignore the sleep in bellow code and execute
                            # completly then exit 
        print_time(self.name,self.delay,self.count) #fuction defined ahead, 1 is the delay of time or variable delay
        thread_lock.release() #after completion of code now released lock 
        print("Exiting: "+self.name + "\n")

class myThread_2(threading.Thread): #subclass
    def __init__ (self,threadId,name,count,delay): #int_id,str_name, int_count_down_time
        threading.Thread.__init__(self) #super class used to avoid creating arguments 
        self.threadID=threadId
        self.name=name
        self.count=count
        self.delay=delay
    
    def run(self):
        print("Starting: "+ self.name) #\n new line
        thread_lock.acquire() # verify if any lock is acquired if not acquire it for mythread_2 threads
        thread_lock.release() #release any possible locks on mythread_2 threads
        print_time(self.name,self.delay,self.count) #fuction defined ahead, 1 is the delay of time or variable delay
        print("Exiting: "+self.name + "\n")

def print_time(name,delay,count):
    while count: #true till not 0
        print(name +" going to sleep") #executes first 
        time.sleep(delay) #delay specified when called func called, puts thread to sleep, and start other thread
        print(name+" after sleep") #indicates thread's waking up
        print("%s: %s %s" %(name,time.ctime(time.time()),count)+"\n") #ctime is current time 
        count -= 1 #reduce count


thread_lock=threading.Lock() #object for locking creating 
thread_1=myThread(1,"Payment thread",5,1) #takes 5 secs with delay of 1 
thread_2=myThread_2(2,"Email thread",10,1) #takes 10 secs with delay of 1  
thread_3=myThread_2(3,"Thankyou Page Thread",3,1) #takes 3 secs with delay of 1


thread_1.start() # function of threading module 
thread_2.start()
thread_3.start()
thread_1.join() # verifys that thread_1 is terminated or is waiting for event exeception
thread_2.join()
thread_3.join()

print("Done main thread") # the main thread in which these two threads are running and switching,
#the above code is executed when all threads within the main thread are executed 
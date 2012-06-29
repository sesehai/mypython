'''
Created on 2012-6-29

@author: luq
'''

import threading  
mylock = threading.RLock()  
num=0  
   
class ThreadDemo(threading.Thread):  
    def __init__(self, name):  
        threading.Thread.__init__(self)  
        self.t_name = name  
          
    def run(self):  
        global num  
        while True:  
            mylock.acquire()  
            print '\nThread(%s) locked, Number: %d'%(self.t_name, num)  
            if num>=4:  
                mylock.release()  
                print '\nThread(%s) released, Number: %d'%(self.t_name, num)  
                break  
            num+=1  
            print '\nThread(%s) released, Number: %d'%(self.t_name, num)  
            mylock.release()  
              
def test():  
    thread1 = ThreadDemo('A')  
    thread2 = ThreadDemo('B')  
    thread1.start()  
    thread2.start()  
   
if __name__== '__main__':  
    test()  
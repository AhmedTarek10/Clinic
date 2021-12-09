from pythonds.basic.queue import Queue
import random
class patient:
    def __init__(self,time):
        self.timestamp=time
        self.ages= random.randrange(21,61)
    def getage(self):
        return self.ages
    def gettimestamp(self):
        return self.timestamp
    def waitingtime(self,currenttime):
        return currenttime-self.timestamp
class  doctors:
    def __init__(self,ages):
        self.workrate = ages
        self.timeremaining=0
        self.currentpatient=None
    def nextone(self,newpatient):
        self.currentpatient=newpatient
        self.timeremaining=newpatient.getage() *60/self.workrate
    def busy(self):
        if self.currentpatient != None:
            return True
        else: return False
    def tick(self):
        if self.currentpatient != None:
            self.timeremaining = self.timeremaining - 1
            if self.timeremaining == 0:
                self.currentpatient = None
def semulation (numsec,workingrate):
    ourdoctor=doctors(workingrate)
    patientqueue=Queue()
    waitingtimes=[]
    for currentsec in range(numsec):
        if random.randrange(1, 361) == 20:
            patient1 = patient(currentsec)
            patientqueue.enqueue(patient1)
        if (not ourdoctor.busy() and not patientqueue.isEmpty()):
            nextpatient = patientqueue.dequeue()
            waitingtimes.append(nextpatient.waitingtime(currentsec))
            ourdoctor.nextone(nextpatient)
        ourdoctor.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait ", averageWait, " secs", patientqueue.size(), " tasks remaining.")

for i in range(10):
    semulation (14400,5)
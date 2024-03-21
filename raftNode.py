import logEntry
import time
import random
from logEntry import logEntry
NodeList = {1:'127.0.0.1:50051',2:'127.0.0.1:50052',3:'127.0.0.1:50053',4:'127.0.0.1:50054'}



class Node:
  isLeader = False
  nodeId = -1
  ipAddr = ""
  port = ""
  currentTerm = 0
  votedFor = None
  log : [logEntry]
  commitLength = 0
  currentRole = "Follower"
  currentLeader = None
  votesReceived = []
  sentLength = {}
  ackedLength = {}
  lastTerm = 0
  leaderId = -1
  startTime = 0
  lastIndex = 0
  timer = 0
  val=False
  data = {}
  
  def __init__(self,nodeId,ip,port):
    self.nodeId = nodeId
    self.ipAddr = ip
    self.port = port
    self.timer = random.uniform(5,11)
    self.log = []
    
  def onCrashRecovery(self):
    self.currentRole = "Follower"
    self.currentLeader = None
    self.votesReceived = []
    self.sentLength = []
    self.ackedLength = []
    
  def onElectionTimeout(self):
    self.currentTerm+=1
    self.currentRole = "Candidate"
    self.votedFor = self.nodeId
    self.votesReceived = [self.nodeId]

  def startTimer(self):
    self.startTime = time.time()
  
  def checkTimeout(self):
    while True:
      if self.cancel():
        return False
      if time.time() > self.startTime+self.timer:
        return True
  def cancel(self):
    return self.val
    #
    # if(len(self.log) > 0):
    #   self.lastTerm = self.log[len(self.log)-1].term

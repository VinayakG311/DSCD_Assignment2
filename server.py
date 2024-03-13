import concurrent
import random
import socket
import sys
import threading
from xxlimited import Null

import grpc
from concurrent import futures
import time
import raft_pb2, raft_pb2_grpc
import os
from raftNode import Node
port = sys.argv[1]
ip = socket.gethostbyname(socket.gethostname())
other_nodes = ['localhost:50051','localhost:50052']
leader = False

node:Node = Node(nodeId="-1",ip="-1",port="-1")


def timeout():
    time_rand = time.time() + random.uniform(1, 2)
    while True:
        if time.time() >= time_rand:
            return True




def StartElection():

    votes = 0
    for i in other_nodes:
        if i==node.ipAddr+node.port:
            continue
        with grpc.insecure_channel(i) as channel:
            stub = raft_pb2_grpc.RaftStub(channel)
            request = raft_pb2.RequestVotesArgs(term=1,candidateId=other_nodes.index(i),lastLogTerm=0,lastLogIndex=0)
            response = stub.RequestVote(request)
            if (response.voteGranted == True and node.currentRole=="Candidate" and node.currentTerm==response.term):
                node.votesReceived.append(response.NodeId)

    if (len(node.votesReceived) >= len(other_nodes) / 2):
        node.currentRole = "Leader"
        node.currentLeader = node.nodeId
        # TODO: Need to think how to get the ip address of followers: One way is to assume every node sent it. which is done below
        # for i in other_nodes:
        #     if i == Node.ipAddr + Node.port:
        #         continue
        #     with grpc.insecure_channel(i) as channel:
        #         stub = raft_pb2_grpc.RaftStub(channel)



def SuspectFail():
    pass

class RaftServicer(raft_pb2_grpc.RaftServicer):


    def AppendEntries(self, request, context):
        print(request.term)
        # return super().AppendEntries(request, context)

    def RequestVote(self, request, context):
        vote = True
        if(request.term > node.currentTerm):
            node.currentTerm = request.term
            node.currentRole="Follower"
            node.votedFor=None
        node.lastTerm=0
        if len(node.log)>0:
            node.lastTerm = node.log[len(node.log)-1].term
        ok = (request.lastLogTerm > node.lastTerm) or (request.lastLogTerm==node.lastTerm and request.lastLogIndex >= len(node.log))

        if request.term == node.currentTerm and ok and node.votedFor==None:
            node.votedFor = request.candidateId
            vote=True
        else:
            vote=False

        return raft_pb2.RequestVotesRes(term=1,voteGranted=vote,longestDurationRem=0)



    def ServeClient(self, request, context):
        print(request.request)
        # return super().ServeClient(request, context)


def serve():
    global node
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    raft_pb2_grpc.add_RaftServicer_to_server(RaftServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    n = int(input("Enter Node ID : "))

    try:
        if(os.path.isdir(f"logs_node_{n}")):
            #take data from log files
            path = os.getcwd() + f"/logs_node_{n}/"
            f = open(path + f"logs.txt", "a+")
            f1 = open(path + "metadata.txt", "a+")
            f2 = open(path + "dump.txt", "a+")
            #For now
            node = Node(nodeId=n, ip=ip, port=port)

        else:
            node = Node(nodeId=n, ip = ip, port=port)
            os.mkdir(f"logs_node_{n}", 0o777)
            path = os.getcwd() + f"/logs_node_{n}/"
            f = open(path + f"logs.txt", "a+")
            f1 = open(path + "metadata.txt", "a+")
            f2 = open(path + "dump.txt", "a+")

        if SuspectFail() or timeout():
            node.currentTerm+=1
            node.votedFor = node.nodeId
            node.votesReceived.append(node.nodeId)
            node.currentRole="Candidate"
            node.lastTerm=0
            if len(node.log)>0:
                node.lastTerm = node.log[len(node.log)-1].term
            StartElection()



    except FileExistsError:
        pass

    try:
        while True:
            time.sleep(3600)  # One hour
    except KeyboardInterrupt:
        server.stop(0)

t=[]
if __name__ == '__main__':

    th1 = threading.Thread(target=serve)
    th2 = threading.Thread(target=timeout)
    t.append(th1)
    t.append(th2)
    try:
        for i in t:
            i.start()
        for i in t:
            i.join()

    except:
        sys.exit(0)



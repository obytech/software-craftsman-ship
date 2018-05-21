import grpc

import sys

import pychat_pb2_grpc as pychat_pb2_grpc
from pychat_pb2 import LoginRequest, LoginStatus, StreamMessagesRequest


def run():
    if len(sys.argv) == 1 or sys.argv[1] is None:
        print("Usage: arg1=username")
        return


    username = sys.argv[1]
    print('username: ' + username)

    channel = grpc.insecure_channel('localhost:50051')
    stub = pychat_pb2_grpc.ChatAPIStub(channel)

    response = stub.login(LoginRequest(username=username))
    print("Greeter client received: " + str(LoginStatus.items()[response.status]))
    if response.status != 0:
        raise RuntimeError("Login failed")

    msgStreamIter = stub.streamMessages(StreamMessagesRequest(token=response.token))
    for msg in msgStreamIter:
        print(msg.destination + ": " + msg.content)


if __name__ == '__main__':
    run()

import time
import uuid
from concurrent import futures

import grpc

from pychat_pb2 import LoginResponse, LoginStatus
from pychat_pb2_grpc import ChatAPIServicer, add_ChatAPIServicer_to_server


class PyChatServer(ChatAPIServicer):
    users = []

    def login(self, request, context):
        if request.username in self.users:
            return LoginResponse(status=LoginStatus.Value('FAILED'))

        self.users.append(request.username)
        print(request.username + ' logged in')
        return LoginResponse(status=LoginStatus.Value('SUCCEED'), token=str(uuid.uuid4()))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ChatAPIServicer_to_server(PyChatServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("started")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

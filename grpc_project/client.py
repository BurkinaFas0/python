#!/home/alex/code/grpc/grpc_simple_project/venv/bin/python3

from concurrent import futures
import logging
import grpc
from protos import file_pb2 as pb2
from protos import file_pb2_grpc as pb2_grpc


class UnaryClient(object):
    def __init__(self):
        self.channel  = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.todoServiceStub(self.channel)

    def _createTodo(self):        
        _todo = pb2.createTodoRequest(name = "AAAAA", completed = False, day = 31  )   
        response = self.stub.createTodo(_todo)
        print("Ответ от сервера: " + response.message)


    def _getAllTodos(self):
        todos = self.stub.getAllTodos(pb2.StringMessage(message="SELECT * from todo;"))
        print(todos)
    

    def echo_request(self):
        response = self.stub.SayHello(pb2.StringMessage(message="you"))
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()   
    client = UnaryClient()
    #client.echo_request()
    #client._createTodo()
    client._getAllTodos()

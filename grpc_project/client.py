#!/home/alex/code/grpc/grpc_simple_project/venv/bin/python3

from concurrent import futures
import logging
import grpc
from protos import file_pb2 as pb2
from protos import file_pb2_grpc as pb2_grpc


MESSAGE = 'Hello'


class UnaryClient(object):
    def __init__(self):
        print("-----------Работает клиент------------")
        self.channel  = grpc.insecure_channel("localhost:50051")
        self.stub = pb2_grpc.todoServiceStub(self.channel)

    def _createTodo(self):        
        _todo = pb2.Todo(id = 0, name = "JJJJ", completed = False,  )
        _todo.id = 0
        _todo.name = "JJJJ"
        _todo.completed = False
        _todo.day = 21 
        print(f"Запрос от клиента {_todo}")
        _request = pb2.createTodoRequest(todo = _todo)     
        return self.stub.createTodo(_request)


    def _getAllTodos(self):
        #mes = pb2.GetallTodosRequest(message='SELECT * from todos;')
        #print(f'{mes}')
        # request = pb2.GetallTodosRequest()
        # request.message = MESSAGE
        self.stub.getAllTodos(pb2.GetallTodosRequest(message="SELECT * from todo;"))
        return self.stub.getAllTodos(pb2.GetallTodosRequest(message="SELECT * from todo;"))
    
    def echo_request(self):
        response = self.stub.SayHello(pb2.HelloRequest(name="you"))
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()   
    client = UnaryClient()
    result = client._getAllTodos()

    print("Ответ от сервера", f'{result}')
    print("-------клиент отработал-------")
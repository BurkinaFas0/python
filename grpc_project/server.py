#!/home/alex/code/grpc/grpc_simple_project/venv/bin/python3
from concurrent import futures
import sys
import grpc
import logging
from protos import file_pb2 as pb2
from protos import file_pb2_grpc as pb2_grpc
import psycopg2


try:
    conn = psycopg2.connect(dbname='grpc', user='py_user', password='inspirion', host='localhost')
except:
    print('Can`t establish connection to database')


cursor = conn.cursor()
conn.autocommit = True

class TodoService(pb2_grpc.todoServiceServicer):
    def createTodo(self, request, context):
        cursor.execute(f'INSERT INTO todo(name, completed, day) values(\'{request.name}\', \'{request.completed}\', \'{request.day}\');')
        return pb2.StringMessage(message="Объект создан!") 
    

    def getAllTodos(self, request, context):
        print("message", request.message)
        cursor.execute(request.message)
        todos = cursor.fetchall()
        todo_arr = []
        for x in todos:
            todo_arr.append(pb2.Todo(id = x[0], name=x[1], completed=x[2], day=x[3]))

        return pb2.todoResponse(todo = todo_arr)
    
    
    def SayHello(self, request, context):
        return pb2.StringMessage(message="Hello, %s!" % request.message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_todoServiceServicer_to_server(
        TodoService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()




def interrupt_connection(sender, **extra):
    print("Exiting the program...")
    cursor.close() 	
    conn.close() 
    sys.exit(0)
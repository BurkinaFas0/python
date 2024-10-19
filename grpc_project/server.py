#!/home/alex/code/grpc/grpc_simple_project/venv/bin/python3
from concurrent import futures
import sys
import grpc
import logging
from protos import file_pb2
from protos import file_pb2_grpc
import psycopg2


try:
    conn = psycopg2.connect(dbname='grpc', user='py_user', password='inspirion', host='localhost')
except:
    print('Can`t establish connection to database')


cursor = conn.cursor()
conn.autocommit = True

class TodoService(file_pb2_grpc.todoServiceServicer):
    def createTodo(self, request):
        print("----------Работает сервер-------------")
        cursor.execute(f'INSERT INTO todo(name, completed, day) values(\'{request.name}\', \'{request.completed}\', \'{request.day}\');')
        print(f"Создан объект --> \'{request.name}\', \'{request.completed}\', \'{request.day}\' " )
        cursor.execute(f'SELECT * FROM todo WHERE name = \'{request.name}\';')
        id, name, completed, day = cursor.fetchone()
        print("Считываем объект для отправки клиенту", id, name, completed, day)
        todo_obj = file_pb2.Todo()
        todo_obj.id = id
        todo_obj.name = name
        todo_obj.completed = completed
        todo_obj.day = day
        print("----------------------- конец обработки запроса")
        return file_pb2.todoResponse(todo_obj) 
    

    def getAllTodos(self, request, context):
        print("message", request.message)
        cursor.execute(request.message)
        #todos = cursor.execute(request.message)
        todo_obj = file_pb2.Todo()
        todo_obj.id = 3
        todo_obj.name = 'Name'
        todo_obj.completed = False
        todo_obj.day = 31
        response_array = []
        response_array.append(todo_obj)
        print("----------------------- конец обработки запроса")
        return file_pb2.todoResponse(todo = response_array)
    
    def SayHello(self, request, context):
        return file_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_pb2_grpc.add_todoServiceServicer_to_server(
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
    cursor.close() 	# закрываем курсор
    conn.close() 
    sys.exit(0)
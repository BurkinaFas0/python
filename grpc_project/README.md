

Генерация код Python из protobuf:
    ./venv/bin/python3 -m grpc_tools.protoc -I ./protos  --python_out=./protos --grpc_python_out=./protos ./protos/file.proto

В случае если один из файлов не будет видеть модули:
    import sys
    sys.path.append(r'/home/alex/code/grpc/grpc_simple_project/protos')
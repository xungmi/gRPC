# Cấu trúc thư mục
practice_basic_2/
├── proto/
│   └── image.proto
├── server/
│   └── image_pb2_grpc.py
│   └── image_pb2.py
│   └── image_server.py
├── client/
│   └── image_client.py
├── config_base
│   └── .env
│   └── config.py
├── images
│   └── example.jpg
# Các bước
- cd /path-to-practice-basic-2/
- python -m grpc_tools.protoc \
  -I=proto \
  --python_out=server \
  --grpc_python_out=server \
  proto/image.proto

import grpc
import sys
import os

# Thêm đường dẫn của server vào PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(PROJECT_ROOT, 'server'))
IMAGE_PATH = os.path.join(PROJECT_ROOT, 'images', 'example.jpg')

import image_pb2
import image_pb2_grpc


def run():
    with open(IMAGE_PATH, "rb") as f:
        image_data = f.read()

    channel = grpc.insecure_channel("localhost:50053")
    stub = image_pb2_grpc.ImageServiceStub(channel)

    request = image_pb2.ImageUploadRequest(
        image_name="example.jpg",
        image_data=image_data
    )
    response = stub.UploadImage(request)
    print("Image uploaded to:", response.image_url)

if __name__ == "__main__":
    run()

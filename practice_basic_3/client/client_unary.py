import grpc
import os
import time
import sys

sys.path.append(os.path.abspath("server"))
import image_pb2, image_pb2_grpc

IMAGE_PATH = "images/big_image.jpg"

def run():
    with open(IMAGE_PATH, "rb") as f:
        data = f.read()

    channel = grpc.insecure_channel(
    "localhost:50051",
    options=[
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),
        ('grpc.max_send_message_length', 100 * 1024 * 1024),
    ])
    stub = image_pb2_grpc.ImageServiceStub(channel)

    request = image_pb2.ImageUploadRequest(image_name="unary.jpg", image_data=data)

    start = time.time()
    response = stub.UploadImage(request)
    end = time.time()

    print("Unary upload time: {:.2f}s".format(end - start))
    print(response.message, response.file_path)

if __name__ == "__main__":
    run()

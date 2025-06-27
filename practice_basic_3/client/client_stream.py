import grpc
import os
import time

import sys
sys.path.append(os.path.abspath("server"))
import image_pb2, image_pb2_grpc

IMAGE_PATH = "images/big_image.jpg"
CHUNK_SIZE = 1024 * 1024  # 1MB

def generate_chunks():
    with open(IMAGE_PATH, "rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            yield image_pb2.ImageChunk(image_name="stream.jpg", chunk_data=chunk)

def run():
    channel = grpc.insecure_channel(
    "localhost:50051",
    options=[
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),
        ('grpc.max_send_message_length', 100 * 1024 * 1024),
    ])
    stub = image_pb2_grpc.ImageServiceStub(channel)

    start = time.time()
    response = stub.UploadImageStream(generate_chunks())
    end = time.time()

    print("Stream upload time: {:.2f}s".format(end - start))
    print(response.message, response.file_path)

if __name__ == "__main__":
    run()

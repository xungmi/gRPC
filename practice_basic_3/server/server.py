import grpc
from concurrent import futures
import time
import os

from image_pb2 import ImageUploadResponse
import image_pb2_grpc

SAVE_DIR = "server/uploads"
os.makedirs(SAVE_DIR, exist_ok=True)

class ImageServiceServicer(image_pb2_grpc.ImageServiceServicer):
    def UploadImage(self, request, context):
        path = os.path.join(SAVE_DIR, request.image_name)
        with open(path, "wb") as f:
            f.write(request.image_data)
        return ImageUploadResponse(message="Image uploaded", file_path=path)

    def UploadImageStream(self, request_iterator, context):
        path = None
        with open(os.path.join(SAVE_DIR, "streamed_image.jpg"), "wb") as f:
            for chunk in request_iterator:
                path = os.path.join(SAVE_DIR, chunk.image_name)
                f.write(chunk.chunk_data)
        return ImageUploadResponse(message="Image uploaded via stream", file_path=path)

def serve():
    server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10),
    options=[
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),  # 100MB
        ('grpc.max_send_message_length', 100 * 1024 * 1024),
    ])


    image_pb2_grpc.add_ImageServiceServicer_to_server(ImageServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running at port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

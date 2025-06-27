import grpc
from concurrent import futures
import image_pb2
import image_pb2_grpc

class ImageService(image_pb2_grpc.ImageServiceServicer):
    def GetImage(self, request, context):
        with open(request.image_name, 'rb') as f:
            image_data = f.read()
        return image_pb2.ImageResponse(image_data=image_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageServiceServicer_to_server(ImageService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Image Server running on port 50052...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

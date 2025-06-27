from PIL import Image
from io import BytesIO
import grpc
import image_pb2
import image_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50052')
    stub = image_pb2_grpc.ImageServiceStub(channel)
    response = stub.GetImage(image_pb2.ImageRequest(image_name='example.jpg'))

    print(f"Received image with {len(response.image_data)} bytes")

    image = Image.open(BytesIO(response.image_data))
    image.show()

if __name__ == '__main__':
    run()

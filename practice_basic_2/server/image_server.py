import grpc
from concurrent import futures
import image_pb2 as image_pb2
import image_pb2_grpc as image_pb2_grpc
import boto3
import uuid

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # '..' là thư mục cha, còn '.' là thư mục hiện tại
from config_base import config

# Tạo client S3 dùng config
s3 = boto3.client(
    "s3",
    region_name=config.AWS_REGION,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
)

class ImageService(image_pb2_grpc.ImageServiceServicer):
    def UploadImage(self, request, context):
        image_key = f"uploads/{uuid.uuid4()}_{request.image_name}"

        # Upload ảnh lên S3
        s3.put_object(
            Bucket=config.S3_BUCKET_NAME,
            Key=image_key,
            Body=request.image_data,
            ContentType="image/jpeg",
        )

        image_url = f"https://{config.S3_BUCKET_NAME}.s3.{config.AWS_REGION}.amazonaws.com/{image_key}"
        return image_pb2.ImageUploadResponse(image_url=image_url)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_pb2_grpc.add_ImageServiceServicer_to_server(ImageService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Server is running on port 50053...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

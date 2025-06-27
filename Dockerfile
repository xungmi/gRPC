FROM python:3.10-slim

WORKDIR /app

# Copy toàn bộ mã nguồn vào image
COPY . .

# Cài đặt các phụ thuộc
RUN pip install --no-cache-dir -r requirements.txt

# Biên dịch file .proto (giả sử file ở proto/image.proto, kết quả ra server/)
RUN python -m grpc_tools.protoc \
  -I=proto \
  --python_out=server \
  --grpc_python_out=server \
  proto/image.proto

  

# Chạy server
CMD ["python", "server/main.py"]

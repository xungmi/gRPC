# Flow
1. Client gửi ảnh (.jpg/.png) dưới dạng byte qua gRPC.
2. Server xử lý ảnh resize về 256x256
3. Server upload ảnh đã xử lý lên AWS S3.
4. Server trả về URL của ảnh.
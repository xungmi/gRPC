import numpy as np
from PIL import Image

# Kích thước gần đúng 500MB
width, height = 9600, 6072

# Tạo mảng ngẫu nhiên RGB
image_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Chuyển thành ảnh
image = Image.fromarray(image_array)

# Lưu ảnh dưới dạng PNG (lossless để giữ kích thước)
image.save("images/big_image.jpg", format="JPEG")

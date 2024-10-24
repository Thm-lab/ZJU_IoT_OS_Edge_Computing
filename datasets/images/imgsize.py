from PIL import Image

# 替换为你的图像文件路径
image_path = "path/to/your/image.jpg"
img = Image.open(image_path)
width, height = img.size

print(f"Width: {width}, Height: {height}")
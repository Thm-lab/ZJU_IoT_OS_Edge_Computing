import os

# 设置文件夹路径
txt_folder = './txt_rotated_Annotations'
jpg_folder = './rotated_JPEGImages'

# 遍历 txt 文件夹
for filename in os.listdir(txt_folder):
    if filename.endswith('.txt'):
        txt_path = os.path.join(txt_folder, filename)

        # 检查文件是否为空
        if os.path.getsize(txt_path) == 0:
            # 删除对应的 jpg 文件
            jpg_path = os.path.join(jpg_folder, filename.replace('.txt', '.jpg'))
            if os.path.exists(jpg_path):
                os.remove(jpg_path)

            # 删除空的 txt 文件
            os.remove(txt_path)
            print(f'Deleted: {txt_path} and {jpg_path}')
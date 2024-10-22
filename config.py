import os
import random
import shutil
import yaml

# 定义路径
base_folder = os.path.join(os.curdir, 'datasets')
images_folder = os.path.join(base_folder, 'images')
annotations_folder = os.path.join(base_folder, 'txt_annotations')
output_folder = os.path.join(base_folder, 'yolov8')

# 划分训练集、验证集和测试集
train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

# 创建输出文件夹及其子文件夹
sets = ['train', 'valid', 'test']
for set_name in sets:
    images_set_path = os.path.join(output_folder, set_name, 'images')
    labels_set_path = os.path.join(output_folder, set_name, 'labels')
    os.makedirs(images_set_path, exist_ok=True)
    os.makedirs(labels_set_path, exist_ok=True)

# 获取所有图片和对应的 TXT 文件，排除 classes.txt
image_files = [
    f for f in os.listdir(images_folder)
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))
]
annotation_files = [
    f for f in os.listdir(annotations_folder)
    if f.lower().endswith('.txt') and f != 'classes.txt'
]

# 确保每张图片都有对应的 TXT 文件
image_basenames = set(os.path.splitext(f)[0] for f in image_files)
annotation_basenames = set(os.path.splitext(f)[0] for f in annotation_files)
common_basenames = list(image_basenames & annotation_basenames)

if not common_basenames:
    raise ValueError("没有找到匹配的图片和标注文件。请检查文件名是否匹配。")

# 打印总数据量
print(f"总数据量: {len(common_basenames)}")

random.shuffle(common_basenames)

train_size = int(len(common_basenames) * train_ratio)
valid_size = int(len(common_basenames) * valid_ratio)
# test_size = len(common_basenames) - train_size - valid_size

train_basenames = common_basenames[:train_size]
valid_basenames = common_basenames[train_size:train_size + valid_size]
test_basenames = common_basenames[train_size + valid_size:]

print(f"训练集: {len(train_basenames)}")
print(f"验证集: {len(valid_basenames)}")
print(f"测试集: {len(test_basenames)}")


# 定义一个函数来复制文件
def copy_files(basenames, set_name):
    for basename in basenames:
        # 复制图片
        for ext in ['.png', '.jpg', '.jpeg', '.bmp']:
            img_file = basename + ext
            src_img_path = os.path.join(images_folder, img_file)
            if os.path.exists(src_img_path):
                shutil.copy(
                    src_img_path,
                    os.path.join(output_folder, set_name, 'images', img_file))
                break
        else:
            print(f"警告: 图片文件 {basename} 未找到。")
            continue  # 跳过没有找到图片的标注文件

        # 复制标注文件
        txt_file = basename + '.txt'
        src_txt_path = os.path.join(annotations_folder, txt_file)
        if os.path.exists(src_txt_path):
            shutil.copy(
                src_txt_path,
                os.path.join(output_folder, set_name, 'labels', txt_file))
        else:
            print(f"警告: 标注文件 {txt_file} 未找到。")


# 复制文件到相应的文件夹
copy_files(train_basenames, 'train')
copy_files(valid_basenames, 'valid')
copy_files(test_basenames, 'test')

# 创建 YAML 配置文件
yaml_content = {
    'train': os.path.abspath(os.path.join(output_folder, 'train', 'images')),
    'val': os.path.abspath(os.path.join(output_folder, 'valid', 'images')),
    'test': os.path.abspath(os.path.join(output_folder, 'test',
                                         'images')),  # 可选
    'nc': 1,  # 根据您的数据集类别数量进行修改
    'names': ['robot dog'],  # 根据您的类别名称进行修改
}

yaml_file_path = os.path.join(output_folder, 'yolov8.yaml')
with open(yaml_file_path, 'w') as yaml_file:
    yaml.dump(yaml_content,
              yaml_file,
              default_flow_style=False,
              allow_unicode=True)

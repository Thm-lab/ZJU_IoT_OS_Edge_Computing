import os
import shutil
import random


def create_yolov8_structure(dataset_dir, train_ratio=0.8):
    annotations_dir = os.path.join(dataset_dir, 'Annotations')
    images_dir = os.path.join(dataset_dir, 'ImageSets')

    # 创建新的文件夹结构
    output_train_dir = os.path.join(dataset_dir, 'train')
    output_val_dir = os.path.join(dataset_dir, 'val')

    os.makedirs(output_train_dir, exist_ok=True)
    os.makedirs(output_val_dir, exist_ok=True)

    # 获取所有图像文件的基本名称
    image_set_file = os.path.join(images_dir,
                                  'train.txt')  # 假设您有一个 train.txt 文件
    with open(image_set_file, 'r') as f:
        image_files = [line.strip() for line in f.readlines() if line.strip()]

    # 随机打乱文件顺序
    random.shuffle(image_files)

    # 计算训练集和验证集的数量
    train_size = int(len(image_files) * train_ratio)
    train_files = image_files[:train_size]
    val_files = image_files[train_size:]

    # 复制文件到新的训练和验证目录
    for filename in train_files:
        # 复制图像
        image_src = os.path.join(images_dir,
                                 filename + '.jpg')  # 假设您的图像是 .jpg 格式
        image_dest = os.path.join(output_train_dir, filename + '.jpg')
        shutil.copy(image_src, image_dest)

        # 复制标签
        annotation_src = os.path.join(annotations_dir,
                                      filename + '.xml')  # 假设标签是 .xml 格式
        annotation_dest = os.path.join(output_train_dir, filename + '.xml')
        shutil.copy(annotation_src, annotation_dest)

    for filename in val_files:
        # 复制图像
        image_src = os.path.join(images_dir, filename + '.jpg')
        image_dest = os.path.join(output_val_dir, filename + '.jpg')
        shutil.copy(image_src, image_dest)

        # 复制标签
        annotation_src = os.path.join(annotations_dir, filename + '.xml')
        annotation_dest = os.path.join(output_val_dir, filename + '.xml')
        shutil.copy(annotation_src, annotation_dest)

    print(f"Training files copied: {len(train_files)}")
    print(f"Validation files copied: {len(val_files)}")


# 示例用法
dataset_directory = './DataSets'  # 请替换为您的 DataSets 文件夹路径
create_yolov8_structure(dataset_directory, train_ratio=0.7)

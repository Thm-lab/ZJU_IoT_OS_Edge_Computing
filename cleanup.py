import os
import xml.etree.ElementTree as ET

images_folder = './datasets/images'
txt_annotations_folder = './datasets/txt_annotations'


def txt_cleanup():
    # 获取标注文件的文件名（去掉后缀）
    annotated_files = set()
    for annotation_file in os.listdir(txt_annotations_folder):
        if annotation_file.endswith('.txt'):
            base_name = os.path.splitext(annotation_file)[0]
            annotated_files.add(base_name)

    # 遍历 images 文件夹，删除没有标注的图片
    for image_file in os.listdir(images_folder):
        if image_file.endswith('.png'):
            base_name = os.path.splitext(image_file)[0]
            if base_name not in annotated_files:
                os.remove(os.path.join(images_folder, image_file))

    # 重新命名剩下的图片和标注文件
    remaining_images = sorted(
        [file for file in os.listdir(images_folder) if file.endswith('.png')])
    for idx, image_file in enumerate(remaining_images):
        new_image_name = f'{idx + 1:03}.png'  # 新的图片名称
        os.rename(os.path.join(images_folder, image_file),
                  os.path.join(images_folder, new_image_name))

        # 处理对应的标注文件
        base_name = os.path.splitext(image_file)[0]
        new_annotation_name = f'{idx + 1:03}.txt'  # 新的标注名称
        if base_name in annotated_files:
            os.rename(
                os.path.join(txt_annotations_folder, base_name + '.txt'),
                os.path.join(txt_annotations_folder, new_annotation_name))


if __name__ == '__main__':
    txt_cleanup()

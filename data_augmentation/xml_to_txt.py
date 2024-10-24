import os
import xml.etree.ElementTree as ET


def xml_to_labelImg_txt(xml_path, txt_path):
    # 解析 XML 文件
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 获取图像尺寸
    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    # 提取边界框信息
    annotations = []
    for obj in root.findall('object'):
        # 将名称改为 '0'
        name = '0'
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # 计算中心点和宽高
        x_center = (xmin + xmax) / 2
        y_center = (ymin + ymax) / 2
        bbox_width = xmax - xmin
        bbox_height = ymax - ymin

        # 格式化为 LabelImg 的 TXT 格式
        annotations.append(
            f"{name} {x_center / width:.6f} {y_center / height:.6f} {bbox_width / width:.6f} {bbox_height / height:.6f}")

    # 写入 TXT 文件
    with open(txt_path, 'w') as f:
        for annotation in annotations:
            f.write(annotation + '\n')


# 使用示例
xml_dir = '../datasets/rotated_Annotations'  # 替换为你的 XML 文件夹路径
txt_dir = '../datasets/txt_rotated_Annotations'  # 替换为你的 TXT 文件夹路径

if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)

# 遍历所有 XML 文件并转换为 TXT
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(xml_dir, xml_file)
        txt_file = xml_file.replace('.xml', '.txt')
        txt_path = os.path.join(txt_dir, txt_file)
        xml_to_labelImg_txt(xml_path, txt_path)
        print(f"Converted {xml_file} to {txt_file}")

import xml.etree.ElementTree as ET
import os


def change_xml():
    """
    功能: 1、保留、修改xml文件某标签内容
         2、修改xml文件存放路径,文件名，图像来源等
         3、本方法采用字符串方式解析打开,删除/保存xml文件
         4、方法是在Windows系统下运行的，方法中的路径请根据不同系统自行更改
    """
    path = "G:\\VOCdevkit_fruit_pro\\VOC2007\\Annotations\\"  # xml文件存放路径
    save_path = "G:\\VOCdevkit_fruit_pro\\VOC2007\\Annotations1\\"  # 修改后的xml文件存放路径
    if not os.path.exists(save_path):  # 如果路径不存在创建路径
        os.makedirs(save_path)
    imgpath = "G:\\VOCdevkit_fruit_pro\\VOC2007\\JPEGImages\\"  # 图像path路径
    files = os.listdir(path)  # 读取路径下所有文件名
    for xmlFile in files:
        if xmlFile.endswith('.xml'):
            tree = ET.ElementTree(file=path + xmlFile)  # 打开xml文件，送到tree解析
            root = tree.getroot()  # 得到文档元素对象
            folder = os.path.dirname(imgpath)
            root[0].text = os.path.basename(folder)   # root[0].text是annotation下第一个子节点中内容，直接赋值替换文本内容
            root[1].text = xmlFile
            root[1].text = root[1].text.replace('xml','jpg')  #修改根节点下的内容
            # root[1].text = root[1].text.split('.')[0] #根据需求决定要不要文件名后缀
            root[2].text = imgpath + root[1].text.replace('xml','jpg')
            # for object in root.findall('object'):
            #     name = object.find('name').text  # 获取每一个object节点下name节点的内容
            #     if name == 'plate':
            #         object.find('name').text = str('pb') #修改指定标签的内容
            #     else:
            #          root.remove(object)    # 删除除了name属性值为'plate'之外object节点的所有object节点
            tree.write(save_path + xmlFile)   # 替换后的内容保存在内存中需要将其写出

if __name__ =="__main__":
    change_xml()


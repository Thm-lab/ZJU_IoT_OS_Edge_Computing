# 针对图像与标签文件混在同一个文件夹中的情况
# 将所有图像文件复制到另一个文件夹

import os.path
import shutil 
import glob

#file_list = glob.glob()
def copyFiles(sourceDir,targetDir):
	for files in os.listdir(sourceDir):
		sourceFile = os.path.join(sourceDir,files)   
		targetFile = os.path.join(targetDir,files)
		if os.path.isfile(sourceFile) and sourceFile.find('.jpg')>0:
			shutil.move(sourceFile,targetFile)

sourceDir = "G:/VOCdevkit_fruit_pro/VOC2007/JPEGmix"
targetDir = "G:/VOCdevkit_fruit_pro/VOC2007/JPEG"

copyFiles(sourceDir,targetDir)


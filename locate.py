import cv2


def draw_rectangle_on_first_frame(video_path, output_image_path, x, y, width,
                                  height):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # 读取第一帧
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return

    # 在帧上绘制矩形框
    # (x, y)是矩形的左上角坐标
    # (x + width, y + height)是矩形的右下角坐标
    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0),
                  2)  # 绿色框，线宽为2

    # 保存处理后的帧为图像
    cv2.imwrite(output_image_path, frame)

    # 释放视频对象
    cap.release()
    print(f"Saved the modified frame as {output_image_path}")


video_file = 'v3.mp4'  # 输入视频文件路径
output_image_file = 'locate.png'  # 输出图像文件路径

# 设置矩形框的参数
x, y, width, height = 265, 175, 340, 190  # x,y,width,height

# 调用函数在第一帧上绘制矩形并保存为图像
draw_rectangle_on_first_frame(video_file, output_image_file, x, y, width,
                              height)

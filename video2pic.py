import subprocess
import os


def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    command = [
        'ffmpeg',
        '-i',
        video_path,
        '-vf',
        'fps=1',  # 每秒一帧
        os.path.join(output_folder, '%03d.png')
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Frames extracted to {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")


if __name__ == '__main__':
    video_file = 'cut3.mp4'
    output_folder = './datasets/images'

    extract_frames(video_file, output_folder)

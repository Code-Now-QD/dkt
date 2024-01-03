# @Time : 2023/8/2 0002 14:24
import os
import cv2
from tqdm import tqdm  # 导入tqdm


def extract_frames(video_path, output_dir, frame_interval=6, target_resolution=(1920, 1080)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = os.path.join(output_dir, video_name)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            resized_frame = cv2.resize(frame, target_resolution)
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, resized_frame)

        frame_count += 1

    cap.release()


def main(root_dir, output_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in tqdm(files, desc="Processing videos"):
            if file.lower().endswith('.mp4'):
                video_path = os.path.join(root, file)
                extract_frames(video_path, output_dir)


if __name__ == "__main__":
    root_dir = "data/4k_60"  # 修改为根目录路径
    output_dir = "data/4k_60_result"  # 修改为输出目录路径
    main(root_dir, output_dir)

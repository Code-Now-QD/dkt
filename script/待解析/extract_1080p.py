import os
import cv2
from tqdm import tqdm  # 导入tqdm


def extract_frames(video_path, output_dir, frame_interval=3):  # 添加 frame_interval 参数，默认为 3
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

        if frame_count % frame_interval == 0:  # 仅保存每 frame_interval 帧
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()


def main(root_dir, output_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in tqdm(files, desc="Processing videos"):
            if file.lower().endswith('.mp4'):
                video_path = os.path.join(root, file)
                extract_frames(video_path, output_dir)


if __name__ == "__main__":
    root_dir = "1080p"  # 修改为根目录路径
    output_dir = "1080p_result"  # 修改为输出目录路径
    main(root_dir, output_dir)

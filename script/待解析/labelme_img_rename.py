import os
from tqdm import tqdm  # Make sure to install this package: pip install tqdm

def rename_images(root_directory, prefix):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # Add more extensions if needed

    total_files = 0
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension.lower() in image_extensions and not filename.startswith(prefix):
                total_files += 1

    progress_bar = tqdm(total=total_files, desc="Renaming Progress", unit="file")

    for root, dirs, files in os.walk(root_directory):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension.lower() in image_extensions and not filename.startswith(prefix):
                old_path = os.path.join(root, file)
                new_filename = f"{prefix}_{filename}{file_extension}"
                new_path = os.path.join(root, new_filename)

                os.rename(old_path, new_path)
                progress_bar.update(1)
                progress_bar.set_postfix(current_file=new_filename)

    progress_bar.close()

if __name__ == "__main__":
    root_directory = "pothole_all_new/images"
    new_prefix = "pothole"

    rename_images(root_directory, new_prefix)

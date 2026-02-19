import os
import shutil

def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.makedirs(dest_dir, exist_ok=True)

    copy_files_recursive(source_dir, dest_dir)
    

def copy_files_recursive(source_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)

    for name in os.listdir(source_dir):
        src_path = os.path.join(source_dir, name)
        dst_path = os.path.join(dest_dir, name)
        print(f" * {src_path} -> {dst_path}")

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)

        elif os.path.isdir(src_path):
            copy_files_recursive(src_path, dst_path)

        else:
            raise ValueError(f"Unsupported file type: {src_path}")

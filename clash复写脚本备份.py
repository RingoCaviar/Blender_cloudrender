import shutil
import os

appdata_path = os.environ.get('APPDATA')
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
def copy_file_with_overwrite(source_file, destination_file):
    try:
        shutil.copy2(source_file, destination_file)
        print(f"文件 {source_file} 已成功复制到 {destination_file} 并覆盖。")
    except FileNotFoundError:
        print(f"文件 {source_file} 未找到。")
    except Exception as e:
        print(f"复制文件时发生错误: {e}")

# 指定源文件路径和目标文件路径（目标文件路径为当前位置，文件名与源文件相同）
source_file_path = appdata_path + r"\io.github.clash-verge-rev.clash-verge-rev\profiles\Script.js"
destination_file_path = f"{script_dir}/Script.js"

# 调用函数进行复制
copy_file_with_overwrite(source_file_path, destination_file_path)

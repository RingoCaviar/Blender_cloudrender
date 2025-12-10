# 文件名: install_blender.py
import os
import sys
import subprocess
import argparse

def install_blender(version, install_path, tmp_dir):
    # --- 1. 变量预处理 ---
    major_ver = version[:3]
    file_name = f"blender-{version}-linux-x64.tar.xz"
    folder_name = f"blender-{version}-linux-x64"
    # 清华源地址
    url = f"https://mirrors.tuna.tsinghua.edu.cn/blender/blender-release/Blender{major_ver}/{file_name}"
    
    full_install_path = os.path.join(install_path, folder_name)

    print(f"🚀 开始处理: Blender {version}")
    print(f"📂 安装目标: {install_path}")
    print(f"💾 缓存目录: {tmp_dir}")

    # --- 2. 创建目录 (替代 !mkdir -p) ---
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir, exist_ok=True)
    
    # 切换工作目录
    if not os.path.exists(install_path):
        os.makedirs(install_path, exist_ok=True)
    os.chdir(install_path)

    # --- 3. 下载文件 (替代 !wget) ---
    # 使用 subprocess 调用系统命令
    if not os.path.exists(file_name):
        print(f"⬇️ 正在下载...")
        # -c 断点续传, --no-check-certificate 防止部分环境证书报错
        cmd_download = ["wget", "-c", url, "-O", file_name, "--no-check-certificate"]
        subprocess.run(cmd_download, check=True)
    else:
        print("⚡ 文件已存在，跳过下载。")

    # --- 4. 解压文件 (替代 !tar) ---
    print("📦 正在解压...")
    cmd_tar = ["tar", "-xf", file_name]
    subprocess.run(cmd_tar, check=True)

    # --- 5. 写入 .bashrc (持久化配置) ---
    print("⚙️ 更新 .bashrc 配置...")
    bash_content = f"""
# --- Blender Auto Config ---
export PATH={full_install_path}:$PATH
export TMPDIR={tmp_dir}
# ---------------------------
"""
    # 读取现有的防止重复写入 (简单判断)
    try:
        with open(os.path.expanduser('~/.bashrc'), 'r') as f:
            current_content = f.read()
    except FileNotFoundError:
        current_content = ""

    if full_install_path not in current_content:
        with open(os.path.expanduser('~/.bashrc'), 'a') as f:
            f.write(bash_content)
        print("✅ .bashrc 更新成功")
    else:
        print("✅ 配置已存在，跳过写入 .bashrc")

    # 删除压缩包 (可选)
    # os.remove(file_name) 

    print(f"\n✨ Blender {version} 安装脚本执行完毕！")
    print(f"⚠️ 注意：在 Jupyter 中使用前，请运行下面的 Python 代码更新当前环境 PATH。")

# --- 命令行参数解析部分 ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blender 自动安装脚本")
    # 定义三个参数
    parser.add_argument("--version", required=True, help="Blender 版本号，例如 5.0.0")
    parser.add_argument("--path", default="/root", help="安装根目录")
    parser.add_argument("--tmp", default="/root/autodl-tmp/TMPDIR", help="临时缓存目录")

    args = parser.parse_args()
    
    install_blender(args.version, args.path, args.tmp)
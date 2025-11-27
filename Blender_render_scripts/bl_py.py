import subprocess
import os
import platform

# ================= 配置区域 (修改这里) =================
# 获取脚本 当前 路径
script_dir = os.path.dirname(os.path.abspath(__file__))
# 设置 工程文件 名
BLEND_FILE = "shot4.blend"
# 生成 工程文件 绝对路径
blend_file_path = os.path.join(script_dir, "shot4.blend")
# 输出文件名
OUTPUT_NAME = "babala"
# 生成 输出文件 绝对路径 默认放在脚本路径内的output文件夹中
output_path = os.path.join(script_dir, "output", OUTPUT_NAME)

# 帧数范围
START = 500
END = 513

GPU_SCRIPT = "setting.py"
setting_path = os.path.join(script_dir, GPU_SCRIPT)

# Blender主程序目录
BLENDER_CMD = r"D:\ProgramFiles\blender-5.0.0-windows-x64\blender.exe" 
# ======================================================

def render():
    # 构建命令列表
    cmd = [
        BLENDER_CMD,           # Blender 命令
        "-b", blend_file_path,      # 后台模式 + 文件路径
        "--factory-startup",
        "-P", setting_path,      # 关键：加载 GPU 设置脚本
        "-s", str(START),      # 起始帧
        "-e", str(END),        # 结束帧
        "-o", output_path, 
        "-a"                   # 执行动画渲染 (Animation)
    ]
    
    # 打印一下命令方便检查 (Windows和Linux通用)
    print(f"正在启动: {' '.join(cmd)}")
    
    # 执行命令 (shell=False 更安全，且自动处理路径空格)
    subprocess.run(cmd)

if __name__ == "__main__":
    render()
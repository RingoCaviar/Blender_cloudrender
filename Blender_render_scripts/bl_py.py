import subprocess
import os
import platform

# ================= 配置区域 (修改这里) =================
script_dir = os.path.dirname(os.path.abspath(__file__))
# 设置你的 工程文件名称
BLEND_FILE = "shot4.blend"

blend_file_path = os.path.join(script_dir, BLEND_FILE)
# 输出文件名 在这里设置输出文件名
OUTPUT_NAME = "babala_"
# 生成 输出文件 绝对路径 默认放在脚本路径内的output文件夹中
output_path = os.path.join(script_dir, "output", OUTPUT_NAME)

# 帧数范围 有需要可以解除注释，记得下方的渲染命令也要解除
# START = 500
# END = 513

GPU_SCRIPT = "setting.py"
setting_path = os.path.join(script_dir, GPU_SCRIPT)

# Blender主程序目录，如果是windows请自行修改
BLENDER_CMD = r"blender" 
# ======================================================

def render():
    # 构建命令列表
    cmd = [
        BLENDER_CMD,           # Blender 命令
        "-b", blend_file_path,      # 后台模式 + 文件路径
        # "--factory-startup",     #使用出厂设置启动Blender，一般不需要开启
        "-P", setting_path,      # 关键：加载 GPU 设置脚本
        # "-s", str(START),      # 起始帧
        # "-e", str(END),        # 结束帧
        "-o", output_path, 
        #"-a",                   # 执行动画渲染 (Animation)
        "-f", "1",               # 执行单帧渲染，和动画渲染参数不能共存！
        "--", "--cycles-device", "OPTIX"
    ]
    
    # 打印一下命令方便检查
    print(f"正在启动: {' '.join(cmd)}")
    
    # 执行命令 (shell=False 更安全，且自动处理路径空格)
    subprocess.run(cmd)

if __name__ == "__main__":
    render()
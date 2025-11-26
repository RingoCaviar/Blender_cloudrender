import subprocess
import sys
import os

my_env = os.environ.copy()
my_env["PYTHONIOENCODING"] = "utf-8"

BL_path        = r"D:\ProgramFiles\blender-5.0.0-windows-x64\blender.exe"
out_path       = r"D:/cache/renderoutput_test"
render_file    = r"D:\Work\2025.11.17.杨斌.西林瓶\西林瓶建模_002.blend"
cy_device      = "OPTIX"
override_scripts = r"D:\cache\blender render test\setting.py"

scene_list = [
    "密封10ml_pose01",
    "密封10ml_pose02",
]

def run_and_decode(cmd, env):
    # 启动进程，把输出流截获 (stdout=subprocess.PIPE)
    p = subprocess.Popen(
        cmd, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, # 把错误信息也合并进来
        env=env
    )
    
    # 循环读取每一行
    while True:
        # 这里的 line 是字节流 (bytes)，不是字符串
        line = p.stdout.readline()
        if not line and p.poll() is not None:
            break
            
        if line:
            # === 这里的逻辑是关键 ===
            # Blender 发送过来的是 UTF-8 字节，我们必须用 utf-8 解码变成 Unicode 字符串
            # 这里的 strip() 是去掉末尾换行符
            text_str = line.decode('utf-8', errors='ignore').strip()
            
            # 直接 print，Python 会自动负责把它编码成 CMD 能看懂的格式 (GBK)
            print(text_str)

for s in scene_list:
    cmd = [
        BL_path,
        "-b",
        "--factory-startup",
        render_file,
        "-S", s,
        "-o", rf"{out_path}\{s}.png",
        "-P", override_scripts,
        "-f", "1",
        "--", "--cycles-device", cy_device,
    ]
    run_and_decode(cmd, my_env)
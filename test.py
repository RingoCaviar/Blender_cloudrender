import os
import subprocess
import locale

def render_blend(blender_path, blend_file, output_dir):
    """
    使用 Blender 命令行渲染指定的 .blend 文件，支持中文路径和输出。
    """
    # 验证路径
    if not os.path.isfile(blender_path):
        print(f"错误: 找不到 Blender 可执行程序: {blender_path}")
        return
    if not os.path.isfile(blend_file) or not blend_file.endswith('.blend'):
        print(f"错误: 找不到有效的 .blend 文件: {blend_file}")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # 如果输出目录不存在，自动创建

    # 设置输出文件的路径和名称
    output_file = os.path.join(output_dir, "render_output")

    # 构建 Blender 渲染命令
    command = [
        blender_path,
        "-b", blend_file,          # 后台模式渲染
        "-o", output_file,         # 输出文件的基础路径
        "-F", "PNG",               # 输出格式：PNG
        "-x", "1",                 # 自动添加扩展名
        "-a"                       # 渲染所有帧
    ]

    # 执行渲染命令
    print("正在执行渲染命令...")
    print(" ".join(command))  # 输出完整的渲染命令供用户检查
    try:
        # 解决中文乱码：设置编码为 'utf-8' 或本地默认编码
        result = subprocess.run(command, check=True, text=True, encoding=locale.getpreferredencoding())
        print("渲染完成！输出目录:", output_dir)
    except subprocess.CalledProcessError as e:
        print(f"渲染失败: {e}")
    except UnicodeDecodeError as e:
        print(f"编码错误: {e}, 请检查系统编码或路径字符。")

if __name__ == "__main__":
    print("=== Blender 渲染脚本 ===")
    # 用户定义 Blender 安装路径、.blend 文件和输出目录
    blender_path = input("请输入 Blender 可执行程序路径: ").strip()
    blend_file = input("请输入 .blend 文件路径: ").strip()
    output_dir = input("请输入渲染输出目录: ").strip()

    # 执行渲染
    render_blend(blender_path, blend_file, output_dir)

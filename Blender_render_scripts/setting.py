import bpy

# =================================================================
# 硬件自动配置脚本 (强制开启显卡)
# =================================================================
def force_enable_gpu(type='OPTIX'):
    print(f"\n>>> 正在初始化硬件设置 (目标: {type})...")
    
    # 获取 Cycles 的首选项
    try:
        cprefs = bpy.context.preferences.addons['cycles'].preferences
    except Exception as e:
        print("!!! 错误: 无法获取 Cycles 首选项，可能未开启 Cycles 插件。")
        return

    # 1. 强制刷新设备列表 (关键！否则脚本可能看不到显卡)
    cprefs.get_devices()

    # 2. 设置计算设备类型 (OPTIX, CUDA, HIP 等)
    cprefs.compute_device_type = type

    # 3. 遍历所有设备，勾选显卡，取消 CPU
    has_gpu = False
    for device in cprefs.devices:
        if device.type == type:
            device.use = True
            print(f"  [√] 已激活 GPU: {device.name}")
            has_gpu = True
        else:
            device.use = False
            # print(f"  [x] 已忽略设备: {device.name}") # 不重要的设备就不打印了
    
    if not has_gpu:
        print("!!! 警告: 未找到任何支持该类型的 GPU！可能退回 CPU 渲染。")
    else:
        print(">>> 硬件配置完成。\n")

# =================================================================
# 执行配置
# =================================================================

# 1. 先激活显卡 (这一步解决了首选项没勾选的问题)
force_enable_gpu('OPTIX') 

# 2. 再设置场景参数
scene = bpy.context.scene
# scene.cycles.device = 'GPU'            # 告诉场景使用 GPU 设备
# scene.cycles.samples = 4             # 采样率

# 3. 设置降噪 (必须配合上面的 OPTIX)
# scene.cycles.use_denoising = True      # 开启降噪
# scene.cycles.denoiser = 'OPTIX'        # 强制使用 OptiX 降噪器
# scene.cycles.denoising_input_passes = 'RGB_ALBEDO_NORMAL' # (可选) 设置降噪输入通道

print(">>> 场景参数已应用。")
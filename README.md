# OpenCV Python 图像处理基础练习集 📸

本项目是一个基于 Python 和 OpenCV 库的集合，涵盖了从基础的图像读取、摄像头调用到高级的仿射变换和批量处理功能。非常适合 OpenCV 初学者作为代码参考。

## 📂 项目结构与功能说明

### 1. 基础操作
* **`opencv_read.py`**: 基础图像加载。展示了如何读取图片、在窗口中显示以及将其另存为新格式（`.png`）。
* **`opencap.py`**: 摄像头实时捕获。调用电脑摄像头（ID 0），设置分辨率，并实时通过插值算法调整预览窗口大小。按下 **'q'** 键即可退出。

### 2. 几何变换 (Geometry Transformation)
* **`pic_affine.py`**: 仿射变换。使用自定义的 $2 \times 3$ 矩阵 $M$ 对图像进行仿射变换（包含缩放和平移效果）。
* **`rotation.py`**: 图像旋转。演示如何获取旋转矩阵（`getRotationMatrix2D`）并对图像执行旋转操作。
* **`resize.py`**: 批量尺寸调整。自动遍历 `back` 文件夹下的所有 `.jpg` 图片，统一缩放为 $640 \times 480$ 像素，并保存到 `back_resize` 目录。

### 3. 其他文件
* **`local_weater.py` & `system_server.py`**: 扩展功能脚本，用于构建基于 MCP 协议的环境监控与天气服务。

## 🛠️ 环境要求

在运行代码之前，请确保你的环境中已安装 Python 及以下依赖库：

```bash
pip install opencv-python numpy

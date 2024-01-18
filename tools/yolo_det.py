import os
import numpy as np
import cv2 
from ultralytics import YOLO
from ultralytics.engine.results import Boxes
import json

# 加载预训练的 YOLOv8n 模型
model = YOLO('models/yolov8n.pt')

# 定义图像文件夹的路径
image_folder = '/home/aldno/data/BUPT/image_data'

# 定义保存结果的文件夹路径
result_folder = '/home/aldno/data/BUPT/result/image_result/'

# 设置要检测的类别
classes = [0, 1, 2, 3, 5, 7]

# 创建保存结果的子文件夹，如果子文件夹不存在
os.makedirs(os.path.join(result_folder, 'results_text'), exist_ok=True)
os.makedirs(os.path.join(result_folder, 'results_image'), exist_ok=True)
os.makedirs(os.path.join(result_folder, 'results_json'), exist_ok=True)

# 获取图像文件夹中的所有图像文件
image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith(('.jpg', '.png', '.jpeg'))]

# 循环遍历每张图像并进行检测
for image_file in image_files:
    # 对当前图像进行推理
    results = model.predict(image_file, classes=classes)
    
    # 构建保存结果的文件名（不包括文件扩展名）
    filename_without_extension = os.path.splitext(os.path.basename(image_file))[0]
    
    # 保存检测结果为文本文件
    results[0].save_txt(os.path.join(result_folder, 'results_text', f'{filename_without_extension}_detection.txt'), save_conf=True)

    # 使用plot()方法绘制检测结果并返回带注释的图像的NumPy数组
    annotated_image = results[0].plot()
    
    # 保存带注释的图像为文件
    image_save_path = os.path.join(result_folder, 'results_image', f'{filename_without_extension}_annotated.jpg')
    cv2.imwrite(image_save_path, annotated_image)

    json_result = results[0].tojson()
    # 构建保存JSON文件的文件路径
    json_save_path = os.path.join(result_folder, 'results_json', f'{filename_without_extension}_detection.json')

    # 保存JSON对象为文件
    with open(json_save_path, 'w') as json_file:
        json.dump(json_result, json_file)

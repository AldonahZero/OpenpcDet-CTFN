import open3d as o3d
import numpy as np
import os

def process_pcd(file_path):
    # 读取 PCD 文件
    pcd = o3d.io.read_point_cloud(file_path)

    # 将 PCD 数据转换为 NumPy 数组
    points = np.asarray(pcd.points)

    # 添加一个全零的强度列
    zeros_intensity = np.zeros((points.shape[0], 1))
    points_with_intensity = np.hstack((points, zeros_intensity))

    return points_with_intensity

def main():
    pcd_dir = '/home/aldno/data/BUPT/pointcloud_data/pcd'
    output_dir = '/home/aldno/data/BUPT/pointcloud_data/processed'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(pcd_dir):
        if file_name.endswith('.pcd'):
            file_path = os.path.join(pcd_dir, file_name)
            points_with_intensity = process_pcd(file_path)

            # 保存为 NumPy 文件
            npy_file_name = file_name.replace('.pcd', '.npy')
            np.save(os.path.join(output_dir, npy_file_name), points_with_intensity)

if __name__ == "__main__":
    main()

import open3d as o3d
import numpy as np
import os

def generate_additional_points(point, distance=0.1):
    """
    为给定的点生成四个额外的点。
    :param point: 原始点 [x, y, z]
    :param distance: 额外点与原始点的距离
    :return: 一个包含四个额外点的数组
    """
    x, y, z = point
    return np.array([
        [x + distance, y, z],
        [x - distance, y, z],
        [x, y + distance, z],
        [x, y - distance, z]
    ])

def pcd2bin(in_file, out_file):
    # 读取 PCD 文件
    pcd = o3d.io.read_point_cloud(in_file)

    # 将点云位置数据转换为 NumPy 数组
    points = np.asarray(pcd.points)

    # 调整 z 轴坐标，使原点位于地面上方约 1.6m
    points[:, 2] += 0.6

     # 为所有点（包括额外的点）设置强度为0
    intensity = np.zeros((points.shape[0], 1))

    # 合并位置和强度数据
    data = np.hstack((points, intensity)).astype(np.float32)

    # 保存为 .bin 文件
    data.tofile(out_file)

def main():
    pcd_dir = '/home/aldno/data/BUPT/pointcloud_data/pcd/'
    bin_dir = '/home/aldno/data/BUPT/pointcloud_data/bin/'

    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)

    for file_name in os.listdir(pcd_dir):
        if file_name.endswith('.pcd'):
            pcd_file = os.path.join(pcd_dir, file_name)
            bin_file = os.path.join(bin_dir, file_name.replace('.pcd', '.bin'))
            pcd2bin(pcd_file, bin_file)

if __name__ == "__main__":
    main()

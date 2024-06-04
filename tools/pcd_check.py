import open3d as o3d
import numpy as np

def print_pcd_info(pcd_path):
    # 加载PCD文件
    pcd = o3d.io.read_point_cloud(pcd_path)

    # 打印PCD的信息
    print("Point Cloud information:")
    print(pcd)
    print("")

    # 获取并打印点云的点数
    print("Number of points:", len(pcd.points))
    print("")

    # 打印点云的一些点（例如前5个点）
    print("First 5 points:")
    print(np.asarray(pcd.points)[:5])

# 指定PCD文件的路径
pcd_file_path = '/home/aldno/data/BUPT/pointcloud_data/pcd/1702023208.100889000.pcd'

# 调用函数
print_pcd_info(pcd_file_path)
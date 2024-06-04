import open3d as o3d
import numpy as np

# 读取 PCD 文件
pcd = o3d.io.read_point_cloud("/home/aldno/data/BUPT/pointcloud_data/pcd/1702023208.100889000.pcd")
print(pcd)
# 检查是否有颜色信息
if len(pcd.colors) == 0:
    print("点云不包含颜色信息。")
else:
    print("点云包含颜色信息。")

    
# 将点云转换为 NumPy 数组
points = np.asarray(pcd.points)

# 检查点云数据的形状
print("Shape of the point cloud data:", points.shape)
# Shape of the point cloud data: (16128, 3)

# 创建一个坐标轴对象，大小可以根据您的点云数据进行调整
coordinate_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])

# 可视化点云和坐标轴
o3d.visualization.draw_geometries([pcd, coordinate_frame])
import numpy as np
import open3d as o3d

# 主要测试一下 .ply文件的基本操作

if __name__ == '__main__':
    print("test .ply files")
    pcd = o3d.io.read_point_cloud("/home/fc/Desktop/Open3D/examples/TestData/fragment.ply")
    print(pcd)
    print(np.asarray(pcd.points))
    # o3d.visualization.draw_geometries([pcd])        # 会显示一张图片

    print("test downsample")
    downpcd = pcd.voxel_down_sample(voxel_size=0.05)
    # o3d.visualization.draw_geometries([downpcd])    # 颜色变淡了

    print("recompute the normal value")
    downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
    o3d.visualization.draw_geometries([downpcd])       # 暂时看不出区别

    print("the normal vector of the 0th point")
    print(downpcd.normals[0])
    print("the first 10th points")
    print(np.asarray(downpcd.normals)[:10, :])
    print()

    # 切割一部分图片下来
    print("crop a image")
    vol = o3d.visualization.read_selection_polygon_volume("/home/fc/Desktop/Open3D/examples/TestData/Crop/cropped.json")
    chair = vol.crop_point_cloud(pcd)
    o3d.visualization.draw_geometries([chair])
    print("")

    # 画上颜色， RGB, 取值 [0, 1]
    print("paint chair")
    chair.paint_uniform_color([1, 0.706, 0])
    o3d.visualization.draw_geometries([chair])
    print("")




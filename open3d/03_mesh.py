import copy
import numpy as np
import open3d as o3d

if __name__ == '__main__':
    mesh = o3d.io.read_triangle_mesh("/home/fc/Desktop/Open3D/examples/TestData/knot.ply")
    print(mesh)
    print(np.asarray(mesh.vertices))
    print(np.asarray(mesh.triangles))

    # 一张没有任何颜色和明暗的图片
    print("show a mesh")
    print(mesh.has_vertex_normals())
    print(mesh.has_vertex_colors())
    o3d.visualization.draw_geometries([mesh])

    # 增加了明暗和纹理
    print("添加一些 normals")
    mesh.compute_vertex_normals()
    print(np.asarray(mesh.triangle_normals))
    o3d.visualization.draw_geometries([mesh])

    # 截取一部分
    mesh1 = copy.deepcopy(mesh)
    mesh1.triangles = o3d.utility.Vector3iVector(
        np.asarray(mesh1.triangles)[:len(mesh1.triangles) // 2, :]   # 这里是取一半的意思
    )
    mesh1.triangle_normals = o3d.utility.Vector3dVector(
        np.asarray(mesh1.triangle_normals)[:len(mesh1.triangle_normals) // 2, :]
    )
    print(mesh1.triangles)
    o3d.visualization.draw_geometries([mesh1])

    # 画上颜色
    mesh1.paint_uniform_color([1, 0.504, 0])
    o3d.visualization.draw_geometries([mesh1])






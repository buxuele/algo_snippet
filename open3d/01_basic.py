import open3d as o3d


def example_import_function():
    pcd = o3d.io.read_point_cloud("/home/fc/Desktop/Open3D/examples/TestData/ICP/cloud_bin_0.pcd")
    print(pcd)

    pcd2 = o3d.io.read_point_cloud("/home/fc/Desktop/Open3D/examples/TestData/fragment.pcd")
    o3d.io.write_point_cloud("new_pcd_file.pcd", pcd2)

    print("test IO for meshes")
    mesh = o3d.io.read_triangle_mesh("/home/fc/Desktop/Open3D/examples/TestData/knot.ply")
    print(mesh)
    o3d.io.write_triangle_mesh("new_mesh.ply", mesh)

    print("test IO for images")
    img = o3d.io.read_image("/home/fc/Desktop/Open3D/examples/TestData/lena_color.jpg")
    print(img)
    o3d.io.write_image("new_iamge.jpg", img)



def example_help_function():
    # help(o3d)
    help(o3d.geometry.PointCloud)
    # help(o3d.io.read_point_cloud)


if __name__ == '__main__':
    # example_help_function()
    example_import_function()
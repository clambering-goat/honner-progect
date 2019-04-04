# examples/Python/Tutorial/Basic/pointcloud.py

import numpy as np
from open3d  import *

if __name__ == "__main__":

    try:
        print("Load a ply point cloud, print it, and render it")
        pcd = read_point_cloud("point_cloud_out_old_working.xyz")
        print(pcd)
        print(np.asarray(pcd.points))
        draw_geometries([pcd])
    except:
        print("error in block 1")

    try:
        print("Load a ply point cloud, print it, and render it")
        pcd = read_point_cloud("p1.xyz")
        print(pcd)
        print(np.asarray(pcd.points))
        draw_geometries([pcd])
    except:
        print("error in block 1")

    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = voxel_down_sample(pcd, voxel_size = 0.05)
    draw_geometries([downpcd])

    print("Recompute the normal of the downsampled point cloud")
    estimate_normals(downpcd, search_param = KDTreeSearchParamHybrid(
            radius = 0.1, max_nn = 30))
    draw_geometries([downpcd])

    print("Print a normal vector of the 0th point")
    print(downpcd.normals[0])
    print("Print the normal vectors of the first 10 points")
    print(np.asarray(downpcd.normals)[:10,:])
    print("")

    print("Load a polygon volume and use it to crop the original point cloud")
    vol = read_selection_polygon_volume("../../TestData/Crop/cropped.json")
    chair = vol.crop_point_cloud(pcd)
    draw_geometries([chair])
    print("")

    print("Paint chair")
    chair.paint_uniform_color([1, 0.706, 0])
    draw_geometries([chair])
    print("done")

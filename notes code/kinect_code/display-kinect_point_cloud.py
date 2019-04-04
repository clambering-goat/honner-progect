# examples/Python/Tutorial/Basic/pointcloud.py

import numpy as np
from open3d  import *

try:
    print("Load a ply point cloud, print it, and render it")
    pcd = read_point_cloud("kinect_point_cloud.xyz")
    print(pcd)
    print(np.asarray(pcd.points))
    draw_geometries([pcd])
except:
    print("error in block 1")

#!/usr/bin/python
# -*- encoding: utf-8 -*-

import numpy as np
from glob import glob
import open3d as o3d

if __name__ == "__main__":    

    # TODO1. Write your bin file path
    bin_path = glob("PATH/TO/YOUR/FILE/XXX.bin")
    
    root_path = bin_path[0]
    bin_pcd = np.fromfile(root_path, dtype=np.float32)

    # TODO2. Write your bin file shape
    # If your bin file is (N, 4), you can use this code
    # But if your bin file is (N, 5), you should change this code with
    # points = (bin_pcd.reshape((-1, 5))[:, 0:3])
    points = bin_pcd.reshape((-1, 4))[:, 0:3]

    visualize_points = points[:,:3]
    o3d_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(visualize_points))
    o3d.visualization.draw_geometries([o3d_pcd])
#!/usr/bin/python
# -*- encoding: utf-8 -*-

import numpy as np
from glob import glob
import open3d as o3d

if __name__ == "__main__":       
    
    # TODO1. Write your pcd file path
    pcd_file_path = "path/to/your/file.pcd"

    point_cloud = o3d.io.read_point_cloud(pcd_file_path)

    o3d.visualization.draw_geometries([point_cloud])
# A python file to visualize LiDAR pointcloud bin file using open3d #
**You just need to modify the .reshape function to match the shape of the point cloud!**
```
    Things to change to visualize .bin file!

    # TODO1. Write your bin file path
    bin_path = glob("PATH/TO/YOUR/FILE/XXX.bin")

    # TODO2. Write your bin file shape
    # If your bin file is (N, 4), you can use this code
    # But if your bin file is (N, 5), you should change this code with
    # points = (bin_pcd.reshape((-1, 5))[:, 0:3])
    points = bin_pcd.reshape((-1, 4))[:, 0:3]
```

---------------------------------------
**IN PROGRESS**
1. ADD origin coordinate
2. ASSIGN colors to all point clouds based on semantic their labels
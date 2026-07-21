![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Python](https://img.shields.io/badge/Python-3.10-yellow)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-red)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![Intel RealSense](https://img.shields.io/badge/Intel-RealSense-blueviolet)

# Object Detection and Depth Estimation using Intel RealSense D435i (ROS 2 + YOLOv8)

A real-time perception system that combines Intel RealSense D435i, ROS 2 Humble, YOLOv8, OpenCV, and RViz2 to perform object detection together with depth estimation.

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#demo">Demo</a>
- <a href="#problem-statement">Problem Statement</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#result">Result</a>
- <a href="#deployment">Deployment</a>
- <a href="#future-work">Future Work</a>
- <a href="#methodology">Methodology</a>

---

<h3 id="demo">Demo</h3>

<!-- Demo GIF -->
demo.gif

<!-- Screenshots -->

---

<h3 id="overview">Overview</h3>

A real-time perception system that combines Intel RealSense D435i, ROS 2 Humble, YOLOv8, OpenCV, and RViz2 to perform object detection together with depth estimation. Each detected object is identified using YOLOv8, while its distance from the camera is calculated using aligned depth data from the RealSense depth sensor.

**Features:**
- Real-time object detection using YOLOv8
- Depth estimation for every detected object
- Intel RealSense D435i RGB-D camera integration
- ROS 2 Humble implementation
- Live PointCloud visualization in RViz2
- Custom ROS2 Python package
- ROS Launch file for simplified execution
- Modular ROS node architecture

**Project Architecture:**
```
Intel RealSense D435i
        │
        ▼
RGB Image + Depth Image
        │
        ▼
ROS2 Topics
        │
        ▼
Custom Python Node
        │
        ├── YOLOv8 Detection
        ├── Depth Extraction
        └── Distance Calculation
        │
        ▼
OpenCV Visualization
        │
        ▼
Bounding Box + Class + Distance
```

**Package Structure:**
```
realsense_yolo/

├── package.xml
├── setup.py
├── realsense_yolo/
│      realsense_yolo_node.py
└── launch/
       realsense_yolo_launch.py
```

---

<h3 id="problem-statement">Problem Statement</h3>

---

<h3 id="tools--technologies">Tools & Technologies</h3>

| Category | Tools Used |
|----------|------------|
| Framework | ROS 2 Humble |
| Hardware | Intel RealSense D435i |
| Computer Vision | YOLOv8, OpenCV |
| Language | Python |
| Visualization | RViz2 |
| Libraries | CV Bridge, rclpy |

---

<h3 id="result">Result</h3>

The system provides:
- Real-time object detection
- Object class labels
- Bounding boxes
- Depth estimation
- Live PointCloud
- ROS visualization through RViz2

---

<h3 id="deployment">Deployment</h3>

### Install Dependencies

```bash
git clone https://github.com/yourusername/realsense-yolo-depth-estimation.git
cd realsense-yolo-depth-estimation
```

### Additional Setup

```bash
colcon build
source install/setup.bash
```

### Run Project

Terminal 1 - Launch RealSense Camera:
```bash
ros2 launch realsense2_camera rs_launch.py
ros2 launch realsense2_camera rs_launch.py pointcloud.enable:=true
```

Terminal 2 - Run YOLO Node:
```bash
ros2 run realsense_yolo realsense_yolo_node
ros2 launch realsense_yolo realsense_yolo_launch.py
```

Terminal 3 - Open RViz2:
```bash
rviz2
```

Add PointCloud2 Topic: `/camera/depth/color/points`

ROS Topics subscribed to:
```
/camera/color/image_raw
/camera/depth/image_rect_raw
```

---

<h3 id="future-work">Future Work</h3>

- Multi-object tracking
- SLAM integration
- Navigation stack
- GPU acceleration
- Jetson deployment
- Object pose estimation
- 3D bounding boxes

---

<h3 id="methodology">Methodology</h3>

```text
Intel RealSense D435i
        │
        ▼
RGB Image + Depth Image
        │
        ▼
ROS2 Topics
        │
        ▼
Custom Python Node
        │
        ├── YOLOv8 Detection
        ├── Depth Extraction
        └── Distance Calculation
        │
        ▼
OpenCV Visualization
        │
        ▼
Bounding Box + Class + Distance
```

---

## Screenshots

1️⃣ **Package Structure**

Filename: `package_structure.png`

Caption: Custom ROS 2 package structure containing the Python node and launch file used for real-time object detection and depth estimation.

---

2️⃣ **RQT Graph**

Filename: `rqt_graph.png`

Caption: ROS 2 communication graph illustrating the interaction between the RealSense camera node, published topics, RViz2, TF frames, and the custom YOLO node.

---

3️⃣ **Launch File**

Filename: `launch_file.png`

Caption: Custom ROS 2 launch file used to start the realsense_yolo_node with predefined configurations.

---

4️⃣ **Python Node**

Filename: `code_snippet.png`

Caption: Implementation of the custom ROS 2 Python node integrating YOLOv8 object detection with RealSense depth estimation.

---

5️⃣ **RViz PointCloud**

Filename: `pointcloud_rviz.png`

Caption: Live 3D PointCloud visualization generated from the Intel RealSense D435i depth camera in RViz2.

---

6️⃣ **RViz Topic Selection**

Filename: `pointcloud_topic.png`

Caption: RViz2 configuration showing the PointCloud2 display subscribed to the /camera/depth/color/points topic.

---

7️⃣ **Detection Output**
<img width="682" height="317" alt="Image" src="https://github.com/user-attachments/assets/4678580c-e0dc-45d2-9b7b-9b05d3b54ec1" />

<img width="682" height="317" alt="Image" src="https://github.com/user-attachments/assets/c27792b6-3138-46be-a781-15c4aa5e672d" />

Caption: Real-time object detection using YOLOv8 with estimated object distance overlaid using aligned depth information.


## Git Commands (if you've forgotten)

```bash
# Initialize repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Create GitHub repository (via GitHub website)

# Connect local repository to GitHub
git remote add origin https://github.com/<username>/realsense-yolo-depth-estimation.git

# Push
git branch -M main
git push -u origin main
```

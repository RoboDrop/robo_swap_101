# SO-101 Robot View

Local interactive viewer with the official SO-101 follower and leader descriptions, STL meshes, six joint sliders, orbit/pan/zoom, demo motion, wireframe, and joint frames. This does not connect to or move hardware.

Install Node.js 22.12+ (or a current LTS release). From a fresh checkout, run:

```sh
git clone https://github.com/RoboDrop/robo_swap_101.git
cd robo_swap_101/robot_viewer
npm ci
npm run dev -- --port 5173
```

Open http://127.0.0.1:5173/. On this Mac, if the terminal resolves an older Node, use `/opt/homebrew/bin/node node_modules/vite/bin/vite.js --host 127.0.0.1 --port 5173`.

## Using the viewer

- Choose **SO-101 Follower** or **SO-101 Leader** from the robot menu.
- Drag the 3D view to orbit, right-drag to pan, and scroll to zoom.
- Move a joint slider to set its angle within the URDF limits.
- **Fit view** recenters the camera; **Zero pose** resets all joint angles.
- **Play motion** starts a sample animation; pause it or move a slider to stop.
- Enable wireframe, joint coordinate frames, or the ground grid under Display.
- **Download URDF** saves the selected description; copy its `assets/` folder too when loading it elsewhere.

Keep the terminal running while using the viewer; press Ctrl+C to stop the server.
If port 5173 is busy, Vite prints the alternate local URL to open.

## Production build

```sh
npm run build
npm run preview -- --port 5173
```

Open the URL printed in the terminal. The build creates a self-contained static site in `dist/`; serve it over HTTP instead of opening `index.html` directly. No ROS installation is required.

## Robot description

`public/robots/so101/so101_new_calib.urdf` is the default follower model. `so101_leader_new_calib.urdf` provides the leader. Keep `assets/` next to the URDF. The directory also retains the upstream old-calibration, camera, and MuJoCo descriptions.

Source: https://github.com/TheRobotStudio/SO-ARM100/tree/main/Simulation/SO101

Pinned revision and source are recorded in `public/robots/so101/provenance.json`; upstream Apache-2.0 licensing is retained in `public/robots/so101/LICENSE`. Model files are unmodified.

New calibration places joint zero near the middle of joint travel. Joint controls use URDF angles in degrees; gripper angles do not map directly to LeRobot's 0–100 gripper units. The upstream leader trigger calibration is provisional. Motion is an illustrative animation, with no collision checking or hardware feedback.

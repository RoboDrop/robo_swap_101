# README media

These assets distinguish recorded hardware behavior from simulated motion. The main [Roboswap README](../../README.md) embeds the GIFs directly; the full video is stored here so it does not depend on Drive sharing permissions.

| File | Source and preparation |
| --- | --- |
| `roboswap-bench.jpg` | The bench photograph embedded on slide 5 of `oct25 studio45 hack presentation.pptx` (`ppt/media/image14.png`), resized and JPEG-compressed. |
| `teleoperation-demo.mp4` | The complete `IMG_9089.MOV` recording linked from slide 9, transcoded to H.264/AAC at 540 px wide with metadata removed. Duration approximately 44.7 seconds; original timing retained. |
| `teleoperation-demo.gif` | Seconds 8–18 of that recording, sampled at 8 fps and 280 px wide. Silent looping excerpt at original speed. |
| `coupling-simulation.gif` | A 10-second VTK render of the repository's actual v4 STL meshes, sampled at 16 fps. The receiver is translucent; the male follows the assembly transform in the v4 build script. No dynamics, forces, or physical validation are implied. |
| `sequence-simulation.gif` | Browser capture of Sequence Studio in simulation only, showing a three-position plan. The preview timeline is sampled across the approximately 5.64-second plan at its nominal timing. |
| `sequence-studio.jpg` | Full interface capture from the same isolated simulation session. |

Original hardware recording: [IMG_9089.MOV on Drive](https://drive.google.com/file/d/1_4_yJLBgcuWlU159tA-3w_Z1VML-Q9Xl/view).

The coupling uses [`male_SO101_flared_5mm_spacer.stl`](../../design/tool_swapper_v4_flared_pipette/cad/male_SO101_flared_5mm_spacer.stl) and [`female_flared_pipette_collar_31mm.stl`](../../design/tool_swapper_v4_flared_pipette/cad/female_flared_pipette_collar_31mm.stl). Placement follows `placed()` in the [build script](../../design/tool_swapper_v4_flared_pipette/build_design.py): translate the male by Z −13 mm, rotate locally by 0–45°, apply the −0.8–0 mm draw-in offset, rotate X by 180°, and translate to the receiver face at Z 27.65 mm. The animation includes an additional approach/withdrawal offset.

The Studio capture uses a temporary sequence library, with hardware disabled. Its illustrative poses, in `shoulder_pan / shoulder_lift / elbow_flex / wrist_flex / wrist_roll / gripper` order, are:

- Approach: `−25 / −15 / 20 / 20 / 0 / 35`
- Move to station: `25 / 20 / −10 / 30 / 30 / 35`
- Return: `0 / 0 / 0 / 0 / 0 / 35`

Each pose has a 0.3-second dwell. Speed is 45 units/s and acceleration is 90 units/s²; arm units are degrees and gripper units are percent. The plan starts at the model's home pose. These are demonstration poses, not a commissioned hardware tool-change sequence. The Studio visual uses its fitted v3 wrist mount; the separate coupling animation shows v4.

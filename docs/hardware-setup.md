# Hardware setup

[← Roboswap overview](../README.md)

Calibration, command-line teleoperation, and pipettor control for the recorded bench setup. For browser-based teaching and playback, see the [Sequence Studio guide](../robot_viewer/README.md).

Robot scripts can move hardware. Keep the workspace clear and support the follower when torque is disabled. The planner does not check collisions; software Stop is a hold command, not a physical emergency stop.

## Robot setup

The local robot environment used Python 3.12 and LeRobot 0.6.1. Create an isolated environment and install the robot dependencies:

```sh
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
source .venv/bin/activate
```

Before running hardware, identify your own serial devices and calibration IDs. Sequence Studio loads the role assignments in `arms.json`; these now match follower `5A7A055478` and leader `5A7A056103`. The standalone calibration and teleoperation scripts do **not** load `arms.json` automatically: update their hard-coded settings or CLI arguments separately. The CLI examples below describe the original bench setup.

Calibrate each arm with its motion area clear and the arm supported as needed:

```sh
python calibrate_arm.py leader
python calibrate_arm.py follower
```

Example teleoperation using the recorded macOS ports (replace them and the IDs for your hardware):

```sh
python teleoperate_arms.py \
  --robot.type=so101_follower \
  --robot.port=/dev/cu.usbmodem5A7A0547771 \
  --robot.id=so101_follower_5A7A054777 \
  --teleop.type=so101_leader \
  --teleop.port=/dev/cu.usbmodem5A680086601 \
  --teleop.id=so101_leader_5A68008660 \
  --fps=30 \
  --smooth-tau=0.06 --smooth-deadband=0.2 --smooth-speed=80
```

The launcher smooths position targets with a 60 ms low-pass time constant, a 0.2-unit deadband, and an 80-unit/second command speed limit. Units are LeRobot calibrated position units, not necessarily degrees. It starts targets at the observed follower position and uses the targets accepted by the follower for subsequent updates. After a loop stall, the speed allowance is capped at one 30 Hz frame to avoid a large catch-up step. Smoothing adds some response lag; increase `--smooth-tau` for stronger filtering or reduce it for quicker response. These options take effect when restarting the launcher. They cannot fix mechanical play, power problems, or servo oscillation while holding still.

The launcher retries configuration writes at least three times and supplies `--robot.max_relative_target` defaults of 10 for shoulder pan/lift, elbow flex, and wrist roll, and 20 for wrist flex and gripper. An explicit `--robot.max_relative_target` argument overrides these defaults. These limits do not establish collision safety.

For an instrumented run, use `diagnose_teleop.py` with the same robot/teleop arguments plus `--teleop_time_s=5` and an explicit `--robot.max_relative_target` setting. The diagnostic script waits three seconds before recording; despite its name, the duration comes from the CLI argument. It overwrites `diagnostics/loop.txt`, `diagnostics/teleop_5s.json`, and `diagnostics/teleop_5s.log`.

## VIAFLO pipettor terminal control

The imported Generation 3 controller provides identity/status, aspirate, dispense,
dry cycle, and purge through a terminal prompt. It currently verifies the existing
125 µL single-channel pipette (SN 07064070). On the pipette select **PC Control
(ComM)**, then run from this repository:

```sh
python3 viaflo_control.py build
python3 viaflo_control.py paired
python3 viaflo_control.py shell --address 00-16-a4-4c-9a-ac
```

Use `help` in the prompt. After physically verifying empty, `confirm-empty`
initializes the session's volume tracking; `cycle 5` performs a 5 µL dry test
with the tip out of liquid. `aspirate 10` and `dispense 10` command µL at speed 1.
See [setup, commands, and device limits](../tools/viaflo/README.md) before operating.
The native Bluetooth helper builds on macOS; serial support has a separate
`requirements-viaflo.txt`. No host network settings are changed.

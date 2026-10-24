"""Launch LeRobot with bounded retries for Feetech configuration writes."""
import sys
from lerobot.motors.feetech import FeetechMotorsBus
from lerobot.scripts.lerobot_teleoperate import main

_original_write = FeetechMotorsBus.write

def write_with_retries(self, data_name, motor, value, *, normalize=True, num_retry=0):
    return _original_write(
        self, data_name, motor, value,
        normalize=normalize, num_retry=max(num_retry, 3),
    )

if __name__ == '__main__':
    FeetechMotorsBus.write = write_with_retries
    if not any(arg.startswith('--robot.max_relative_target') for arg in sys.argv[1:]):
        sys.argv.append('--robot.max_relative_target={"shoulder_pan":10,"shoulder_lift":10,"elbow_flex":10,"wrist_flex":20,"wrist_roll":10,"gripper":20}')
    main()

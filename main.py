import time
import cozmo
from cozmo.objects import CustomObject
from cozmo.util import degrees, distance_mm, speed_mmps
from custom_map import CustomMap

def cozmo_program(robot: cozmo.robot.Robot):
    # réinitialisation des objets
    robot.world.delete_all_custom_objects()
    print(robot.pose.position)

    m = CustomMap(robot)

    # Stop 1
    robot.turn_in_place(degrees(-5)).wait_for_completed()
    robot.drive_straight(distance_mm(200), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-85)).wait_for_completed()

    # Stop 2
    robot.drive_straight(distance_mm(115), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    # Stop 3
    robot.drive_straight(distance_mm(275), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    # Stop 4
    robot.drive_straight(distance_mm(105), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-90)).wait_for_completed()

    # Stop 5
    robot.drive_straight(distance_mm(250), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(180)).wait_for_completed()

    # Stop 6
    robot.drive_straight(distance_mm(220), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()

    # Stop 7
    robot.drive_straight(distance_mm(130), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-45)).wait_for_completed()
    robot.drive_straight(distance_mm(135), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(-35)).wait_for_completed()

    # Stop 8
    robot.drive_straight(distance_mm(110), speed_mmps(50)).wait_for_completed()
    robot.turn_in_place(degrees(85)).wait_for_completed()

    while True:
        time.sleep(1)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)
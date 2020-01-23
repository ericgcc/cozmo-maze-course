import time
import cozmo
from cozmo.objects import CustomObject
from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    # réinitialisation des objets
    robot.world.delete_all_custom_objects()
    print(robot.pose.position)

    # Turn 1
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 2
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 3-4
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(900), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 5
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 6
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(600), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 7-9
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(900), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 10
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(600), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 11-12
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(600), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 13-14
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(900), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 15-16
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(600), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 17
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 18
    robot.turn_in_place(degrees(-90)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 19
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(300), speed_mmps(50), should_play_anim=True).wait_for_completed()

    # Turn 19
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(350), speed_mmps(50), should_play_anim=True).wait_for_completed()

    while True:
        time.sleep(1)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)
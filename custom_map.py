import cozmo
from cozmo.util import degrees, Pose

class CustomMap:

    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot
        self.stop_1 = Pose(695.86, 0, 0, angle_z=degrees(0))
        self.stop_2 = Pose(745, -700, 0, angle_z=degrees(0))
        self.stop_3 = Pose(225, -420, 0, angle_z=degrees(-90))
        self.stop_4 = Pose(150, 150, 0, angle_z=degrees(0))
        self.stop_5 = Pose(350, 550, 0, angle_z=degrees(-90))
        self.stop_6 = Pose(50, 350, 0, angle_z=degrees(180))
        self.stop_7 = Pose(0, 0, 0, angle_z=degrees(180))

        self.WALL_HEIGHT = 25.04  # mm
        self.WALL_WIDTH = 11.73  # mm

        self.create_walls()

    def create_walls(self):
        # --- VERTICAL WALLS ---
        vw1_center = Pose(422.82, 50, 0,  angle_z=degrees(0))
        vw1 = self.robot.world.create_custom_fixed_object(vw1_center, 845.65, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw2_center = Pose(353.89, -75.63, 0,  angle_z=degrees(0))
        vw2 = self.robot.world.create_custom_fixed_object(vw2_center, 107.8, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw3_center = Pose(48.56, -98.83, 0,  angle_z=degrees(0))
        vw3 = self.robot.world.create_custom_fixed_object(vw3_center, 97.61, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw4_center = Pose(246.22, -225, 0,  angle_z=degrees(0))
        vw4 = self.robot.world.create_custom_fixed_object(vw4_center, 100.71, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw5_center = Pose(120.87, -575, 0,  angle_z=degrees(0))
        vw5 = self.robot.world.create_custom_fixed_object(vw5_center, 195.811, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw6_center = Pose(441, -794.13, 0,  angle_z=degrees(0))
        vw6 = self.robot.world.create_custom_fixed_object(vw6_center, 828, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw7_center = Pose(696.66, -98.98, 0,  angle_z=degrees(0))
        vw7 = self.robot.world.create_custom_fixed_object(vw7_center, 274.52, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw8_center = Pose(639.69, -223.03, 0,  angle_z=degrees(0))
        vw8 = self.robot.world.create_custom_fixed_object(vw8_center, 160.60, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw9_center = Pose(570.86, -325, 0,  angle_z=degrees(0))
        vw9 = self.robot.world.create_custom_fixed_object(vw9_center, 333.38, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw10_center = Pose(571.26, -594.15, 0,  angle_z=degrees(0))
        vw10 = self.robot.world.create_custom_fixed_object(vw10_center, 73.101, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw11_center = Pose(796.33, -621.59, 0,  angle_z=degrees(0))
        vw11 = self.robot.world.create_custom_fixed_object(vw11_center, 98.64, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        # --- HORIZONTAL WALLS ---
        hw1_center = Pose(5.92, -449.65, 0,  angle_z=degrees(0))
        hw1 = self.robot.world.create_custom_fixed_object(hw1_center, self.WALL_WIDTH, 683.52, self.WALL_HEIGHT, relative_to_robot=True)

        hw2_center = Pose(91.80, -118.21, 0,  angle_z=degrees(0))
        hw2 = self.robot.world.create_custom_fixed_object(hw2_center, self.WALL_WIDTH, 27.03, self.WALL_HEIGHT, relative_to_robot=True)

        hw3_center = Pose(201.73, -398.6, 0,  angle_z=degrees(0))
        hw3 = self.robot.world.create_custom_fixed_object(hw3_center, self.WALL_WIDTH, 335.45, self.WALL_HEIGHT, relative_to_robot=True)

        hw4_center = Pose(302.08, -13.10, 0,  angle_z=degrees(0))
        hw4 = self.robot.world.create_custom_fixed_object(hw4_center, self.WALL_WIDTH, 114.52, self.WALL_HEIGHT, relative_to_robot=True)

        hw5_center = Pose(565.26, -160.93, 0,  angle_z=degrees(0))
        hw5 = self.robot.world.create_custom_fixed_object(hw5_center, self.WALL_WIDTH, 112.46, self.WALL_HEIGHT, relative_to_robot=True)

        hw6_center = Pose(714.63, -272.73, 0,  angle_z=degrees(0))
        hw6 = self.robot.world.create_custom_fixed_object(hw6_center, self.WALL_WIDTH, 87.67, self.WALL_HEIGHT, relative_to_robot=True)

        hw7_center = Pose(392.48, -429.3, 0,  angle_z=degrees(0))
        hw7 = self.robot.world.create_custom_fixed_object(hw7_center, self.WALL_WIDTH, 225.5, self.WALL_HEIGHT, relative_to_robot=True)

        hw8_center = Pose(540.58, -540.25, 0,  angle_z=degrees(0))
        hw8 = self.robot.world.create_custom_fixed_object(hw8_center, self.WALL_WIDTH, 96.06, self.WALL_HEIGHT, relative_to_robot=True)

        hw9_center = Pose(602.13, -694.14, 0,  angle_z=degrees(0))
        hw9 = self.robot.world.create_custom_fixed_object(hw9_center, self.WALL_WIDTH, 188.25, self.WALL_HEIGHT, relative_to_robot=True)

        hw10_center = Pose(839.8, -285.93, 0,  angle_z=degrees(0))
        hw10 = self.robot.world.create_custom_fixed_object(hw10_center, self.WALL_WIDTH, 660.17, self.WALL_HEIGHT, relative_to_robot=True)

        hw11_center = Pose(752.87, -596.05, 0,  angle_z=degrees(0))
        hw11 = self.robot.world.create_custom_fixed_object(hw11_center, self.WALL_WIDTH, 39.93, self.WALL_HEIGHT, relative_to_robot=True)


        # if None not in (wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14):
        #    print("fixed_objects created successfully")
        #    return (wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14)

        # print("An error occurred creating walls")
        # return None
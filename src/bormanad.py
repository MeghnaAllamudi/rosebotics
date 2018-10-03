"""
  Capstone Project.  Code written by Drew Borman.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    #run_test_go_stop()
    test_forward()


def run_test_go_stop():
    """ Tests the   go   and   stop   Snatch3rRobot methods. """
    robot = rb.Snatch3rRobot()

    robot.go(50, 25)
    time.sleep(2)
    robot.stop()

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
    robot.left_wheel.reset_degrees_spun(0)

    time.sleep(2)

    robot.go(100, 100)
    time.sleep(3)
    robot.stop(rb.StopAction.COAST.value)

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())


def forward(robot, n, x):
    robot = rb.Snatch3rRobot
    time_pass = time.time()
    delta_time = n
    robot.right_wheel.start_spinning(x)
    robot.left_wheel.start_spinning(x)
    while True:

        if time.time() >= time_pass + delta_time:
            break
            robot.right_wheel.stop_spinning()
            robot.left_wheel.stop_spinning()


def test_forward():
    "Tests forward function"
    robot = rb.Snatch3rRobot
    forward(robot, 10, 100)

main()

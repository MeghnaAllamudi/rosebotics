"""
  Capstone Project.  Code written by JUSTIN OGASAWARA.
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
    spin_test()


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

def spin(robot, N, X):

    time_pass = time.time()
    delta_time = N
    robot.right_wheel.start_spinning(X)
    robot.left_wheel.start_spinning(-X)
    while True:
        if time.time() >= time_pass + delta_time:
            break
    robot.right_wheel.stop_spinning()
    robot.left_wheel.stop_spinning()
def spin_test():
    robot = rb.Snatch3rRobot()
    spin(robot, 5,100)



main()

"""
  Capstone Project.  Code written by MeghnaAllamudi.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    #run_tests()
    run_tests()



def run_tests():
    """ Runs various tests. """
   # run_test_go_stop()
   turn_test()


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

def turn(n,x):
    robot = rb.Snatch3rRobot()
    time_start = time.time()
    deltatime = n
    while True:
        robot.left_wheel.start_spinning(x)
        robot.right_wheel.start_spinning(0)
        if time.time() == time_start() + deltatime:
            robot.left_wheel.stop_spinning()
            robot.right_wheel.stop_spinning()
    
def turn_test():
    robot = rb.Snatch3rRobot()
    turn(robot,20,20)


main()

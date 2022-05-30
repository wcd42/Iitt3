import sys
from PyQt6 import QtWidgets
from Iteration3.Course import Course
from Iteration3.ActiveSystem import ActiveSystem
from Controller.KU_Planner_login import MainWindowGUI
from Iteration3.mysqlcoursedao import MySQLCourseDAO

def main():

    # create a DAO (database access object)
    courseDAO = MySQLCourseDAO()

    ActiveSystem.set_dao(courseDAO)
    # set up the database (drop the existing table!)
    courseDAO.setup()
    # start a connection to the database
    # connect to the database
    courseDAO.connect()
    # list all entries (it should be empty)
    courseDAO.find_all()

    # add som test persons
    course1 = Course(1, "ku", "dev")
    ActiveSystem.add_course(course1)
    courseDAO.insert_course(course1)

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindowGUI()
    app.exec()

    print("The GUI is closed - printing the current employee table")
    courseDAO.find_all()

    allcourses = courseDAO.find_all()
    for emp in allcourses:
        print(emp)

    print("closing the database")
    print("take a look at the current state via MySQL workbench")

    courseDAO.close()
    print("goodbye")

if __name__ == '__main__':
    main()
from PyQt6 import QtWidgets, uic
from Iteration3.Course import Course
from Iteration3.ActiveSystem import ActiveSystem


class SubmitCourseGUI(QtWidgets.QWidget):
    def __init__(self):
        super(SubmitCourseGUI, self).__init__()
        uic.loadUi('/Users/williamdevlin/PycharmProjects/pythonProject7/Controller/KU_Planner_submitcourse.ui', self)

        self.pushButtonOK.clicked.connect(self.ok_button_pressed)
        self.pushButtonClear.clicked.connect(self.clear_button_pressed)
        self.pushButtonCancel.clicked.connect(self.cancel_button_pressed)

        self.show()

    def ok_button_pressed(self):

        coursename = self.firstNameLineEdit.text()
        faculty = self.lastNameLineEdit.text()
        courseID = self.cPRNumberLineEdit.text()

        try:
            course = Course(coursename, faculty, courseID)

            print("Course:", course)

            # Let us update the list off employees and print it

            ActiveSystem.add_course(course)
            coursedao = ActiveSystem.get_dao()
            coursedao.insert_course(course)

        except Exception as e:
            print("Arrgh! Something went wrong!!", e)
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Input error")
            msg.setText("Badly formatted input!")
            msg.setDetailedText(str(e))
            msg.exec()
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            # Loop over the fields and clear them
            for field in line_edits:
                field.clear()

        print("-" * 30 + "\nThe Model has the following courses")
        for e in ActiveSystem.get_course_list():
            print(e)

        print("-" * 30 + "\nModel has the active course ")
        print(ActiveSystem.get_current_course())

    def clear_button_pressed(self):

        button = QtWidgets.QMessageBox.question(self, "Clear fields", "All input fields will be cleared")

        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            for field in line_edits:
                field.clear()
        else:
            print("No!")

    def cancel_button_pressed(self):

        button = QtWidgets.QMessageBox.question(self, "Exit form?", "Are you done entering employees?")

        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")
            print(type(self.parent()))
            if type(self.parent()) == QtWidgets.QStackedWidget:
                self.parent().setCurrentIndex(0)
            self.close()  # This will close Widget

        else:
            print("No!")


from PyQt6 import QtWidgets, uic
from Iteration3.ActiveSystem import Course
from Iteration3.ActiveSystem import ActiveSystem


class SearchCourseGUI(QtWidgets.QWidget):

    search_course: Course = None

    def __init__(self):
        super(SearchCourseGUI, self).__init__()
        uic.loadUi('/Users/williamdevlin/PycharmProjects/pythonProject7/Controller/KU_Planner_courserequests.ui', self)

        self.pushButtonSearch.clicked.connect(self.search_button_pressed)
        self.pushButtonOK.clicked.connect(self.ok_button_pressed)
        self.pushButtonClear.clicked.connect(self.clear_button_pressed)

        self.show()

    def search_button_pressed(self):
        search_id = self.courseidLineEdit.text()
        print("Search cpr:", search_id)

        for e in ActiveSystem.get_course_list():
            print(e.get_course_id())
            if e.get_course_id() == search_id:
                self.coursenameLineEdit.setText(e.get_course_name())
                self.facultyLineEdit.setText(e.get_faculty())
                self.courseidLineEdit_2.setText(e.get_course_id())
                self.search_course = e
                print("search_course: ", self.search_course)
                break


    def ok_button_pressed(self):
        # This is executed when the OK button is pressed
        # Let us set the current person to be the one we looked up

        print("OK button pressed!")

        print("search_employee at OK: ", self.search_course)

        if self.search_course is not None:
            ActiveSystem.set_current_course(self.search_course)

        # You could create an alert message here stating if no employee was found

        print("-" * 30 + "\nThe Model has the following courses")
        for e in ActiveSystem.get_course_list():
            print(e)

        print("-" * 30 + "\nModel has the active course ")
        print(ActiveSystem.get_current_course())

        # If started from the stacked widget we want to return to the default window:
        if type(self.parent()) == QtWidgets.QStackedWidget:
            self.parent().setCurrentIndex(0)

        self.close()

    def clear_button_pressed(self):

        print('Clear button pressed!')

        button = QtWidgets.QMessageBox.question(self, "Clear fields", "All input fields will be cleared")

        if button == QtWidgets.QMessageBox.StandardButton.Yes:
            print("Yes!")
            self.course_employee = None
            # Find all fields of type QLineEdit
            line_edits = self.findChildren(QtWidgets.QLineEdit)
            # Loop over the fields and clear them
            for field in line_edits:
                field.clear()
        else:
            print("No!")

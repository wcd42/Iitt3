from PyQt6 import QtWidgets, uic

from Controller.KU_Planner_submitcourse import SubmitCourseGUI

from Controller.KU_Planner_courserequests import SearchCourseGUI


class MainWindowGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindowGUI, self).__init__()
        uic.loadUi('/Users/williamdevlin/PycharmProjects/pythonProject7/Controller/KU_Planner_login.ui', self)

        # Keep the space in the GUI when a widget is hidden, so that the window doesn't
        # get garbled

        not_resize = self.stackedWidget.sizePolicy()
        not_resize.setRetainSizeWhenHidden(True)
        self.stackedWidget.setSizePolicy(not_resize)

        # instantiate the widgets for adding and searching employees
        self.new_emp_gui = SubmitCourseGUI()
        self.search_emp_gui = SearchCourseGUI()

        # instantiate a widget for "default" window

        # Now add the defined widgets to the stackedWidget
        self.stackedWidget.addWidget(self.new_emp_gui)
        self.stackedWidget.addWidget(self.search_emp_gui)

        # Menubar actions
        self.actionAdd_Course.triggered.connect(self.start_add_employee)
        self.actionSearch_C.triggered.connect(self.start_search_employee)

        # combobox actions
        self.comboBox.activated.connect(self.activated)
        self.stackedWidget.setCurrentIndex(0)
        self.show()

    def start_add_employee(self):
        print("start_add_employee")
        self.stackedWidget.setCurrentIndex(1)

    def start_search_employee(self):
        print("start_search_employee")
        self.stackedWidget.setCurrentIndex(2)

    def activated(self, index):
        """
        controller for the combobox menu
        It will launch and instance of the NewEmployeeGUI og the SearchEmployeeGUI
        """

        print(index)
        if index == 1:
            self.w = SubmitCourseGUI()
            self.w.show()

        if index == 2:
            self.w2 = SearchCourseGUI()
            self.w2.show()
class Course:

    def __init__(self, course_id: int, faculty: str, course_name: str):
        self.__course_id: int = course_id
        self.__faculty: str = faculty
        self.__course_name: str = course_name


    def __str__(self):
        return f"Course ID: {str(self.__course_id)}, Faculty: {str(self.__faculty)} Course name: {str(self.__course_name)}"

    def get_course_id(self):
        return self.__course_id

    def set_faculty(self, new_faculty: str):
        self.__faculty = new_faculty

    def get_faculty(self):
        return self.__faculty

    def get_course_id(self):
        return self.__course_id

    def set_course_id(self, new_course_id: int):
        self.__course_id = new_course_id

    def get_course_name(self):
        return self.__course_name

    def set_course_name(self, new_course_name: str):
        self.__course_name = new_course_name

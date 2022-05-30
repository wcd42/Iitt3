from Iteration3.Course import Course
from mysql1.DAO_MySQL import DAO_MySQL

class ActiveSystem(object):

    list_courses: [Course] = []
    current_course: Course = None
    dao: DAO_MySQL = None

    @classmethod
    def add_course(cls, e):
        cls.list_courses.append(e)

    @classmethod
    def set_current_course(cls, c):
        cls.current_course = c

    @classmethod
    def get_current_course(cls):
        return cls.current_course

    @classmethod
    def get_course_list(cls):
        return cls.list_courses

    @classmethod
    def set_dao(cls, dao):
        cls.dao = dao

    @classmethod
    def get_dao(cls):
        return cls.dao
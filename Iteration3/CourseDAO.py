from abc import abstractmethod
from Iteration3.DAO import DAO
from Iteration3.Course import Course
from typing import List
from Iteration3.CourseSearchType import CourseSearchType


class CourseDAO(DAO):

    @abstractmethod
    def insert_course(self, course: Course):
        pass

    @abstractmethod
    def update_course(self, course: Course) -> bool:
        pass

    @abstractmethod
    def delete_course(self, course: Course) -> bool:
        pass

    @abstractmethod
    def find_course_by_property(self, search_type: CourseSearchType, value: object) -> List[Course]:
        pass

    @abstractmethod
    def find_all(self) -> List[Course]:
        pass
from enum import unique, Enum


@unique
class CourseSearchType(Enum):
    """
    Class for enumerating course languages
    """

    IDCOURSE = 1
    FACULTY = 2
    COURSENAME = 3


from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups):
    if not groups:
        with open("groups.pickle", "wb") as file:
            pickle.dump(groups, file)
        return 0

    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students):
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information():
    try:
        with open("groups.pickle", "rb") as file:
            groups = pickle.load(file)
            specialty_names = set(group.specialty.name for group in groups)
            return list(specialty_names)
    except FileNotFoundError:
        return []


def read_students_information():
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)
            return students
    except FileNotFoundError:
        return []

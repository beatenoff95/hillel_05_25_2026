from __future__ import annotations

import random
from pathlib import Path

from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'students.db'}"


class Base(DeclarativeBase):
    pass


class Enrollment(Base):
    __tablename__ = "enrollments"

    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
        primary_key=True,
    )
    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id", ondelete="CASCADE"),
        primary_key=True,
    )


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120), unique=True)

    courses: Mapped[list[Course]] = relationship(
        secondary="enrollments",
        back_populates="students",
    )

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name='{self.first_name} {self.last_name}')"


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True)
    teacher: Mapped[str] = mapped_column(String(100))

    students: Mapped[list[Student]] = relationship(
        secondary="enrollments",
        back_populates="courses",
    )

    def __repr__(self) -> str:
        return f"Course(id={self.id}, title='{self.title}')"


def create_tables(engine) -> None:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def seed_data(session: Session) -> None:
    courses = [
        Course(title="Python Basic", teacher="Olena Kovalenko"),
        Course(title="Databases", teacher="Andrii Shevchenko"),
        Course(title="Web Development", teacher="Iryna Bondar"),
        Course(title="QA Automation", teacher="Dmytro Melnyk"),
        Course(title="Data Analysis", teacher="Natalia Tkachenko"),
    ]
    session.add_all(courses)
    session.flush()

    first_names = [
        "Ivan",
        "Olena",
        "Petro",
        "Iryna",
        "Dmytro",
        "Sofia",
        "Andrii",
        "Nazar",
        "Kateryna",
        "Maksym",
        "Anna",
        "Bohdan",
        "Viktoria",
        "Roman",
        "Yuliia",
        "Artem",
        "Maria",
        "Oleksandr",
        "Anastasiia",
        "Taras",
    ]
    last_names = [
        "Ivanenko",
        "Petrenko",
        "Shevchenko",
        "Kovalenko",
        "Bondarenko",
        "Tkachenko",
        "Melnyk",
        "Kravchenko",
        "Boyko",
        "Savchenko",
        "Polishchuk",
        "Rudenko",
        "Moroz",
        "Lysenko",
        "Marchenko",
        "Pavlenko",
        "Oliinyk",
        "Hrytsenko",
        "Kozak",
        "Tkachuk",
    ]

    random.seed(21)
    students = []
    for index, (first_name, last_name) in enumerate(zip(first_names, last_names), start=1):
        student = Student(
            first_name=first_name,
            last_name=last_name,
            email=f"student{index}@example.com",
        )
        student.courses = random.sample(courses, k=random.randint(1, 3))
        students.append(student)

    session.add_all(students)
    session.commit()


def add_student_to_course(
    session: Session,
    first_name: str,
    last_name: str,
    email: str,
    course_title: str,
) -> Student:
    course = session.scalar(select(Course).where(Course.title == course_title))
    if course is None:
        raise ValueError(f"Course '{course_title}' does not exist.")

    student = session.scalar(select(Student).where(Student.email == email))
    if student is None:
        student = Student(first_name=first_name, last_name=last_name, email=email)
        session.add(student)

    if course not in student.courses:
        student.courses.append(course)

    session.commit()
    session.refresh(student)
    return student


def get_students_by_course(session: Session, course_title: str) -> list[Student]:
    return list(
        session.scalars(
            select(Student)
            .join(Student.courses)
            .where(Course.title == course_title)
            .order_by(Student.last_name, Student.first_name)
        )
    )


def get_courses_by_student(session: Session, email: str) -> list[Course]:
    return list(
        session.scalars(
            select(Course)
            .join(Course.students)
            .where(Student.email == email)
            .order_by(Course.title)
        )
    )


def update_student_email(session: Session, student_id: int, new_email: str) -> Student:
    student = session.get(Student, student_id)
    if student is None:
        raise ValueError(f"Student with id={student_id} does not exist.")

    student.email = new_email
    session.commit()
    session.refresh(student)
    return student


def update_course_teacher(session: Session, course_title: str, new_teacher: str) -> Course:
    course = session.scalar(select(Course).where(Course.title == course_title))
    if course is None:
        raise ValueError(f"Course '{course_title}' does not exist.")

    course.teacher = new_teacher
    session.commit()
    session.refresh(course)
    return course


def delete_student(session: Session, email: str) -> bool:
    student = session.scalar(select(Student).where(Student.email == email))
    if student is None:
        return False

    session.delete(student)
    session.commit()
    return True


def print_student_courses(session: Session, email: str) -> None:
    courses = get_courses_by_student(session, email)
    print(f"Courses for {email}:")
    for course in courses:
        print(f"- {course.title} ({course.teacher})")


def print_course_students(session: Session, course_title: str) -> None:
    students = get_students_by_course(session, course_title)
    print(f"Students on course '{course_title}':")
    for student in students:
        print(f"- {student.first_name} {student.last_name}, {student.email}")


def main() -> None:
    engine = create_engine(DATABASE_URL, echo=False)
    create_tables(engine)

    with Session(engine) as session:
        seed_data(session)

        print("Initial data: 5 courses and 20 randomly enrolled students were created.\n")

        new_student = add_student_to_course(
            session=session,
            first_name="Yevhen",
            last_name="Vyshnevskyi",
            email="yevhen.vyshnevskyi@example.com",
            course_title="Databases",
        )
        print(f"Added student: {new_student}\n")

        print_course_students(session, "Databases")
        print()

        print_student_courses(session, "yevhen.vyshnevskyi@example.com")
        print()

        updated_student = update_student_email(
            session,
            student_id=new_student.id,
            new_email="yevhen.updated@example.com",
        )
        print(f"Updated student email: {updated_student.email}")

        updated_course = update_course_teacher(
            session,
            course_title="Databases",
            new_teacher="Serhii Database",
        )
        print(f"Updated course teacher: {updated_course.title} - {updated_course.teacher}")

        was_deleted = delete_student(session, "yevhen.updated@example.com")
        print(f"Deleted updated student: {was_deleted}")

        deleted_student_courses = get_courses_by_student(session, "yevhen.updated@example.com")
        print(f"Courses for deleted student: {deleted_student_courses}")


if __name__ == "__main__":
    main()

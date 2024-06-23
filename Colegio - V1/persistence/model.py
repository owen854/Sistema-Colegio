from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Tabla de asociación entre estudiantes y cursos
student_course = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Tabla de asociación entre profesores y asignaturas
teacher_subject = Table('teacher_subject', Base.metadata,
    Column('teacher_id', Integer, ForeignKey('teachers.id')),
    Column('subject_id', Integer, ForeignKey('subjects.id'))
)

class Auth_User(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150))
    password = Column(String(128))
    role = Column(String(50), nullable=False)
    id_user = Column(String(6), nullable=False, unique=True)

    def __repr__(self):
        return f'AuthUser({self.username}, {self.password})'

    def __str__(self):
        return self.username

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    courses = relationship('Course', secondary=student_course, back_populates='students')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    subjects = relationship('Subject', secondary=teacher_subject, back_populates='teachers')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    teachers = relationship('Teacher', secondary=teacher_subject, back_populates='subjects')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='courses')
    students = relationship('Student', secondary=student_course, back_populates='courses')
    evaluations = relationship('Evaluation', back_populates='course')
    schedule = relationship('Schedule', uselist=False, back_populates='course')

class Evaluation(Base):
    __tablename__ = 'evaluations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer)
    course_id = Column(Integer, ForeignKey('courses.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    course = relationship('Course', back_populates='evaluations')
    student = relationship('Student', back_populates='evaluations')

class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    day = Column(String(20))
    time = Column(String(20))
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='schedule')

# Relaciones inversas para algunas clases
Teacher.courses = relationship('Course', back_populates='teacher')
Student.evaluations = relationship('Evaluation', back_populates='student')

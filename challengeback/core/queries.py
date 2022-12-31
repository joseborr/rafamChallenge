from models import Friendship,Student,Lesson

def sign_up_course(student,lesson):
    '''sign up a student for a course'''
    lesson.students.add(student)

def accept_friendship(student_sender,student_receiver)->Friendship:
    ''''the student sender creates a friendship with student receiver which is returned'''
    friendship = Friendship()
    friendship.save()
    friendship.friends.add(student_sender,student_receiver)

    return friendship

def list_all_students():
    '''list of all students in system'''
    return Student.objects.all()

def list_lessons_from_student(student:Student):
    return Lesson.objects.filter(students__username = student.username)

def student_is_unique(student:Student):
    return Student.objects.filter(username = student.username) == None




from core.models import Friendship,Student,Lesson

def sign_up_course(student,lesson):
    '''sign up a student for a course'''
    lesson.students.add(student)

def accept_friendship(student_sender,student_receiver)->Friendship:
    ''''the student sender creates a friendship with student receiver which is returned'''

    if student_sender.id == student_receiver.id:
        return None
    if frienship_exists(student_sender,student_receiver):
        return None
    friendship = Friendship()
    friendship.save()
    friendship.friends.add(student_sender,student_receiver)

    return friendship

def list_all_students():
    '''list of all students in system'''
    return Student.objects.all()

def list_lessons_from_student(student:Student):
    '''list lessons taken by a student'''
    return Lesson.objects.filter(students__username = student.username)

def student_is_unique(student:Student):
    '''returns if a student already exists'''
    return Student.objects.filter(username = student.username) == None

def list_all_lessons():
    '''list all lessons'''
    return Lesson.objects.all()

def list_student_friends(id):
    '''return the list of friends from the student's id provided'''

    frienships = Friendship.objects.filter(friends = id)
    friends = []
    student = get_student_by_id(id)
    for friendship in frienships:
        for friend in friendship.friends.all():
            if friend.username != student.username:
                friends.append(friend)
    return friends

def get_student_by_id(id):
    return Student.objects.get(pk=id)

def frienship_exists(student_sender,student_receiver):
    frienships = Friendship.objects.all()
    friends = [student_sender,student_receiver]
    for single_friendship in frienships:
        if (single_friendship.friends.all()[0] in friends 
                            and single_friendship.friends.all()[1] in friends):
            return True
    return False

def list_all_friendships():
    return Friendship.objects.all()


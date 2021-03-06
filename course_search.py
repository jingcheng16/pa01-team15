'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''


from schedule import Schedule


schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
independent (filter by whether the course is a independent study)
coinstructor (filter by subject and whether the course has coinstructor)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['c','course']:
            code = input("enter a code:")
            schedule = schedule.code([code])
        elif command in ['i','instructor']:
            instructor = input("enter instructor last name or email:")
            schedule = schedule.instructor([instructor])
        elif command in ['l','title']:
            phrase = input("enter a phrase of the course title:")
            schedule = schedule.title([phrase])
        elif command in ['d','description']:
            phrase = input("enter a phrase of the course description:")
            schedule = schedule.description([phrase])
        elif command in ['n','independent']:
            subject = input("enter a subject")
            schedule = schedule.independent_course([subject])
        elif command in ['cn', 'coursenum']:
            phrase = input('enter a coursenum:')
            schedule = schedule.coursenum([phrase])
        elif command in ['d','detail']:
            detail = input("enter a detail")
            schedule = schedule.detail([detail])
        elif command in ['co','coinstructor']:
            subject = input("enter a subject to find the courses have coinstructor in the subject:")
            schedule = schedule.coinstructor([subject])
        elif command in ['type']:
            phrase = input("enter a type:")
            schedule = schedule.type([phrase])
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)
def print_course(course):
    '''
    print_course prints a brief description of the course
    print_course prints a brief description of the course // test for video
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

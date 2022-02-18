'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json
import re

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        ''' sort function sort the courses by their subjects'''
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        print("can't sort by "+str(field)+" yet")
        return self

    def title(self, phrase):
        '''title filters the courses by phrase entered by user'''
        return Schedule([course for course in self.courses if re.search(phrase[0],course['name'])])

    def description(self, phrase):
        '''description filters the courses by phrase entered by user'''
        return Schedule([course for course in self.courses if re.search(phrase[0],course['description'])])

    def independent_course(self, subject):
        '''independent_course filters the courses by if the course is independent study'''
        return Schedule([course for course in self.courses if course['subject'] in subject and course['independent_study'] is True])

    def code(self, codes):
        '''code filters the courses by code entered by user'''
        if re.search(" ",codes[0]):
            return Schedule([course for course in self.courses if re.search(course['subject'], codes[0]) and re.search(course['coursenum'], codes[0])])
        return Schedule([course for course in self.courses if course['code'][0] in codes or course['code'][1] in codes])

    def instructor(self, instructor):
        '''instructor filters the courses by instructor's name and email'''
        if len(self.lastname(instructor).courses) > 0:
            return self.lastname(instructor)
        return self.email(instructor)

    def coursenum(self, phrase):
        '''coursenum filters the courses by its coursenum'''
        return Schedule([course for course in self.courses if re.search(phrase[0],course['coursenum'])])

    def detail(self, detail):
        '''course filters the courses by details'''
        return Schedule([course for course in self.courses if re.search(detail[0],course['details'])])

    def type(self, phrase):
        '''type filters the courses by types'''
        return Schedule([course for course in self.courses if re.search(phrase[0], course["type"])])

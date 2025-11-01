class Journal:
    
    
    def __init__(self, klass):
        self.klass = klass
        self.class_journal = {}

    
    def add_student(self, students):
        for i in range(len(students)):
            
            self.class_journal[students[i]] = {}
        
    
    def add_subjects(self, subject):
        for student in self.class_journal:
            self.class_journal[student][subject] = []


    def rate_students(self, student, subject, mark):
        self.class_journal[student][subject].append(mark)
    

    def print_statistics(self, student, subject):
        print(self.class_journal[student][subject])
    

    def print_middle(self, student, subject):
        print(round(sum(self.class_journal[student][subject]) / len(self.class_journal[student][subject]), 2))

        
    def test(self):
        print(self.class_journal)
    
    
    
clas1=Journal('10-I')
clas1.add_student(['Пётр Васин', 'Вовочка', 'Антон'])
clas1.add_subjects('Английский язык')
clas1.add_subjects('Программирование')

clas1.rate_students('Вовочка', 'Программирование', 4)
clas1.rate_students('Вовочка', 'Программирование', 5)
clas1.rate_students('Вовочка', 'Программирование', 3)
clas1.rate_students('Вовочка', 'Программирование', 5)
clas1.rate_students('Вовочка', 'Программирование', 5)
clas1.rate_students('Вовочка', 'Программирование', 1)

clas1.print_statistics('Вовочка', 'Программирование')
clas1.print_middle('Вовочка', 'Программирование')



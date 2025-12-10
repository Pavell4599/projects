import random as rd 


class Puppy:
    def __init__(self, index):
        self.index = index
        self.states = ['идеальное здоровье', 'нормальное здоровье', 'допустимое здоровье', 'предболезненнное состояние', 'болеет']
        self.state = rd.randint(0, 4)
        
   
    def get_treatment(self):
        if self.state != 0:
            self.state -= 1
            
            
    def is_healthy(self):
        if self.state == 0:
            print('Да, щенок здоров.')
        else:
            print('Щенок не здоров.')
            
        
class Dog:
    def __init__(self, dogs_count):
        self.dogs_count = dogs_count
        self.puppies = {}
        for i in range(self.dogs_count):
            self.puppies['dog_' + str(i)] = Puppy(i)
    
    
    def heal_all(self):
        for i in range(len(self.puppies)):
            dog_name = 'dog_' + str(i)
            if self.puppies[dog_name].state != 0:
                self.puppies[dog_name].get_treatment()
        
    
    def all_are_healthy(self):
        list_of_dogs = list(self.puppies.values())
        list_of_states = list(dog.state for dog in list_of_dogs)
        return all(state == 0 for state in list_of_states)
            
    
    
    def give_away_all(self):
        self.puppies = {}
    

class Vet:
    def __init__(self, name, dog):
        self.name = name
        self.plant = dog
    
    
    def work(self):
        self.plant.heal_all()
        
        
    def care(self):
        if self.plant.all_are_healthy() == True:
            self.plant.give_away_all()
            print('Все щенки здоровы и их отдали в хорошие руки.')
        else:
            print('Еще не все щенки здоровы.')
        
        
    def knowledge_base(self):
        if len(self.plant.puppies) == 0:
            print('Щенков нет.')
            
        else:
            for i in range(len(self.plant.puppies)):
                dog_name = 'dog_' + str(i)
                dog_state_index = self.plant.puppies[dog_name].state
                dog_state = self.plant.puppies[dog_name].states[dog_state_index]
               
                print(dog_name, dog_state)
            

        
if __name__ == '__main__':
    print('******** Тест 1 ********')
    dog_mother_1 = Dog(7)
    veter = Vet('Алексей Ветеренар', dog_mother_1)
    
    veter.knowledge_base()
    veter.work()
    veter.work()
    veter.work()
    veter.work()
    veter.care()
    veter.knowledge_base()
    
    # print('******** Тест 2 ********')
    # dog_mother_2 = Dog(4)
    # veter = Vet('Алексей Ветеренар', dog_mother_2)
    
    # veter.work()
    # veter.care()
    # veter.work()
    # veter.care()
    # veter.work()
    # veter.care()
    
    # print()
    # print('Это словарь со всеми щенками, если они все здоровы, то он пустой')
    # print(veter.plant.puppies)
    # print()






from Person import Person
from Worker import Worker


class Manager(Person, Worker):
    def __init__(self, name, age, company, position):
        Person.__init__(self, name, age)
        Worker.__init__(self, company, position)

    def get_full_info(self):
        return f'{Person.get_info(self)}, {Worker.get_info(self)}'

manager = Manager("Alice", 35, "Tech Corp", "Project Manager")
print(manager.get_full_info())
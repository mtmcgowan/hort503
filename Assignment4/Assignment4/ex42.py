## Animal is-a object (yes.sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-an animal
class Dog(Animal):

    def __init__(self,name):
        ## Dog has-a name
        self.name = name

## Cat is-an animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-an object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name
        
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary:
        ## I dunno
        super(Employee, self).__init__(name)
        ## Person has-a salary
        self.salary = salary

## Fish is-an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## Mary has-a pet satan
mary.pet = satan

## Frank is-an employee
frank = Employee("Frank", 120000)

## Frank has-a pet rover
frank.pet = ZeroDivisionError

## flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()


# Study Drills

# 1. Research why Python added this strange object class and what it means.
# Flexibility

# 2. Is it possible to use a class like it's an object?
# An object is a class

# 3. Fill out the animals, fish and people in this exercise with functions that make them do things. See what happens when functions are in a "base-class" like Animal versus in, say, Dog.

# 4. Find other people's code and work out all the is-a and has-a relationships.

# 5. Make some new relationships that are lists and dictionaries so you can also have "has-many" relationships.

# 6. Do you think there's such thing as an "is-many" relationshipo? Read about "multiple inheritance," then avoid it if you can.

"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages to object orientation are Encapsulation,
   Abstraction, and Polymorphism.

   Encapsulation: All the code and its related attributes and methods are all stored in one class.
   Abstraction: Hides code details we don't need to see and yet can call upon.
   Polymorphism: Components are interchangeable. Subclasses can inherit from its parent
   classes the methods and attributes and apply different instances.

2. What is a class?
    A class is essentially a template for creating objects. It isn't anything 
    by itself but it describes how to make something. It contains specific methods and
    instances that a parent class itself or its subclasses can use.

3. What is an instance attribute?
    An instance attribute is unique to that particular instance. For example, 
    a person's specific name (when name is a class attribute) is an instance 
    attribute since it can vary.

4. What is a method?
    A method is a special kind of function (differs from regular function) that is 
    nested in a class. It always takes self as the first parameter.

5. What is an instance in object orientation?
    An instance is a unique representation of an object. For example, given the 
    Hackbright staff as a class, their titles would be an instance of that class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is common among all parts of that class whereas an instance 
   attribute is unique to that instance/object. For example, from our study hall,
   Hackbrighters would be the parent class, all the Hackbrighters would have a "names"
   attributes and that's considered the class attribute. However, the Hackbrighters' names 
   individually are different, so that would be an instance attribute.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """All students"""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Questions and correct answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question + " ")
        return user_answer == self.correct_answer

class Exam(object):
    """An exam"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def adminster(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score = score + 1
          
        return score

class Quiz(Exam):
    """Returns true if at least 50 percet of the answers are correct"""

    def num_of_questions(self):
        return len(self.question)

    def evaluate(self):
        return (self.adminster()/self.num_of_questions()) >= .5
      

def take_test(exam, student):
    """Keeps record of student score after exam is administered"""
    score = exam.administer()
    student.score = score

def example():
    """Creates exam with questions, creates a student, and administer test to that student"""
    
    exam = Exam("Final Exam")
    exam.add_question("When is the general election being held?", "Tuesday, November 8th")
    exam.add_question("Who is the republican candidate?" , "Donald Trump")
    student = Student("Yusra", "Ahmed", "Made up address")
    take_test(exam, student)
















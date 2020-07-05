class Instructor:
    degree = "PhD (Magic)"
    def __init__(self, name):
        self.name = name # this is an instance attribute
        
    def lecture(self, topic):
        print("Today we're learning about " + topic)
        
dumbledore = Instructor("Dumbledore")

class Student:
    instructor = dumbledore
    
    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)

    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}
        
    def add_student(self, student):
        self.students[student.name] = student
        
    def assist(self, student):
        student.understanding += 1

def test1():
    """
    >>> snape = TeachingAssistant("Snape")
    >>> harry = Student("Harry", snape)
    >>> harry.attend_lecture("potions")
    Today we're learning about potions
    Dumbledore is awesome!
    
    >>> hermione = Student("Hermione", snape)
    >>> hermione.attend_lecture("herbology")
    Today we're learning about herbology
    Dumbledore is awesome!

    >>> hermione.visit_office_hours(TeachingAssistant("Hagrid"))
    Thanks, Hagrid

    >>> harry.understanding
    1
    
    >>> snape.students["Hermione"].understanding
    2

    >>> Student.instructor = Instructor("Umbridge")
    >>> Student.attend_lecture(harry, "transfiguration")
    Today we're learning about transfiguration
    I miss Dumbledore.
    """

class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.senger_name = sender_name
        self.recipient_name = recipient_name

class Mailman:
    """Each Mailman has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}
        
    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.
        """   
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), mailman
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """
    def __init__(self, mailman, name):
        self.inbox = []
        self.name = name
        self.mailman = mailman
        mailman.register_client(self, name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """  
        self.mailman.send(Email(msg, self.name, recipient_name))

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)

def test2():
    """
    >>> mailman = Mailman()
    >>> c1 = Client(mailman, 'Tom')
    >>> 'Tom' in mailman.clients
    True

    >>> c2 = Client(mailman, 'Bob')
    >>> c1.compose('Hello, Bob', 'Bob')
    >>> c2.inbox[0].message
    'Hello, Bob'
    >>> c2.inbox[0].senger_name
    'Tom'
    >>> c2.inbox[0].recipient_name
    'Bob'
    >>> len(c2.inbox)
    1
    >>> c2.compose('Hi, Tom', 'Tom')
    >>> c1.inbox[0].message
    'Hi, Tom'
    >>> c1.compose('How are you', 'Bob')
    >>> len(c2.inbox)
    2
    """

class Pet(object):
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' syas woof!')

class Cat(Pet):
    def __inti__(self, name, owner, lives=9):
        self.lives = lives
        Pet.__init__(self, name, owner)

    def talk(self):
        print(self.name + ' syas meow!')
        
    def lose_life(self):
        """A cat can only lose a life if they have at
        least one life. When lives reaches zero, 'is_alive'
        becomes False.
        """
        if self.lives:
            self.lives -= 1
        else:
            self.is_alive = False

class NoisyCat(Cat):
    def talk(self):
        Cat.talk(self)
        Cat.talk(self)

class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)
    
class B(A):
    def f(self):
        return 4

def test_yolo():
    """
    >>> x = Yolo(1)
    >>> x.g(3)
    4
    >>> x.g(5)
    6
    >>> x.motto = 5
    >>> x.g(5)
    10
    """
class Yolo():
    def __init__(self, motto):
        self.motto = motto
    def g(self, n):
        return self.motto + n

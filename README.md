### In this repository I learnt several OOP concepts in Python topicwise. This README file contains a gist of everything I learnt so far.

1. Basics of OOP - I learnt to create a class and object with a car example. I learnt the usage of the __init__ method (which is aka a constructor) since it initialises an object with attributes and methods defined in the class. I varied the code I saw on Bro Code's youtube channel to include a for_sale attribute.

2. Class variables - In this example I understood class variables which are attributes common to all instances of this class such as school_name for a Student class. It's also easy to use the class variables inside of a an instance method for example to increment the class variable of num_of_students.

3. Inheritance - In this example, I learnt that child classes can inherit attributes and methods from a parent class. The child classes not only retain the methods and attributes defined in the parent classes, but can also have their own methods and attributes and when their objects are created, they can use them.

4. Pending multiple and multilevel inheritance
   
5. Abstract classes - I learnt how to define an abstract class by inheriting from ABC and using the @abstractmethod decorator for methods in it. The child classes must use all the abstract methods defined in the abstract class, otherwise it will give an error. It's basically meant to be used as a strict blueprint.

6. The super() method - the super() method calls an attribute or a method of the parent class in its child class and runs it in-place. It is super-effective to bring in attributes and methods from a parent class in a child class for ease of access.

7. Polymorphism - It is an object's ability to have multiple forms such as Pizza is a Circle so it is also a shape. Pizza inherits from Circle which was inheriting from Shape. Hence, methods defined in the Circle class like area can be used on the pizza as well to calculate its area given its radius.

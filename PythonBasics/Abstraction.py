
# Giving the access on functionality but hiding implementation


# ABC - Abstract Base Class

# Example :


from abc import ABC,abstractmethod

## Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete class( impleted abstract methods from abstract class
class Car(Vehicle):
    def start(self):
        print("Car engine started...")

    def stop(self):
        print("Car engine stopped...")



# Usage
# v=Vehicle()  # cannot create object for the abstract class

c=Car()
c.start()
c.stop()

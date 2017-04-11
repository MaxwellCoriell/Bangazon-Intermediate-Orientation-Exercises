import unittest
from animals import *

class TestAnimals(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setup")
        self.chameleon = Animal("Jimmy")
        self.collie = Dog("Lassie")

    def test_AnimalHasCorrectName(self):
        self.assertEqual("Jimmy", self.chameleon.get_name())

    def test_AnimalSetSpeciesMustWork(self):
        self.chameleon.set_species("Furcifer timoni")
        self.assertEqual("Furcifer timoni", self.chameleon.get_species())

    def test_AnimalWalkMustWork(self):
        self.chameleon.set_legs(4)
        self.chameleon.walk()
        self.assertEqual(.4, self.chameleon.speed)

    def test_DogWalkMustWork(self):
        self.collie.set_legs(4)
        self.collie.walk()
        self.assertEqual(.8, self.collie.speed)

    def test_ChameleonIsAnimal(self):
        self.assertIsInstance(self.chameleon, Animal)

    def test_CollieIsDog(self):
        self.assertIsInstance(self.collie, Dog)


if __name__ == '__main__':
    unittest.main()
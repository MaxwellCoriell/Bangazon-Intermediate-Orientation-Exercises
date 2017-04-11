import unittest
from animals.py import *

class TestTheAnimals(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		'''
		In the test class' setUpClass() method, create an instance of Animal and Dog.
		'''
		self.animal = Animal()
		self.angus = Dog('Angus')

	def test_animal_name_property_has_correct_value(self):
		'''
		Animal object has the correct name property.
		'''
		self.assertEqual(self.animal.name, 'Buddy')

	def test_animal_species_property_has_correct_value(self):
		self.assertEqual(self.animal.species, 'Panda')

	def test_dog_species_property_has_correct_value(self):
		'''
		Set a species and verify that the object property of species has the correct value.
		'''
		self.assertEqual(self.angus.species, 'Dog')

	def test_walk_method_set_speed(self):
		'''
		Invoking the walk() method set the correct speed on the both objects.
		'''
		legs = 4
		self.animal.set_legs(legs)
		self.animal.walk()

		self.angus.set_legs(legs)
		self.angus.walk()

		self.assertEqual(self.animal.speed, 0.4)
		self.assertEqual(self.angus.speed, 0.8)

	def test_animal_object_is_correct_type(self):
		'''
		The animal object is an instance of Animal.
		'''
		self.assertIsInstance(self.animal, Animal)

	def test_dog_object_is_correct_type(self):
		'''
		The dog object is an instance of Dog.
		'''
		self.assertIsInstance(self.angus, Dog)


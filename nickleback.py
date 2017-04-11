# In this exercises, you're going to use a conditional statement inside a comprehension. 
# Let's look at a basic example:

# nums = range(10)
# small_numbers = [num for num in nums if num < 6]
# # Only add numbers to the new list if the value is less than 6
# print(small_numbers)
# print("-----------")

# words = ['big', 'red', 'dog', 'ate', 'his', 'food']
# three_letters_words = [ word.title() for word in words if len(word) == 3 ]
# # len(stringVariable) is equivalent to stringVariable.length in JavaScript
# print(three_letters_words)
# print("-----------")

# Define a set that contains tuples. Each tuple should contain two strings:
## name of an artist
## song by that artist
# Make sure that some of the songs are from the band Nickleback

songs = {
	('Nickleback', 'Animal'),
	('Emery', "'So Cold I Could See My Breath'"),
	('letlive', "'Muther'"),
	('Nickleback', "'How You Remind Me'"),
	('Thursday', "'War All The Time'"),
	('Nickleback', "'Photograph'"),
	('City & Colour', "'The Girl'")
}
print("Some of These Songs Suck: ")
print("-------------------------")
print(songs)
print("-----------")
print("-----------")

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

fuckNickleback = [song for song in songs if song[0] != 'Nickleback']
# print(fuckNickleback)
# print("-----------")


print("These Songs Don't Suck: ")
print("-----------------------")
for (artist, songTitle) in fuckNickleback:
	print(artist + " -- " + songTitle)
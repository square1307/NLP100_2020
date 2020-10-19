
#00. Reversed string
#Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).

def C1_00(input):
	return input[::-1]
print(C1_00("stressed"))

#01. “schooled”
#Obtain the string that concatenates the 1st, 3rd, 5th, and 7th letters in the string “schooled”.

def C1_01(input):
	return input[::2]
print(C1_01("schooled"))

#02. “shoe” + “cold” = “schooled”
#Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.

def C1_02(inputA, inputB):
	return ''.join([a+b for (a,b) in zip(inputA,inputB)])
print(C1_02("shoe","cold"))
		

#03. Pi
#Split the sentence “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics”. into words, and create a list whose element presents the number of alphabetical letters in the corresponding word.

def C1_03(input):
	return [len(word) for word in input.split()]
print(C1_03("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"))

#04. Atomic symbols
#Split the sentence “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can”. into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words and the first two letters from the other words. Create an associative array (dictionary object or mapping object) that maps from the extracted string to the position (offset in the sentence) of the corresponding word.

def C1_04(input):
	index_first_letter = (1, 5, 6, 7, 8, 9, 15, 16, 19)
	return {word[0:(1 if index in index_first_letter else 2)]: index for (index, word) in enumerate(input.split())}
print(C1_04("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"))

#05. n-gram
#Implement a function that obtains n-grams from a given sequence object (e.g., string and list). Use this function to obtain word bi-grams and letter bi-grams from the sentence “I am an NLPer”

def C1_05(input,n=1):
	return [input[i:i+n] for (i, word) in enumerate(input) if len(input[i:i+n]) == n]
print(C1_05("I am an NLPer",2))
print(C1_05("I am an NLPer".split(),2))

#06. Set
#Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$, respectively. Obtain the union, intersection, difference of the two sets. In addition, check whether the bigram “se” is included in the sets $X$ and $Y$

def C1_06(input):
	def n_gram(input, n=2):
		return [input[i:i+n] for (i, word) in enumerate(input) if len(input[i:i+n]) == n]
	input_sets = [set(n_gram(word)) for word in input]
	print("Union:", input_sets[0] | input_sets[1])
	print("Intersection:", input_sets[0] & input_sets[1])
	print("Difference:", input_sets[0] - input_sets[1])
C1_06(["paraparaparadise","paragraph"])
	

#07. Template-based sentence generation
#Implement a function that receives arguments, x, y, and z and returns a string “{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y, and z, respectively. In addition, confirm the return string by giving the arguments x=12, y="temperature", and z=22.4.

def C1_07(x,y,z):
	return "{y} is {z} at {x}".format(x=x,y=y,z=z)
print(C1_07(x=12, y="temperature", z=22.4))

#08. cipher text
#Implement a function cipher that converts a given string with the specification:
#
#Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
#Keep other letters unchanged
#Use this function to cipher and decipher an English message.


def C1_08(input):
	return ''.join([chr(219-ord(c)) if (c.islower()) else c for c in input])
msg = '''William Shakespeare (bapt. 26 April 1564 – 23 April 1616) was an English playwright, poet, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist.'''
print(C1_08(msg))
print(C1_08(C1_08(msg)))

#09. Typoglycemia
#Write a program with the specification:
#
#Receive a word sequence separated by space
#For each word in the sequence:
#If the word is no longer than four letters, keep the word unchanged
#Otherwise,
#Keep the first and last letters unchanged
#Shuffle other letters in other positions (in the middle of the word)
#Observe the result by giving a sentence, e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind “.

def C1_09(input):
	import random
	return ' '.join([word if len(word) <= 4 else word[0]+''.join(random.sample(list(word[1:-1]),len(word)-2))+word[-1] for word in input.split()])
print(C1_09("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"))
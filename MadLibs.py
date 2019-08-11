#! python3
# This is a little Mad Libs game.
# It asks you to enter an adjective, verb, and two nouns to complete a sentence.

import re, shelve, os

# Shelve.
variant = 0
if os.path.exists('.\\Results'):
	pass
else:
	os.mkdir('.\\Results')
os.chdir('.\\Results')
historySh = shelve.open('Variants')
os.chdir('..')

# File management.
orig = open('orig.txt', 'r')
baseLine = orig.read()
orig.close()

# Creating regular expression for VERB, NOUN, ADJECTIVE.
pattern = re.compile('ADJECTIVE|NOUN|VERB')
mo1 = re.findall(pattern, baseLine)

# Cycles for replacing.
for i in range(len(mo1)):
	if mo1[i] in baseLine and mo1[i] == 'ADJECTIVE':
		baseLine = re.sub(mo1[i], input('Enter an adjective:\n'), baseLine)
	if mo1[i] in baseLine and mo1[i] == 'NOUN':
		baseLine = re.sub(mo1[i], input('Enter a noun:\n'), baseLine, 1)
	if mo1[i] in baseLine and mo1[i] == 'VERB':
		baseLine = re.sub(mo1[i], input('Enter a verb (Past Indefinite):\n'), baseLine)
variant += 1

# Show and write the result to a file.
print('\n' + baseLine)
result = open('Result.txt', 'w')
result.write(baseLine)
result.close()

# Save the variant with shelve module.
os.chdir('.\\Results')
historySh['variant' + str(variant)] = baseLine
historySh.close()

# To check available saved variants, type the following into console.
# os.chdir('.\\Results')
# hist = shelve.open('Variants')
# for i in hist.keys():
# 	print(i)

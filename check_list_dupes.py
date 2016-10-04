# !python3
# This script was created to take a list and check for duplicates
# by adding the first occurance to a new list and then saving
# the new list to a text file

text_file = open("biglist.txt", "r")
lines = text_file.readlines()
text_file.close()

unique_list = [] # An empty list to add the unique lines to

for line in lines:
	if line not in unique_list:
		unique_list.append(line)
		
# Save the lines to a new text file
unique_file = open("uniquefile.txt", "w")
unique_file.writelines(unique_list)
unique_file.close()
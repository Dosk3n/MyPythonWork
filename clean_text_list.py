# !python3
# This script was created to take a list of urls that I needed the
# directories from and strip away the parts I didnt need using index

# Read the entire file to a list
# Example of list:
# Checking http://deansadventure.com/yonetim.php : not found
# Checking http://deansadventure.com/yonetim.html : not found
# Checking http://deansadventure.com/yonetici.php : not found
text_file = open("bloglist.txt", "r")
lines = text_file.readlines()
text_file.close()

clean_list = [] # An empty list to add the cleaned line

for line in lines:
	# Strips away the first 35 chars and adds the remaining to newline
	# leaving us with yonetim.php : not found
	newline = line[34:len(line)]
	#print(newline)
	
	# Find the index of : and go back one to start from the space before
	colon_index = newline.index(':')
	index = colon_index - 1
	
	# Add the chars up to the index of : to a new variable
	clean_line = newline[0:index] + "\n" # add a new line for when we add to text file
	
	# Add the cleaned line to the clean_list
	clean_list.append(clean_line)
	
# Save the lines to a new text file
clean_file = open("cleanfile.txt", "w")
clean_file.writelines(clean_list)
clean_file.close()
	

	
	
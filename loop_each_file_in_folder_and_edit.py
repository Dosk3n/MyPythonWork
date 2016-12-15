#! Python3
#
# Script to load each VNC file in current directory and then make an edit
# to change the port number in each file.
#

import os

# Find the names of all vnc files in current folder and add
# to an array.
file_names = []
for file in os.listdir("."):
	if file.endswith(".vnc"):
		file_names.append(file)
		
# For each file in the folder that mached our search.
for file in file_names:

	f = open(file, "r")
	lines = []
	# Add each line of file to an array so we can edit easily.
	for line in f:
		lines.append(line)
	f.close()

	# Port data in position 2. Update port num.
	# Proxy port data in position 4. Update port num.
	lines[2] = "port=5901\n"
	lines[4] = "proxyport=5901\n"
	
	# Save to file to a different folder and write each line to new file
	f = open("./classic/" + file, "w")
	for line in lines:
		f.write(line)
	f.close
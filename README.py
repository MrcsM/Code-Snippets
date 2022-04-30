# Extremely simple README creator because I'm lazy and inputting the .cc and .h files and describing them is easier than actually writing everything else
# Credit to Prof. Darryl Hill @ Carleton University, he had this coded originally for making simple .cc and .h files for COMP2404 assignments and I ended up
# doing this with the code

import sys

if len(sys.argv)<3:
	print("no assignment # or description detected")
	exit()
	
cl = sys.argv[1]
desc = sys.argv[2:]

title = "ASSIGNMENT " + cl
print(title)

result ='''~~~~~ {title} README ~~~~~
Marcus Moquin - ######### - COMP2404 - Assignment {cl} ({description})

Files & Brief Description
 - <insert .cc> & <insert .h>
  - <define>
 - <insert .cc> & <insert .h>
  - <define>
 - <insert .cc> & <insert .h>
  - <define>
 - <insert .cc> & <insert .h>
  - <define>
 - <insert .cc> & <insert .h>
  - <define>
 - <insert .cc> & <insert .h>
  - <define>
 - <insert .cc> & <insert .h>
  - <define>

Compilation and Execution
 - Compiling:
  - Make sure you are in the main directory, which contains all of the source code and header files.
  - Once you are there, run "make a{cl}"
 - Executing:
  - Once you have used the makefile to compile the code, run "./a{cl}" and go through the menu.

~~~~~ {title} README ~~~~~
'''.format(title = title, cl = cl, description = " ".join(desc))

f = open("README.txt",'w')
f.write(result)
f.close()
print("Created README.txt for " + title)

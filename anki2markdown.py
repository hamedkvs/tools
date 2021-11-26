# This tool converts '#' separated anki notes (i.e each note is put into a line in which the fields are separated by 
# the character '#'.) to markeddown notation, so it can be better viewed over browsers
# instead of seeing hard to read text. 
# 
# The filename shall be sent to the program as a command line argument.
# The result would ba a file with an ".md" extension which will reside inside a folder called "github_prett" at the 
# same location as the initial file.
#
# Example of the input file: 
# input.txt:
# livre#book#i have a book
# eau#water#i need some water
# 
# Now we try to do the conversion:
# user@system$ python3 anki2markdown.py input.txt
#
import sys
import os.path

def process(line):
    #some code
    line = line.replace("<br/>", "\n")
    keyval = line.split("#")
    question = keyval[0]
    answer = keyval[1]
    question = '# '+question
    res = question + '\n'+answer
    return res

def saveToFile(anki_filepath, final_list):
    #some code
    directory = os.path.dirname(sys.argv[1])
    filename = os.path.basename(sys.argv[1])
    b,ext = os.path.splitext(filename)
    new_filename = b + ".md"
    new_dir = os.path.join(directory, "github_prett")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    with open(os.path.join(new_dir,new_filename), "w") as f:
        for line in final_list:
            f.write(line + "\n")
    return

file=sys.argv[1]
result=[]
with open(file, 'r') as f:
    for line in f:
        result.append(process(line))
saveToFile(file, result)

    

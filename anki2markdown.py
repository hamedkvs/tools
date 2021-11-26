# This tool converts '#' separated anki notes to markeddown notation, so it can be better viewed over browsers
# in stead of seeing so called ugly gibberish. The filename shall be sent as a command languge argument.
# The result would ba a file with an ".md" extension which will reside inside a folder called "github_prett" at the 
# same location as the initial file.
import sys
import os.path

def process(line):
    #some code
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

    

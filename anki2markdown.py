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

    

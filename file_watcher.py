
import operator
from stat import ST_CTIME
import os, sys, time
from sheff_QA import answer_question,make_pipe
import json
path = "questions/" ;  #or you can assign the return value of your 
                                 #function (the updated path as per your question) 
                                 #which operates on the file 'new_file'  to this variable. 
files = os.listdir(path);

def mostRecentFile(path):
    all_files = os.listdir(path);
    file_times = dict();
    for file in all_files:
        file = os.path.join(path,file)
        #print(file)
        file_times[file] = time.time() - os.stat(file).st_ctime;
    return  sorted(file_times.items(), key=operator.itemgetter(1))[0][0]

if __name__ == "__main__":


    pipe = make_pipe()
    old_file = ""
    new_file = "PLACEHOLDER.txt"
    old_files =  all_files = os.listdir(path);
    print(old_files)
    print("STARTING TO LISTEN FOR QUESTIONS!")
    while True:
        old_file = new_file
        new_file = mostRecentFile(path)
        
        if new_file.split("/")[-1] not in old_files and  new_file != old_file:
            print(new_file)
            q_id = new_file.split("/")[-1].split(".")[0].split("_")[-1]
            print("Q_ID:",q_id)
            with open(new_file) as f:
                text = f.read()
            print(text)
            a = answer_question(text,pipe) #we can do stuff with this a object later :)
            #print(a)
            print("found %s answers!"%len(a['answers']))
            out_dict = {}
            for i,t in enumerate(a['answers']):
                t.contect = t.context.strip("\n")
                print(i,t.answer,t.score,t.context)
                #t.contect = t.context.strip("\n")
                out_dict[i] = {"answer": t.answer,"score":t.score,"context":t.context}
            #print("score",a['answers'][0].score)
            text_to_send = a['answers'][0].answer
            with open("answers/a_%s.txt"%q_id,"w") as f:
                #f.write(text_to_send)
                json.dump(out_dict,f)
        else:
            print("no new questions!")
        time.sleep(2)
#flag{b1n42y_s3r2ch_f7w}
import os
import subprocess
#getting the current working directory (test run of os package)
a = os.getcwd()
print(a)
#As the files of bruteforcer and word-list were in the same directory, there was no need to change directory
#converting the wordlist.txt into actual python list for implementing binary search
password_file = open("wordlist.txt", "r")
word_list = (password_file.read()).splitlines()
password_file.close()
#sorting the list in order to be used in binary search
word_list.sort()
#code for executing binary search
start = 0
end = len(word_list) - 1
while True:
    mid = int(0.5*(start + end))
    string = word_list[mid]
    #piping in python using Popen
    p1 = subprocess.Popen(["echo", string], stdout=subprocess.PIPE)
    answer = subprocess.Popen(['./bruteforcer'],stdin=p1.stdout,stdout=subprocess.PIPE)
    #closing the p1 stdout to avoid high processing usage
    p1.stdout.close()
    output = str(answer.communicate()[0]).split()[-1]
    print( "Answer is " + output)
    if output == "low":
        start = mid
    elif output == "high":
        end = mid
    else:
        break

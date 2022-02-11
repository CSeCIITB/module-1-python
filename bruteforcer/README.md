You are given a program `bruteforcer` which can be run using the following commands while in this directory
```bash
chmod +x bruteforcer #If the file is not marked as executable
./bruteforcer
```
The program prompts for an input when executed and will print out the flag on giving the correct password. 
The password is an entry in the provided `wordlist.txt` file. Your task is to write a script that automatically finds this correct password. <br>
Though, the problem here is that the wordlist contains 5 million passwords and checking each one sequentially will take a lot of time. 
This is where you can use the information on whether the password you provide is larger or smaller
([lecicographically](https://en.wikipedia.org/wiki/Lexicographic_order)) than the correct password. This information can be used to perform
a [binary search](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search) over the wordlist and quiclkly find the answer.

## Submission instruction
Create a file `script.py` which solves the challenge. The first line of this file should contain a comment with the flag you obtained.

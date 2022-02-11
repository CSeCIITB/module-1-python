This one will need a bit of explaining... <br>
You already are given the flag files `flag1.txt` and `flag2.txt` corresponding to the 2 levels of the challenge : `jail1.py` and `jail2.py`. <br>
<br>
The task now in level 1 is to be able to get the contents of `flag1.txt` while executing `jail1.py`. On running `jail1.py` by executing `python3 jail1.py`
or `python jail1.py` (whichever works), the program prompts for an input and calls
[**eval**](https://www.programiz.com/python-programming/methods/built-in/eval) on the passed input. Is calling **eval** safe here? And if not, how can
you use it to solve the challenge?<br>
Level 2 is completely similar except the fact that it implements a blacklist on the strings allowed in the input. So, you may need to modify your
solution from level 1 to read `flag2.txt`.

## Submission Instructions
Create files `ans1.txt` and `ans2.txt` with the corresponding inputs to the programs that print the flag.

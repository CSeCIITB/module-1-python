#flag{b1n42y_s3r2ch_f7w}

file = open("file.txt", "r")    #file.txt is sorted version of given file

passwords = []
for line in file:
  password = line.strip()
  passwords.append(password)
file.close()

x,y = input('start point:').split()
start = int(x)+int(y)
l,m = input('end point:').split()
end = int(l)+int(m)
passwords = passwords[start:end]
a = len(passwords)
print(f"start point {start}, end point {end} and {a//2}th password is {passwords[a//2]}")

#if password is low, enter start point and (a//2) from previous execution in "start" then 0 and previous end point in "end"
#if password is high, enter previous start point and 0 in "start" then previous start point and (a//2) in end
#initial start is (0 0) and initial end is (5189455 0)

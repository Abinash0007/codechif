s = input()
#take string input
n = s.count("n") -1 #count number of n's in the string and subtract 1
i = s.count("i")
e = s.count("e")
t = s.count("t")
print max(0,(min(n//2,i,e//3,t)))

s = input()
n = s.count("n") -1
i = s.count("i")
e = s.count("e")
t = s.count("t")
print max(0,(min(n//2,i,e//3,t)))
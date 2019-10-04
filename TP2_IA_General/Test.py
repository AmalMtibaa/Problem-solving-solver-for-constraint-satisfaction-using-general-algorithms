# for i in range(0, 1):
#     ch=input().split(" ")[1]
#     tmp=ch.split(",")
#     tmp[0]=tmp[0][1:]
#     tmp[len(tmp)-1]=tmp[len(tmp)-1][0:(len(tmp[len(tmp)-1])-1)]
#     print(tmp)

c="if case == 1{"
cond=c.split(" ")
if cond[len(cond)-1] == "{":
    cond = cond[0:len(cond) - 1]
else:
    cond[len(cond) - 1] = cond[len(cond) - 1][0:len(cond[len(cond) - 1]) - 1]

print(cond)
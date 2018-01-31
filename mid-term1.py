with open(r"C:\Users\Administrator\github\zhangyu\report.txt",encoding = "utf-8") as f:
    report = f.readlines()

nop = len(report)#number of people
for i in range(nop):
    total = 0
    nos = len(report[i].split()[1:])#number of subjects
    for j in report[i].split()[1:]:
        total += int(j)
    average = total/nos
    report[i] = report[i].replace("\n"," %d %.2f\n"%(total,average))

report.sort(key = lambda x :x.split()[-1],reverse = True)
for i in range(nop):
    if i == 0:
        rank = 1
    else:
        if report[i].split()[-1] == report[i-1].split()[-1]:
            rank = int(report[i-1].split()[0])
        else:
            rank = i + 1
    if rank <= 9:
        report[i] = str(rank) + "    " + report[i]
    else:
        report[i] = str(rank) + "   " + report[i]

top = "0    平均 "
for i in range(2,nos+4):
    total = 0.0
    for j in range(nop):
        total += float(report[j].split()[i])
    average = total/nop
    top += "%.2f "%average
top += "\n"
report.insert(0,top)
report.insert(0,"名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分\n")
for i in range(1,nop+2):
    for j in range(2,nos+4):
        if float(report[i].split()[j]) < 60.0:
            report[i] = report[i].replace(report[i].split()[j],"不及格",1)

with open(r"C:\Users\Administrator\github\zhangyu\grade.txt","w",encoding = "utf-8") as f:
    f.writelines(report)

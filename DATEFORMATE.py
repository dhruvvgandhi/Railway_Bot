from googlesearch.googlesearch import GoogleSearch
import sys
from Tkinter import *
import sys
import datetime
from datetime import datetime
import calendar

arg1 = sys.argv[1]
arg2 = sys.argv[2]


def con(st):
	qt=st.split("-")
	qm=""

	if int(qt[1])==1:
		qm="Jan"

	if int(qt[1])==2:
		qm="Feb"

	if int(qt[1])==3:
		qm="Mar"

	if int(qt[1])==4:
		qm="Apr"

	if int(qt[1])==5:
		qm="May"

	if int(qt[1])==6:
		qm="Jun"

	if int(qt[1])==7:
		qm="Jul"

	if int(qt[1])==8:
		qm="Aug"

	if int(qt[1])==9:
		qm="Sep"

	if int(qt[1])==10:
		qm="Oct"

	if int(qt[1])==11:
		qm="Nov"

	if int(qt[1])==12:
		qm="Dec"

	qd=qm+" "+qt[0]+" "+qt[2]
	my_date=datetime.strptime(qd, '%b %d %Y')
	sg=calendar.day_name[my_date.weekday()][0:3]
	fd=sg+"-"+qm+" "+qt[0]
	print(fd)
	return fd


response = GoogleSearch().search("indiarailinfo seat availability in "+arg1+" on 15-09-2018")
x=""
y=""
for result in response.results:
	x=result.getText()
	print(x)

	x=x.split("WaitlistCharting",1)[1]
	x=x.replace("oldRefresh","\n")
	
	x=x.replace("Avbl","\tAvbl")
	
	x=x.replace("WL","\tWL")
	x=x.replace("RAC","\tRAc")
	
	x=x.replace("AC","\tAC")
	x=x.replace("SL","\tSC")
	x=x.replace("CC","\tCC")
	x=x.replace("2nd","\t2nd")

	x=x.replace("-Refresh","\n")
	x=x.split("Getting Latest",1)[0]
	x=x.split("Date",1)[1]
	y=x.split("Freshness",1)[0]
	x=x.split("Update",1)[1]
	print("\t"+y)
	print(x)

	break;
master = Tk()

master.title("Seat Availability")
y=y.split("\t")
q=len(y)
for i in range(0,q):
	Label(master, text=y[i],width=20).grid(row=0,column=i)
Label(master, text="Date",width=20).grid(row=0,column=0)

f=""
kt=""
gt=con(arg2)
if gt in x:
	f=x.split(gt)
	kt=gt
else:
	stk=int(arg2[0:2])
	if stk>23:
		stk=stk-7
	sg=stk
	for stk in range(sg,28):
		smp=str(stk)
		if stk<10:
			smp="0"+smp
		th=smp+arg2[2:10]
		print(th)
		kt=con(th)
		print("--"+kt+"--")
		if kt in x:
			f=x.split(kt)
			break;


x=f[1]
x=kt+x


print(x)



g=x.split("\n")
l=0;
o=len(g)
if o<10:
	l=o
else:
	l=10

for j in range(0,l):

	m=g[j].split("\t")
	n=len(m)

	i=0
	for i in range(0,n):
		re=m[i]
		if "Avbl" in re:
			re=re[0:9]

		if "WL" in re:
			re="WL"
		
		if "RAc" in re:
			re="RAC"
		if "n" in re and i !=0:
			re="--"
		if "h" in re and i!=0:
			re="--"
		
		Label(master, text=re,width=20).grid(row=j+1,column=i)


mainloop()
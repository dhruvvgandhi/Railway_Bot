from tkinter import *
import requests , json 
import os
from tkinter import messagebox
from datetime import datetime
import calendar

global api_key
api_key = "4ng2pv0vx8"
def u1():
	global roota1
	roota1 = Toplevel()
	roota1.title('Live Status')
	roota1.focus_set()
	base_url = "https://api.railwayapi.com/v2/live/train/"

	train_number = str(e1.get())


	current_date = str(f1.get())

	complete_url = base_url + train_number + "/date/" + current_date + "/apikey/" + api_key + "/"

	response_ob = requests.get(complete_url) 

	result = response_ob.json() 

	if result["response_code"] == 200 : 


		train_name = result["train"]["name"] 

		y = result["route"] 

		source_station = y[0]["station"]["name"] 

		destination_station = y[len(y)-1]["station"]["name"] 

		position = result["position"] 

		print(" train name : " + str(train_name) + "\n source station : " + str(source_station) + "\n destination station : "+ str(destination_station) + "\n current status : " + str(position) ) 
		print("\n\n\n\n\n");
		i=len(y)

		Label(roota1, text=str("No.")).grid(row=0,column=0)
		Label(roota1, text=str("Station")).grid(row=0,column=0)
		Label(roota1, text=str("Arrived")).grid(row=0,column=1)
		Label(roota1, text=str("Departed")).grid(row=0,column=2)
		Label(roota1, text=str("Distance")).grid(row=0,column=3)
		Label(roota1, text=str("SchArr")).grid(row=0,column=4)
		Label(roota1, text=str("ActArr")).grid(row=0,column=5)
		Label(roota1, text=str("SchDep")).grid(row=0,column=6)
		Label(roota1, text=str("ActDep")).grid(row=0,column=7)
		Label(roota1, text=str("SchDate")).grid(row=0,column=8)
		Label(roota1, text=str("ActDate")).grid(row=0,column=10)
		Label(roota1, text=str("Late By")).grid(row=0,column=11)
		for k in range(0,i):
			nu=k
			da=y[k]["day"]
			d0=y[k]["station"]["name"]
			d1=y[k]["has_arrived"]
	    
			if str(d1)=="True":
				d1="YES"
			else:
				d1="NO"
			d2=y[k]["has_departed"]
			if str(d2)=="True":
				d2="YES"
			else:
				d2="NO"
			d3=y[k]["distance"]
			d4=y[k]["scharr"]
			d5=y[k]["schdep"]
			d6=y[k]["actarr"]
			d7=y[k]["actdep"]
			d8=y[k]["scharr_date"]
			d9=y[k]["actarr_date"]
			d10=y[k]["latemin"]
			if str(d1)=="NO":
				d6="--"
			if str(d2)=="NO":
				d7="--"
			
			if str(d4)=="Source":
				d6="Source"
			
			if str(d5)=="Destination":
				d7="Destination"

			print(str(nu+1)+"\t"+str(d0)+"\t"+str(d1)+"\t"+str(d2)+"\t"+str(d3)+"\t"+str(d4)+"\t"+str(d5)+"\t"+str(d6)+"\t"+str(d7)+"\t"+str(d8)+"\t"+str(d9)+"\t"+str(d10))
			Label(roota1, text=str(nu+1)).grid(row=nu+1,column=0)
			Label(roota1, text=str(d0)).grid(row=nu+1,column=0)
			Label(roota1, text=str(d1)).grid(row=nu+1,column=1)
			Label(roota1, text=str(d2)).grid(row=nu+1,column=2)
			Label(roota1, text=str(d3)).grid(row=nu+1,column=3)
			Label(roota1, text=str(d4)).grid(row=nu+1,column=4)
			Label(roota1, text=str(d6)).grid(row=nu+1,column=5)
			Label(roota1, text=str(d5)).grid(row=nu+1,column=6)
			Label(roota1, text=str(d7)).grid(row=nu+1,column=7)
			Label(roota1, text=str(d8)).grid(row=nu+1,column=8)
			Label(roota1, text=str(d9)).grid(row=nu+1,column=10)
			Label(roota1, text=str(d10)).grid(row=nu+1,column=11)

	else : 
		messagebox.showinfo("Invalid", "No Record Found")
	
		print("record is not found for given request") 



def u2():
	global roota2
	roota2 = Toplevel()
	roota2.title('PNR Status')
	roota2.focus_set()
	base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"
	val=e2.get()
	cur=base_url+val+"/apikey/"+api_key+"/"
	response_ob = requests.get(cur) 

	result = response_ob.json() 

	if result["response_code"] == 200 : 
		Label(roota2, text="PNR",width=15).grid(row=0,column=0)
		Label(roota2, text=str(result["pnr"]),width=15).grid(row=0,column=1)
		print(str(result["pnr"])+"\n")
		Label(roota2, text="DOJ",width=15).grid(row=1,column=0)
		Label(roota2, text=str(result["doj"]),width=15).grid(row=1,column=1)
		Label(roota2, text="From",width=15).grid(row=2,column=0)
		Label(roota2, text=str(result["from_station"])).grid(row=2,column=1)
		Label(roota2, text="To",width=15).grid(row=3,column=0)
		Label(roota2, text=str(result["to_station"])).grid(row=3,column=1)
		Label(roota2, text="Res From",width=15).grid(row=4,column=0)
		Label(roota2, text=str(result["boarding_point"])).grid(row=4,column=1)

		Label(roota2, text="Res To",width=15).grid(row=5,column=0)
		Label(roota2, text=str(result["reservation_upto"])).grid(row=5,column=1)

		Label(roota2, text="Chart Prepared",width=15).grid(row=6,column=0)
		Label(roota2, text=str(result["chart_prepared"])).grid(row=6,column=1)
		Label(roota2, text="Train",width=15).grid(row=7,column=0)
		Label(roota2, text=str(result["train"]["name"])).grid(row=7,column=1)
		Label(roota2, text=str(result["train"]["number"])).grid(row=7,column=2)
		Label(roota2, text="Class",width=15).grid(row=8,column=0)
		Label(roota2, text=str(result["journey_class"]["name"])).grid(row=8,column=1)
		Label(roota2, text="Passanger Details",width=15).grid(row=9,column=3)
		fa=int(result["total_passengers"])
		y=result["passengers"]
		
		Label(roota2, text="No.",width=15).grid(row=11,column=0)
		Label(roota2, text="Current Status",width=15).grid(row=11,column=1)
		Label(roota2, text="Booking Status",width=15).grid(row=11,column=2)
		for i in range(0,fa):
			Label(roota2, text=str(y[i]["no"]),width=15).grid(row=12+i,column=0)
			Label(roota2, text=str(y[i]["current_status"]),width=15).grid(row=12+i,column=1)
			Label(roota2, text=str(y[i]["booking_status"]),width=15).grid(row=13+i,column=2)
	else : 
		messagebox.showinfo("Invalid", "No Record Found")
	
		print("record is not found for given request") 

def u3():
	global roota3
	roota3 = Toplevel()
	roota3.title('Train Route')
	roota3.focus_set()
	base_url = "https://api.railwayapi.com/v2/route/train/"
	val=e3.get()
	cur=base_url+val+"/apikey/"+api_key+"/"
	response_ob = requests.get(cur) 

	result = response_ob.json() 
	if result["response_code"] == 200 : 
		Label(roota3, text="Tain No. :").grid(row=0,column=0)
		Label(roota3, text=val,width=15).grid(row=0,column=1)
		
		Label(roota3, text="Tain Name :").grid(row=1,column=0)
		Label(roota3, text=str(result["train"]["name"]),width=15).grid(row=1,column=1)
		Label(roota3, text="Days :").grid(row=2,column=0)
		Label(roota3, text="Run  :").grid(row=3,column=0)
		Label(roota3, text="MON").grid(row=2,column=1)
		Label(roota3, text="TUE").grid(row=2,column=2)
		Label(roota3, text="WED").grid(row=2,column=3)
		Label(roota3, text="THU").grid(row=2,column=4)
		Label(roota3, text="FRI").grid(row=2,column=5)
		Label(roota3, text="SAT").grid(row=2,column=6)
		Label(roota3, text="SUN").grid(row=2,column=7)
		y=result["train"]["days"]
		Label(roota3, text=str(y[0]["runs"])).grid(row=3,column=1)
		Label(roota3, text=str(y[1]["runs"])).grid(row=3,column=2)
		Label(roota3, text=str(y[2]["runs"])).grid(row=3,column=3)
		Label(roota3, text=str(y[3]["runs"])).grid(row=3,column=4)
		Label(roota3, text=str(y[4]["runs"])).grid(row=3,column=5)
		Label(roota3, text=str(y[5]["runs"])).grid(row=3,column=6)
		Label(roota3, text=str(y[6]["runs"])).grid(row=3,column=7)
		Label(roota3, text="Class").grid(row=4,column=0)
		Label(roota3, text="Available").grid(row=5,column=0)
		z=result["train"]["classes"]
		j=len(z)
		
		for i in range(0,j):
			Label(roota3, text=str(z[i]["code"])).grid(row=4,column=i+1)
			Label(roota3, text=str(z[i]["available"])).grid(row=5,column=i+1)
		Label(roota3, text="Route").grid(row=6,column=2)
		z=result["route"]
		j=len(z)
		print(str(j)+"\n")
		Label(roota3, text="No.").grid(row=7,column=0)
		Label(roota3, text="City").grid(row=7,column=1)
		Label(roota3, text="Day").grid(row=7,column=2)
		Label(roota3, text="SchArr").grid(row=7,column=3)
		Label(roota3, text="SchDep").grid(row=7,column=4)
		Label(roota3, text="Halt").grid(row=7,column=5)

		Label(roota3, text="Distance").grid(row=7,column=6)
		i=0
		k=0
		while k<j:
			print(str(k)+"\n")
			i=k
			Label(roota3, text=str(z[k]["no"])).grid(row=8+k,column=0)
			print(str(k)+"a")
			Label(roota3, text=str(z[k]["station"]["name"])).grid(row=8+k,column=1)
			print(str(k)+"\n")
			Label(roota3, text=str(z[k]["day"])).grid(row=8+i,column=2)
			print(str(k)+"b")
			Label(roota3, text=str(z[k]["scharr"])).grid(row=8+i,column=3)
			print(str(k)+"\n")
			Label(roota3, text=str(z[k]["schdep"])).grid(row=8+i,column=4)
			print(str(k)+"\n")
			Label(roota3, text=str(z[k]["halt"])).grid(row=8+i,column=5)
			print(str(k)+"\n")
			Label(roota3, text=str(z[k]["distance"])).grid(row=8+i,column=5)
			print(str(k)+"c")
			k=k+1
			print(str(k)+"\n")

	
	else : 
		messagebox.showinfo("Invalid", "No Record Found")
	
		print("record is not found for given request") 


def u4():
	global roota4
	roota4 = Toplevel()
	roota4.title('Fare')
	roota4.geometry("300x100")
	roota4.focus_set()
	base_url = "https://api.railwayapi.com/v2/check-seat/train/"
	val1=e4.get()
	val2=f4.get()
	val3=g4.get()
	val4=h4.get()
	val5=i4.get()
	val6=j4.get()
	val7=k4.get()
	cur="https://api.railwayapi.com/v2/fare/train/"+val1+"/source/"+val2+"/dest/"+val3+"/age/"+val7+"/pref/"+val5+"/quota/"+val6+"/date/"+val4+"/apikey/"+api_key+"/"

	
	print(cur)
	response_ob = requests.get(cur) 
	result = response_ob.json() 
	if result["response_code"] == 200 : 
		Label(roota4, text="Fare :").grid(row=0,column=0)
		Label(roota4, text=result["fare"]).grid(row=0,column=1)

	else : 
		messagebox.showinfo("Invalid", "No Record Found")
	
		print("record is not found for given request") 

def u5():
	global roota5
	roota5 = Toplevel()
	roota5.title('Trains')
	roota5.focus_set()
	base_url = "https://api.railwayapi.com/v2/check-seat/train/"
	val1=e5.get()
	val2=f5.get()
	val3=g5.get()
	cur="https://api.railwayapi.com/v2/between/source/"+val1+"/dest/"+val2+"/date/"+val3+"/apikey/"+api_key+"/"

	
	print(cur)
	response_ob = requests.get(cur) 
	result = response_ob.json() 
	if result["response_code"] == 200 : 
		y=result["trains"]
		j=len(y)
		i=0
		
		Label(roota5, text="Train No.").grid(row=0,column=0)
		Label(roota5, text="Train Name").grid(row=0,column=1)
		Label(roota5, text="Dep").grid(row=0,column=4)
		Label(roota5, text="Arr").grid(row=0,column=5)
		Label(roota5, text="Duration").grid(row=0,column=6)
		Label(roota5, text="From").grid(row=0,column=7)
		Label(roota5, text="To").grid(row=0,column=8)
		Label(roota5, text="2S").grid(row=0,column=9)
		Label(roota5, text="CC").grid(row=0,column=10)
		Label(roota5, text="FC").grid(row=0,column=11)
		Label(roota5, text="SL").grid(row=0,column=12)
		Label(roota5, text="2A").grid(row=0,column=13)
		Label(roota5, text="1A").grid(row=0,column=14)
		Label(roota5, text="3E").grid(row=0,column=15)
		Label(roota5, text="3A").grid(row=0,column=16)
		Label(roota5, text="MON").grid(row=0,column=17)
		Label(roota5, text="TUE").grid(row=0,column=18)
		Label(roota5, text="WED").grid(row=0,column=19)
		Label(roota5, text="THU").grid(row=0,column=20)
		Label(roota5, text="FRI").grid(row=0,column=21)
		Label(roota5, text="SAT").grid(row=0,column=22)
		Label(roota5, text="SUN").grid(row=0,column=23)
		while i<j:
			Label(roota5, text=str(y[i]["number"])).grid(row=i+1,column=0)
			Label(roota5, text=str(y[i]["name"])).grid(row=i+1,column=1)
			Label(roota5, text=str(y[i]["src_departure_time"])).grid(row=i+1,column=4)
			Label(roota5, text=str(y[i]["dest_arrival_time"])).grid(row=i+1,column=5)
			Label(roota5, text=str(y[i]["travel_time"])).grid(row=i+1,column=6)
			Label(roota5, text=str(y[i]["from_station"]["name"])).grid(row=i+1,column=7)
			Label(roota5, text=str(y[i]["to_station"]["name"])).grid(row=i+1,column=8)
			m=0;
			n=y[i]["classes"]
			while m<8:
				Label(roota5, text=str(n[m]["code"])).grid(row=i+1,column=9+m)
				m=m+1
			m=0;
			n=y[i]["days"]
			while m<7:
				Label(roota5, text=str(n[m]["runs"])).grid(row=i+1,column=17+m)
				m=m+1

			i=i+1

	else : 
		messagebox.showinfo("Invalid", "No Record Found")
	
		print("record is not found for given request") 

def u6():
	val1= str(e6.get())
	val2=str(f6.get())
	st=val2
	
	os.system('python a.py '+val1+' '+st)

def v1():
	global root1
	root1 = Toplevel()
	root1.title('Live Status')
	root1.focus_set()
	Label(root1, text="Train No.").grid(row=0)
	Label(root1, text="Date").grid(row=1)
	global e1
	global f1
	e1 = Entry(root1, width=15)
	e1.grid(row=0, column=1)
	f1 = Entry(root1, width=15)
	f1.grid(row=1, column=1)
	
	b = Button(root1,text='Get Status',width=15,command=u1)
	b.grid(row=2, column=1)


def v2():
	global root2
	root2 = Toplevel()
	root2.title('PNR Status')
	root2.focus_set()
	Label(root2, text="PNR No.").grid(row=0)

	b = Button(root2,text='Get Status',width=15,command=u1)
	b.grid(row=2, column=1)
	global e2
	e2 = Entry(root2, width=15)
	e2.grid(row=0, column=1)


def v3():
	global root3
	root3 = Toplevel()
	root3.title('Train Route')
	root3.focus_set()
	Label(root3, text="Train No.").grid(row=0)

	b = Button(root3,text='Get Route',width=15,command=u3)
	b.grid(row=2, column=1)
	global e3
	e3 = Entry(root3, width=15)
	e3.grid(row=0, column=1)




def v4():
	global root4
	root4 = Toplevel()
	root4.title('Fare')
	root4.focus_set()
	Label(root4, text="Train No.").grid(row=0)
	Label(root4, text="Souce Station code").grid(row=1)
	Label(root4, text="Desti Station code").grid(row=2)
	
	Label(root4, text="Date").grid(row=3)
	Label(root4, text="Class code").grid(row=4)
	Label(root4, text="Quota code").grid(row=5)
	Label(root4, text="Age").grid(row=6)
	b = Button(root4,text='Get Fare',width=15,command=u4)
	b.grid(row=7, column=1)
	global e4
	e4 = Entry(root4, width=15)
	e4.grid(row=0, column=1)
	global f4
	f4 = Entry(root4, width=15)
	f4.grid(row=1, column=1)
	global g4
	g4 = Entry(root4, width=15)
	g4.grid(row=2, column=1)
	global h4
	h4 = Entry(root4, width=15)
	h4.grid(row=3, column=1)
	global i4
	i4 = Entry(root4, width=15)
	i4.grid(row=4, column=1)
	global j4
	j4 = Entry(root4, width=15)
	j4.grid(row=5, column=1)
	global k4
	
	k4 = Entry(root4, width=15)
	k4.grid(row=6, column=1)


def v5():
	global root5
	root5 = Toplevel()
	root5.title('Train List')
	root5.focus_set()
	Label(root5, text="Source").grid(row=0)
	Label(root5, text="Destination").grid(row=1)
	Label(root5, text="Date").grid(row=2)
	b = Button(root5,text='Get Trains',width=15,command=u5)
	b.grid(row=3, column=1)
	global e5
	e5 = Entry(root5, width=15)
	e5.grid(row=0, column=1)
	global f5
	f5 = Entry(root5, width=15)
	f5.grid(row=1, column=1)
	global g5
	g5 = Entry(root5, width=15)
	g5.grid(row=2, column=1)
	



def v6():
	global root6
	root6 = Toplevel()
	root6.title('Seat Availability')
	root6.focus_set()
	Label(root6, text="Train No.").grid(row=0)
	Label(root6, text="Date").grid(row=1)
	b = Button(root6,text='Get Availability',width=15,command=u6)
	b.grid(row=3, column=1)
	global e6
	e6 = Entry(root6, width=15)
	e6.grid(row=0, column=1)
	global f6
	f6 = Entry(root6, width=15)
	f6.grid(row=1, column=1)

global root
root = Tk()
root.title("Indian Railways")
root.geometry("430x150")
	
global cou
cou=1
	
Label(root, text='Main Menu').grid(row=0, column=1)
b = Button(root,text='Live Status',width=15,command=v1)
b.grid(row=1, column=0)
b = Button(root,text='PNR Status',width=15,command=v2)
b.grid(row=1, column=1)
b = Button(root,text='Train Route',width=15,command=v3)
b.grid(row=1, column=2)

b = Button(root,text='Fare',width=15,command=v4)
b.grid(row=2, column=0)
b = Button(root,text='Trains Between Stn',width=15,command=v5)
b.grid(row=2, column=1)
b = Button(root,text='Seat Availability',width=15,command=v6)
b.grid(row=2, column=2)
root.mainloop()


#importing required modules
import json,csv
roomno=[] 
data =[]
#rooms=[]
#This function to store the customer details into a data source

def data_store():
    with open('customer_data.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile,dialect='excel')
        csvwriter.writerow(roomno)
        csvfile.close()
    
        roomno.clear()
class hotel():
	def __init__(self):
		print("Hotel allocation")
#checkin module for the checkin to hotel, take details of customer and allocate room number
	def CheckIn(self):
		global rooms
		
		Budget = input("Enter your budget:")
		if Budget in rooms.keys(): # 1000 or 2000 or 3000 or 4000 or 5000:
			print("Room Allocatting based on Budget")
			for check in rooms[Budget]:
				if rooms[Budget][check]["name"]=="" and rooms[Budget][check]["phno"]=="":
					Name = input("Enter your name :")
					phno = input("Enter your Number: ")
					print("""Room Booked successfully
					Room NO :""",check)
					rooms[Budget][check]["name"]=Name
					rooms[Budget][check]["phno"]=phno
				
					roomno.append("Name: "+Name+" - Contact: "+str(phno)+" - Roomno : "+str(check))
					data_store()

					break
			else:
				print("sorry in your budget all rooms are full..")
		else:
			print("No Rooms on your Budget...")

	#The checkout function for the customer checkout the room, take the details and roomno update to data source
	def CheckOut(self):
		print("checking out customer")
		global rooms
		RoomNO = input("Enter your Room No:")
		if len(RoomNO)!=0:
			floorno = str(int(RoomNO[0])*1000)
			Name = input("Enter your Name:")
			if floorno in rooms.keys():
				#print(rooms[floorno].keys(),RoomNO)
				if RoomNO in rooms[floorno].keys():
					#print("room ocup")
					if Name == rooms[floorno][RoomNO]["name"]:
						print("valid credentials")
						rooms[floorno][RoomNO]["name"]=""
						rooms[floorno][RoomNO]["phno"]=""                 
						print("Thanks For visiting our hotel") 
						data.append("Name :"+Name+" - RoomNo :"+RoomNO)
					else:
						print("invalid details")
				else:
					print("wrong details")
		else:
			print("wrong input")
    
class customer():
#customer_data function to return the details of residing in a given room
	def Customer_Data(self):
		RoomNo = input("Enter Room NO:")
		if len(RoomNo)!=0:
			floorno = str(int(RoomNo[0])*1000)
			if floorno in rooms.keys():
				if RoomNo in rooms[floorno].keys():
					for i in rooms.values():
						for j in i.keys():
							if RoomNo==j:
								d=list(i[j].values())
								print("People are staying in this room:-"+" Name:",d[0]," Phno:",d[1])
								break		
				else:
					print("Incorrect RoomNo..Please check Room No.")
		
            
#this is main method the program interpreting from here
if __name__=="__main__":
	h=hotel()
	c=customer()
while True:
        with open("data.json","r") as my_data:
            my_data1 = my_data.read()
            rooms = (json.loads(my_data1))
        print("######## Welcome To The Hotel DevOps ######")
        print('''   1.CheckIN
    2.CheckOut
    3.Customer Data of residing room
    4.Exit
        ''')
        choice = input("Enter your Chouice:")
        if choice=="1" or (choice).lower()=="checkin":
            h.CheckIn()
        elif choice=="2" or (choice).lower()=="checkout":
            h.CheckOut()
        elif choice=="3" or (choice).lower()=="customer Data":
            c.Customer_Data()
        elif choice=="4" or (choice).lower()=="exit":
            exit()
            
        with open ('data.json','w') as delete_data:
            delete_data.write(json.dumps(rooms)) 
    
    




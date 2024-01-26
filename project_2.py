## Project_Title: TIP CALCULATOR

print("Welcome to the tip calculator")
total_bill=input("What was the total bill?\n₹")
percentage_tip=input("What percentage tip would you like to give (10, 12, 15) ?\n")
total_num_of_people=input("How many people to split the bill?\n")
total_tip=(int(percentage_tip)/100)*float(total_bill)
total_billwithtip=float(total_bill)+total_tip
tip_individual=total_billwithtip/int(total_num_of_people)
print(f"Each person should pay: ₹{round(tip_individual,2)}")
## Project_Title: TIP CALCULATOR

print("Welcome to the tip calculator")
total_bill=input("What was the total bill?\n₹")
percentage_tip=input("What percentage tip would you like to give (0, 10, 12, 15) ?\n")
total_num_of_people=input("How many people to split the bill?\n")
total_tip=(int(percentage_tip)/100)*float(total_bill)
total_billwithtip=float(total_bill)+total_tip
tip_individual=total_billwithtip/int(total_num_of_people)
final_amount="{:.2f}".format(tip_individual)
print(f"Each person should pay: ₹{final_amount}")

## if round function doesn't work properly then use the following code
# "{:.2f}".format(tip_individual)
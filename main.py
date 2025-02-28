

print("Welcome to the tip calculator")

bill = float(input("what Was the total Bill ? $"))
tip = int (input("How much tip would you like to give ?  10$,20$,30$,40$,50$"))
people = int(input("How many people to Split the Bill?"))

# 10/100 or 12/100 or 15/100

tip_as_percent = tip/100
total_tip_amount =bill*tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,1)

print(f"Total Bill per Person ! $ {final_amount}")
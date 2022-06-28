expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum_not_a_func = 0

for x in expenses:
    sum_not_a_func = sum_not_a_func + x
print("You spent $" + str(sum_not_a_func))
print("You spent $", sum_not_a_func) #the comma can replace the + and we don't need to call str()
print("You spent $", sum_not_a_func, " on lunch this week.", sep="") #sep sets what the separator should be, in the above print() $ sum_not_a_func is with a space, with sep the space is gone

total = sum(expenses) #sum() is already a function in Python, it takes inside of it an iterable, so this already does the for
print("You spent $", total, " on lunch this week.", sep="")

#asking for qty of expenses
usr_expenses = []
num_expenses = int(input("\nEnter the number of expenses: "))

for i in range(num_expenses):
    usr_expenses.append(float(input("Enter the value of the expese:")))

total_usr = sum(usr_expenses)
print("You spent $", total_usr, sep="")
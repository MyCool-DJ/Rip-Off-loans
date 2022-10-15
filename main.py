print("I am your AI banker, you wanted a loan")
loan = (int(input("Enter the amount you want to borrow here: ")))
apr = 0.05
print("The amount of interest you will pay per year at 5% interest on your loan of", loan, "is")
for i in range(10):
	loan += (loan*apr)
	print("Year", i+1, "is", round(loan,2))
print("Thank you for choosing our rip-off bank")

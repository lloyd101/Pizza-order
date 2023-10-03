# Name = Lloyd Ngaindjo
# Student # = 251301088
# Email = lngindj@uwo.ca

year = int(input("Please enter the year that you want to calculate the personal interest: "))
# This Value represents the year at which the user wants to calculate interest for.
numExpen = int(input("Please enter the number of expenditure categories:"))
# This value indicates the number of expenditure categories they spent money on
totalPrevExp = 0.0
# This variable represents the number of total expenses of previous year
totalYofExp = 0.0
# This value indicates the number of total expenses for the year of interest

while numExpen > 0:
# the loop will keep running as long as the number of categories is not 0
    PrevExp = int(input("Please enter expenses for previous year:"))
    # Prompt to expense
    totalPrevExp = totalPrevExp + PrevExp
    yofExp = int(input("Please enter expenses for year of interest:"))
    totalYofExp = totalYofExp + yofExp
    numExpen = numExpen - 1  # this equation helps determine the end of the loop by subtracting 1 from the number
    # of numExpen indicated by the user, as shown in the while loop, the loop runs again as long as the numExpen
    # is greater than 0

inf_rate = ((totalYofExp - totalPrevExp) / totalYofExp) * 100
# This formula helps us find the inflation rate of the user

print("Personal inflation rate for {} is".format(year), inf_rate, "%")
# This prints out the inflation rate percentage

Inflation_type = " "
if inf_rate < 3:
    Inflation_type = "low"
    # this if-statement to print out the type of inflation rate if inf_rate is smaller than 3%
elif inf_rate >= 3 and inf_rate < 5:
    Inflation_type = "moderate"
    # this if-statement to print out the type of inflation rate if inf_rate is greater than 3% and smaller than 5%
elif inf_rate >= 5 and inf_rate < 10:
    Inflation_type = "high"
    # this if-statement to print out the type of inflation rate if inf_rate is greater than 5% and smaller than 10%
elif inf_rate >= 10:
    Inflation_type = "hyper"
    # this if-statement to print out the type of inflation rate if inf_rate is greater than 10%

print("Type of inflation: ", Inflation_type)
# this prints out the type of inflation depending on the type of inflation

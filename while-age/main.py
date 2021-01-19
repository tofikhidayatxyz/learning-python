import time

# Define current year
currentYear = int(time.strftime('%Y'))

# input
print('Masukan tahun lahir: ')
loopYear = int(input(':'))

# loop years
while loopYear <= currentYear:
    print(f"Tahun { loopYear } \n")
    loopYear += 1
    
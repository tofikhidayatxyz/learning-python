userData = {}
inputNewUser = 'Y'

while(inputNewUser.lower() == 'y') :
    #input from console
    print('Masukan data nama pengguna : ')
    userName = input()
    print('Masukan data umur pengguna : ')
    userAge = int(input())
    #assign to object
    userData[userName] = userAge

    #promp need reinput
    print('Masukan data lagi ? [Y/N]')
    inputNewUser = input()

# output

print("\n=========== Output ============\n")
loopIndex = 0
for key, value in userData.items() :
    loopIndex += 1
    print(f"{ loopIndex }. Orang dengan nama { key }")
    print(f"{ loopIndex }. Berumur { value } tahun")
    print("\n==========================\n")

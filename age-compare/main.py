import time
from functools import reduce

# Global variabel
currentYear = int(time.strftime('%Y'))
userData = []

# Get Age Function
getAge = lambda born : abs(currentYear - born)

# Input From console
inputNewData = 'Y'
while(inputNewData.lower() == 'y') :
    userObject = {}
    print('Masukan nama : ')
    userObject['name'] = input()
    print('Masukan tahun lahir : ')
    userObject['born'] = int(input())
    userData.append(userObject)
    userObject = {}
    print('Ingin menambah user ? [Y/N]')
    inputNewData = input()

# Filter user by youngest
userData = sorted(userData, key= lambda x: getAge(x['born']), reverse=True)
# Find user with oldest
olderUser = reduce(lambda x, y : x if getAge(x['born']) > getAge(y['born']) else y, userData)
# Print result to console
print("\n\n===================================\n")
print(f"{olderUser['name']} adalah orang paling tua dengan umur {getAge(olderUser['born'])} tahun")
print("Dengan perbedan umur dengan yang lain adalah : ")
print("===================================")
# Compare oldest user with another user
for index, user in enumerate(userData) :
    if user['name'] != olderUser['name']:
        print(f"No : {index}")
        print(f"Nama : {user['name']}")
        print(f"Umur : {getAge(user['born'])} tahun")
        print(f"Selisih umur : {abs(getAge(user['born']) - getAge(olderUser['born']))} tahun")
        print("===================================")
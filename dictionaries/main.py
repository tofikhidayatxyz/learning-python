about = {}
isInsert = 'Y' 
hobbies = []

# Nama
print('Siapa nama kamu ?')
about['nama'] = input()
# #nim
print('Brapa NIM kamu ?')
about['nim'] = input()
# #alamat
print('Dimana kamu tinggal ?')
about['alamat'] = input()

#hobby
while(isInsert.lower() == 'y' ) :
    print('Masukan Hobby kamu : ')
    newHobby = input()
    hobbies.append(newHobby)
    print('Isi hobby lagi ? : [Y/N] ')
    isInsert = input()

about['hobbies'] =  hobbies

# Output
print('\n\n========= Output =========\n\n')
for key, value in about.items():
    # check instance is list
    if isinstance(value, list):
        print('Hobby Kamu adalah : ')
        #looping hobbies
        for index, hobby in enumerate(value):
            print('\t' + str(index + 1) + '. ' +   hobby)
    else:
        print(key.capitalize() + ' kamu adalah :' + value + '\n')
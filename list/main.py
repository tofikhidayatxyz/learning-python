
# Learning 3 
# Hobby

# Define variable as array
hobbies = []
# running code
isInsert = 'Y' 

while(isInsert.lower() == 'y' ) :
    print('Masukan Hobby kamu : ')
    newHobby = input()
    hobbies.append(newHobby)
    print('Isi lagi ? : [Y/N] ')
    isInsert = input()

print('Hobby Kamu adalah : ')
for index, hobby in enumerate(hobbies):
    print('\t' + str(index + 1) + '. ' +   hobby)
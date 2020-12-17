print('Siapa Nama Kamu ? ')
name = input()
print('Apa NIM Kamu ? ')
nim = input()
print('Apa Aja Hobby Kamu ? (Pisahkan dengan koma)')
hobbies = input()


print("||================||")
print('Nama Kamu adalah : '+ name)
print('NIM Kamu adalah : '+ nim)
print('Hobby kamu adalah : ')

for index, hobby in enumerate(hobbies.split(',')):
    print('\t' + str(index + 1) + '. ' +   hobby)
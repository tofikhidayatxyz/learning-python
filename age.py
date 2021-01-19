import time

currentYear = int(time.strftime('%Y'))

myName = input()
myBorn = int(input())
myAge = abs(currentYear - myBorn)

friendName = input()
friendBorn = int(input())
friendAge = abs(currentYear - friendBorn)

print(f"Umur ku {myAge}")
print(f"Umur Temanku {friendAge}")

if(myAge > friendAge) :
    print(f"Aku lebih tua daripada temanku {friendName}")
    print(f"Selisih kami adalah {abs(friendBorn - myBorn)}")
elif (myAge == friendAge) :
    print(f"Aku sama dengan temanku {friendName}")
else :
    print(f"Temanku {friendName} lebih tua daripada aku")
    print(f"Selisih kami adalah {abs(friendBorn - myBorn)}")



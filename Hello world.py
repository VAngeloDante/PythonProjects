my_name = "Mateusz"
my_age = 33
my_hobby = "Magic"

array = [[0 for _ in range(5)] for _ in range(5)]  # 5x5 array filled with zeros
array_2 = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]  # 5x5x5 array filled with zeros

print(f"Hello, my name is {my_name}, I'm {my_age} old and my favourite hobby is {my_hobby}")
print(f"in order to properly print strings with varialbles you should use f-prints")
print(array)
print(array_2)


userInput_Age = input("Type your age and press Enter: ")
userInput_Name = input("Type your name and press Enter: ")
userInput_Hobby = input("Type your hobby and press Enter: ")
print(f"Hello, my name is {userInput_Name}, I'm {userInput_Age} old and my favourite hobby is {userInput_Hobby}")
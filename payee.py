import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's names,separated by a comma.")
names = namesAsCSV.split(",")
items = len(names)
random_answer = random.randint(0,items - 1)
payee = names[random_answer]
print(payee + " will buy the meal today!")


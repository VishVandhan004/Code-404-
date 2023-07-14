a = float(input("probability of friday and absent: "))
b = float(input("probability of friday: "))
absentandfriday = a/b
# we are finding that the student is absent on friday. so, P(Absent given that Friday) = P(being friday and absent) / P(friday)
print("final answer:",absentandfriday)

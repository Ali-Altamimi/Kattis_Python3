life_periods = int(input())
QALY = 0
for x in range(life_periods):
    quality_of_life, number_of_years = input().split(' ')
    QALY += float(quality_of_life) * float(number_of_years)

print(QALY)

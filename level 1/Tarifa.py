megabytes_per_month = int(input())
months = int(input())
megabytes_spend = 0
for i in range(months):
    megabytes_spend += int(input())

print((megabytes_per_month * (months + 1)) - megabytes_spend)
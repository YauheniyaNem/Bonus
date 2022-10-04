import math

name1 = input()
base1 = float(input())

name2 = input()
base2 = float(input())

name3 = input()
base3 = float(input())


def round_up(n, decimals=-1):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
    
brutto_bonus1 = round_up(base1 * 100 / 86, -1)
brutto_bonus2 = round_up(base2 * 100 / 86, -1)
brutto_bonus3 = round_up(base3 * 100 / 86, -1)

income_tax1 = round(brutto_bonus1 / 100 * 13, 2)
income_tax2 = round(brutto_bonus2 / 100 * 13, 2)
income_tax3 = round(brutto_bonus3 / 100 * 13, 2)

netto_bonus1 = round(brutto_bonus1 - income_tax1 - brutto_bonus1 /100 * 1, 2)
netto_bonus2 = round(brutto_bonus2 - income_tax2 - brutto_bonus2 /100 * 1, 2)
netto_bonus3 = round(brutto_bonus3 - income_tax3 - brutto_bonus3 /100 * 1, 2)

pension_contribution = round((brutto_bonus1 + brutto_bonus2 + brutto_bonus3) /100 * 35, 2)
insurance_fee = round((brutto_bonus1 + brutto_bonus2 + brutto_bonus3) /100 * 0.6, 2)

print(name1.upper(), "                    ", base1)
print("Премия", brutto_bonus1)
print("Подоходный налог", income_tax1)
print("К выплате", netto_bonus1, "\n")


print(name2.upper(), "                    ", base2)
print("Премия", brutto_bonus2)
print("Подоходный налог", income_tax2)
print("К выплате", netto_bonus2, "\n")

print(name3.upper(), "                    ", base3)
print("Премия", brutto_bonus3)
print("Подоходный налог", income_tax3)
print("К выплате", netto_bonus3, "\n")

print ("ФСЗН", pension_contribution)
print("Белгосстрах", insurance_fee)



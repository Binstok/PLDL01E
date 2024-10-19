
start = 180.00
end = 922.50
step = 22.50

current = start
while current < end:
    print("SSS Contribution:", current)
    current += step

print("===============================================================================")

compensation_ranges = [
    {"range": "P20,833 and below", "tax": 0.00},
    {"range": "P20,833 - P33,332", "tax": "0.00 + 15% over P20,833"},
    {"range": "P33,333 - P66,666", "tax": "P1,875.00 + 20% over P33,333"},
    {"range": "P66,667 - P166,666", "tax": "P8,541.80 + 25% over P66,667"},
    {"range": "P166,667 - P666,666", "tax": "P33,541.80 + 30% over P166,667"},
    {"range": "P666,667 and above", "tax": "P183,541.80 + 35% over P666,667"},
]

for i, range_data in enumerate(compensation_ranges):
    print(f"Bracket {i+1}: {range_data['range']}")
    print(f"Tax: {range_data['tax']}\n")

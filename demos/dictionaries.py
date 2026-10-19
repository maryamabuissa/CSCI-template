

height_in_inches = {"Joe": 68, "Sara": 60, "Laurel": 73}

print(height_in_inches)

for name, inches in height_in_inches.items():
    print(f"{name} is {inches // 12} feet {inches % 12} inches tall")

fruit_prices = {}

fruit_prices["orange"] = 1
fruit_prices["banana"] = 0.2
fruit_prices["watermelon"] = 7
fruit_prices["orange"] = 2
fruit_prices["pinapple"] = 7
print(fruit_prices)
print(len(fruit_prices))

print(fruit_prices["apple"]) # keyerror

if "apple" in fruit_prices:
    print(fruit_prices["apple"]) # keyerror
if 7 in fruit_prices:
    print(fruit_prices[7]) # not what we want

if 7 in fruit_prices.values():
    for fruit in fruit_prices:
        if fruit_prices[fruit] == 7:
            print(fruit)

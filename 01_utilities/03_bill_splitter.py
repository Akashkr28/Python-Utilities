def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

num_people = int(input("Enter the number of people: "))
names = []

for i in range(num_people):
    name = input(f"Enter the name of person #{i + 1}: ").strip()
    names.append(name)

total_bill = get_float("Enter the total bill amount in number only: ")

share = round(total_bill / num_people, 2)

print("\n" + "*" * 40)
print(f"Total Bill: {total_bill}")
print(f"Each person should pay: {share}")

for name in names:
    print(f"{name}: {share}")

print("\n" + "*" * 40)
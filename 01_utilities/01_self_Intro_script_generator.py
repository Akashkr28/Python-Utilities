import datetime

name = input("What is your name? ").strip()
age = input("How old are you? ").strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your favorite hobby? ").strip()

intro_message = (
    f"Hello my name is {name}. I'm {age} years old, I live in {city}."
    f"I work as a {profession} and I absolutely enjoy {hobby} in free time."
    f" Nice to meet you!"
)

current_date =  datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"


border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"
print("\n" + final_output)
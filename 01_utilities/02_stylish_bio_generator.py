import textwrap
name = input("Enter your name: ").strip()
profession = input("Enter your profession: ").strip()
passion = input("What are you passionate about? ").strip()
emoji = input("Choose an emoji that represents you: ").strip()
website = input("Enter your personal or professional website URL: ").strip()

print("\nChoose a style for your bio: ")
print("1. Simple Line ")
print("2. Vertical Flair ")
print("3. Emoji Sandwich ")

style = input("Enter 1, 2, or 3: ").strip()

def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n💡 {passion} \n {website}"
    elif style == "2":
        return f"{emoji} {name}\n {profession}🔥\n {passion} \n {website}🔥"
    elif style == "3":
        return f"{emoji*3}\n {name} - {profession}\n {passion}\n {website} \n {emoji*3}"
    
bio = generate_bio(style)

print("\nHere is your stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a file? (y/n): ").lower()

if save == 'y':
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print(f"Bio saved")
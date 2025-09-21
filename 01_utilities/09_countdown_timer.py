import time

while True:
    try:
        seconds =int(input("⏰Enter the time in seconds: "))
        if seconds < 1:
            print("❌ Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("❌ Please enter a valid number.")

print("\n 🔔 Timer Started...")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"⏱️ Time Left: {time_format}", end="\r")
    time.sleep(1)

print("\n 🎉 Time's Up! take a break or Move on to next task")
print("\a")
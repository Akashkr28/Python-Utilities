import datetime

enrty = input("What did you learn today? ").strip()
rating = input("⭐️ How productive was the day? (1-5): ").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")

journal_entry = f"\n 🗓️ {date_str}\n{enrty}"
if rating:
    journal_entry += f"\n Productivity Raating: {rating}\n"
journal_entry += "\n" + "-" * 50

with open("Learning_journal.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print("\n Journal entry saved successfully to 'Learning_journal.txt' file.")
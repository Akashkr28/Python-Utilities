1. Challenges Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.
# Your Program should do the following:
    1. Ask the user for their name, age, city, profession, and favorite hooby.
    2. Format this data into a warm, friendly paragraph of self-introduction.
    3. Print the final paragraph in a clean and readable format.

## Example Output:
    # If the user inputs: -
        1. Name: kash
        2. Age: 29
        3. City: Jamshedpur
        4. Profession: Software Developer
        5. Hobby: Playing Guitar

### Your Script might output:
    "Hello! My name is Akash. I'm 29 years old and live in Jamshedpur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

#### Bonus:
    - Add the current date to the end of the paragraph like:
    "Logged on: 2025-09-17"
    - Wrap the printed message with a decorative border of stars (*).

---------------------------------------------------------------------------------------------------
2. Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility thst ask the user for a few key details and generats a short, stylish bio that could be used for social media platform like Instagram or Twitter.

# Your Program should
    1. Prompt the user to enter their:
        - Name
        - Profession
        - One-Liner Passion or goal
        - Favorite emoji (optional)
        - Website or handle (optional)
    
    2. Generate as stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

    3. Add optional hastags or emoji for  flair.

## Example:

Input:
    Name: Priya
    Profession: Designer
    Passion: Making things look good
    Emoji: 🎨
    Website: www.priyadesigns.com

Output:
    🎨 Riya | Designer
    💡 Making things look good
    🌟 www.priyadesigns.com

### Bonus:
    - Let the user pick from 2-3 different layout styles.
    - Ask the user if they want to save the result into a `.txt` file.

---------------------------------------------------------------------------------------------------
3. Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

# Your Progrem should:
    1. Ask how many people are in the group.
    2. Ask for each person's name.
    3. Ask for the total bill amount.
    4. Calculate the amount each person should pay.
    5. Display how much each person owes in a clean and readable format.

## Example:
    Total Bill: ₹1200
    People: Aman, Neha, Ravi

    Each Person Owes: ₹400

## Final Output:
    Aman owes: ₹400
    Neha owes: ₹400
    Ravi owes: ₹400

### Bonus:
    - Round to 2 decimal places
    - Print a decorative summary box

---------------------------------------------------------------------------------------------------
4. Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

# Your Program should:
    1. Ask the user for for their age in years (accept float values too).
    2. Convert that age into:
        - Total days
        - Total hours
        - Total minutes
    3. Display the results in a readable format.

## Assumptions:
    - You can use 365.25 days/year to account for leap years.
    - You don't need to handle time zone or exact birthdates in this version.

## Example:
    Input:
        Age: 25

    Output:
        You are approximately:
            - 9,131 days old
            - 219,144 hours old
            - 13,148,640 minutes old

### Bonus
    - Add comma formatting for large number.
    - Let the user try again without restarting the program

---------------------------------------------------------------------------------------------------
5. Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and add emojis after specific keywords to make it more expressive.

# Your Program should:
    1. Ask the user to input a message.
    2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
    3. Print the updated message with emojis.

## Example:
    Input:
        I love to code and drink tea when I'm happy.

    Output:
        I 🎉 love to code and 🍵 tea when I'm happy 😎.

### Bonus:
    - Make it case-sensitive (match "Happy" or "happy")
    - Handle punctuation (like commas or periods right after keywords)

---------------------------------------------------------------------------------------------------
6. Challenge: Daily Learning Journal Logger

Build a python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt`
file along with a timestamp.

# Your Program should:
    1. Ask the user what they learned today.
    2. Add the entry to a file called `learning_journal.txt`.
    3. Each entry should include the date and time it was written.
    4. The journal should **append** new entries rather than overwrite.

### Bonus
    - Add an optional rating (1-5) for how productive the day was.
    - Show a confirmation message after saving the entry.
    - Make sure the format is clean and easy to read when opening the file.

## Example:
    🗓️ 2025-09-20 - 14:15 PM
    Today I learned about how list comprehensions work in Python!
    Productivity Rating: 4/5

---------------------------------------------------------------------------------------------------
7. Challenge: Terminal-Based Task List Manager

Create a Python script that lets user manage a to-do list directly from the terminal.

# Your Program should:
    1. Allow user to:
        - Add a task
        - View all tasks
        - Mark a task as completed
        - Remove a task
        - Exit the app
    2. Save all tasks in a text file named `tasks.txt` so data persists between sessions.
    3. Display tasks with an index number and a  ✔️ if the task is completed.

## Example Menu:
    1. Add Task
    2. View Tasks
    3. Mark Task as Completed
    4. Delete Task
    5. Exit

## Example Output:
    Your Tasks:
        Buy Groceries || not_done
        Finih Python Project || done
        Read a Book || not_done

### Bonus:
    - Prevent empty tasks from being added.
    - Validate tasks number before completing/deleting.

---------------------------------------------------------------------------------------------------
8. Challenge: Password Strength Checker and & Suggestion Tools

Build a Python script that checks the strength of a password based on:
    1. Length (at least 8 characters).
    2. At least one uppercase letter.
    3. At least one lowercase letter.
    4. At least one digit.
    5. At least one special character.

# Your Program should:
    - Ask the user to input a password.
    - Tell them what's missing if it's weak
    - If the password is strong, confirm it.
    - Suggest a strong random password if the input is weak.

### Bonus:
    - Hide password input using `getpass` (no echo on screen).

---------------------------------------------------------------------------------------------------
9. Challenge: Set a Countdown Timer

Create a Python script that allows the users to set a timer in seconds. The script should:

# Your Program should:
    1. Ask the user for the number of seconds to set the timer.
    2. Show a live countdown in the terminal.
    3. Notify the user when thr timer ends with a final message and sound (if possible).

### Bonus:
    - Format the remaining time as MM:SS
    - Use a beep sound (`\a`) at the end if the terminal supports it.
    - Prevents negative or non-integer inputs.

---------------------------------------------------------------------------------------------------
10. Challenge: Building a Caesar Cipher (Secret Message Encryptor and Decryptor)

Create a Python Script that helps you send secret message to your friend usind simple encryption.

# Your Program should:
    1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
    2. If Encryption is selected:
        - Ask for a message and a numeric secret key.
        - Use a Caesar Cipher (shift letters by the key value).
        - Output the encrypted message.
    3. If Decryption is selected:
        - Ask for the message and key.
        - Reverse the encryption to get the original message.

# Rules:
    - Only encrypt letters; leave spaces and punctuations as-is.
    - Make sure the letters wrap around (e.g., 'z' + 1 -> 'a').

### Bonus:
    - Allow uppercase and lowercase letters handling.
    - Show a clean interface.

---------------------------------------------------------------------------------------------------
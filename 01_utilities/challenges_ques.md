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
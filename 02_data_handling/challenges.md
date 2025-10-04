1. Challenge: CLI Contact Book (CSV-Powered)

    Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

    ## Your Programs should:
        1. Ask the user ti choose one of the following options:
            - Add a new contact
            - View all contacts
            - Search for a Contact by name
            - Exit
        2. Store Contacts in a file called `contacts.csv` with columns:
            - Namw
            - Phoen
            - Email
        3. If the file doesn't exist, create it automatically.
        4, Keep the Interface clean and clear.

    ## Example Output:
        1. Add a new contact
        2. View all contacts
        3. Search for a Contact 
        4. Exit

    ## Bonus:
        - Format the contact list in a table-like view.
        - Allow Partial match search.
        - Prevent duplicates names for being added.

---------------------------------------------------------------------------------------------------
2. Challenge: Student Marks Analyzer

    Create a pyhton program that allows a user to input student names along with their markss and then calculate useful statistics.

    ## Your Program should:
        1. Let the user input multiple students with their marks(name + integer score).
        2. After input is complete, display
            - Average Marks
            - Highest Marks and Student(s) who scored it
            - Lowest marks and student(s) who scored it
            - Total number of students

    ## Bonus:
        - Allow the user to enter all data first, then view the report.
        - Format output clearly in a report-style layout.
        - Prevent duplicate students names.

---------------------------------------------------------------------------------------------------
3. Challenge: Personal Movie Tracker with JSON

    Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDB

    ## Your Program should:
        1. Store all movie data in a `movie.json` file.
        2. Each movie should have:
            - Title
            - Genre
            - Rating (out of 10)
        3. Allow the user to:
            - Add a movie
            - View all movies
            - Search movies by title or genre
            - Exit the app
    
    ## Bonus:
        - Prevent duplicates title from being added.
        - Format output in a clean table.
        - Use JSON for reading/writing structured data.

---------------------------------------------------------------------------------------------------
4, Challenge: Real-Time Weather Logger (API + CSV)

    Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

    ## Your Program should:
        1. Ask the user for a city name.
        2. Fetch weather data using the OpenWeatherMap API.
        3. Store the followning in a CSV file (`weather_log.csv`):
            - Date (auto-filled as today's date)
            - City
            - Temprature (in Celsius)
            - Weather Condition(e.g. Clear, Rain)
        4. Prevents duplicates entries for the same city on the same day.
        5. Allow user to:
            - Add new weather log
            - View all logs
            - Show average, highest, lowest tempratures, and most frequent conditions

    ## Bonus:
        - Format output in a clean table.
        - Handle API failures and invalid city names gracefully.

---------------------------------------------------------------------------------------------------
6. Challenge: JSON-to-Excel Converter Tool

    Create a python utility that reads structured data (like you'd get from an API) from a `.json` file
    and convert it to a CSV file that can be opened in Excel.

    ## Your Program Should:
        1. Read from a file named `api_data.json` in the same folder.
        2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
        3. Automatically extract field names such as CSV headers
        4. Handle nested structures by flattening or skipping them.

    ## Bonus:
        - Provide feedback on how many records were converted.
        - Allow users to define which fields to extract.
        - Handle missing fields gracefully.

---------------------------------------------------------------------------------------------------
8. Challenge: JSON Flattener

{
    "user": {
        "id": 1,
        "name": "Riya",
        "email": "riya@example.com",
        "address": {
            "city": "Delhi",
            "pincode": 110001
        }
    },
    "roles": ["admin", "wditor"]
    "is_active": true
}

Flatten this to:

{
    "user.id": 1,
    "user.name": "Riya",
    "user.email": "riya@example.com",
    "user.address.city": "Delhi",
    "user.address.pincode": 110001,
    "roles": ["admin", "wditor"]
    "is_active": true
}

---------------------------------------------------------------------------------------------------
9. Challenge: Offline Credential Manager

    Create a CLI tool to manage login credentials (website, username, password) in a encoded local file (`vault.txt`).

    ## Your Program should:
        1. Add new credentials (website, username, password)
        2. Automatically rate password strength (weak, medium, strong)
        3. Encode the saved content using Base64 for simple offline obfuscation.
        4. View all saved credentials (decoding them).
        5. Update password for any existing website entry (assignment).

    ## Bonus:
        - Support searching for a website entry
        - Mask password when showing in the list.

---------------------------------------------------------------------------------------------------
10. Challenge: Offline Notes Locker

    Create a terminal based app that allows user to save, view, and search personal notes securely in a encrypted file.

    ## Your Program should:
        1. Let user add notes with title and content.
        2. Automatically encrypt each note using Fernet (AES under the hood).
        3. Store all encrypted notes in a single vault `.vault` file (JSON format).
        4. Allow listing of titles and viewing/decrypting selected notes.
        5. Support searching by title or keyword.

    ## Bonus:
        - Add timestamps to notes.
        - Use a master password to unlock the vault.
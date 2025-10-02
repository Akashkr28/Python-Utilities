01_Task: if-else
    Given an integer, , perform the following conditional actions:

    If  is odd, print Weird
    If  is even and in the inclusive range of  to , print Not Weird
    If  is even and in the inclusive range of  to , print Weird
    If  is even and greater than , print Not Weird

    Input Format
        - A single line containing a positive integer, .

    Output Format
        - Print Weird if the number is weird. Otherwise, print Not Weird.

-------------------------------------------------------------------------------
02_Task: Find the Runner-Up Score!
    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

    Input Format

    The first line contains . The second line contains an array   of  integers each separated by a space.

    Output Format
        Print the runner-up score.

    Sample Input 0
        5
        2 3 6 6 5
    Sample Output 0
        5

-------------------------------------------------------------------------------
03_Task: Nested Lists
    iven the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

    Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

    Example:
        record = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    The ordered list of scores is [37.2, 37.21, 37.21, 39, 41], so the second lowest score is [37.2]. There are two students with that score: ['Tina', 'Harry']. Ordered alphabetically, the names are printed as:

    Harry
    Tina

    Input Format:
        The first line contains an integer, , the number of students.
        The 2N subsequent lines describe each student over 2 lines.
        - The first line contains a student's name.
        - The second line contains their grade.
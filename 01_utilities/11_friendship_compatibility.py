def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeiou')

    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    return min(score, 100)

def run_friendship_calculator():
    print("Friendship Compatibility Calculator")
    name1 = input("Enter the name of Friend A: ").strip()
    name2 = input("Enter the name of Friend B: ").strip()

    score = friendship_score(name1, name2)

    print(f"The friendship score between {name1} and {name2} is: {score}")
run_friendship_calculator()
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # map returns a map object, so first convert it to a list:
    scores = list(arr)
    
    # Use a set to keep only unique scores (to Remove Duplicates):
    unique_scores = set(scores)
    
    # Find the highest score:
    max_score = max(unique_scores)
    
    # Remove it from the set so the next maximum is the runner-up:
    unique_scores.remove(max_score)
    
    # The new maximum of the remaining set is the runner-up:
    runner_up = max(unique_scores)
    
    print(runner_up)
"""Write a function input_scores() that:
· Uses a while loop
. Asks user to enter scores
· Stops when user types -1
· Stores scores in a list
. Returns the list"""

def input_scores():
    scores = []
    
    while True:
        user_input = input("Please enter score (-1 to stop): ")
        score = int(user_input)
        
        if score == -1:
            break
        
        scores.append(score)
    
    return scores


# Test the function
if __name__ == "__main__":
    result = input_scores()
    print(f"Entered scores: {result}")
    print(f"Total scores: {len(result)}")
    if result:
        print(f"Average: {sum(result) / len(result):.2f}")
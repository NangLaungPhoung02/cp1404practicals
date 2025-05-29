import random
def main():
    score = float (input("Enter score:"))
    result = validate_score (score)
    print (result)
    random_score = random.randint(1,100)
    print (f"Random score:{random_score:.2f}")
    print(validate_score(random_score))

def validate_score(score):
    """ Validating the score by the previous garde."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "pass"
    else:
        return "Bad"

main()
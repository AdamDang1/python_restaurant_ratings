"""Restaurant rating lister."""




# put your code here
def read_scores():
    scores_txt = open('scores.txt')
    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)
    
    return scores


def add_restaurant(scores):
    print("Add your new restaurant and rate it up to 5!")
    restaurant = input("Restaurant name: ")
    score = int(input("Score out of 5: "))

    scores[restaurant] = score


def print_sorted_scores(scores):
    for restaurant, score in sorted(scores.items()):
        print(f"{restaurant} is rated a {score} out of 5.")

scores = read_scores()

add_restaurant(scores)

print_sorted_scores(scores)
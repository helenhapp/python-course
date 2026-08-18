import random

movies = [
    "Kiki's Delivery Service",
    "The Matrix",
    "Howl's Moving Castle",
    "Coco"
]

MENU = '''
Choose a command:
v - view the list
a - add a movie
r - remove a movie
p - pick a random movie
q - quit
'''

while True:
    command = input(f"{MENU}> ").strip().lower()

    if command == "v":
        for i in range(len(movies)):
            print(f"{i+1}. {movies[i]}")
        
    elif command == "a":
        movie = input("Movie to add: ")
        if movie:
            movies.append(movie)
        
    elif command == "r":
        movie = input("Movie to remove: ")
        if movie in movies:
            movies.remove(movie)
        else:
            print("This movie isn't in the list.")
            
    elif command == "p":
        print("Tonight's movie:", random.choice(movies))
        
    elif command == "q":
        print("Goodbye!")
        break
    
    else:
        print("Unknown command.\n")
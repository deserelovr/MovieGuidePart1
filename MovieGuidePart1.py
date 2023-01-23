#Jasmine BUmbray
#CIS261
#MovieGuidePart1

def Display_movie():
    print("Movie List\n")
    print("Command Menu")
    print("List - Show all movies")
    print("Add - Add a new movie")
    print("Remove - Delete a movie from list")
    print("Exit - leave the list\n")

def List(movie_list):
    for l, movie in enumerate(movie_list, start=1):
        print(f"{l}. {movies}")

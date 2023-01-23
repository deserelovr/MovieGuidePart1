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
    

def Add(movie_list):
    movie = input("Enter Movie name: ")
    movie_list.append(movie)
    print(f'{movie} has been added.\n')

def Remove(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted.\n")


def main():
   movie_list["Nobody," "Mean Girls," "Boyz N the Hood"]

   display_menu()
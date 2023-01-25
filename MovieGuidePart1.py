#Jasmine BUmbray
#CIS261
#MovieGuidePart1

def display_movielist():
    print("Movie List\n")
    print("Command Menu")
    print("list - Show all movies")
    print("add - Add a new movie")
    print("remove - Delete a movie from list")
    print("done - leave the list\n")

def list(movie_list):
    for m, movie in enumerate(movie_list, start=1):
        print(f"{m}. {movie}")
    print()
    

def add(movie_list):
    movie = input("Enter Movie name: ")
    movie_list.append(movie)
    print(f'{movie} has been added.\n')

def remove(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted.\n")


def main():
   movie_list = ["Nobody",
                "Mean Girls", 
                "Boyz N the Hood"]

   display_movielist()

   while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)   
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            remove(movie_list)  
        elif command.lower() == "done":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("See Ya!")
    

if __name__ == "__main__":
    main()


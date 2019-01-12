def display_menu():
    print("\nWelcome To Our Classic Movies Library")
    print ("------------------------------------\n")
    print("Type (list)  : Display list of all movies")
    print("Type (date)  : To Display the released date of the movies")
    print("Type (rent)  : To Rent A Movie")
    print("Type (add)   : Add a Movie To the list")
    print("Type (delete): Delete/Remove a moive from the list")
    print("Type (exit ) : Exit the Application\n")

def list(movie_list):
    for i in movie_list:
        print(i)
        
import locale
result=locale.setlocale(locale.LC_ALL,'')
if result=='c':
    locale.setlocale(locale.LC_ALL,'en_us')
def dat(movie_list):
    for f in movie_list:
        print(f)
def add (movie_list):
    movie=input("Would You Like Add a Movie ? Enter Name of The Movie\t")
    movie_list.append (movie)
    print("You have add a movie to the library named ",movie,"\n")
    print("************************************************")
    for i in movie_list:
        print(i)

def delete (movie_list):
    mdelete=input ("Which movie would like to remove from the list ?")
    movie_list.remove(mdelete)
   
    for m in movie_list:
        print(m)
def rent (movie_list):
    mrent=input("Enter the name of the movie you want to rent: \t")
    if mrent=='Ben Hur':
        print ("The rent for this movie is " +locale.currency(15,grouping=True))
    elif mrent=='The Queen of Egypt':
        print("The rent for this movie is " +locale.currency(10,grouping=True))
    elif mrent=='Touch of Evil':
        print("The rent for this movie is " +locale.currency(8,grouping=True))
    elif mrent=='Vertigo':
        print("The rent for this movie is " +locale.currency(10,grouping=True))
    elif mrent=='The Message':
        print("The rent for this movie is " +locale.currency(12,grouping=True))
    else:
        print("The rent for this movie is " +locale.currency(7,grouping=True))
def main ():
    movie_list=['Vertigo','Touch of Evil', 'The Queen of Egypt', 'The Message','Ben Hur']
    movie_date=[1958, 1960, 1963,1977,1959]
    movie_date.extend(movie_list)
    movie_list.sort()


    display_menu()

    while True:
        choice=input("Please select Our Menu  options :  ")
        if choice.lower()=='list':
            list(movie_list)
        elif choice.lower()=='date':
            dat(movie_date)
        elif choice.lower()=='rent':
            rent(movie_date)
        elif choice.lower()=='add':
            add(movie_list)
        elif choice.lower()=='delete':
            delete(movie_list)
        elif choice.lower()=='exit':
            break
        else:
            print("Invalid Option Has Been Entered !")
    print ("Have a nice day !")
    

if __name__ == "__main__":
    main()

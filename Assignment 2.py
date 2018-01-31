# Program Name  : Event Cinema Booking system
# Created by    : Francois Mindiel
# Created date  : 31/03/16
# Version       : 1.0
# Description   : This program is to find movies available at Event Cinema Ltd.
#                 I have been charged with designing a system to find and print an on-screen ticket for users to
#                 book movie ticket.
#

# Update History:


import movielib                                     # used to import functions and movies from movielib.py


def showIntro(company):                             # prints welcome message on the screen, using company name as value
    print("=================================\n")
    print("Welcome to Movie Ordering System!")
    print("Copyright: "+company + "\n")
    print("=================================\n")
    print("Start ordering when you are ready\n")




def displayMenu():                                  # displays menu and returns value for user choice regarding movies
    print("=================================\n")
    print("1 - Find listings by movie name.\n"
          "2 - Find listings by day of week.\n"
          "0 - Quit.\n")
    try:                                            # ensures that input is valid
        menuitem = int(input("How would you like to order your movie?\n"
          "(enter a number from the menu):"))
    except:
        menuitem = "Wrong Option"

    return menuitem

quitOrder = False
COMPANYNAME = "Event Cinema Ltd"
quitSystem = False

daysOfWeek = ["Sat","Sun","Mon","Tue","Wed","Thu","Fri"]        #create list for days of the week

movieList = []                                                  #create a list of movies





showIntro(COMPANYNAME)


while quitOrder == False:                           # to ensure that loop repeats until user chooses not to.
    itemChoice = displayMenu()

    if itemChoice == 1:
        print("\n"*50)
        print("******************************************\n"
              "You would like to find listings by 'movie'\n"
              "******************************************")
        print("\n******************************************"
              "\nHere is today's list of movies:"
              "\n******************************************")
        i = 0
        for movie in movielib.movies():

            print (i, movie[0])                                                        # adds index next to movies
            movieList.append(movie[0])
            i += 1

        selectedMovie = int(input("Please choose index of movie you wish to select:")) # ensures integer is inputted
        print("\n"*50)
        print("\n***************************************************************"
              "\nMovie details for "+ movieList[selectedMovie] +
              "\n***************************************************************")


        movielib.findMovie(searchmovie=movieList[selectedMovie])
        movielib.findMovieDates(movieList[selectedMovie])

        print("\n***************************************************************")


    elif itemChoice == 2:
        print("\n"*50)
        print("******************************************\n"
              "You would like to find listings by 'day'\n"
              "******************************************\n")
        j = 0
        for day in daysOfWeek:                                                      # lists days, with index
            print(j, day )
            j += 1

        selectedDay = int(input("Please choose index of movie you wish to select:"))
        print("\n"*50)
        print("******************************************"
              "\nMovies and schedules available on "+ daysOfWeek[selectedDay]+
              "\n******************************************\n")

        movielib.findMoviesOnThisDay(daysOfWeek[selectedDay])


    elif itemChoice == 0:                                                           # used to quit menu
        quitOrder = True

    else:
        print("\n"*50)
        print ("Wrong option! Please choose a valid option")





while quitSystem == False:                                                  #loop to validate ticketing/exit from system
    print("Have you found a movie that you like? Want to print another ticket?\n")

    hasSelected = input("'y' for yes / 'n' for no:")

    if hasSelected == "y":
        selectedSession = input("Please type in the name of the movie, as well as the day & time you would like:")

        print("\n"*50)
        print("*****************************************************")
        print("*\t\tMovie Ticket for " + COMPANYNAME + "\t\t\t*")
        print("*****************************************************")
        print("*                                                   *")
        print("\t\t" + selectedSession)
        print("*                                                   *")
        print("*****************************************************")
        print("\n\n\n\n\n")

    elif hasSelected == "n":
        print("\n"*50)
        print("Nevermind... Thanks for using our Movie Ordering System\n"
              "copyright: " + COMPANYNAME)
        quitSystem = True

    else:
        print("\n"*50)
        print("This is not a valid option!")













# This is the end of the program
# Francois Mindiel ID 2804582
# This work is protected by copyright laws!

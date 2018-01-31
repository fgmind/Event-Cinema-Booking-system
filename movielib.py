#
# Movie data
# import this into your Python file using:
# import movielib
#
# (place this file in the same place as your Python file

#list of movies - CSV
def moviesthisweek():
    return """13 Hours, The Secret Soldiers of Benghazi:(R16): 144 mins: No Free Tickets:
Dad's Army:(PG) :100 mins: No Free Tickets:
Deadpool:(R16) :108 mins :No Free Tickets:
Gods of Egypt:(M): 127 mins: No Free Tickets:
Grimsby: (R16): 82 mins: No Free Tickets:
Hail, Caesar!: (PG): 106 mins: No Free Tickets:
How To Be Single: (M) 110 mins: No Free Tickets:
Mahana: (M): 102 mins: No Free Tickets:"""

#list of movie days and times - CSV
def moviesschedule():
    return """13 Hours, The Secret Soldiers of Benghazi:Mon:10:35 AM:
13 Hours, The Secret Soldiers of Benghazi:Tue:10:35 AM:
13 Hours, The Secret Soldiers of Benghazi:Wed:10:35 AM:
13 Hours, The Secret Soldiers of Benghazi:Mon:8:20 PM:
13 Hours, The Secret Soldiers of Benghazi:Tue:8:20 PM:
13 Hours, The Secret Soldiers of Benghazi:Wed:8:20 PM:
Dad's Army:Mon:2:40 PM:
Dad's Army:Wed:2:40 PM:
Dad's Army:Tue:10:30 AM:
Dad's Army:Tue:2:40 PM:
Deadpool:Mon:11:30 AM:
Deadpool:Mon:2:00 PM:
Deadpool:Mon:4:20 PM:
Deadpool:Mon:6:40 PM:
Deadpool:Mon:9:00 PM:
Deadpool:Tue:11:30 AM:
Deadpool:Tue:2:00 PM:
Deadpool:Tue:4:20 PM:
Deadpool:Tue:6:40 PM:
Deadpool:Tue:9:00 PM:
Deadpool:Wed:11:30 AM:
Deadpool:Wed:2:00 PM:
Deadpool:Wed:4:20 PM:
Deadpool:Wed:6:40 PM:
Deadpool:Wed:9:00 PM:
Gods of Egypt:Mon:1:00 PM:
Gods of Egypt:Mon:3:45 PM:
Gods of Egypt:Mon:6:20 PM:
Gods of Egypt:Mon:8:30 PM:
Gods of Egypt:Tue:1:00 PM:
Gods of Egypt:Tue:3:45 PM:
Gods of Egypt:Tue:6:20 PM:
Gods of Egypt:Tue:8:30 PM:
Gods of Egypt:Wed:1:00 PM:
Gods of Egypt:Wed:3:45 PM:
Gods of Egypt:Wed:8:30 PM:
Grimsby:Wed:6:30 PM:
Hail, Caesar!:Mon:1:30 PM:
Hail, Caesar!:Mon:3:50 PM:
Hail, Caesar!:Mon:6:15 PM:
Hail, Caesar!:Mon:8:30 PM:
Hail, Caesar!:Tue:1:30 PM:
Hail, Caesar!:Tue:3:50 PM:
Hail, Caesar!:Tue:6:15 PM:
Hail, Caesar!:Tue:8:30 PM:
Hail, Caesar!:Wed:1:30 PM:
Hail, Caesar!:Wed:3:50 PM:
Hail, Caesar!:Wed:6:45 PM:
Hail, Caesar!:Wed:8:30 PM:
How To Be Single:Mon:10:40 AM:
How To Be Single:Mon:3:40 PM:
How To Be Single:Mon:6:10 PM:
How To Be Single:Tue:10:40 AM:
How To Be Single:Tue:3:40 PM:
How To Be Single:Tue:6:10 PM:
How To Be Single:Wed:10:40 AM:
How To Be Single:Wed:3:40 PM:
How To Be Single:Wed:6:10 PM:
Mahana:Mon:10:30 AM:
Mahana:Mon:11:10 AM:
Mahana:Mon:1:40 PM:
Mahana:Mon:4:00 PM:
Mahana:Mon:6:20 PM:
Mahana:Mon:8:40 PM:
Mahana:Wed:10:30 AM:
Mahana:Wed:11:10 AM:
Mahana:Wed:1:40 PM:
Mahana:Wed:4:00 PM:
Mahana:Wed:6:20 PM:
Mahana:Wed:8:40 PM:
Mahana:Tue:11:10 AM:
Mahana:Tue:1:40 PM:
Mahana:Tue:4:00 PM:
Mahana:Tue:6:20 PM:
Mahana:Tue:8:40 PM:"""


#create list of movies
def movies():
    movies=moviesthisweek()
    tempmovielist=movies.split('\n')
    newmovielist=[]
    for list in tempmovielist:
        newmovielist=newmovielist+[list.split(":")]
    return newmovielist

#create list of movietimes
def movietimes():
    movietimes=moviesschedule()
    tempmovietimelist=movietimes.split('\n')
    newmovietimelist=[]
    for movietimelist in tempmovietimelist:
        newmovietimelist=newmovietimelist+[movietimelist.split(":")]
    return newmovietimelist

#find a movie and how long it goes for
def findMovie(searchmovie):
    for movie in movies():
        if movie[0] == searchmovie:
            print ("Time for ",searchmovie, "is",movie[2])

#find a movie and its days /times
def findMovieDates(movie):
    #print (day)
    count=0
    for movietime in movietimes():
        try:
            if movietime[0] == movie:
                print(movietime[0]," is scheduled for ",movietime[1], " at ",movietime[2],":",movietime[3])
                count=count+1
        except:
            #error handling
            #bad list value
            print('')
    if count==0:
        print('*********************')
        print('Sorry no movies found')
        print('*********************')

#find a list of movies on a particular day
def findMoviesOnThisDay(day):
    #print (day)
    count=0
    for movietime in movietimes():
        try:
            if movietime[1] == day:
                print(movietime[0]," is scheduled for ",movietime[1], " at ",movietime[2],":",movietime[3])
                count=count+1
        except:
            #error handling
            #bad list value
            print('')
    if count==0:
        print('*********************')
        print('Sorry no movies found')
        print('*********************')

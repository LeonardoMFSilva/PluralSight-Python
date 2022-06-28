# This is a map in Python that stores key and value pairs
current_movies = {"The Grinch" : "11:00am",
                  "Rudolph": "1:00pm",
                  "Frosty": "3:00pm",
                  "Christmas Vacation": "5:00pm"}


# It also can be done it like this:
#current_movies = {}
#current_movies["The Grinch"] = "11:00am"

print("We're showing the following movies:")
for key in current_movies:
    print(key)
movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)
if (showtime == None):
    print("Requested showtime is not available")
else:
    print(movie, "is available at", showtime)
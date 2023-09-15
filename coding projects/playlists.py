playlist = {"title" : "bus ride", "author" : "colt", "songs" : [{"title":"song1", "artist" : ["blue"], "duration": 2.5},
 {"title":"song2", "artist" : ["men"], "duration": 1.3}, 
   {"title":"song1", "artist" : ["blue"], "duration": 2.5}]}

total_length = 0
for song in playlist ["songs"]: 
    total_length += song["duration"]
print(total_length)
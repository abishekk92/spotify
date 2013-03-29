limit,to_select=map(int,raw_input().split(" "))
def get_song(index):
	f1,name=raw_input().split(" ")
	index=index+1
	return {"index":index,"quality":int(f1),"name":name,"quality_metric":index*int(f1)}
songs=[get_song(index) for index in range(limit)]
sorted_songs=sorted(songs,key=lambda song:song["quality_metric"])
for song in sorted_songs[::to_select]: print song["name"],song["quality_metric"]


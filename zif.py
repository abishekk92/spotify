limit,to_select=map(int,raw_input().split(" "))
def get_song(index):
	f,name=raw_input().split(" ")
	index=index+1
	return {"index":index,"quality":int(f),"name":name,"quality_metric":index*int(f)}
songs=[get_song(index) for index in range(limit)]
songs.sort(key=lambda song:(song["quality_metric"],-song["index"]),reverse=True)
for song in songs[:to_select]: print song["name"]


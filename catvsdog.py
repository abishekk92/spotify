from collections import Counter
test_cases=int(raw_input())
def get_vote():
	return tuple(raw_input().split())
def max_voters():
	cats,dogs,voters=map(int,raw_input().split())
	votes=[get_vote() for i in range(voters)]
	keep_count,kick_count=map(Counter,map(list,zip(*votes)))
	print "\n".join(map(str,votes))
	print map(lambda vote: {"degree":keep_count[vote[1]]+kick_count[vote[0]],"vote":vote},votes)
	return 0
results=[max_voters() for i in range(test_cases)]
#for result in results : print result


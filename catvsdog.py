from collections import Counter
test_cases=int(raw_input())
def get_vote():
	keep,kick=raw_input().split(" ")
	return {"keep":keep,"kick":kick}
def max_voters():
	cats,dogs,voters=map(int,raw_input().split(" "))
	votes=[get_vote() for i in range(voters)]
	keep=map(lambda vote: vote["keep"],votes)
	kick=map(lambda vote: vote["kick"],votes)
	keep_count,kick_count=Counter(keep),Counter(kick)
	keep_it=[]
	for item in set(keep_count.keys()+kick_count.keys()):
		if keep_count[item] >= kick_count[item]:keep_it.append(item)
		return max(map(lambda pet: keep_count[pet],keep_it))
results=[max_voters() for i in range(test_cases)]
for result in results : print result


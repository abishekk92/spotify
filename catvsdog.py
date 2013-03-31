from collections import Counter
test_cases=int(raw_input())
def get_vote():
	keep,kick=raw_input().split(" ")
	return (keep,kick)
def get_conflicts(votes):
	count=0
	for vote in votes:
		if vote[::-1] in votes:	count=count+1
	return count/2
def max_voters():
	cats,dogs,voters=map(int,raw_input().split(" "))
	votes=[get_vote() for i in range(voters)]
	conflict=get_conflicts(votes)
	return voters-conflict
results=[max_voters() for i in range(test_cases)]
for result in results : print result


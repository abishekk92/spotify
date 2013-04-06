from collections import Counter
test_cases=int(raw_input())
def get_vote():
	return tuple(raw_input().split())
def max_matching(graph):
	return len(filter(lambda node : len(node) is not 0,graph.values()))
def max_voters():
	cats,dogs,voters=map(int,raw_input().split())
	votes=[get_vote() for i in range(voters)]
	min_conflicts=max_matching({cat_lover:set(filter(lambda vote: cat_lover[0] is vote[1] or cat_lover[1] in vote[0],votes)) for cat_lover in filter(lambda vote: vote[0][0]=='C',votes) })
	return voters-min_conflicts

results=[max_voters() for i in range(test_cases)]
for result in results : print result


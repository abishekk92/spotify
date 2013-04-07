test_cases=int(raw_input())
def min_cardinality(graph):
	#Eppestein's Hopcroft Karp Implementation
	matching = {}
	for u in graph:
		for v in graph[u]:
			if v not in matching:
				matching[v] = u
				break

	while True:
		preds = {}
		unmatched = []
		pred = dict([(u,unmatched) for u in graph])
		for v in matching:
			del pred[matching[v]]
		layer = list(pred)

		while layer and not unmatched:
			newLayer = {}
			for u in layer:
				for v in graph[u]:
					if v not in preds:
						newLayer.setdefault(v,[]).append(u)
			layer = []
			for v in newLayer:
				preds[v] = newLayer[v]
				if v in matching:
					layer.append(matching[v])
					pred[matching[v]] = v
				else:
					unmatched.append(v)

		if not unmatched:
			unlayered = {}
			for u in graph:
				for v in graph[u]:
					if v not in preds:
						unlayered[v] = None
			return (matching,list(pred),list(unlayered))

		def recurse(v):
			if v in preds:
				L = preds[v]
				del preds[v]
				for u in L:
					if u in pred:
						pu = pred[u]
						del pred[u]
						if pu is unmatched or recurse(pu):
							matching[v] = u
							return 1
			return 0

		for v in unmatched: recurse(v)

def get_vote(i):
	input_split=raw_input().split()
	input_split.append(i)
	return tuple(input_split)

def max_matching(graph):
	return len(min_cardinality(graph)[0])

def max_voters():
	cats,dogs,voters=map(int,raw_input().split())
	votes=[get_vote(i) for i in range(voters)]
	graph={cat_lover: set(filter(lambda vote: vote[1] == cat_lover[0] or vote[0] == cat_lover[1],votes)) for cat_lover in filter(lambda vote: vote[0][0] is 'C',votes)}
	min_conflicts=max_matching(graph)	
	return voters-min_conflicts

results=[max_voters() for i in range(test_cases)]

for result in results : print result


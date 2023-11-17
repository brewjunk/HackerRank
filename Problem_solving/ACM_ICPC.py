#ACM ICPC Team | HackerRank

n,m = 4,5
topic = ['10101','11100','11010','00101']


def acmTeam(topic):
	possibilities = [[a, b] for v, a in enumerate(topic) for b in topic[v + 1:]]
	max_topics = []
	count_topics = 0
	c = 0
	for i in possibilities:
		x = i[0]
		y = i[1]
		for p in y:
			if p == '1' or x[c] == '1':
				count_topics += 1
			c += 1
		c = 0
		max_topics.append(count_topics)
		count_topics = 0
	total_max_topics = max(max_topics)
	count_of_teams = max_topics.count(total_max_topics)
	return total_max_topics, count_of_teams


print(acmTeam(topic))

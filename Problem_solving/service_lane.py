#Service Lane | HackerRank
n = 8
t = 5
width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
def serviceLane(n,cases):
	m_width = []
	for i in cases:
		m_width.append(min(width[i[0]:i[1]+1]))

	return m_width

print(serviceLane(n,cases))
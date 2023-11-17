#Queens Attack | HackerRank

n,k = 5, 3 #chessboard, number of obsticles
r_q,c_q = 4, 3 #Queens position
obstacles = [[5, 5],[4,2],[2,3]]



def queensAttack(n, k, r_q, c_q, obstacles):
    return n,k,r_q,c_q,obstacles

print(queensAttack(n, k, r_q, c_q, obstacles))
#Flatland Space Stations | HackerRank

n,m = 5,2
c = [0,4]

# 0 | 1 | 2 | 3 | 4
# *               *
import math

def flatlandSpaceStations(n, c):
#c = [0,4]
    ans = max(c[0]-0,(n-1)-c[-1])
    print(ans,'ans')
    for i in range(len(c)-1):
        print(i,'i')
        mid = math.floor((c[i]+c[i+1])//2)
        print(mid,'mid')
        res = min(abs(c[i]-mid),abs(c[i+1]-mid))
        print(res,'res')
        ans = max(ans,res) 
        print(ans,'ans')
    return ans

print(flatlandSpaceStations(n,c))


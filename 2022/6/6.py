with open("6.txt") as f:
    s = f.read().strip()
    
def getPositionOfMarker(s, n):
    for i in range(n,len(s)):
        if len(set(s[i-n:i])) == n:
            return(i)

print(getPositionOfMarker(s, 4), getPositionOfMarker(s, 14))
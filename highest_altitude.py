arr = list(map(int,input().split()))
highest_altitude = 0
t = 0
for s in arr:
    t += s
    highest_altitude = max(highest_altitude,t)
    
print(highest_altitude)
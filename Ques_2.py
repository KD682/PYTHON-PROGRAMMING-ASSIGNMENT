import statistics
n = list(map(int,input().split()))        #n=Number
max_n = max(n)
min_n = min(n)
mean_n = round(statistics.mean(n),2)
sd = round(statistics.stdev(n),2)         #sd=Standard deviation 
v = round(statistics.variance(n),2)       #v=Variance
print(max_n, min_n, mean_n, sd, v)

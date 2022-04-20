s = input();             #s=string
f = [None] * len(s);     #f=frequency
   
for i in range(0, len(s)):  
    f[i] = 1;  
    for j in range(i+1, len(s)):  
        if(s[i] == s[j]):  
            f[i] = f[i] + 1;    
            s = s[ : j] + '0' + s[j+1 : ];  
            
for i in range(0, len(f)):
    f[i] = int(f[i])
    f.sort(reverse = True)
    if(s[i] != ' ' and s[i] != '0'):  
        print(str(f[i]));  

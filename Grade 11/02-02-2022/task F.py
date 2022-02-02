n = int(input())
time = 540
time+=n*45
time+=(n-1)//2*20
time+=((n-1)%2)*5
print(time//60,time%60)
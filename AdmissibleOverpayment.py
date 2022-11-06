def solution(prices, notes, x):
    sum=0
    for i in range(len(notes)):
        if('higher' in notes[i]):
            t = notes[i].find("%")
            num = notes[i][:t]
            change=float(num)
            high=prices[i]-((prices[i]*100)/(100+change))
            sum+=high
        elif "lower" in notes[i]:
            t = notes[i].find("%")
            num = notes[i][:t]
            change=float(num)
            low=((prices[i]*100)/(100-change))-prices[i]
            sum-=low
        elif ('Same' in notes[i]):
            sum+=0
    print("a: ",sum)
            
    if sum>x:
        return False
    elif sum<=x:
        return True


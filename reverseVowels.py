class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_of_s=[]
        sum=0  #string number of s
        sum2=0  #string number of vowels_of_s
        for i in s:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
                vowels_of_s.append(i)
        vowels_of_s.reverse()
        my_list=list(s)
        for i in my_list:
            if i == i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
                my_list[sum]=vowels_of_s[sum2]
                sum2+=1
            sum+=1
            if sum2>=len(vowels_of_s):
                break
        a="".join(my_list)
        return a
        
s=input()
print(Solution.reverseVowels(self=s,s=s))

        
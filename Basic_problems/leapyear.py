Find the leap year 

Sample Input 
1990

Sample Output 
False

Explanation 
1990 is not a multiple of 4 hence it's not a leap year.



def is_leap(year):
    leap = False
    
    if(year%400==0):
        return not(leap)
    elif(year%4==0):
        if(year%100==0):
            return leap
        else:
            return not(leap)
    else: 
        return leap

year = int(input())
print(is_leap(year))

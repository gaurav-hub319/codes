#Problem number 1 -Given an integer, convert it to a roman numeral
#Solution:-
def convertRoman(n):
    #Code here
    arr = [[5000, 'V'],[4000, 'XV'],[3000, 'MMM'],[2000, 'MM'],[1000, 'M'],[900, 'CM'],[500, 'D'],[400, 'CD'],[100, 'C'],[90, 'XC'],[50, 'L'],[40, 'XL'],[10, 'X'], [9, 'IX'], [8, 'VIII'],[7, 'VII'],[6,'VI'],[5,'V'], [4,'IV'], [3,'III'],[2, 'II'],[1, 'I']]
    s= ''
    a = 0
    while n!=0:
        for i in range (len(arr)):
            if n>=arr[i][0] :
                s +=arr[i][1]
                n-= arr[i][0]
                break
    return s
n=int(input())
print(convertRoman(n))




# Problem 2: ### You are given an array prices where prices[i] is the price of a given stock on the ith day. 

#Solution:

def maxProfit(price, n):
    profit = [0]*n
    max_price = price[n-1]
 
    for i in range(n-2, 0, -1):
 
        if price[i] > max_price:
            max_price = price[i]
        profit[i] = max(profit[i+1], max_price - price[i])
    min_price = price[0]
 
    for i in range(1, n):
 
        if price[i] < min_price:
            min_price = price[i]
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
 
    result = profit[n-1]
 
    return result
#main function
price=[int(x) for x in input().split()]
print(maxProfit(price,len(price)))

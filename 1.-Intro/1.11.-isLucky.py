'''
Ticket numbers usually consist of an even number of digits.A ticket number is
considered lucky if the sum of the first half of the digits is equal to the
sum of the second half.

Given a ticket number n, determine if it's lucky or not.
'''
def solution(n):
    toString = str(n)
    pivot = len(toString)//2
    half1 = toString[:pivot]
    half2 = toString[pivot:]
    return sum(map(int,half1)) == sum(map(int,half2))

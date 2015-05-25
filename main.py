#!/usr/bin/env python

#from solution_150 import Solution
from solution_180 import Solution

def main():
    solution = Solution()
    '''
    with open('data.in', 'r') as f:
        for line in f.readlines():
            print solution.majorityElement(map(int, line.split()))
    '''
    while True:
        try:
            a = int(raw_input().strip())
            #a, b = map(int, raw_input().strip().split())
            #a = map(int, raw_input().strip().split())
            print solution.countPrimes(a)
        except EOFError:
            break;

if __name__ == '__main__':
    main()

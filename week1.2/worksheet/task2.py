# Worksheet 1.2: Task 2 Solution
import sys 
from util import read_numbers

numbers = read_numbers()  

if len(numbers) == 0:     
    sys.exit("Error: no numbers provided")  
minimum = min(numbers) 
maximum = max(numbers) 
mean = sum(numbers)/len(numbers) 

sorted_nums = sorted(numbers) 
length = len(sorted_nums) 
mid = length // 2 
if length % 2 == 1:
    median = sorted_nums[mid] 
else:    
    median = (sorted_nums[mid-1] + sorted_nums[mid]) / 2 

print(f"Minimum = {minimum}") 
print(f"Maximum = {maximum}") 
print(f"Mean = {mean}")
print(f"Median = {median}")
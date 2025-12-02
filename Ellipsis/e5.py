'''
Check If A Variable Is An Ellipsis Object And Print Appropriate Message If It Is
'''
nums=[1,2,3,4,5,6,...,7,8,9]  
for i in nums:
    if i is ...:
        print("Skipping Ellipsis Object")
        continue
    print(f"Reading Item:{i}")
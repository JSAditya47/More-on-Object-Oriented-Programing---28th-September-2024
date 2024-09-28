class pair_elements:
    
    def twoSum(self, nums, target):
        
        lookup = {}
        
        for i, num in enumerate(nums):
            
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
            
value = int(input("Enter Sum for Which You Want To Make This Search: "))

resTup = pair_elements().twoSum( (10, 20, 30, 40 ,50, 60, 70, 80), value)
print(f"{resTup[0]} index + {resTup[1]} index = {value}")
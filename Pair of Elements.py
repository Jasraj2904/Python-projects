class pair_elements():
    def two_sum(self , nums , target):
        lookup = {}
        for i,num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target - num] , i)
            lookup[num] = i
value = int(input("Enter your sum for which you want to search : "))
print("index1 = %d , index2 = %d" %pair_elements().two_sum((10 , 20 , 30 , 40 , 50 , 60 , 70 ) , value))
repeat = "yes"
nums = []
while repeat == "yes":
    num = int(input("enter a number"))
    nums.append(num)
    repeat = input("do you want to enter another number? yes / no")
mean = sum(nums) / len(nums)
meanDeviation = 0
for x in nums:
    meanDeviation += x - mean
print("the mean is ", mean)
print("the mean deviation is ",meanDeviation/len(nums))
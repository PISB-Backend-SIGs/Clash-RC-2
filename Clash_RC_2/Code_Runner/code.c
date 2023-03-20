
def find_max_product(nums):
    if len(nums) < 2:
        return None

    nums.sort()
    if nums[-1] <= 0:
        return nums[-2] * nums[-1]

    return max(nums[-1] * nums[-2], nums[0] * nums[1])

a= list(map(int,input().split()))
s = find_max_product(a)
print(s)

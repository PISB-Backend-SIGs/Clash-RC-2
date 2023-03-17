import uuid


# t =uuid.uuid4
# print(t)
# uuid.uuid4()
# s=0
# if (!s):
    # pr/int("hello")

if not(False):
    print("Hello")


def find_max_product(nums):
    if len(nums) < 2:
        return None

    nums.sort()
    if nums[-1] <= 0:
        return nums[-2] * nums[-1]

    return max(nums[-1] * nums[-2], nums[0] * nums[1])
l = list(map(int,input().split()))
a = find_max_product(l)
print(a)

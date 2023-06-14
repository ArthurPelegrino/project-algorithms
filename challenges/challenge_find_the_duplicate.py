def find_duplicate(nums):
    # print("numeros param", nums)
    nums.sort()
    # print("numbers sort", nums)
    if nums is None or nums is str:
        return False
    else:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                if nums[i] < 0:
                    return False
                else:
                    return nums[i]
    return False


# print(find_duplicate([1, 2, 3]))

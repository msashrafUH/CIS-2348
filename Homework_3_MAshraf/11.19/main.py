#Muhammad S Ashraf 1763709
if __name__ == '__main__':
    nums = [int(num) for num in input().split()]
    if len(nums) > 9:
        print("Too many inputs")
    else:
        if len(nums) % 2 == 1:
            print(nums[len(nums) // 2])
        else:
            print(nums[len(nums) // 2 - 1], nums[len(nums) // 2])
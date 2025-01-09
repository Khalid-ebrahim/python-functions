def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest


def largest(nums):
  nums.sort()
  return nums[-1]
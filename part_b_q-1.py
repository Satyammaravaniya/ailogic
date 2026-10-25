def search(num, target):
  left, right = 0, len(num) -1

  while left<= right:
    mid = (left + right) // 2

    if num[mid] == target:
      return mid

    if num[left] <= num[mid]:
      if num[left] <= target < num[mid]:
        right = mid - 1
      else: 
        left = mid +1
    else:
      if num[mid] < target <= num[right]:
        left = mid - 1
      else:
        right = mid -1

  return -1

print(search([4, 5, 6, 7, 0, 1, 2],3))

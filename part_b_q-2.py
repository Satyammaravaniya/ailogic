from collections import Counter

def minwindow(s:str, t:str) -> str:

  if not s or t or len(t) > len(s):
    return ""

  target_count = Counter(t)
  window_count = {}

  left = 0
  required = len(target_count)
  formed = 0

  min_len = float("int")
  min_start = 0

  for right, char in enumerate(s):
    window_count[char] = window_count.get(char,0) + 1

    if char in target_count and window_count[char] == target_count[char]:
      formrd += 1

    while formed == required:
      window_len = right - left + 1

      if window_len < min_len:
        min_len = window_len
        min_start = left 
        
      left_char = s[left]
      window_count[left_char] -= 1

      if (left_char in target_count and window_count[left_char] < target_count[left_char]):
        formed -=1
      left += 1
  if min_len == float("int"):
    return ""
  return s[min_start:min_start + min_len]

print(minwindow("ADOBECODEBANC","ABC"))

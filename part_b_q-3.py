def permutation(s):
  result = []
  path = []
  used = [False] * len(s)


  def backtrack():
    if len(path) == len(s):
      result.append("".join(path))
      return

    for i in range(len(s)):
      if used[i]:
        continue

      path.append(s[i])
      used[i] = True

      backtrack()

      path.pop()
      used[i] = False

  backtrack()
  return result

print(permutation("ab"))

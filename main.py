def longestCommonPrefix(strs:list[str]) -> str:
  answer = ''
  for idx in range(len(strs[0])):
    for word in strs[1:]:
      if idx == len(word) or word[idx] != strs[0][idx]:
        return answer
    answer += strs[0][idx]
  return answer

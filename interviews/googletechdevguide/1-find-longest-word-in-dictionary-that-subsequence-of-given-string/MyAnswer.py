import sys
import collections

def find_longest_word_in_string(letters, words):
  dd = collections.defaultdict(lambda: 'N/A')
  Pair = collections.namedtuple('pair', ['w', 'i'])
  for word in words:
    if dd[word[0]] == 'N/A':
      dd[word[0]] = []
    dd[word[0]].append(Pair(word, 0))
  for letter in letters:
    if dd[letter] == 'N/A':
      pass
    else:
      pairs = dd[letter][:]
      dd[letter] = []
      for pair in pairs:
        if len(pair.w) > pair.i:
          pair = Pair(pair.w, pair.i + 1)
        if len(pair.w) > pair.i:
          if dd[pair.w[pair.i]] == 'N/A':
            dd[pair.w[pair.i]] = []
          dd[pair.w[pair.i]].append(pair)
        else:
          dd[letter].append(pair)
  resPair = Pair('', 0)
  for letter in dd:
    for pair in dd[letter]:
      if pair.i > resPair.i:
        resPair = pair
  return resPair.i, resPair.w

if __name__ == '__main__':
  S = "abppplee"
  D = ["able", "ale", "apple", "bale", "kangaroo"]
  i, w = find_longest_word_in_string(S, D)
  print(i, w)
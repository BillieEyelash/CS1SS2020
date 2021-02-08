def get_words():
  numOfLines = int(input())
  words = list()
  for i in range(numOfLines):
    line = input().split()
    for word in line:
      words.append(word)
  return words

def find_most_frequent(wordsList):
  wordCountDict = dict()
  for word in wordsList:
    wordCountDict[word] = wordCountDict.get(word, 0) + 1
  for key in wordCountDict:
    biggest = 0
    if wordCountDict[key] > wordCountDict[biggest]:
      biggest = key

def run():
  print(find_most_frequent(get_words()))

run()

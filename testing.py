def wordtesting(word):

  word_len = len(word)
  print(word_len)
  print (word[-3:word_len])
  if word_len>=3:
      result = word+"ing"
  else:
      result = word
  return(result)

word = "playing"
print(wordtesting((word)))


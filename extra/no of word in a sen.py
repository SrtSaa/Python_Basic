#calculate number of word in a sentence

sentence = input()
space = ' ' # there is a single space between the quotes
num_words = sentence.count(space) + 1
print(num_words)
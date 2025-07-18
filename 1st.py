sentence=input("Enter the  string")
vowels={'a','e','i','o','u','A','E','I','O','U'}
words=sentence.split()
for word in words:
  vowel_count=0
for char in word:
 if char in vowels:
     vowel_count+=1
print(Word:'{word}',Vowels:'{vowel_count}')


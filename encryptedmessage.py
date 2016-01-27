def encrypt(sentence):

   words_list = sentence.split("")
   print(words_list)
   for i in range(0,len(words_list)):
          if (i+1) % 2 != 0:
                   words_list[i] = words_list[i][::-1]
          else:

                   temp_words =""
                   vowels = ""

                   for char in words_list[i]:
                     if char in ['a','A','e','E','i','I','o','O','u','U']:
                               vowels += char


                     else:
                               temp_words += char
                               words_list[i]=temp_words+vowels


   return ''.join(words_list)


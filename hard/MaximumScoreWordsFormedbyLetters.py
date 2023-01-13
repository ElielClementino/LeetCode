from collections import Counter
from itertools import chain, combinations


letters = ["a","a","c","d","d","d","g","o","o"]
words = ["dog","cat","dad","good"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

def maxScoreWords(words, letters, score) -> int:
    concatened_words = []
    concat_word = ''
    spliced_list = []
    lista_count = []
    soma = 0
    asc_sum = []

    def powerset(list_name):
        combinacoes = list(chain.from_iterable(combinations(list_name, r) for r in range(len(list_name)+1)))
        return combinacoes
    combined_list = powerset(words)

    def contains_all(A, B):
        for compare in B:
            condition = Counter(A) >= Counter(compare)
            if condition:
                lista_count.append(compare)
        return 


    for word in combined_list:
        concat_word = ''.join(word)
        concatened_words.append(concat_word)


    for splicer in concatened_words:
        spliced_list.append(list(splicer))


    contains_all(letters, spliced_list)


    for lista in lista_count:
        soma = 0
        for letter in lista:
            soma += score[ord(letter) - 97]
        asc_sum.append(soma)
    return max(asc_sum)

print(maxScoreWords(words, letters, score))
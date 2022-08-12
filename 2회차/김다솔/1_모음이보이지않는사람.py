import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
for tc in range(1, T+1):
    word = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = []
    for i in word:
        if i not in vowels:
            consonants.append(i)
    print(f'#{tc} ', *consonants, sep='')
    
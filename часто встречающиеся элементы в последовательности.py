from collections import Counter
import json

if __name__ == '__main__':

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under', 'look'
    ]

    word_counts = Counter(words) #counter можно скормить любую последовательность
    #top_words = word_counts.most_common()
    print(word_counts)  # Выведет подсчет по словам
    # json_dict = json.dumps(top_words)  # серилизация в JSON
    # print(json_dict)
    print(f" 'eyes' = {word_counts['eyes']}")

    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes'] #дополнительный список
    # for word in morewords: #обновление вручную
    #     word_counts[word] += 1
    # print(word_counts['eyes'])
    word_counts.update(morewords) #обновление подсчета слов
    print(word_counts)

    print("________________")
    a = Counter(words)
    b = Counter(morewords)
    print(a)
    print(b)
    c = a + b # Объединяем счетчики
    print(c)
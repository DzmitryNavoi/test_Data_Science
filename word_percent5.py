def word_distribution_percentage(search_queries):
    
    num_words=[]
    for i in search_queries:
        k=i.split()
        num_words.append(len(k))
    sorted_array=sorted(num_words)

    word_count_distribution = {}
    for i in sorted_array:
        if i in word_count_distribution:
            word_count_distribution[i]+= 1
        else:
            word_count_distribution[i] = 1 
    
    dict = {1:"слово",
            2:"слова",
            3:"слова",
            4:"слова",
            5:"слов",
            6:"слов",
            7:"слов",
            8:"слов",
            9:"слов",
            10:"слов",
            }

    for key, value in word_count_distribution.items():
        p = (value*100)/sum(word_count_distribution.values())
        for i, j  in dict.items():
            if key == i:
                print(f'{key} {j}:  {int(p)}%')


search_queries = ["watch new movies", "coffee near me", "how to find the determinant",
                  "python", "data science jobs in UK", "courses for data science", 
                  "taxi", "google", "yandex", "bing", "foreign exchange rates USD/BYN", 
                  "Netflix movies watch online free", "Statistics courses online from top universities"]

word_distribution_percentage(search_queries)
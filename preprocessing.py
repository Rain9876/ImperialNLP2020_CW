import nltk
import jieba
import codecs




#####  Tokenization #####

# For both Chinese and English
# Chinese jieba : https://github.com/fxsjy/jieba
# English nltk : https://www.nltk.org/data.html


# Think about the order of these steps
# Do they needed in checking the similarity?

#### Before Tokenization
# Punctuation removal ?
# Stop Word removal ?
# Rare words removal ?
# File "stop_words.txt", Do we need it???


#### After Tokenization
# Stemming ?
# Lemmatization ?

#########################

if __name__ == "__main__":


    # Tokenization (Chinese)
    str_in = ["他把欧文扔进了挖掘机挖出儿子心脏的坑里.",
              "Alpha Phi Alpha 还参加了 Dimes 'WalkAmerica 的 3 月活动 ， 并在 2006 年筹集了 181 000 美元。",
              "1995 年 ， Deftones 发行了首张专辑《肾上腺素》。",
              "He shoves Owen into the pit where Digger rips out his son's heart.",
              "Alpha Phi Alpha also participates in the March of Dimes' WalkAmerica and raised over $181,000 in 2006.",
              "In 1995, Deftones released their debut album Adrenaline."]

    for sent in str_in:
        seg_list = jieba.cut(sent)
        print("Default Mode: " + "/ ".join(seg_list))





    # Tokenization (English)
    # Can do the same in the tutorial or directly use jieba





    # stopwords = codecs.open('stopwords', 'r', 'utf-8').read().split(',')
    # for seg in seg_list:
    #     if seg not in stopwords:
    #         print(seg)








##### Embedding #####

### For both Chinese and English
# Chinese ??   https://github.com/Embedding/Chinese-Word-Vectors
# English ??







##### Transform #####

### For both Chinese and English
# https://openai.com/blog/language-unsupervised/
# https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf

# How to implement, Online code examples ??




### Linear classification ####
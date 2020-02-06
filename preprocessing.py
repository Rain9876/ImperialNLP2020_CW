import nltk
import jieba
import codecs

#####  Tokenization #####

# For both Chinese and English
# Chinese jieba : https://github.com/fxsjy/jieba
# English nltk : https://www.nltk.org/data.html

# Think about the order of these steps
# Do they needed in checking the similarity?

# Punctuation removal ?
# Stop Word removal ?
# Rare words removal ?
# File "stop_words.txt", Do we need it???

# Stemming ?
# Lemmatization ?



####
## define stopwords.txt by us or use pre-defined online ???


import utils
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


def preprocessing_english(corpus):
    re_punctuation_en = '[\%\-\£\…?\(\)\"\!\[\]\s,/.\']'
    tokenized_corpus_processed = []
    porter = PorterStemmer()
    wordnet_lem = WordNetLemmatizer()

    for sentence in corpus:
        # punctuation remove
        tokenized_sentence_PR = re.split(re_punctuation_en, sentence)
        # Empty set remove
        tokenized_sentence_PR = list(filter(None, tokenized_sentence_PR))
        # Processed sentences
        tokenized_sentence_processed = []
        for token in tokenized_sentence_PR:
            token = token.lower()
            if token not in stopwords.words("english"):
                # Stemming
                token = porter.stem(token)
                # Lemmization
                token = wordnet_lem.lemmatize(token, pos="v")
                tokenized_sentence_processed.append(token)
        tokenized_corpus_processed.append(tokenized_sentence_processed)

    for i in tokenized_corpus_processed:
        print(i)
    return tokenized_corpus_processed

def preprocessing_chinese(corpus):
    porter = PorterStemmer()
    wordnet_lem = WordNetLemmatizer()

    tokenized_corpus_processed =[]
    for sentence in corpus:
        # Slice the sentences to token
        tokenized_sentence = jieba.cut(sentence)
        stopwords_ch = utils.readFile('/stopwords_ch.txt')[0].split(",")
        punctuation_ch = utils.readFile('/punctuation.txt')

        tokenized_sentence_processed=[]
        for token in tokenized_sentence:
            # Remove token of space
            token = token.replace(' ', '')
            if token not in stopwords_ch and token not in punctuation_ch and token:
                # Fine processing for english in Chinese
                if re.search('[a-zA-Z]', token):
                    token = token.lower()
                    token = porter.stem(token)
                    token = wordnet_lem.lemmatize(token, pos="v")
                tokenized_sentence_processed.append(token)
        tokenized_corpus_processed.append(tokenized_sentence_processed)

    for i in tokenized_corpus_processed:
        print(i)
    return tokenized_corpus_processed


#########################

if __name__ == "__main__":

    nltk.download('stopwords')

    Chinese = utils.readFile("/en-zh/train.enzh.mt")
    English = utils.readFile("/en-zh/train.enzh.src")

    corpus_en = English[:20]
    corpus_ch = Chinese[:20]
    # print(set(stopwords.words('english')))
    for i in range(len(corpus_ch)):
        en_p = preprocessing_english([corpus_en[i]])
        ch_p = preprocessing_chinese([corpus_ch[i]])
    print("=="*30)



    # # Tokenization (Chinese)
    # str_in = ["他把欧文扔进了挖掘机挖出儿子心脏的坑里.",
    #           "Alpha Phi Alpha 还参加了 Dimes 'WalkAmerica 的 3 月活动 ， 并在 2006 年筹集了 181 000 美元。",
    #           "1995 年 ， Deftones 发行了首张专辑《肾上腺素》。",
    #           "He shoves Owen into the pit where Digger rips out his son's heart.",
    #           "Alpha Phi Alpha also participates in the March of Dimes' WalkAmerica and raised over $181,000 in 2006.",
    #           "In 1995, Deftones released their debut album Adrenaline."]
    #
    # for sent in str_in:
    #     seg_list = jieba.cut(sent)
    #     print("Default Mode: " + "/ ".join(seg_list))



##### Embedding #####

### For both Chinese and English
# Chinese ??   https://github.com/Embedding/Chinese-Word-Vectors
# English ??
# How many word embedding do we need ???




##### Transform #####

### For both Chinese and English
# https://openai.com/blog/language-unsupervised/
# https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf
#
# How to implement, Online code examples
# Bert with transformer pytorch
# https://pypi.org/project/pytorch-pretrained-bert/






##### Linear classification #####

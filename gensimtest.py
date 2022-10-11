text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

import pprint

# 创建停用词表
stoplist = set('for a of the and to in'.split(' '))
# 全部转换为小写、空格分词、停用词
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in text_corpus]

# 统计词频
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# 保留出现超过一次的词语
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
# pprint.pprint(processed_corpus)

from gensim import corpora
dictionary = corpora.Dictionary(processed_corpus)

# print(dictionary)

# pprint.pprint(dictionary.token2id)

# new_doc = "Human computer interaction"
# new_vec = dictionary.doc2bow(new_doc.lower().split())
#
# print(new_vec)

bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
# pprint.pprint(bow_corpus)

from gensim import models
tfidf = models.TfidfModel(bow_corpus)
words = "system minors".lower().split()
# print(tfidf[dictionary.doc2bow(words)])

from gensim import similarities
index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=12)
query_document = 'system engineering'.split()
query_bow = dictionary.doc2bow(query_document)
sims = index[tfidf[query_bow]]
print(list(enumerate(sims)))
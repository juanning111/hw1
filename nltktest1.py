import nltk

# 断句
from nltk.tokenize import sent_tokenize
text = """Hello Mr. Smith, how are you doing today? The weather is great, and \
city is awesome.The sky is pinkish-blue. You shouldn't eat cardboard"""

tokenized_text = sent_tokenize(text)
print(tokenized_text)

# 分词
sent = "I am almost dead this time"
token = nltk.word_tokenize(sent)
print(token)

# 停用词
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
print(stop_words)
text = "Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome."

word_tokens = nltk.tokenize.word_tokenize(text.strip())
filtered_word = [w for w in word_tokens if not w in stop_words]

print("word_tokens: ", word_tokens)
print("filtered_word: ", filtered_word)

# 词汇规范化：词形还原
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('leaves'))

# 基于Porter词干提取算法
word='unable'

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
print('porter:',porter_stemmer.stem(word))

# 基于Lancaster 词干提取算法
from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
print('lancaster:',lancaster_stemmer.stem(word))

# 基于Snowball 词干提取算法
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer('english')
print('snowball:',snowball_stemmer.stem(word))

sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens = nltk.word_tokenize(sent)
tags = nltk.pos_tag(tokens)
print(tags)

from nltk.corpus import wordnet

word = wordnet.synsets('illusion')
print(word)

print(word[0].definition())
print(word[1].definition())
print(word[2].definition())
print(word[3].definition())

from gensim.parsing.preprocessing import preprocess_string
from gensim import corpora
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

# like DEFAULT_FILTERS, but without stemming
_FILTERS = [lambda x: x.lower(), strip_tags, strip_punctuation, strip_multiple_whitespaces,
                   strip_numeric, remove_stopwords, strip_short]

def preprocess_string(s, filters=_FILTERS):
    s = utils.to_unicode(s)
    for f in filters:
        s = f(s)
    return s.split()

def clean(abstracts):
    filters = []
    texts = [
        preprocess_string(text)
        for text in abstracts
    ]
    # Create WordNetLemmatizer object
    wnl = WordNetLemmatizer()
    return texts

def make_dictionary(texts):
    # Dictionary of the number of times a word appears in all of the text
    dictionary = corpora.Dictionary(texts)
    # Filter out uncommon words, keep the most common words
    dictionary.filter_extremes(no_below=5, keep_n=50000)
    return dictionary

def make_corpus(dictionary, texts):
    # Corpus uses the bag-of-words format (bow), i.e. each row in the data is a list of words with their associated word counts.
    corpus = [dictionary.doc2bow(text) for text in texts]
    return corpus
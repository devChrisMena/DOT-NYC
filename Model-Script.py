import tensorflow
import re
import pandas as pd
import csv
import os, sys
from tensorflow.keras.models import load_model

# Vocabulary: All words used, starting by the most frequent
with open(os.path.join(sys.path[0], 'aclImdb/imdb.vocab')) as f:
    vocab = [word.rstrip() for word in f]
    # Keep only most frequent 5000 words rather than all 90000
    # Just saving memory - the long tail occurs too few times
    # for the model to learn anything anyway
    vocab = vocab[:5000]
    print('%d words in vocabulary' % (len(vocab),))




def text_tokens(text):
    text = text.lower()
    text = re.sub("\\s", " ", text)
    text = re.sub("[^a-zA-Z' ]", "", text)
    tokens = text.split(' ')
    return tokens


def bow_onehot_vector(tokens):
    vector = [0] * len(vocab)
    for t in tokens:
        try:
            vector[vocab.index(t)] = 1
        except:
            pass  # ignore missing words
    return vector

sentiment = load_model("Model_1.h5")

# stats data
data = []
csv_file = pd.read_csv('post_data.csv') # open csv file

for text in csv_file['Comment']:
  test_text = text
  test_tokens = text_tokens(test_text)
  print(test_text)
  predicton = sentiment.predict([bow_onehot_vector(test_tokens)])[0]
  print(predicton)
  stats = (text, predicton)
  data.append(stats)

# saving data
with open('post_data.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['Tweet', 'Prediction']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
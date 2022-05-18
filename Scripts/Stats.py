from operator import index
from tensorflow.keras.models import load_model
import re
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import csv
import os

# Vocabulary: All words used, starting by the most frequent
with open('aclImdb/imdb.vocab', encoding="UTF-8") as f:
    vocab = [word.rstrip() for word in f]
    # Keep only most frequent 5000 words rather than all 90000
    # Just saving memory - the long tail occurs too few times
    # for the model to learn anything anyway
    vocab = vocab[:5000]
    print('%d words in vocabulary' % (len(vocab),))

def text_tokens(text):
    if type(text) == float:
        return ''
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
        except ValueError:
            pass
        except Exception:
            pass  # ignore missing words
    return vector

def twitterStats():
    filename = 'Twitter_' + datetime.datetime.now().strftime("%Y%m%d") + '.csv'
    try:
        twitter = pd.read_csv(filename, index_col=0)
    except:
        print('File does not ')
    # stats data
    data = []
    sentiment = load_model('saved_model/model.h5')

    for text in twitter['Comments']:
        test_text = text
        test_tokens = text_tokens(test_text)
        print(test_text)
        predicton = sentiment.predict([bow_onehot_vector(test_tokens)])[0]
        print(predicton)
        stats = (text, predicton)
        data.append(stats)

    # saving data
    with open('tweet_data.csv', 'w', newline='', encoding='utf-8') as f:
        header = ['Tweet', 'Prediction']
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    stats_file =  pd.read_csv('tweet_data.csv')
    p = stats_file['Prediction']
    x = []

    for y in p:
        x.append(float(y[1:-1]))

    neutral = 0
    positive = 0
    negative = 0

    for value in x:
        if float(value) >= 0.7:
            positive += 1
        elif float(value) < 0.7 and float(value) >= 0.5:
            neutral +=1
        else:
            negative +=1

    twitter['Prediction'] = x
    twitter.loc[:, ~twitter.columns.str.contains('^Unnamed')]
    twitter.to_csv(filename)

    try:
        os.remove('tweet_data.csv')
    except:
        print('No file')

    labels = ['Positive', 'Neutral', 'Negative']
    val = [positive, neutral, negative]
    explode = (0, 0.1, 0,)

    bar_fig = 'Twitter_Bar_Plot' + datetime.datetime.now().strftime("%Y%m%d") + '.png'
    plt.bar(labels, val)
    plt.show()

    pie_fig = 'Twitter_Pie_Chart' + datetime.datetime.now().strftime("%Y%m%d") + '.png'
    plt.figure(figsize=(3, 3))
    plt.pie(val, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.show()


def instagramStats():
    filename = 'Instagram_' + datetime.datetime.now().strftime("%Y%m%d") + '.csv'
    ig = pd.read_csv(filename, index_col=0)
    # stats data
    data = []
    sentiment = load_model('saved_model/model.h5')

    for text in ig['Comment']:
        test_text = text
        test_tokens = text_tokens(test_text)
        print(test_text)
        predicton = sentiment.predict([bow_onehot_vector(test_tokens)])[0]
        print(predicton)
        stats = (text, predicton)
        data.append(stats)

    # saving data
    with open('ig_data.csv', 'w', newline='', encoding='utf-8') as f:
        header = ['Comment', 'Prediction']
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    stats_file =  pd.read_csv('ig_data.csv')
    p = stats_file['Prediction']
    x = []

    for y in p:
        x.append(float(y[1:-1]))

    neutral = 0
    positive = 0
    negative = 0

    ig['Prediction'] = x
    ig.to_csv(filename)

    try:
        os.remove('ig_data.csv')
    except:
        print('No file')

    for value in x:
        if float(value) >= 0.7:
            positive += 1
        elif float(value) < 0.7 and float(value) >= 0.5:
            neutral +=1
        else:
            negative +=1

    labels = ['Positive', 'Neutral', 'Negative']
    val = [positive, neutral, negative]
    explode = (0, 0.1, 0,)

    bar_fig = 'Instagram_Bar_Plot' + datetime.datetime.now().strftime("%Y%m%d") + '.png'
    plt.bar(labels, val)
    plt.show()

    pie_fig = 'Instagram_Pie_Chart' + datetime.datetime.now().strftime("%Y%m%d") + '.png'
    plt.figure(figsize=(3, 3))
    plt.pie(val, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.show()

if __name__ == "__main__":
    instagramStats()
    twitterStats()
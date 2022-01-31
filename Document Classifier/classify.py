# classify.py : Classify text objects into two categories
#
# PLEASE PUT YOUR NAMES AND USER IDs HERE
# Ayush Sanghavi : sanghavi       Vighnesh Kolhatkar : vkolhatk       Vishwas Desai : visdesai
# Based on skeleton code by D. Crandall, March 2021
#

import sys
import pandas as pd
import re


def load_file(filename):
    objects = []
    labels = []
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ', 1)
            labels.append(parsed[0] if len(parsed) > 0 else "")
            objects.append(parsed[1] if len(parsed) > 1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}


# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to documents
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each document
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#


# Function to clean the dataset (train and test).
# In this function, the data that is in dictionary format is converted to pandas dataframe
# Here, the characters other than alphabets are replaced with empty spaces.
# The remaining words contain uppercase and lowercase chars. It's converted to lowercase.
# Redundant spaces are removed from the start and end of words.

def clean_set(set_clean):
    set_clean = pd.DataFrame.from_dict(set_clean, orient='index')
    set_clean = set_clean.transpose()
    # set_clean.head()
    # set_clean['objects'] = set_clean['objects'].str.replace('\W', ' ') # Removes punctuation
    set_clean['objects'] = set_clean.replace(regex=r'[^a-zA-Z]+', value=' ')
    # set_clean['objects'] = set_clean.replace(regex = r'_', value = '')
    set_clean['objects'] = set_clean['objects'].str.lower()
    set_clean['objects'] = set_clean['objects'].str.strip()
    return set_clean


# Model fit function is created which takes parameters : prior probabilities P(EastCoast), P(WestCoast), and
# likelihood : likelihood_eastcoast and likelihood_westcoast
# calculates the posterior probabilities of P(EastCoast|tweet) and P(WestCoast|tweet) using the
# Naive-Bayesian formula for conditionally independent variables
# If P(EastCoast|tweet) is greater than P(WestCoast|tweet) then it returns class as EastCoast
# else it returns class WestCoast

def model_fit(tweet, p_westcoast, p_eastcoast, likelihood_westcoast, likelihood_eastcoast):
    tweet = tweet.split(" ")
    p_westcoast_given_tweet = p_westcoast
    p_eastcoast_given_tweet = p_eastcoast

    for word in tweet:
        if word in likelihood_westcoast:
            p_westcoast_given_tweet *= likelihood_westcoast[word]

        if word in likelihood_eastcoast:
            p_eastcoast_given_tweet *= likelihood_eastcoast[word]

    if p_eastcoast_given_tweet > p_westcoast_given_tweet:
        return 'EastCoast'
    elif p_eastcoast_given_tweet < p_westcoast_given_tweet:
        return 'WestCoast'

# Ref: https://towardsdatascience.com/introduction-to-na%C3%AFve-bayes-classifier-fa59e3e24aaf
# Ref : https://www.youtube.com/watch?v=O2L2Uv9pdDA
def classifier(train_data, test_data):
    # Cleaning the training and testing data
    train_set = clean_set(train_data)
    test_set = clean_set(test_data)
    class1 = train_set['classes'].iloc[0]
    class2 = train_set['classes'].iloc[1]

    # Reference: https://gist.githubusercontent.com/sebleier/554280/raw/7e0e4a1ce04c2bb7bd41089c9821dbcf6d0c786c/NLTK's%2520list%2520of%2520english%2520stopwords
    stopword = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its',
                'before',
                'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they',
                'not',
                'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because',
                'doing',
                'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 'be',
                'we',
                'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 'or', 'own', 'into', 'yourself',
                'down',
                'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more',
                'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will',
                'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have',
                'in',
                'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after',
                'most', 'such', 'why', 'off', 'yours', 'so', 'the', 'having', 'once', 'jobs', 'job', 'amp', 'im']

    # Creating a vocabulary of unique words in tweets without the stopwords
    vocabulary = []
    for twt in train_set['objects'].values.tolist():
        twt = twt.split(" ")
        for word in twt:
            if word not in stopword and word != "" and word != " ":
                vocabulary.append(word)
    vocabulary = list(set(vocabulary))

    # Isolating westcoast and eastcoast tweets first
    westcoast_tweets = train_set[train_set['labels'] == 'WestCoast']
    eastcoast_tweets = train_set[train_set['labels'] == 'EastCoast']

    # P(westcoast) and P(eastcoast)
    p_westcoast = len(westcoast_tweets) / len(train_set)
    p_eastcoast = len(eastcoast_tweets) / len(train_set)

    # N_westcoast
    n_words_per_westcoast_tweet = westcoast_tweets['objects'].apply(len)
    n_westcoast = n_words_per_westcoast_tweet.sum()

    # N_eastcoast
    n_words_per_eastcoast_tweet = eastcoast_tweets['objects'].apply(len)
    n_eastcoast = n_words_per_eastcoast_tweet.sum()

    # Initiate Likelihood
    likelihood_westcoast = {unique_word: 0 for unique_word in vocabulary}
    likelihood_eastcoast = {unique_word: 0 for unique_word in vocabulary}

    # Calculating the Likelihood
    for word in vocabulary:
        n_word_given_westcoast = westcoast_tweets['objects'].str.contains(
            word).sum()  # westcoast_tweets already defined
        p_word_given_westcoast = (n_word_given_westcoast + 1) / (n_westcoast)
        likelihood_westcoast[word] = p_word_given_westcoast

        n_word_given_eastcoast = eastcoast_tweets['objects'].str.contains(
            word).sum()  # eastcoast_tweets already defined
        p_word_given_eastcoast = (n_word_given_eastcoast + 1) / (n_eastcoast)
        likelihood_eastcoast[word] = p_word_given_eastcoast

    ## Testing model on test set
    # The function model_fit is applied on all the rows of the column 'objects' and the values are stored
    # in a a new column created 'predicted'
    # Results are stored in a list which is created by converting the 'predicted' column to list format.

    test_set_final = test_set.copy(deep=True)
    test_set_final['predicted'] = test_set_final['objects'].apply(model_fit, args=(
    p_westcoast, p_eastcoast, likelihood_westcoast, likelihood_eastcoast))
    results = test_set_final['predicted'].values.tolist()

    return results


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    if (train_data["classes"] != test_data["classes"] or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # #make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results = classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([(results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"]))])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))



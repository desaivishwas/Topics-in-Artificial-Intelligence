# Part-of-speech tagging

##### Referred sources have been cited

Part of Speech Tagging (POS) is a process of tagging sentences with part of speech such as nouns, verbs, adjectives and adverbs, etc.


### Problem Statement
Use the training corpus to estimate parameters and, display the output a) Simple Model b) HMM c) Complex model.
The problem consists of 3 parts:-

    - Performing a Parts of Speech tagging on a simplified Bayes Net
    - Performing Parts of Speech tagging using HMM / Viterbi algorithm
    - Performing Parts of Speech tagging by implementing Gibbs Sampling


--------
Firstly, by using the trained data, we store the emission, transition probabilities in a dictionary.

### Bayes Net
The bayes net probability was calculated and thenn stored in a dictionary. The probability of each word given speech was stored and normalized.

### Formulating the estimation:

Consider W as the input word sequence and T is an input tag (POS) sequence i.e.

`W = w1,w2,…wn`

`T = t1,t2,…tn`

Our goal is to find a tag sequence T that maximizes P(T | W).

Using Bayes rule:

`maximize P(T∣W)=P(W∣T)∗P(T)/P(W)∝P(W∣T)∗P(T)`

----------
## Implementation
### Getting the posterior probability

- Normalize the sum of all the words and pos from their dictionaries.
  
- For Bayes Net, we calculate the posterior probability using the emission probability.
  
- For the bayes net we calculate the probability using the emission probability. 
  
- Similiarly for the Viterbi algorithm, we make us of the emission probability and transition probabilty in getting the posterior probability. 

- And for Gibbs sampling, we calculate the probability using the emission, transions probabilty and Parts of Speech count.
Emission Probability

----------
#### Emission Probability : Each word's emission probability was calculated and stored in a dictionary. Emission probability is a set of probabilities that each word is of the correct parts of speech i.e. the probabilty of the word 'Bruce' being a noun etc.

---------
#### Transmission Probability: The likelihood of a particular sequence, such as a noun being preceded by a model, a model by a verb, and a verb by a noun, is known as the transition probability. The probability should be high for a sequence to be right.

---------
#### Viterbi: The Viterbi algorithm is a dynamic programming algorithm for finding the most likely sequence of hidden states—called the Viterbi path—that results in a sequence of observed events. After applying the Viterbi algorithm the model tags the sentence into its correct tags.

---------
#### Gibbs sampling: The ability to sample from the target distribution's conditional distributions. Given a joint distribution and sampling them iteratively by its conditional distributions will give a samples which contain tags that will occur frquenlty of a particular word which is then assigned as its final tag.
-------
### References: 
- https://www.mygreatlearning.com/blog/pos-tagging/
- https://courses.engr.illinois.edu/cs440/fa2018/Lectures/lect20.html
- https://www.freecodecamp.org/news/an-introduction-to-part-of-speech-tagging-and-the-hidden-markov-model-953d45338f24/
- https://medium.com/analytics-vidhya/parts-of-speech-pos-and-viterbi-algorithm-3a5d54dfb346



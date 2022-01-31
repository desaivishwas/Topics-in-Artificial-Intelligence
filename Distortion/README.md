# Noisy Image Converter
#### Reading text using Simple Bayes' Net, Variable Elimination and Viterbi Algorithm

## Problem Statement : 
- Our goal is to recognize the text in the images given

- But the images are noisy.

- Assumption : All text has same font and font size. We’ll also assume that our text only has the 26 uppercase latin characters, the 26 lowercase characters, the 10 digits, space, and 7 punctuation symbols.

- We pass the following system arguments ; 
  1) courier-train.png that has the image of the letters used for training.
  2) The train-text.txt; that is the representative of English Language.
  3) Passing one of test image.
    
## Motivation : 
- Using the advantages of Simple Bayes' nets and HMM we are trying to actually implement and recognize the text.
- Most modern systems in this technological era are good at recognizing texts but it gets difficult when the character is weird or lack of training data or when the character is isolated.
- Using the concept of HMM, viterbi algorithm and probabilities, we can incorporate the art of recognizing the characters of the texts.  


## Implementation: 

### load_letters : 
- This function was given to us as a starter code.
- It makes sure about the font size and represents the image as List of Lists in which the characters are represented as a 2D grid of black and white dots.

### load_training_letters:
- Loading the 26 alphabets, in both lower and upper cases, 10 digits, space, and 7 punctuation symbols.

-------
- We are then calculating the transition probabilities of each Character.
- Transition probability is the probability of moving from one state to another.
- We then create a char_fringe which stores the characters as list.
- We calculate the initial probabilities and then the emission probabilities.
- After we have initial probabilities, transition probabilities and emission probabilities we implement different methods to
  recognize the text in an image provided as test-image file and display the recognized text.
-------
- First Approach : Our first approach was Simple Bayes' Net.
- Second Approach : HMM Variable Elimination method
- Third Approach : Viterbi Algorithm
-------
- We are using a sample text file as a texual training data file to calculate the initial probabilities as well as
  the transition probabilities. 
- To calculate the emission probability; We compare the pixels and the pixel info of each of the character of the image training data.
- For the same; we have used the pixel information we have. There would be two cases: first is when the image is densely populated with black pixels and second is when the image has sparse black pixels.
- We assign some weights to black, less black pixels and non matching pixels where the test image character's pixel is white and train image character's pixel is black.
-------
- For Variable elimination:
- To perform var elimination we have called two functions : calc_fwd_prob and calc_bwd_prob on chars of the test image.
  We marginalize the near-by chars to estimate the target char.  
-------
- For viterbi algorithm ; state1 is our current state and state0 is our previous state.
  We calculate the most probable state at time t, and find the previous hidden state.
- We use heapq (priority queue) to pop the states and find the previous max state.
------
- References: 
  
  - https://www.youtube.com/watch?v=kqSzLo9fenk
  
  - https://beginnersbook.com/2019/03/python-ord-function/#:~:text=The%20ord()%20function%20in,value%20of%20character%20'B'
  
  - https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.89.6415&rep=rep1&type=pdf
  
  - https://towardsdatascience.com/optical-character-recognition-ocr-with-less-than-12-lines-of-code-using-python-48404218cccb
  
------

# Document classification

## Description 

### Cleaning :

- The train data and test data is in dictionary format. 
- It is cleaned using the clean_set function .
- In this function, the data that is in dictionary format is converted to pandas dataframe
- Here, the characters other than alphabets are replaced with empty spaces.
- The remaining words contain uppercase and lowercase chars. It's converted to lowercase.
- Redundant spaces are removed from the start and end of words.



### Classifier :

- The cleaned data is then used. 

- It Creates a vocabulary of unique words in tweets without the stopwords.

- The westcoast and eastcoast tweets are isolated first in a separate dataframe.

- P(westcoast) and P(eastcoast) are computed.

- N_westcoast and N_eastcoast are computed which contains number of WestCoast tweet words and number of EastCoast tweet words respectively.

- Likelihood Probabilities are computed with Laplace Smoothing : number of words|EastCoast + 1/ number of EastCoast tweet words and 
    number of words|WestCoast + 1/ number of WestCoast tweet words are computed.




### Model_fit():
- This function takes parameters : prior probabilities P(EastCoast), P(WestCoast), and likelihood : likelihood_eastcoast and likelihood_westcoast
    calculates the posterior probabilities of P(EastCoast|tweet) and P(WestCoast|tweet) using the

- Naive-Bayesian formula for conditionally independent variables

- If P(EastCoast|tweet) is greater than P(WestCoast|tweet) then it returns class as EastCoast
    else it returns class WestCoast




### Testing :

- Testing model on test set

- The function model_fit is applied on all the rows of the column 'objects' and the values are stored
    in a a new column created 'predicted'

- Results are stored in a list which is created by converting the 'predicted' column to list format.



### The probabilities : P(WestCoast), P(EastCoast), P(tweet|WestCoast), P(tweet|EastCoast) are computed with Laplace smoothing :
        Probability of WestCoast : 0.4934607131909676
        Probability of EastCoast : 0.5065392868090324
            
### Then Naive-Bayes Classifier is applied using the functions 'classifier' and 'model_fit'
- `Accuracy of our classifier :  82.75 `


-  Summarizing Naive-Bayes Classifier, it assumes class conditional independent probabilities, where we calculate 'likelihood' 
    i.e.  P(word | WestCoast) and P(word | EastCoast)  and the prior probabilities i.e. P(WestCoast) and P(EastCoast).

- Then, we use the Naive-Bayesian equation to calculate the Posterior Probabilities i.e. P(WestCoast | word) and P(EastCoast | word). 

- We compare both the values and if P(WestCoast | word) > P(EastCoast | word) we classify it as 'WestCoast'
    else if P(EastCoast | word) > P(WestCoast | word) we classify it as 'EastCoast' 

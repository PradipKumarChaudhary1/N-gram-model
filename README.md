# N-gram-model
Next word prediction using tri-gram model

We built a model which will predict next possible word after every time when we pass some word as an input.
To build this model we have used the concept of Bigrams,Trigrams and quadgrams.
A bigram or digram is a sequence of two adjacent elements from a string of tokens, which are typically letters, syllables, or words.
From the Markov Assumption, we can formally define N-gram models.
Bigrams help to provide the conditional probability of a token given the preceding token, when the relation of the conditional probability is applied:

P(Wi∣Wo…Wi−1 )≈P(Wi∣Wi−1 ) =P(Wi,Wi−1 )/P(Wi-1)

So we have to use tri-gram model.

If we continue the estimation equation, we can form one for trigrams:

P(x3 | x2,x1) = count(x1,x2,x3)/count(x1,x2)

Probability of occurrence of the word given last two words is our trigram model.

process-

1- preprocessing and cleaning the training text  

2- After Preprocessing of the corpus:
We then created a python dictionary by storing the current word as a list of 'values' and previous word as a 'key’.We then created another dictionary of a dictionary of python for storing required probabilities for both bigram and trigram model.For storing probabilities of first two words of the sentence we have used bigram model and for the rest of the words, we have used trigram model.
We then sort the probabilities in decreasing order.
User could type any word at first time after user input our model will suggest top five words according to bigram model probability distribution.When user type second word our model
suggest top five words according to trigram model probability distribution.

3-  apply tri-gram model

4- Smoothing :We also applied  laplace’s smoothing to both our trigram and bigram model.
   Smoothing is done to avoid zero probability for new word prediction.
 
          P(word)= (wordcount+1)/(Total number of words+V)
    We simply add 1 to the numerator and the vocabulary size (V = total number of distinct words) to the denominator of our probability      estimate for bigrams and for trigrams V=total number of distinct bigrams.

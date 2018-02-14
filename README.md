# Confidence Acuraccy test
**Summary:** The script test whether conversation transcripts' confidence is correlated with their accuracy, and visualize this correlation

__Script Details_:_
- Name :        Compare Algorithm's Confidence Level to its Performance
- Arguments :   
    1. A json file of the transcript with confidence level
    2. A txt file of the real transcript
- Returning :   None
- Author :      Yonathan Guttel yesguttel@gmail.com
- Date :        13.02.2018
- Version :     1.0.0
 
### Description

The "Confidence Acuraccy test" scripts is meant to test the hypothesis that automated algorithm confidence in their prediction is correlated which the accuracy of their prediction. That is to say, We assume that the more "sure" the algorithm is in it's answer, the less likely it is to be mistaken.

In order to test this assumption we confornt an audion-to-text ML algorithm which give a conversation transcript based on its recording, with the actual transcript of the conversation. The algorithm produce, alongside the word identification, also a confidence level for each word it predict, and this allows us to test our hypothesis.

The codes recieve a json file, containing transcript of a conversation which was converted to text from audio by an automated algorithm.  the `json` file contain inter alia all the transcript words and a confidence level for each word prediction. a second files the code request oif a `txt` file with the real transcript in it (which will use to test the json transcript accuracy).

The main analysis is based on calculating the proportion of successful predictions out of all predictions for each confidence level, and than calculate the regression of confidence levels vs. the proportion of successful predictions.

***
The code does the following steps (not mentioning regular step such as library uploading, parameters setting  and etc.):

First I create 3 function for later use:
1. `element_json_extractor` - recieves the transcript `json` file and can extract the 'word', 'confidence', 'type', 'from' or 'to' elements as a list. Can be used to extract the words and confidence level form the json file of the transcript.
2. `text_levenshtein_distance` - is computing the Levenshtein distance (the minimal edit distance) between the two texts- in our case the predicted and true transcripts - recives two list to compare and return a comparison list.
3. `accuracy_confidence_correlation` - is the main function of this scripts. It recieves two lists - a comparison list whichwas producted by the text_levenshtein_distance function, and a confidence_list which is a list of the confidence level of each word in the json transcript text (produced by the element_json_extractor function). It has also a optional parameter TH_min_num, which define what is the minimum number of occurances for a confidence level in the text in order to be included in the analysis (so we could remove low occurrences which can acts as outliers). The function return a data frame with two columns; the first column is confidence levels and contain only rows for which the occurance is greater than TH_min_num, and a second column with a ratio of the true prediction out of all the prediction for each specific confidence level.


Than the script is run for the test:
1. Upload the data.
2. Extract word and confidence lists using `element_json_extractor`.
3. Write transcript word list to a `txt` file.
4. Computing the Levenshtein distance of the words list and the true data using `text_levenshtein_distance`.
5. Create a data frame of the results using `accuracy_confidence_correlation`.
6. Visualization of the results
7. Write transcript word list to a `HTML` file, in which low confidennce words are highlighted in red.


***
### Conclusions

Runing it on our data produced the following results:


![alt text](https://github.com/YG15/Confidence_Acuraccy_test/blob/master/images/1st_results_14022018.png  "Logo Title Text 1")

As it can be seen from the data, we couldn't prove high correlation between the confidences level and the accuracy. I suspect that this is a byproduct of one of two things- the fact that almost all predictions are in confidence level 1, which make it prone to mistakes, and a short text, which doesn't allow us to quantify accurately the rest of the confidence levels.



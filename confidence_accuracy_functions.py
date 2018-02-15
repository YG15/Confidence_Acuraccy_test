# Name :        confidence_accuracy_function
# Description : Store the needed function for Confidence_Accuracy test script
# Arguments :   None
# Returning :   None
# Author :      Yonathan Guttel <yesguttel@gmail.com
# Date :        15.02.2018
# Version :     1.0.0

# The "element_json_extractor" recieves the transcript json file and can extract
# the 'word', 'confidence', 'type', 'from' or 'to' elements as a list
import numpy as np
import difflib
import pandas as pd
from IPython.core.display import display, HTML

def element_json_extractor (json, element): #element can be
    transcripts_list=[]
    # break json into parts
    for term in enumerate(json):
        # extract the transcript part from each part of the json
        sub_json= json[term[0]]['result'][0]['alternative'][0]['words']
        for sub_term in enumerate(sub_json):
            # build a list of all the desired elements
            transcripts_list.append(sub_json[sub_term[0]][element])
    # returning the list
    return transcripts_list


# The "text_levenshtein_distance" is computing the Levenshtein distance (the minimal edit distance)
# between the two texts- in our case the predicted and true transcripts

def text_levenshtein_distance (words_list,true_data):
    d = difflib.Differ()
    compare_list=list(d.compare( words_list,true_data))
    return compare_list


# The "accuracy_confidence_correlation" function is the main function of this scripts
# It saves all words occurances and assign them 1 if correct and 0 if wrong.
# The function receives two lists - a comparison list which is a product of the text_levenshtein_distance fun
# and a confidence_list which is a list of the confidence level of each word in the json transcript text
# (produced by the element_json_extractor function ). its has also a optional parameter TH_min_num,
# which define what is the minimum number of occurances for a confidence level in the text in order to be
# included in the analysis.
# The function return a data frame with two columns, and rowa as the number of words which had confidence
# level greater than TH_min_numthe. The first column is confidence levels, the second column is prediction with 1 in case
# the prediction was right and 0 in case it wasn't

def accuracy_confidence_correlation(compare_list, confidence_list, TH_min_num=0):
    # create vector with all possible confidence level
    confid_range = np.arange(0, 1.01, 0.01)
    confid_list = [str(round(a, 2)) for a in confid_range]
    # creates a dictionary to store results
    result_dic = {}
    index = 0
    # count cases in which the transcript list fits the true text ("-") and when it doesn't (" ")
    for item in compare_list:
        if item[0] == " ":
            conf_level = str(float(confidence_list[index]))
            result_dic.setdefault(conf_level, []).append(0)
            index += 1
        if item[0] == "-":
            conf_level = str(float(confidence_list[index]))
            result_dic.setdefault(conf_level, []).append(1)
            index += 1
    list_con_levels = []
    list_con_levels_results = []
    for key in result_dic.keys():
        if len(result_dic[key]) > TH_min_num:
            for elements in result_dic[key]:
                list_con_levels.append(float(key))
                list_con_levels_results.append(elements)
    final_df = pd.DataFrame({'confidence_level': list_con_levels, 'prediction': list_con_levels_results})

    return final_df


# Display text as HTML that highlight in red low confidence words V1

def html_displayer(words_list,confidence_list,TH_highligh_low,TH_low_conf):
    html_string=''
    for lines in enumerate(words_list):
        if TH_highligh_low==False:
            html_string=html_string+('<h4>' +lines[1]+ '</h4>\n')
        else:
            if confidence_list[lines[0]]>TH_low_conf:
                html_string=html_string+('<h4>' +lines[1]+ '</h4>\n')
            else:
                html_string=html_string+('<h4 style=\"background-color:red;\">' +lines[1]+ '</h4>\n')
    #print(html_string)
    display(HTML(html_string))
import json
import math
def load_journal(file):     #Function for loading json data.
    file = open(file,'r')
    data = file.read()
    json_data =json.loads(data)
    return json_data        #Json data returned. 


def compute_phi(events):    #Find correlation of given event.
    file = 'journal.json'
    journal = load_journal(file)#Loading json data and stored to a variable.
    n11 , n10 , n01 ,n00   = 0 , 0 , 0 , 0 
    event = events
    for daily_journal in journal:           #Loop to get daily journel and checking conditions to find values for calculation of correlation.
        if event in (daily_journal['events']):
            if daily_journal['squirrel']== True:
                n11 += 1
            else: 
                n10 += 1
        else:
            if daily_journal['squirrel']== True:
                n01 += 1
            else: 
                n00 += 1

    n1plus = n11 + n10
    n0plus = n01 + n00
    nplus1 = n11 + n01
    nplus0 = n10 + n00

# ϕ = (n₁₁ * n₀₀ - n₁₀ * n₀₁) / sqrt(n₁₊ * n₀₊ * n₊₁ * n₊₀)
    phi = (n11 * n00 - n10 * n01) / math.sqrt(n1plus * n0plus * nplus1 *nplus0) 
    return phi      #Correlation of an event returned.


def compute_correlation(): #Function to compute correlation of each events in the journal.
    file = 'journal.json'
    journal = load_journal(file)
    correlation_data = {}       #Created dictionary for adding an event and its correlation value.
    count = 0
    for daily_journal in journal:   #loop to get daily event and value.
        for event  in daily_journal['events']:     #Loop to get events of each day from daily journal.
            if event not in correlation_data:       #Checking whether event already present in dictionary.
                correlation_value = compute_phi(event)   #Calculating correlation for each event using 'compute_phi' function.   
                correlation_data[event]=correlation_value   #Adding key and value to dictionary.
            else:
                pass

    return correlation_data #Returning dictionary.

def diaganose():    #Function to calculate highly negatively correlated and highly  positively correlated. 
    correlations = compute_correlation()    #Dictionary of correlated value and events.
    correlation_list =list( correlations.values())
    correlation_list.sort()
    highly_negatively_correlation = correlation_list[0]
    highly_postively_correlation = correlation_list[-1]
    for correlated_data in correlations.items():
        if correlated_data[1] == highly_postively_correlation:
            highly_negatively_correlated = correlated_data[0]
        if correlated_data[1] == highly_negatively_correlation:
            highly_postively_correlated = correlated_data[0]

    print("Highly negatively correlated: " ,highly_negatively_correlated,highly_negatively_correlation)

    print("Highly positively correlated: " ,highly_postively_correlated,highly_postively_correlation)

diaganose()

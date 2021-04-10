from textblob import Textblob as tb

'''
Description: This code tests the polarity and subjectivity of the Bradford data file.

def get_polarity(text):
    '''
    This function returns the polarity of a text on a scale of [-1, 1], with -1
    representing a negative sentiment and 1 representing a positive sentiment.
    Parameters:
        :text: str
    Returns:
        A float representing the polarity of the text.
    '''
    return tb(text).sentiment.polarity
    
def get_subjectivity(text):
    '''
    This function returns the subjectivity of a text on a scale of [0, 1], with the closer 
    to 1 meaning the text is more opinionated rather than factual.
    Parameters:
        :text: str
    Returns:
        A float representing the subjectivity of the text.
    '''
    return tb(text).sentiment.subjectivity
    
def get_polarity_analysis(text):
    '''
    This function returns the polarity analysis of a text as Negative, Neutral, or Positive.
    Parameters:
        :text: str
    Returns:
        A str representing the polarity of the sentiment.
    '''
    score = get_polarity(text)
    if score < 0:
        return 'Negative Sentiment'
    elif score == 0:
        return 'Neutral Sentiment'
    else:
        return 'Positive Sentiment'
    
def get_subjectivity_analysis(text): 
    '''
    This function returns the subjectivity analysis of a text as Objective, Moderately Objective, Moderately Subjective, or Subjective.
    Parameters:
        :text: str
    Returns:
        A str representing the subjectivity of the sentiment.
    '''
    score = get_subjectivity(text)
    if score == 0:
        return 'Objective Statement'
    elif score < 0.4:
        return 'Moderately Objective Statement'
    elif score > 0.7:
        return 'Subjective Statement'
    else: 
        return 'Moderately Subjective Statement'

def p_s_analysis(text):
    print(text)
    print('Polarity: ', round(get_polarity(text), 3), '-', 'Subjectivity: ', round(get_subjectivity(text), 3))
    print(get_polarity_analysis(text), ': ', get_subjectivity_analysis(text))

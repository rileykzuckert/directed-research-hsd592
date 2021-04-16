'''
Description: This function, in combination with the Bradford data frames, assesses the valence (polarity and subjectivity) of a user's input in a practice medical student interview.
'''
def get_polarity(df):
    '''
    This function returns the polarity of a text on a scale of [-1, 1], with -1
    representing a negative sentiment and 1 representing a positive sentiment.
    Parameters:
        :text: str
    Returns:
        A float representing the polarity of the text.
    '''
    polarity_list = []
    user_inputs = df['User']
    for i in range(len(user_inputs)):
      polarity = tb(user_inputs[i]).sentiment.polarity
      polarity_list.append(polarity)
    return polarity_list

def get_subjectivity(df):
    '''
    This function returns the subjectivity of a text on a scale of [0, 1], with the closer 
    to 1 meaning the text is more opinionated rather than factual.
    Parameters:
        :text: str
    Returns:
        A float representing the subjectivity of the text.
    '''
    subjectivity_list = []
    user_inputs = df['User']
    for i in range(len(user_inputs)):
      subjectivity = tb(user_inputs[i]).sentiment.subjectivity
      subjectivity_list.append(subjectivity)
    return subjectivity_list

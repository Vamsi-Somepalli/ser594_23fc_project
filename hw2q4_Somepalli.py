import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

__author__ = "Vamsi Krishna Somepalli"
__date__ = "9/25/2023"
__assignment = "SER594: Homework 2 Q4 Programming"


def web_scrapping(url, classname):
    # Import Requests, Beautiful Soup
    import requests
    from bs4 import BeautifulSoup
    
    """
    :param url: URL for web scrapping
    :param classname:  classname string of the element with reviews
    :return: list 

    Request data for the url. 
    Create a soup (parse the html data).
    Manually: go to inspect element on the reviews and check the class of the element.
    Get and return the plain text (preferably in list format).
    """
    # TODO
    reviews=[]
    res = requests.get(url)
    if(res.status_code==200):
        soup = BeautifulSoup(res.text, 'html.parser')
        review_elements = soup.find_all(class_=classname)
        for element in review_elements:
            reviews.append(element.get_text())
    # Return the plain text (list)
    return reviews


def preprocessing(reviews):
    # Import nltk - only use nltk library to perform all the following processing.
    import nltk
    """
    :param reviews: Reviews list
    :return: Dataframe with processed reviews
    Lower-case all words.
    Remove all punctuations.
    Remove stopwords. (Stopwords are the lists in the nltk library that are trivial and not relevant to the context/text.)
    Perform lemmatization on the data.
    """
    # TODO
    reviews['cleaned_review'] = reviews['review'].apply(lambda rew: rew.lower())#tolowercase
    reviews['cleaned_review']=reviews['cleaned_review'].str.replace('[^\w\s]|_','', regex=True)#remove_punctuation
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    reviews['cleaned_review'] = reviews['cleaned_review'].apply(lambda rew: ' '.join([word for word in rew.split() if word not in stop_words]))#stopwords
    # Lemmatization
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()
    reviews['cleaned_review'] = reviews['cleaned_review'].apply(lambda rew: ' '.join([lemmatizer.lemmatize(word) for word in rew.split()]))
    # Return the dataframe with the processed data
    return reviews


if __name__ == '__main__':
    # give your desired urls and classnames, preferably from yelp
    url1,url2 = "https://www.yelp.com/biz/firehouse-subs-san-antonio-15","https://www.yelp.com/biz/bindaas-indian-street-food-cafe-tempe#reviews"
    classname1,classname2 = "comment__09f24__D0cxf","comment__09f24__D0cxf"

    # Part 1
    review_list1 = web_scrapping(url1, classname1)
    review_list2 = web_scrapping(url2, classname2)
    #print(review_list1)
    # Create a pandas dataframe from array
    df1 = pd.DataFrame(np.array(review_list1), columns=['review'])
    df2 = pd.DataFrame(np.array(review_list2), columns=['review'])
    # Part 2
    processed_review1 = preprocessing(df1)
    processed_review2 = preprocessing(df2)
    print(processed_review1['cleaned_review'])
    print(processed_review2['cleaned_review'])
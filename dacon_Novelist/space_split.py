from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import re

def space_split (data) :
    """ Simple Space Split Preprocessing 
    
        Input : Pandas Series  
        
        you have to download nltk stopwords   
        
        "import nltk
        nltk.download('stopwords')
        " 

    """


    stwd = stopwords.words('english')
    
    pat= re.compile('[^a-z ]')

    pre_list= []
    for i in range(len(data)):
        data[i]= data[i].lower()
        data[i]= data[i].strip()
        a= pat.sub('',data[i])
        a= a.split(' ')

        token_list=[]
        
        for token in a:
            if token not in stwd:
                token_list.append(token)
            
        pre_list.append(token_list)
    



    return pre_list
    

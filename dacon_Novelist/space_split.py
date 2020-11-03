
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

def space_split (data,token_len) :
    """ Simple Space Split Preprocessing 
    
        Input
        data : Pandas Series 
        token_len : remove token length under token_len  

        
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
            if token not in stwd and len(token) > token_len :
                token_list.append(token)
            
        pre_list.append(token_list)
    

    return pre_list
    




def lemmatization (data) :
    """ 
        after space_split, input data
        Input : data preprocessed with space_split
        
        you have to download nltk wordnet, universal_tagset   
        
        "import nltk
        nltk.download('wordnet')
        nltk.download('universal_tagset')
        " 
        """ 


    wnl = WordNetLemmatizer()

    lemma_list =[]
    for j in range(len(data)):
        token_list=[]
        for i in range(len(data[j])):
            if get_wordnet_pos(pos_tag([data[j][i]],tagset='universal')[0][1]) !='':
                token_list.append(wnl.lemmatize(data[j][i],get_wordnet_pos(pos_tag([data[j][i]],tagset='universal')[0][1])))
            else :
                token_list.append(wnl.lemmatize(data[j][i]))

        lemma_list.append(token_list)

    return lemma_list

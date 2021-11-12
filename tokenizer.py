import re

def tokenizer(sentence, nlp, stop_words):
    """
    Function for tokenization and lemmatization of sentence.
    Some regexps for data cleaning and processing.

    Parameters
    ----------
    sentence : string
        sentence to be tokenized.
    nlp : spacy.lang.en.English
        spacy pipeline (language model).

    Returns
    -------
    tokens : list(string)
        list of tokens from sentence.

    """
    #remove distracting single quotes
    sentence = re.sub('\'','',sentence)

    #remove digits and words containing digits
    sentence = re.sub('\w*\d\w*','',sentence)

    #replace extra spaces with single space
    sentence = re.sub(' +',' ',sentence)
    
    #remove punctuations
    sentence = re.sub(r'[^\w\s]',' ',sentence)
    
    #creating token object
    tokens = nlp(sentence)
    
    #lower, strip and lemmatize
    tokens = [word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in tokens]
    
    #remove stopwords, and exclude words less than 2 characters
    tokens2 = [word for word in tokens if (word not in stop_words and len(word) > 2)]
    
    #return tokens
    tokens = ' '.join(tokens2)
    return tokens

    
    
    
    
    
    
    
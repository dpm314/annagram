# Old way with two FOR loops:
"""
def stringAnagram(query, dictionary):
    queryCount = [0]*len(query)
    for (queryIndex, queryWord) in enumerate(query):
        for dictionaryWord in dictionary:
            if len(queryWord) == len(dictionaryWord) and set(queryWord) - set(dictionaryWord) == set():
                queryCount[queryIndex] +=1
    return queryCount
"""
################################################################################
# Solution using only one FOR loop:
def stringAnagram1Loop(query, dictionary):
    queryCount = [0]*len(query)
    for (queryIndex, queryWord) in enumerate(query):
        localCount = [1 for dictionaryWord in dictionary if len(queryWord) == len(dictionaryWord) and set(queryWord) - set(dictionaryWord) == set()]
        queryCount[queryIndex] = len(localCount)
    return(queryCount)
#%% Tests:
dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']
print( stringAnagram1Loop(query, dictionary)) #prints [3, 2, 0] w^5
#%%
dictionary = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on']
query = ['two', 'bca', 'no', 'listen']
print( stringAnagram1Loop(query, dictionary)) #prints [2, 1, 2, 3] w^5
################################################################################
# Solution using only No FOR loop:
def stringAnagramListComp(query, dictionary):
    return [len([1 for dictionaryWord in dictionary if sorted(queryWord)==sorted(dictionaryWord)]) for queryWord in query]
#%% Tests:
dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']
print( stringAnagramListComp(query, dictionary)) #prints [3, 2, 0] w^5
#%%
dictionary = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on', 'aabc']
query = ['two', 'bca', 'no', 'listen', 'ccba']
print( stringAnagramListComp(query, dictionary)) #prints [2, 1, 2, 3] w^5
################################################################################
#%%
def stringAnagramLambda(query, dictionary):
    f = lambda queryWord:[1 for dictionaryWord in dictionary if sorted(queryWord)==sorted(dictionaryWord)]
    return [len(f(word)) for word in query]
dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']
print( stringAnagramLambda(query, dictionary)) #prints [3, 2, 0] w^5
#%%
dictionary = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on', 'aaaabc']
query = ['two', 'bca', 'no', 'listen', 'ccccba']
print( stringAnagramLambda(query, dictionary)) #prints [2, 1, 2, 3] w^5
#%%

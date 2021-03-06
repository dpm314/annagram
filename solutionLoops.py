def stringAnagram(query, dictionary):
    queryCount = [0]*len(query)
    for (queryIndex, queryWord) in enumerate(query):
        for dictionaryWord in dictionary:
            if len(queryWord) == len(dictionaryWord) and set(queryWord) - set(dictionaryWord) == set():
                queryCount[queryIndex] +=1
    return queryCount
#%% Tests:
dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']
print( stringAnagram(query, dictionary)) #prints [3, 2, 0] w^5
#%%
dictionary = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on']
query = ['two', 'bca', 'no', 'listen']
print( stringAnagram(query, dictionary)) #prints [2, 1, 2, 3] w^5

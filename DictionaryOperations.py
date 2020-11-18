TestDictionary = {'Key1':'v1','key2':'v2', 'key3':'v3'}
print(TestDictionary['key3'])
DictionaryWithListandDictinary = {'k1':'v1','k2':22,'k3':[1,2,3,4],'k4':{'InnerK1':'InnerV1','InnerK2':'InnerV2', 'InnerK3':'InnerV3'}}
print(DictionaryWithListandDictinary['k1'])
print(DictionaryWithListandDictinary['k2'])
print(DictionaryWithListandDictinary['k3'])
print(DictionaryWithListandDictinary['k3'][1])
print(DictionaryWithListandDictinary['k4'])
print(DictionaryWithListandDictinary['k4']['InnerK2'])
print(TestDictionary.values())
print(TestDictionary.keys())
print(TestDictionary.items())


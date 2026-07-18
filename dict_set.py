#dictionary = store key:value pair , mutable,does not store duplicate values
#set=collection of unorderd items, set is mutable but elements r immutable and must be unique

dict={
    "name":"Janvi",
    "age":21,
    "location":"Pune",
    "marks":{ # nested dictionary
        "FE":8.77,
        "SE":8.94,
        "TE":9.33
    }
}
print(dict)
print(dict["marks"]) #retrive marks
dict["name"]="Tanvi" #change the name 
print(dict["marks"]["FE"])
print(dict.keys()) # return all keys
print(dict.values()) #return values
print(dict.items()) #return key value pairs
len(dict) #length of dict
pair=list(dict) #list of dictionary
print(pair[0]) #index o key-value
dict.get("name") #another method to get the value , if key is not present this will return no error
dict.update({"city":"goa"}) #updates dict

set={1,5,20,"Janvi",21,"Pune","Pune"} #duplicate values r ignored
len(set) #length
collection={} # empty dictionary
print(type(set))   
set1=set() #empty set
#set functions
set1.add(50000) #add value to set,we can add str
set1.remove(20) #remove value
set1.clear() #empties the set
set1.pop() #removes any random values
set.union(set1) #combines both set values and returns new
set.intersection(set1) #combines common values only

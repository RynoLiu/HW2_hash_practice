word_hash = {}

#Open File
with open("hw2_data.txt","r") as file:
    content = file.readline()
    
    while content:
        search = word_hash.get(content)
        if search == None:
            word_hash[content]=1
        elif search != None:
            word_hash[content]=word_hash[content]+1
        
        content = file.readline() #讀下一行

    print("共",len(word_hash),"種不同單字。")           
    for key,value in word_hash.items():
        print("%s出現%d次" %(key,value),end="\n")
        
   
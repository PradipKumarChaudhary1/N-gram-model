import io
first_possible_word={}
second_possible_word={}
transition={}

def expandDict(dictionary,key,value):  #storing into dictionary current word as a 'value' and previous word as a 'key'
    if key not in dictionary:
        dictionary[key]=[]
    dictionary[key].append(value)

def get_next_probability(word_list):  #finding probability of each word
    word_list_length=len(word_list)
    probability_dict={}
    for item in word_list:
        probability_dict[item]=probability_dict.get(item,0)+1  #calculating frequncy of any word
    for key,value in probability_dict.items():  #calculating probability and store into dictionary according to thire key and probability as a value
        probability_dict[key]=(value+1)/(word_list_length+9484)
    probability_dict=sort_prob(probability_dict)
    return probability_dict

def sort_prob(dictionary):  #sorting of dictionary through values
    keys_list=list(dictionary.keys())
    values_list = list(dictionary.values())
    for i in range(len(values_list)-1):
        for j in range(len(values_list)-i-1):
            if values_list[j]<values_list[j+1]:
                temp=values_list[j]
                values_list[j]=values_list[j+1]
                values_list[j+1]=temp
                temp=keys_list[j]
                keys_list[j]=keys_list[j+1]
                keys_list[j+1]=temp

    sort_dict={}
    for i in range(len(values_list)):
        sort_dict[keys_list[i]]=values_list[i]
    return sort_dict
def trainModel():

    for line in open("test_nextword.txt"):
        tokens=line.rstrip().lower().split()
        tokens_length=len(tokens)
        for i in range(tokens_length):
            token=tokens[i]
            if i==0:   #if word is ffirst word of every sentence
                first_possible_word[token]=first_possible_word.get(token,0)+1
            else:
                prev_token=tokens[i-1]
                if i==1:  #if word is 2nd word of the senetnce
                    expandDict(second_possible_word,prev_token,token)
                if i==tokens_length-1:  #if word is last of sentence
                    expandDict(transition,(prev_token,token),'END')
                else:
                    prev_prev_token=tokens[i-2]
                    expandDict(transition,(prev_prev_token,prev_token),token)

    first_possible_word_total=sum(first_possible_word.values())  #finding total frequency n first_possible word
    for key,value in first_possible_word.items():  #calculating probability of first word in each sentence and store according to that word
        first_possible_word[key]=(value+1)/(first_possible_word_total+9484)

    for prev_word,next_word_list in second_possible_word.items():
        second_possible_word[prev_word]=get_next_probability(next_word_list)

    for word_pair,next_word_list in transition.items():
        transition[word_pair]=get_next_probability(next_word_list)

def next_word(tpl):
    #print(transitions)
    if(type(tpl) == str):   #it is first word of string.. return from second word
        d = second_possible_word.get(tpl)   #tpl match with key and return value, value is already dictionary
        if (d is not None):
            return list(d.keys())[:5]   #since d is already dictionary so return keys
        else:
            #prob = 1 / 9484
            prob = 1 / 5105
            smooth_dict={}

            for key in second_possible_word.keys():
                dd=second_possible_word.get(key)
                for key1,value1 in dd.items():
                    if value1<=prob:
                        smooth_dict[key1]=value1

            return list(smooth_dict.keys())[:5]

    if(type(tpl) == tuple): #incoming words are combination of two words.. find next word now based on transitions
        d = transition.get(tpl)
        if(d == None):
            return ""
        return list(d.keys())[:5]
    return "" #wrong input.. return nothing

if __name__ == '__main__':

    import msvcrt
    trainModel()
    print("Enter some thing:")
    c=' '
    sent = ''
    last_suggestion = []
    while (c != b'\r'):  # stop when user preses enter
        if (c!=b'\t'):     #if previous character was tab, then it write 1st suggestion no wait for inputing
            c=msvcrt.getch()  #inputing charcter by character
        else:
            c=b' '
        if c!=b'\t':
            print(str(c.decode('UTF-8')),end='',flush=True)
        sent=sent+str(c.decode('UTF-8'))
        if c==b' ':
            tkns=sent.split()
            if len(tkns)<2:  #if 2nd word want to write after 1st
                last_suggestion=next_word(tkns[0].lower())
                print(last_suggestion,end=' ',flush=True)
            else:
                last_suggestion=next_word((tkns[-2],tkns[-1]))  #beacaue its a try gram model so we need to last and last to last word
                print(last_suggestion,end=' ',flush=True)
        if c==b'\t' and len(last_suggestion)>0 :
            print(last_suggestion[0],end=" ",flush=True)
            sent=sent+" "+last_suggestion[0]


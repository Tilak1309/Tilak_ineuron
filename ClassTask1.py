import logging

logging.basicConfig(filename="ClassTask1.log", level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
logging.info(("This is my log for the ClassTask1 with timestamp"))
class TypeError1(Exception):
    pass

class PrevClass:

    def ListExtract(self,l):
        '''This method would extract all the lists'''
        logging.info("Invoked the List Extract method for logging")
        try:
            logging.info("Accessing the List")
            for i in l:
                if type(i)==list:
                    logging.info("Following list is found")
                    logging.info(i)
        except Exception as e:
            logging.exception("Please enter a correct iterable object like list,dictionary,tuple,set",e)

    def ItemExtract(self,l1,key):
        '''This method extracts an Item/key from the list'''
        logging.info("Invoked the itemExtract method for logging")
        count = 0
        try:
           for i in l1:
                if type(i) != int:
                    if type(i) == dict:
                        for k, x in i.items():
                            if x == key or k == key:
                                logging.info("Found- '%s' in- %s as- %s ", key, type(i), i)
                                count+=1
                    else:
                        for j in i:
                            if j == key:
                                logging.info("Found- %s -in following- %s ", key, type(i))
                                count += 1

                elif i == key:
                    count += 1
                    logging.info("Found- %s in l ", key)

           if count==0:
               logging.info("Key- '%s' NOT FOUND",key)

        except Exception as e:
            logging.info(e)
    def DictKeyExtract(self,d):
        '''This method is used to extract keys from a dictionary until 2nd level of nested dictionary'''
        logging.info("Entered dictionary key extraction method ")
        try:
            if type(d)!=dict:
                raise TypeError1("Please enter a dictionary for this method to work")
            l=[]
            for i, j in d.items():
                if type(j)==dict:
                    for k,_ in j.items():
                        l.append(k)
                else:
                    l.append(i)
            logging.info("Following is the list of keys in the dictionary- %s", l)
        except Exception as e:
            logging.exception("following exception raised-%s",e)
        #except TypeError as v:
        #    logging.exception(v)

    def DictValueExtract(self,d):
        '''This method is used to extract keys from a dictionary until 2nd level of nested dictionary'''
        logging.info("Entered dictionary Values extraction method ")
        try:
            if type(d)!=dict:
                raise TypeError("Please enter a dictionary for this method to work")
            l=[]
            for i, j in d.items():
                if type(j)==dict:
                    for k,m, in j.items():
                        if type(m) in (int,str):
                            l.append(m)
                        else:
                            l.extend(m)
                else:
                    l.append(j)
            logging.info("Following is the list of values in the dictionary- %s", l)
        except Exception as e:
            logging.exception("following exception raised-%s",e)
        except TypeError as v:
            logging.exception(v)

l=[3,4,5,6,7,234,[23,456,67,8,78,78],[345,56,87,8,98,9],(234,6657,6),6,{"key1":"sudh",234:[23,45,656]}]
#l="adfaf"
obj1=PrevClass()
obj1.ListExtract(l)
obj1.ItemExtract(l,600009000)
d={'a':[1,2,3,],"b":23,6:"abc","c":{1:[234,456],"abc":12,"dfg":123455}}
#d=[{'a':[1,2,3,],"b":23,6:"abc","c":{1:[234,456],"abc":12,"dfg":123455}}]
#d1={'a':[1,2,3,],"b":23,6:"abc","c":{1:[234,456],"abc":12,"dfg":123455}}
obj1.DictKeyExtract(d)
logging.info(d)
obj1.DictValueExtract(d)

class file():
    #keep only 104weeks, 
    def write_file(self, data):
        import json
        with open('datafile', 'w') as f:
            str1 = json.dumps(data)
            f.write(str1)
    
    def read_file(self):
        import os.path
        if (os.path.exists('datafile') != True):
            #create file
            with open('datafile','w+') as f:
                return -1
        else:
            with open('datafile') as f:
                data = f.read()
            return data
             
    def print_table(self, data):
        if(data != None):
            data_s = data.split()
            for str1 in data_s:
                print(str1)
        else:
            print("Nothing")
        
     
     



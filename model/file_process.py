import json
from os.path import exists

class Note:
    def __init__(self):
        self.file_name: str = None

    def create_file(self,file_name:str,path:str=None):
        file_name = file_name +'.json'
        file_exists = exists(file_name)
        if file_exists == False:
            self.file_name = file_name
            with open(file_name, "w") as outfile:
                json.dump({0:{}}, outfile)
                outfile.close()
            return "Dosya oluşturuldu: {0}".format(file_name)
        else:
            self.file_name = file_name
            print("bu dosya daha önce oluşturulmuş")


    def read_file(self):
        with open(self.file_name, 'r') as openfile:
            json_file_value = json.load(openfile)
        print('id   ','Konu   ','Not   ','Etiket   ')
        for i in json_file_value:
            value=json_file_value[i]
            
            print(i,value['subject'],value['note'],value['label'])

        return json_file_value
        


    def add_item(self,readed_value:dict,input_value:object):
        readed_value[int(list(readed_value)[-1])+1] = vars(input_value)
        with open(self.file_name, "w") as outfile:
            json.dump(readed_value, outfile)
            outfile.close()


    def del_note(self,_id:int):
        with open(self.file_name, 'r') as openfile:
            json_file_value = json.load(openfile)
        del  json_file_value[str(_id)]
        with open(self.file_name, "w") as outfile:
            json.dump(json_file_value, outfile)

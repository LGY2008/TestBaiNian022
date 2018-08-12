import yaml,os
class ReadYaml():
    def __init__(self,file_name):
        self.file_name=os.getcwd()+os.sep+"Data"+os.sep+file_name+".yml"

    def read_yaml(self):
        with open(self.file_name,"r",encoding="utf-8") as f:
            return yaml.load(f)

if __name__ == '__main__':
    # # print(read_yaml().keys())
    # # values=read_yaml().values()
    # for value in values:
    #     print(value.get("input_text"))
    print(ReadYaml("search_data").read_yaml())
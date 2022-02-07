
class Hed:
    '''
    Convert headers to python dictionary

    Create a file txt and paste the header in it
    '''
    
    def __init__(self,fileName:str) -> None:
        '''
        fileName-> takes the name of the file
        '''
        self.fileName = fileName
        self.__check_file()
        with open(self.fileName,'r+')as read_file:
            header_dic = Hed.C_header(read_file.readlines())
            read_file.truncate(0)
        with open(self.fileName,'w')as write_file:
            write_file.write(str(header_dic))
            
    @staticmethod        
    def C_header(header_string:str)->str:
        '''
        The method that converts to dic

        header_string-> takes header as a string
        '''
        header= {}
        for i in header_string:
            key , value = i.replace('\n','').split(': ')
            header[key] =  value
        return("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in header.items()) + "}")
    def __check_file(self)->None:
        if self.fileName.endswith('.txt'):
            with open(self.fileName,'r')as r_file:
                read = r_file.readlines()
                print(read)
                if ":" in read[0] or ":" in read[1]:
                    return None
        raise Exception("the file should be .txt or header is wrong ")




        

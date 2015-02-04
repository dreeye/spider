
class Comm:
    
    def replace(text,tuple,replace):
        for i in tuple:
            text = text.replace(i,replace)
        return text

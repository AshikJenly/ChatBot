
class chatHist:
    def __init__(self):
        self.messageHist=[]
        
    def get_list(self):
        print(self.messageHist)
        return self.messageHist

    def make_list(self,val):
        mess=('ChatBot reply from openai and what happens if it was a very long reply',val)
        self.messageHist.append(mess)

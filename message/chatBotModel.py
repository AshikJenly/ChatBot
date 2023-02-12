
import pandas as pd
import openai
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent






class Get_Response:
    def __init__(self) -> None:
        API_KEY="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"
        openai.api_key=API_KEY
        try:
            self.contact = pd.read_csv(BASE_DIR.join('DataFrames/Contact_csv'),index_col=0)
            self.History_df=pd.read_csv(BASE_DIR.join('DataFrames/Historic_Csv_file'),index_col=0)
            self.contact_df_info=['contact','phone_number','resolve','error']
            self.history_df_info =['which','company','invest','worth']
        except:
            print("Error Occured in Loading Data")

    
    def get_dataFrame(self,text):
    
        text = text.lower()
        for c in self.contact_df_info:
            c=c.lower()
            if c in text:
                return  True,self.contact
        for c in self.history_df_info:
            c=c.lower()
            if c in text:
                return True,self.History_df
        return False,None
    def correct_spelling(self,text):
        completion=openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"correct spelling of the text '{text}'",
        )
        
        text = completion.get('choices')[0]['text']
        return text
    def get_prompt(self,text):
        
        available,Frame=self.get_dataFrame(text)
    #     print(Frame.head())
        prompt = f"Answer for this '{text}' in grammatical way"
        if available:
            prompt=f"Answer for this question '{text}' using this dataFrame {Frame}"
        
        return prompt
    def get_resp(self,txt):
        out ="OOps error occured while loading reply :)"
        try:
            text=self.correct_spelling(txt)
            response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.get_prompt(text),
        #     prompt=f"Answer for this question in grammatical way '{text}' using this dataframe {History_df} ",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.1)
            
            out=response["choices"][0]["text"]
        except:
            pass
        return out


class chatHist:
    def __init__(self):
        self.messageHist=[]
        self.get_res=Get_Response()
    def get_list(self):
       
        return self.messageHist

    def make_list(self,val):
        # mess=('ChatBot reply from openai and what happens if it was a very long reply',val)
        mess=(self.get_res(val),val)
        self.messageHist.append(mess)


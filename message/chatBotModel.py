""""""
import pandas as pd
import openai
from pathlib import Path
API_KEY="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"
openai.api_key=API_KEY
BASE_DIR = Path(__file__).resolve().parent.parent

import PyPDF2

from nltk.corpus import stopwords

class Get_Response:
    def __init__(self):
       
            self.pdf_content=self.read_pdf()  #read pdf
            self.extract_main_contents()    #extract main contents from the pdf
            
    def read_pdf(self):
        try:
            pdf_file = open('E:\chatBot\From_Linux\CHATBOT\DataFrames\AshikJenlypdf (2).pdf', 'rb')
            pdf_reader =PyPDF2.PdfReader(pdf_file)
            num_pages=len(pdf_reader.pages)
            text=""
            for i in range(num_pages):
                page = pdf_reader.pages[i]
                text += page.extract_text()
        except:
            print("Error Occured in Loading Data")
           
        # print(text)
        return text
    

    def correct_spelling(self,text):

        completion=openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"correct spelling of the text '{text}'",
        )
        
        text = completion.get('choices')[0]['text']
        return text
    
    def extract_main_contents(self):
        contents_temp=self.pdf_content
        self.main_contents=[c.lower() for  c in contents_temp.split() if c.lower() not in stopwords.words('english')]
        # print(self.main_contents)
        self.greeting_words=['hii','hello','hai','how are you?','thanks','thankyou','okay','good morning','help']
  
  
    def get_prompt(self,text):
        txt_list=text.split(' ')
        # txt_list=[t for t in text.split(' ') if t.lower() not in stopwords.words('english')]
        for word in txt_list:
            if word.lower() in self.main_contents:
                return 'main'
   
        for word in txt_list:
            if word.lower() in self.greeting_words:
                    return 'greet'
        return None
       
        
        
    def get_resp(self,txt):
        
        prompt_temp=""
        which_promt=self.get_prompt(txt)
        if which_promt!=None:
            if which_promt=='main':
                prompt_temp=f"reply for this question '{txt}' from this file '{self.pdf_content}' ",
            elif which_promt=='greet':
                prompt_temp=f"reply for this question '{txt}'"
            
                
            out ="OOps error occured while loading reply :)"
            try:
                # text=self.correct_spelling(txt)
               
                response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt_temp,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.1)
                
                out=response["choices"][0]["text"]
            except:
                pass
            return out
        else:
            return "I’m sorry. I couldn’t quite understand that.\nCan you try asking me another way?"


class chatHist:
    def __init__(self):
        self.messageHist=[]
        self.get_res=Get_Response()
    def get_list(self):
       
        return self.messageHist

    def make_list(self,val):
        # mess=('ChatBot reply from openai and what happens if it was a very long reply',val)
        mess=(self.get_res.get_resp(val),val)
        self.messageHist.append(mess)


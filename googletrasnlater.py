from tkinter import *
from tkinter import ttk , messagebox
# from googletrasnlater import Translator
from googletrans import LANGUAGES
from googletrans import Translator
#+++++++++++++++++++++++++++++ star  translator  functionaliy ++++++++++++++++++++++

def change(text= 'type', src = 'English', dest = 'Hindi'):
    try:
        text1 = text
        sec1 = src
        dest1 = dest
        trans = Translator()
        trans1 = trans.translate(text,src = sec1, dest = dest1)
        return trans1.text
    except:
        messagebox.showwarning("Warning ", 'Please  input a sentence ')


def data(event = None ):
    
    s = comb_sor.get()
    d = comb_dest.get()
    
    msg = sor_txt.get(1.0, END)
    print(s,d,msg , f' the type of  soure is {type(s)}, dect {type(d)}, and msg {type(msg)}')
    textget = change(text= msg,src=s,dest=d)
    dec_txt.delete(1.0,END)
    dec_txt.insert(END,textget)

#+++++++++++++++++++++++++++++ End translator  functionaliy ++++++++++++++++++++++


root = Tk()
root.title(" Python Translator")
root.geometry('500x1000')

root.config(bg= 'Red')
### intro label
lab_txt = Label(root , text= "Translator", font= ("Time New Roman", 40, "bold"))
lab_txt.place( x = 100, y = 40, height= 50, width=300)

frame = Frame(root).pack(side= BOTTOM)

lab_txt = Label(root , text= "Source Text", font= ("Time New Roman", 20, "bold"),fg='black',bg='red')
lab_txt.place( x = 100, y = 100, height= 20, width=300)

sor_txt = Text(frame, font=('Time New Roman',20,'bold'),wrap=WORD)
sor_txt.place( x = 10, y = 130, height= 150, width=480)

list_text = list(LANGUAGES.values())
## combobox 
comb_sor = ttk.Combobox(frame, value = list_text, state= 'readonly')
comb_sor.place(x=10,y=300, height=40,width=100)
comb_sor.set('English')

button_change =Button(frame,text='Translate',relief= RAISED,command=data)
button_change.place(x=170,y=300, height=40,width=150)

comb_dest = ttk.Combobox(frame, value = list_text,state= 'readonly')
comb_dest.place(x=330,y=300, height=40,width=150)
comb_dest.set('English')

lab_txt = Label(root , text= "Dext Text", font= ("Time New Roman", 20, "bold"),fg='black',bg='red')
lab_txt.place( x = 100, y = 360, height= 20, width=300)


dec_txt = Text(frame, font=('Time New Roman',20,'bold'),wrap=WORD)
dec_txt.place( x = 10, y = 400, height= 150, width=480)



root.mainloop()
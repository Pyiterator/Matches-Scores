import tkinter as tk
from PIL import ImageTk,Image
from bs4 import BeautifulSoup                                                                            #webscrapping
import urllib.request                                                                                    #for fetching url
score_page='https://static.cricinfo.com/rss/livescores.xml'                                              #url for scrap the score
page=urllib.request.urlopen(score_page)                                                                  #to open that url
soup=BeautifulSoup(page,'html.parser')                                                                   #intially it will be on html form to convert it to readible format ,we are pasing it
result=soup.find_all('description')
ls=[]                                                                                                     #empt list for live score
for match in result:
    ls.append(match.get_text())


def score():
    T.insert(tk.END, ls)


def clear():
    T.delete(1.0, tk.END)

#GUI work start
root=tk.Toplevel()
root.geometry('1200x675')

img=ImageTk.PhotoImage(Image.open("matches.jpg"))
panel=tk.Label(root,image=img)
panel.place(x=0,y=0)

T=tk.Text(root)                 #text area creation
T.place(x=30,y=250,height=250,width=300)

l=tk.Label(root,text="Live Score",fg="white",bg="black")
l.place(x=30,y=400,height=100,width=300)


b1=tk.Button(root,text="Score",bg="black",fg="red",command=score)
b1.place(x=800,y=200,height=100,width=250)

b2=tk.Button(root,text="Clear",bg="black",fg="red",command=clear)
b2.place(x=800,y=400,height=100,width=100)

root.mainloop()


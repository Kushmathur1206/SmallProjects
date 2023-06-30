from tkinter import *
window=Tk()
window.title('CYBER MAPPERS')
label_Heading=Label(window,text='CYBER MAPPERS')
label_Heading.config(font=('Helvetica bold',40))
label_Heading.grid(row=0,column=1)

#Enter Name 
label_Name=Label(window,text='Your Name').grid(row=1,column=0)
Name = Entry(window,width=50)
Name.grid(row=1,column=1)


#Enter URL
label_URL=Label(window,text='Product URL').grid(row=2,column=0)
URL = Entry(window,width=50)
URL.grid(row=2,column=1)


#Enter Span_id
label_span_id=Label(window,text="Product's Span Id").grid(row=3,column=0)
Span_id = Entry(window,width=50)
Span_id.grid(row=3,column=1)
Span_id.insert(0,'B_NuCI')


#Enter Div id
label_span_id=Label(window,text="Product's Div Id").grid(row=4,column=0)
Div_id = Entry(window,width=50)
Div_id.grid(row=4,column=1)
Div_id.insert(0,'_30jeq3 _16Jk6d')

#Enter Desired price
label_Desired_price=Label(window,text='Your Desired Price').grid(row=5,column=0)
DP = Entry(window,width=50)
DP.grid(row=5,column=1)

#Enter Email ID
label_Email_id=Label(window,text='Your Email Address').grid(row=6,column=0)
Email = Entry(window,width=50)
Email.grid(row=6,column=1)

def Submit():
   
   import requests
   from bs4 import BeautifulSoup
   import smtplib


   def checkprice():
      headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
      page=requests.get(URL.get(), headers=headers)
      soup=BeautifulSoup(page.content, 'html.parser')
      global title
      title=soup.find('span', class_=Span_id.get())
      price=soup.find('div', class_=Div_id.get())
             
      y=''
      for i in price.text:
         if i.isnumeric():
            y+=i
      convertedprice = int(y)
             
             
      if convertedprice<int(DP.get()):
         send_mail()
         label_1=Label(window,text='Your Product:').grid(row=10,column=0)
         lab1= Entry(window,width=50)
         lab1.grid(row=10,column=1)
         lab1.insert(0,title.text)
         label_2=Label(window,text='Current Price:').grid(row=11,column=0)
         lab2=Entry(window,width=50)
         lab2.grid(row=11,column=1)
         lab2.insert(0,price.text)        
      

   def send_mail():
      server = smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.login('worklakshay21@gmail.com','wyzybtpgcpyviddr')

      subject='Price Reduced! Hurry.'
      body='Your product {} is selling at a price below Rs {}. Go and Buy nowww at the link below: \n\n {}'.format(title.text,DP.get(),URL.get())
      msg = f"Subject: {subject}\n\n{body}".encode('utf-8')
      server.sendmail('kushwork1206@gmail.com',Email.get(),msg)

      Submit_label=Label(window,text='Thank you '+ Name.get() +', EMAIL HAS BEEN SENT!')
      Submit_label.grid(row=8,column=1)
      server.quit()   
   checkprice()

button= Button(window,text='Submit',padx=40,command=Submit)
button.grid(row=7,column=1)

window.mainloop()
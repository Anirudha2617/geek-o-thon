import tkinter 
import time
from  tkinter import *
import random
from PIL import Image,ImageTk
from tkinter import filedialog,messagebox
import pickle
import os

value=""               #calculator value
id_entry = 0
pwd_entry = 0

user = None

def restaurants():

    #functions
    def menu ():
        root3=Toplevel()
        root3.title("Menu")
        root3.config(bg="black")
        root3.geometry("2000x2000")
    
        Food = {"Burger":'100',"Pizza":'120','Tacos':'115','Fries':'70','Momos':'90','sandwich':'75','OnionRings':"90",'Noodles':'100','Popcorn':"60"}
    
        m_frame=Frame(root3,bd=10,relief=RIDGE)
        m_frame.grid(row=0,column=0)
        t=Label(m_frame,text='FOOD',font=("candles",20,"bold"),bd=5,width=9)
        t.grid(row=0,column=0,sticky=W)
        for i,j in enumerate(Food):
            burger=Label(m_frame,text=j,font=("candles",20,"bold"),bd=5,width=9)
            burger.grid(row=i+1,column=0,sticky=W)
    
        label_cost=Label(m_frame,text="COST ",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=0,column=1)
        for i,j in enumerate(Food):
            label_cost=Label(m_frame,text=Food[j]+" RS",font=("candles",20,"bold"),bd=5,width=9)
            label_cost.grid(row=i+1,column=1)
    
        
        d_frame=Frame(root3,bd=10,relief=RIDGE)
        d_frame.grid(row=0,column=1)
    
        e_frame=Frame(root3,bd=10,relief=RIDGE)
        e_frame.grid(row=0,column=2)
    
        t=Label(d_frame,text='DRINKS',font=("candles",20,"bold"),bd=5,width=13)
        t.grid(row=0,column=0,sticky=W)
    
        coffee=Label(d_frame,text='COFFEE',font=("candles",20,"bold"),bd=5,width=9)
        coffee.grid(row=1,column=0,sticky=W)
        
        coke=Label(d_frame,text='COKE',font=("candles",20,"bold"),bd=5,width=9)
        coke.grid(row=2,column=0,sticky=W)
    
        thumpsup=Label(d_frame,text='THUMPS UP',font=("candles",20,"bold"),bd=5,width=9)
        thumpsup.grid(row=3,column=0,sticky=W)
        sprite=Label(d_frame,text='SPRITE',font=("candles",20,"bold"),bd=5,width=9)
        sprite.grid(row=4,column=0,sticky=W)
        mojito=Label(d_frame,text='MOJITO',font=("candles",20,"bold"),bd=5,width=9)
        mojito.grid(row=5,column=0,sticky=W)
        icetea=Label(d_frame,text='ICE TEA',font=("candles",20,"bold"),bd=5,width=9)
        icetea.grid(row=6,column=0,sticky=W)
        coldcoffee=Label(d_frame,text='COLD COFFEE',font=("candles",20,"bold"),bd=5,width=12)
        coldcoffee.grid(row=7,column=0,sticky=W)
        milk=Label(d_frame,text='MILKSHAke',font=("candles",20,"bold"),bd=5,width=10)
        milk.grid(row=8,column=0,sticky=W)
        fruitpunch=Label(d_frame,text='FRUIT PUNCH',font=("candles",20,"bold"),bd=5,width=12)
        fruitpunch.grid(row=9,column=0)
    
        label_cost=Label(d_frame,text="COST ",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=0,column=1)
        label_cost=Label(d_frame,text="30 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=1,column=1)
        label_cost=Label(d_frame,text="30 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=2,column=1)
        label_cost=Label(d_frame,text="30 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=3,column=1)
        label_cost=Label(d_frame,text="30 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=4,column=1)
        label_cost=Label(d_frame,text="100 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=5,column=1)
        label_cost=Label(d_frame,text="75 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=6,column=1)
        label_cost=Label(d_frame,text="110 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=7,column=1)
        label_cost=Label(d_frame,text="120 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=8,column=1)
        label_cost=Label(d_frame,text="90 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=9,column=1)
    
        ICE=Label(e_frame,text='ICECREAMS',font=("candles",20,"bold"),bd=5,width=12)
        ICE.grid(row=0,column=0,sticky=W)
        vanilla=Label(e_frame,text='Vanilla',font=("candles",20,"bold"),bd=5,width=12)
        vanilla.grid(row=1,column=0,sticky=W)
        strawberry=Label(e_frame,text='Strawbery',font=("candles",20,"bold"),bd=5,width=12)
        strawberry.grid(row=2,column=0,sticky=W)
        chocolate=Label(e_frame,text='Chocolate',font=("candles",20,"bold"),bd=5,width=12)
        chocolate.grid(row=3,column=0,sticky=W)
        blackcurrent=Label(e_frame,text='Blackcurrent',font=("candles",20,"bold"),bd=5,width=12)
        blackcurrent.grid(row=4,column=0,sticky=W)
        butterscotch=Label(e_frame,text='BUtterscotch',font=("candles",20,"bold"),bd=5,width=12)
        butterscotch.grid(row=5,column=0,sticky=W)
        kesarpista=Label(e_frame,text='Kesarpista',font=("candles",20,"bold"),bd=5,width=12)
        kesarpista.grid(row=6,column=0,sticky=W)
        almondchoco=Label(e_frame,text='almondchoco',font=("candles",20,"bold"),bd=5,width=12)
        almondchoco.grid(row=7,column=0,sticky=W)
        darkchocolate=Label(e_frame,text='Darkchocolate',font=("candles",20,"bold"),bd=5,width=12)
        darkchocolate.grid(row=8,column=0,sticky=W)
        almondcarmel=Label(e_frame,text='Almondcarmel',font=("candles",20,"bold"),bd=5,width=12)
        almondcarmel.grid(row=9,column=0,sticky=W)
        
        label_cost=Label(e_frame,text="COST ",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=0,column=1)
        label_cost=Label(e_frame,text="50 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=1,column=1)
        label_cost=Label(e_frame,text="60 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=2,column=1)
        label_cost=Label(e_frame,text="70 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=3,column=1)
        label_cost=Label(e_frame,text="80 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=4,column=1)
        label_cost=Label(e_frame,text="80 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=5,column=1)
        label_cost=Label(e_frame,text="90 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=6,column=1)
        label_cost=Label(e_frame,text="90 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=7,column=1)
        label_cost=Label(e_frame,text="90 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=8,column=1)
        label_cost=Label(e_frame,text="100 RS",font=("candles",20,"bold"),bd=5,width=9)
        label_cost.grid(row=9,column=1)
    
        f_frame=Frame(root3,bd=10,relief=RIDGE)
        f_frame.grid(row=1,column=1)
     
    def reset():
        text_Receipt.delete(1.0,END)
        burger_e.set("0")
        pizza_e.set("0")
        tacos_e.set("0")
        fries_e.set("0")
        momos_e.set("0")
        sandwich_e.set("0")
        onion_e.set("0")
        noodle_e.set("0")
        popcorn_e.set("0")
        vanilla_e.set("0")
        strawberry_e.set("0")
        chocolate_e.set("0")
        blackcurrent_e.set("0")
        butterscotch_e.set("0")
        kesarapista_e.set("0")
        almondchoco_e.set("0")
        darkchocolate_e.set("0")
        almondcarmel_e.set("0")
        coffee_e.set("0")
        coke_e.set("0")
        thumsup_e.set("0")
        sprite_e.set("0")
        mojito_e.set("0")
        icetea_e.set("0")
        coldcoffee_e.set("0")
        milkshake_e.set("0")
        fruitpunch_e.set("0")
        
        text_burger.config(state=DISABLED) 
        text_pizza.config(state=DISABLED) 
        text_fries.config(state=DISABLED) 
        text_momos.config(state=DISABLED) 
        text_tacos.config(state=DISABLED) 
        text_noodle.config(state=DISABLED) 
        text_popcorn.config(state=DISABLED) 
        text_onion.config(state=DISABLED) 
        text_sandwich.config(state=DISABLED) 
        text_coffee.config(state=DISABLED) 
        text_thumsup.config(state=DISABLED) 
        text_coke.config(state=DISABLED) 
        text_sprite.config(state=DISABLED) 
        text_mojito.config(state=DISABLED) 
        text_icetea.config(state=DISABLED) 
        text_coldcoffee.config(state=DISABLED) 
        text_milkshake.config(state=DISABLED) 
        text_fruitpunch.config(state=DISABLED) 
        text_vanilla.config(state=DISABLED) 
        text_strawberry.config(state=DISABLED) 
        text_chocolate.config(state=DISABLED) 
        text_blackcurrent.config(state=DISABLED) 
        text_butterscotch.config(state=DISABLED) 
        text_kesarpista.config(state=DISABLED) 
        text_darkchocolate.config(state=DISABLED) 
        text_almondchoco.config(state=DISABLED) 
        text_almondcarmel.config(state=DISABLED) 
        
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)
        var23.set(0)
        var24.set(0)
        var25.set(0)
        var26.set(0)
        var27.set(0)
        
        
        costoficevar.set("")
        costoffoodvar.set("")
        costofdrinkvar.set("")
        subtotalvar.set("")
        totalcostvar.set("")
        servicetaxvar.set("")
     
    def send():
        '''def send_msg():
            message=textarea.get(1.0,END)
            phnumber=mobile_no.get()
            hema='l04yfuUk5DgeGZYo2cpCQ3N6m8wFAbnq9jV7IWPXEasBMdtiK1IvpdGNQuLV8Tnflmqz01YR9ke54owK'
            Url="https://www.fast2sms.com/dev/bulk"
            parameters={
                   "authorization":hema,
                   "message":phnumber,
                   "sender-id":"FSTSMS",
                   "route":"p",
                   "language":"english" }
            response=requests.get(hema,params=parameters)
            dic=response.json()       
            result=dic.get("return")
            if result==True:
                messagebox.showinfo("sent scuscessfully","sent sucessfully")
            else:
                messagebox.showerror("error","Something went Wrong")'''
        
        
        
        
        
        
        
        root2=Toplevel()
        root2.title("Send Bill")
        root2.config(bg="red")
        root2.geometry("485x620+50+50")
        mobilenum=Label(root2,text="Mobile Number",font=("arial",18,"underline","bold"),bg="yellow")
        mobilenum.pack(pady=5)
        
        mobile_no=Entry(root2,font=("helvetica",22,"bold"),bd=10,width=24,relief=RIDGE)
        mobile_no.pack(pady=5)
        
        bill_details=Label(root2,text="Bill Details",font=("arial",18,"underline","bold"),bg="yellow")
        bill_details.pack(pady=5)
        
        textarea=Text(root2,font=("arial",12,"bold"),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        
        textarea.insert(END,f'Receipt Ref:\t\t'+billnum+"\t\t"+date+"\n")
        textarea.insert(END,"***************************************************************\n")
        if costoffoodvar.get()!='0Rs':
            textarea.insert(END,f'Cost of Food\t\t\t{priceofFood}Rs\n')
    
        if costofdrinkvar.get()!="0Rs": 
                    textarea.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
        if costoficevar.get()!="0Rs":
                    textarea.insert(END,f'Cost Of Icecreams\t\t\t{priceofIcecream}Rs\n')
        if subtotalvar.get()!="0Rs":
                    textarea.insert(END,f'Sub Total \t\t\t{subtotalofitems}Rs\n')
        
        textarea.insert(END,f'ServiceTax\t\t\t{50}Rs\n')
        
        if totalcostvar.get()!="0Rs":
                     textarea.insert(END,f'Total Cost\t\t\t{total_cost}Rs\n')
        textarea.insert(END,"***************************************************************\n")
    
    
    
        send_button=Button(root2,font=("arial",19,"bold"),bg="yellow",bd=7,relief=GROOVE,text="Send")
        send_button.pack(pady=5)
        
        
        root2.mainloop()
           
    def save():
        
        with open("receipt\\"+user+'.txt','a+') as f:
            bill_data=text_Receipt.get(1.0,END)
            f.writelines(bill_data)

        '''url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",title=user)
        bill_data=text_Receipt.get(1.0,END)
        url.write(bill_data)
        url.close()'''
        messagebox.showinfo("Information","Your Bill Is Saved Successfully")
   
    def receipt():
        global billnum
        global date
        text_Receipt.delete(1.0,END)#for clearing
        x=random.randint(100,10000)
        billnum="BILL"+str(x)
        date=time.strftime('%d/%m/%Y')
        text_Receipt.insert(END,"Receipt Ref :\t\t"+billnum+"\t\t"+date+"\n")
        text_Receipt.insert(END,"***************************************************************\n")
        text_Receipt.insert(END,"Items\t\t     Cost Of Items(Rs)\n")
        text_Receipt.insert(END,"***************************************************************\n")
        if burger_e.get()!='0':
            text_Receipt.insert(END,f'Burger\t\t\t{int(burger_e.get())*100}\n\n')
        
        if pizza_e.get()!='0':
            text_Receipt.insert(END,f'Pizza\t\t\t{int(pizza_e.get())*120}\n\n')
    
        if tacos_e.get()!='0':
            text_Receipt.insert(END,f'tacos\t\t\t{int(tacos_e.get())*115}\n\n')
        
        if fries_e.get()!='0':
            text_Receipt.insert(END,f'Fries\t\t\t{int(fries_e.get())*70}\n\n')
    
        if momos_e.get()!='0':
            text_Receipt.insert(END,f'Momos\t\t\t{int(momos_e.get())*90}\n\n')
    
        if sandwich_e.get()!='0':
            text_Receipt.insert(END,f'Sandwich\t\t\t{int(sandwich_e.get())*75}\n\n')
        
        if onion_e.get()!='0':
            text_Receipt.insert(END,f'Onion rings\t\t\t{int(onion_e.get())*90}\n\n')
    
        if noodle_e.get()!='0':
            text_Receipt.insert(END,f'Noodle\t\t\t{int(noodle_e.get())*100}\n\n')
    
        if popcorn_e.get()!='0':
            text_Receipt.insert(END,f'popcorn\t\t\t{int(popcorn_e.get())*60}\n\n')
    
        if coffee_e.get()!='0':
            text_Receipt.insert(END,f'Coffee\t\t\t{int(coffee_e.get())*30}\n\n')
    
        if coke_e.get()!='0':
            text_Receipt.insert(END,f'coke\t\t\t{int(coke_e.get())*30}\n\n')
    
        if thumsup_e.get()!='0':
            text_Receipt.insert(END,f'Thumsup\t\t\t{int(thumsup_e.get())*30}\n\n')
    
        if sprite_e.get()!='0':
            text_Receipt.insert(END,f'sprite\t\t\t{int(sprite_e.get())*30}\n\n')
    
        if mojito_e.get()!='0':
            text_Receipt.insert(END,f'mojito\t\t\t{int(mojito_e.get())*100}\n\n')
    
        if icetea_e.get()!='0':
            text_Receipt.insert(END,f'IceTea\t\t\t{int(icetea_e.get())*75}\n\n')                   
    
        if coldcoffee_e.get()!='0':
            text_Receipt.insert(END,f'Cold Coffee\t\t\t{int(coldcoffee_e.get())*110}\n\n')
        
        if milkshake_e.get()!='0':
            text_Receipt.insert(END,f'milkshake\t\t\t{int(milkshake_e.get())*120}\n\n')
    
        if fruitpunch_e.get()!='0':
            text_Receipt.insert(END,f'Fruit Punch\t\t\t{int(fruitpunch_e.get())*90}\n\n') 
    
        if vanilla_e.get()!='0':
            text_Receipt.insert(END,f'Vanilla\t\t\t{int(vanilla_e.get())*50}\n\n')
    
        if strawberry_e.get()!='0':
            text_Receipt.insert(END,f'Strawberry\t\t\t{int(strawberry_e.get())*60}\n\n')
    
        if chocolate_e.get()!='0':
            text_Receipt.insert(END,f'Chocolate\t\t\t{int(chocolate_e.get())*70}\n\n')
    
        if blackcurrent_e.get()!='0':
            text_Receipt.insert(END,f'Blackcurrent \t\t\t{int(blackcurrent_e.get())*80}\n\n')
    
        if butterscotch_e.get()!='0':
            text_Receipt.insert(END,f'Butterscotch\t\t\t{int(butterscotch_e.get())*80}\n\n')
    
        if kesarapista_e.get()!='0':
            text_Receipt.insert(END,f'Kesarapista\t\t\t{int(kesarapista_e.get())*90}\n\n')                          
        
        if almondchoco_e.get()!='0':
            text_Receipt.insert(END,f'AlmondChoco\t\t\t{int(almondchoco_e.get())*90}\n\n')
    
        if darkchocolate_e.get()!='0':
            text_Receipt.insert(END,f'DarkChocolate\t\t\t{int(darkchocolate_e.get())*90}\n\n')
    
        
        if almondcarmel_e.get()!='0':
            text_Receipt.insert(END,f'AlomndCarmel\t\t\t{int(almondcarmel_e.get())*100}\n\n')
        
        text_Receipt.insert(END,"***************************************************************\n")
        if costoffoodvar.get()!='0Rs':
            text_Receipt.insert(END,f'Cost of Food\t\t\t{priceofFood}Rs\n\n')
    
        if costofdrinkvar.get()!="0Rs": 
                    text_Receipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costoficevar.get()!="0Rs":
                    text_Receipt.insert(END,f'Cost Of Icecreams\t\t\t{priceofIcecream}Rs\n\n')
        if subtotalvar.get()!="0Rs":
                    text_Receipt.insert(END,f'Sub Total \t\t\t{subtotalofitems}Rs\n\n')
        
        text_Receipt.insert(END,f'ServiceTax\t\t\t{50}Rs\n\n')
        
        if totalcostvar.get()!="0Rs":
                     text_Receipt.insert(END,f'Total Cost\t\t\t{total_cost}Rs\n\n')
        text_Receipt.insert(END,"***************************************************************\n")
        messagebox.showinfo("Information","DONE")
    
    def  totalcost():
        global priceofDrinks
        global priceofFood
        global priceofIcecream
        global subtotalofitems
        global total_cost
        if var1.get() !=0 or var2.get() !=0 or var3.get() !=0 or var4.get() !=0 or var5.get() !=0 or var6.get() !=0 or var7.get()!=0 or var1.get() !=0 or var8.get() !=0 or var9.get() !=0 or var10.get() !=0 or var11.get() !=0 or\
        var12.get() !=0 or var13.get() !=0 or var14.get() !=0 or var15.get() !=0 or var16.get() !=0 or var17.get() !=0 or var18.get() !=0 or var19.get() !=0 or var20.get() !=0 or var21.get() !=0 or var22.get() !=0 or var24.get() !=0 or\
        var25.get() !=0 or var26.get() !=0 or var27.get() !=0:
    
                        item1=int(burger_e.get())  #100
                        item2=int(pizza_e.get())   #120var1
                        item3=int(tacos_e.get())  #115
                        item4=int(fries_e.get())  #70
                        item5=int(momos_e.get())  #90
                        item6=int(sandwich_e.get()) #75
                        item7=int(onion_e.get())  #90
                        item8=int(noodle_e.get()) #100
                        item9=int(popcorn_e.get()) #60
        
        
                        item10=int(coffee_e.get())  #30
                        item11=int(coke_e.get())   #30
                        item12=int(thumsup_e.get()) #30
                        item13=int(sprite_e.get())  #30
                        item14=int(mojito_e.get())  #100
                        item15=int(icetea_e.get())  #75
                        item16=int(coldcoffee_e.get()) #110
                        item17=int(milkshake_e.get()) #120
                        item18=int(fruitpunch_e.get()) #90
        
        
                        item19=int(vanilla_e.get()) #50
                        item20=int(strawberry_e.get()) #60
                        item21=int(chocolate_e.get()) #70
                        item22=int(blackcurrent_e.get()) #80
                        item23=int(butterscotch_e.get()) #80
                        item24=int(kesarapista_e.get()) #90
                        item25=int(almondchoco_e.get()) #90
                        item26=int(darkchocolate_e.get()) #90
                        item27=int(almondcarmel_e.get()) #100
    
                        priceofFood=(item1*100)+(item2*120)+(item3*115)+(item4*70)+(item5*90)+(item6*75)+(item7*90)+(item8*100)+(item9*60)
        
                        priceofDrinks=(item10*30)+(item11*30)+(item12*30)+(item13*30)+(item14*100)+(item15*75)+(item16*110)+(item17*120)+(item18*90)
    
                        priceofIcecream=(item19*50)+(item20*60)+(item21*70)+(item22*80)+(item23*80)+(item24*90)+(item25*90)+(item26*90)+(item27*100)
        
                        costoffoodvar.set(str(priceofFood)+"Rs")
                        costofdrinkvar.set(str(priceofDrinks)+"Rs")
                        costoficevar.set(str(priceofIcecream)+"Rs")
    
                        subtotalofitems=priceofFood+priceofDrinks+priceofIcecream
                        subtotalvar.set(str(subtotalofitems)+ "Rs")
        
                        servicetaxvar.set("50 Rs")
                        
                        total_cost=subtotalofitems+50
                        totalcostvar.set(str(total_cost)+" Rs")
        else:
            messagebox.showinfo("Error","No Item is selected")
      
    def burger():
        if var1.get()==1:
            text_burger.config(state=NORMAL)#change state back to normal
            text_burger.delete(0,END) # deletee 0 value
            text_burger.focus() #cursor to blink
        else:
            text_burger.config(state=DISABLED)    
            burger_e.set("0")
    
    def pizza():
        if var2.get()==1:
            text_pizza.config(state=NORMAL)#change state back to normal
            text_pizza.delete(0,END) # deletee 0 value
            text_pizza.focus() #cursor to blink
        else:
            text_pizza.config(state=DISABLED)    
            pizza_e.set("0")
    
    def tacos():
        if var3.get()==1:
            text_tacos.config(state=NORMAL)#change state back to normal
            text_tacos.delete(0,END) # deletee 0 value
            text_tacos.focus() #cursor to blink
        else:
            text_tacos.config(state=DISABLED)    
            tacos_e.set("0")
    
    def fries():
        if var4.get()==1:
            text_fries.config(state=NORMAL)#change state back to normal
            text_fries.delete(0,END) # deletee 0 value
            text_fries.focus() #cursor to blink
        else:
            text_fries.config(state=DISABLED)    
            fries_e.set("0")
    
    def momos():
        if var5.get()==1:
            text_momos.config(state=NORMAL)#change state back to normal
            text_momos.delete(0,END) # deletee 0 value
            text_momos.focus() #cursor to blink
        else:
            text_momos.config(state=DISABLED)    
            momos_e.set("0")
    
    def sandwich():
        if var6.get()==1:
            text_sandwich.config(state=NORMAL)#change state back to normal
            text_sandwich.delete(0,END) # deletee 0 value
            text_sandwich.focus() #cursor to blink
        else:
            text_sandwich.config(state=DISABLED)    
            sandwich_e.set("0")
    
    def onion():
        if var7.get()==1:
            text_onion.config(state=NORMAL)#change state back to normal
            text_onion.delete(0,END) # deletee 0 value
            text_onion.focus() #cursor to blink
        else:
            text_onion.config(state=DISABLED)    
            onion_e.set("0")
    
    def noodle():
        if var8.get()==1:
            text_noodle.config(state=NORMAL)#change state back to normal
            text_noodle.delete(0,END) # deletee 0 value
            text_noodle.focus() #cursor to blink
        else:
            text_noodle.config(state=DISABLED)    
            noodle_e.set("0")
    
    def popcorn():
        if var9.get()==1:
            text_popcorn.config(state=NORMAL)#change state back to normal
            text_popcorn.delete(0,END) # deletee 0 value
            text_popcorn.focus() #cursor to blink
        else:
            text_popcorn.config(state=DISABLED)    
            popcorn_e.set("0")
    
    
    def coffee():
        if var10.get()==1:
            text_coffee.config(state=NORMAL)#change state back to normal
            text_coffee.delete(0,END) # deletee 0 value
            text_coffee.focus() #cursor to blink
        else:
            text_coffee.config(state=DISABLED)    
            coffee_e.set("0")
    
    
    def coke():
        if var11.get()==1:
            text_coke.config(state=NORMAL)#change state back to normal
            text_coke.delete(0,END) # deletee 0 value
            text_coke.focus() #cursor to blink
        else:
            text_coke.config(state=DISABLED)    
            coke_e.set("0")
    
    
    def thumpsup():
        if var12.get()==1:
            text_thumsup.config(state=NORMAL)#change state back to normal
            text_thumsup.delete(0,END) # deletee 0 value
            text_thumsup.focus() #cursor to blink
        else:
            text_thumsup.config(state=DISABLED)    
            thumsup_e.set("0")
    
    
    def sprite():
        if var13.get()==1:
            text_sprite.config(state=NORMAL)#change state back to normal
            text_sprite.delete(0,END) # deletee 0 value
            text_sprite.focus() #cursor to blink
        else:
            text_sprite.config(state=DISABLED)    
            sprite_e.set("0")
    
    
    def mojito():
        if var14.get()==1:
            text_mojito.config(state=NORMAL)#change state back to normal
            text_mojito.delete(0,END) # deletee 0 value
            text_mojito.focus() #cursor to blink
        else:
            text_mojito.config(state=DISABLED)    
            mojito_e.set("0")
    
    def icetea():
        if var15.get()==1:
            text_icetea.config(state=NORMAL)#change state back to normal
            text_icetea.delete(0,END) # deletee 0 value
            text_icetea.focus() #cursor to blink
        else:
            text_icetea.config(state=DISABLED)    
            icetea_e.set("0")
    
    def coldcoffee():
        if var16.get()==1:
            text_coldcoffee.config(state=NORMAL)#change state back to normal
            text_coldcoffee.delete(0,END) # deletee 0 value
            text_coldcoffee.focus() #cursor to blink
        else:
            text_coldcoffee.config(state=DISABLED)    
            coldcoffee_e.set("0")
    
    def milkshake():
        if var17.get()==1:
            text_milkshake.config(state=NORMAL)#change state back to normal
            text_milkshake.delete(0,END) # deletee 0 value
            text_milkshake.focus() #cursor to blink
        else:
            text_milkshake.config(state=DISABLED)    
            milkshake_e.set("0")
    
    def fruitpunch():
        if var18.get()==1:
            text_fruitpunch.config(state=NORMAL)#change state back to normal
            text_fruitpunch.delete(0,END) # deletee 0 value
            text_fruitpunch.focus() #cursor to blink
        else:
            text_fruitpunch.config(state=DISABLED)    
            fruitpunch_e.set("0")
    
    
    def vanilla():
        if var19.get()==1:
            text_vanilla.config(state=NORMAL)#change state back to normal
            text_vanilla.delete(0,END) # deletee 0 value
            text_vanilla.focus() #cursor to blink
        else:
            text_vanilla.config(state=DISABLED)    
            vanilla_e.set("0")
    
    def strawberry():
        if var20.get()==1:
            text_strawberry.config(state=NORMAL)#change state back to normal
            text_strawberry.delete(0,END) # deletee 0 value
            text_strawberry.focus() #cursor to blink
        else:
            text_strawberry.config(state=DISABLED)    
            strawberry_e.set("0")
    
    def chocolate():
        if var21.get()==1:
            text_chocolate.config(state=NORMAL)#change state back to normal
            text_chocolate.delete(0,END) # deletee 0 value
            text_chocolate.focus() #cursor to blink
        else:
            text_chocolate.config(state=DISABLED)    
            chocolate_e.set("0")
    
    def blackcurrent():
        if var22.get()==1:
            text_blackcurrent.config(state=NORMAL)#change state back to normal
            text_blackcurrent.delete(0,END) # deletee 0 value
            text_blackcurrent.focus() #cursor to blink
        else:
            text_blackcurrent.config(state=DISABLED)    
            blackcurrent_e.set("0")
    
    def butterscotch():
        if var23.get()==1:
            text_butterscotch.config(state=NORMAL)#change state back to normal
            text_butterscotch.delete(0,END) # deletee 0 value
            text_butterscotch.focus() #cursor to blink
        else:
            text_butterscotch.config(state=DISABLED)    
            butterscotch_e.set("0")
    
    
    def kesarpista():
        if var24.get()==1:
            text_kesarpista.config(state=NORMAL)#change state back to normal
            text_kesarpista.delete(0,END) # deletee 0 value
            text_kesarpista.focus() #cursor to blink
        else:
            text_kesarpista.config(state=DISABLED)    
            kesarapista_e.set("0")
    
    def almondchoco():
        if var25.get()==1:
            text_almondchoco.config(state=NORMAL)#change state back to normal
            text_almondchoco.delete(0,END) # deletee 0 value
            text_almondchoco.focus() #cursor to blink
        else:
            text_almondchoco.config(state=DISABLED)    
            almondchoco_e.set("0")
    
    def darkchocolate():
        if var26.get()==1:
            text_darkchocolate.config(state=NORMAL)#change state back to normal
            text_darkchocolate.delete(0,END) # deletee 0 value
            text_darkchocolate.focus() #cursor to blink
        else:
            text_darkchocolate.config(state=DISABLED)    
            darkchocolate_e.set("0")
    
    def almondcarmel():
        if var27.get()==1:
            text_almondcarmel.config(state=NORMAL)#change state back to normal
            text_almondcarmel.delete(0,END) # deletee 0 value
            text_almondcarmel.focus() #cursor to blink
        else:
            text_almondcarmel.config(state=DISABLED)    
            almondcarmel_e.set("0")
    


    root=Tk() #root for screen 

    root.title("USER:"+user)


    root.geometry("1330x690+0+0")
    #root.resizable(0,0)

    root.config(bg="cyan")

    top_Frame=Frame(root,bd=15,relief=RIDGE)
    top_Frame.pack(side=TOP)

    label1=Label(top_Frame,text="RESTAURANT MANAGEMENT SYSTEM",font=("italics",30,"bold"),bg="cyan")
    label1.grid(row=0,column=0)

    #frames

    menu_frame=Frame(root,bd=10,relief=RIDGE)
    menu_frame.pack(side=LEFT)


    cost_frame=Frame(menu_frame,bd=4,relief=RIDGE,bg="Blue",pady=10)
    cost_frame.pack(side=BOTTOM)

    food_frame=LabelFrame(menu_frame,text="FOOD",font=("arial",20,"bold"),bd=10,relief=RIDGE,bg="blue")
    food_frame.pack(side=LEFT)

    ice_frame=LabelFrame(menu_frame,text="ICECREAMS",font=("arial",20,"bold"),bd=10,relief=RIDGE,bg="blue")
    ice_frame.pack(side=LEFT)

    drinks_frame=LabelFrame(menu_frame,text="DRINKS",font=("arial",20,"bold"),bd=10,relief=RIDGE,bg="blue")
    drinks_frame.pack(side=LEFT)

    right_frame=Frame(root,bd=15,relief=RIDGE,bg="blue")
    right_frame.pack(side=RIGHT)



    cal_frame=Frame(right_frame,bd=1,relief=RIDGE,bg="blue")
    cal_frame.pack()

    reciept_frame=Frame(right_frame,bd=4,relief=RIDGE)
    reciept_frame.pack()

    button_frame=Frame(right_frame,bd=4,relief=RIDGE,bg="red")
    button_frame.pack()


    # food

    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()
    var15=IntVar()
    var16=IntVar()
    var17=IntVar()
    var18=IntVar()
    var19=IntVar()
    var20=IntVar()
    var21=IntVar()
    var22=IntVar()
    var23=IntVar()
    var24=IntVar()
    var25=IntVar()
    var26=IntVar()
    var27=IntVar()

    burger_e=StringVar()
    pizza_e=StringVar()
    tacos_e=StringVar()
    fries_e=StringVar()
    momos_e=StringVar()
    sandwich_e=StringVar()
    onion_e=StringVar()
    noodle_e=StringVar()
    popcorn_e=StringVar()



    coffee_e=StringVar()
    coke_e=StringVar()
    thumsup_e=StringVar()
    sprite_e=StringVar()
    mojito_e=StringVar()
    icetea_e=StringVar()
    coldcoffee_e=StringVar()
    milkshake_e=StringVar()
    fruitpunch_e=StringVar()



    vanilla_e=StringVar()
    strawberry_e=StringVar()
    chocolate_e=StringVar()
    blackcurrent_e=StringVar()
    butterscotch_e=StringVar()
    kesarapista_e=StringVar()
    almondchoco_e=StringVar()
    darkchocolate_e=StringVar()
    almondcarmel_e=StringVar()

    costoffoodvar=StringVar()
    costofdrinkvar=StringVar()
    costoficevar=StringVar()
    subtotalvar=StringVar()
    servicetaxvar=StringVar()
    totalcostvar=StringVar()












    burger_e.set("0")
    pizza_e.set("0")
    tacos_e.set("0")
    fries_e.set("0")
    momos_e.set("0")
    sandwich_e.set("0")
    onion_e.set("0")
    noodle_e.set("0")
    popcorn_e.set("0")







    vanilla_e.set("0")
    strawberry_e.set("0")
    chocolate_e.set("0")
    blackcurrent_e.set("0")
    butterscotch_e.set("0")
    kesarapista_e.set("0")
    almondchoco_e.set("0")
    darkchocolate_e.set("0")
    almondcarmel_e.set("0")



    coffee_e.set("0")
    coke_e.set("0")
    thumsup_e.set("0")
    sprite_e.set("0")
    mojito_e.set("0")
    icetea_e.set("0")
    coldcoffee_e.set("0")
    milkshake_e.set("0")
    fruitpunch_e.set("0")






    burger=Checkbutton(food_frame,text='burger',font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var1,width=7,command=burger)
    burger.grid(row=0,column=0,sticky=W)



    pizza=Checkbutton(food_frame,text="pizza",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var2,width=7,command=pizza)
    pizza.grid(row=1,column=0,sticky=W)

    tacos=Checkbutton(food_frame,text="tacos ",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var3,width=7,command=tacos)
    tacos.grid(row=2,column=0,sticky=W)

    fries=Checkbutton(food_frame,text="fries ",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var4,width=7,command=fries)
    fries.grid(row=3,column=0,sticky=W)


    momos=Checkbutton(food_frame,text="momos",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var5,width=7,command=momos)
    momos.grid(row=4,column=0,sticky=W)

    sandwich=Checkbutton(food_frame,text="sandwich",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var6,width=7,command=sandwich)
    sandwich.grid(row=5,column=0,sticky=W)

    onion=Checkbutton(food_frame,text="onionring",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var7,width=7,command=onion)
    onion.grid(row=6,column=0,sticky=W)

    noodle=Checkbutton(food_frame,text="noodle",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var8,width=7,command=noodle)
    noodle.grid(row=7,column=0,sticky=W)

    popcorn=Checkbutton(food_frame,text="popcorn",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var9,width=7,command=popcorn)
    popcorn.grid(row=8,column=0,sticky=W)


    text_burger=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=burger_e,bd=7,width=6)
    text_burger.grid(row=0,column=1)

    text_pizza=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=pizza_e,bd=7,width=6)
    text_pizza.grid(row=1,column=1)

    text_tacos=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=tacos_e,bd=7,width=6)
    text_tacos.grid(row=2,column=1)


    text_fries=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=fries_e,bd=7,width=6)
    text_fries.grid(row=3,column=1)

    text_momos=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=momos_e,bd=7,width=6)
    text_momos.grid(row=4,column=1)

    text_sandwich=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=sandwich_e,bd=7,width=6)
    text_sandwich.grid(row=5,column=1)

    text_onion=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=onion_e,bd=7,width=6)
    text_onion.grid(row=6,column=1)

    text_noodle=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=noodle_e,bd=7,width=6)
    text_noodle.grid(row=7,column=1)

    text_popcorn=Entry(food_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=popcorn_e,bd=7,width=6)
    text_popcorn.grid(row=8,column=1)


    #drinks label
    coffee=Checkbutton(drinks_frame,text="coffee",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var10,width=7,command=coffee)
    coffee.grid(row=0,column=0,sticky=W)

    coke=Checkbutton(drinks_frame,text="coke",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var11,width=7,command=coke)
    coke.grid(row=1,column=0,sticky=W)

    thumpsup=Checkbutton(drinks_frame,text="thumsup",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var12,width=7,command=thumpsup)
    thumpsup.grid(row=2,column=0,sticky=W)


    sprite=Checkbutton(drinks_frame,text="sprite",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var13,width=7,command=sprite)
    sprite.grid(row=3,column=0,sticky=W)


    mojito=Checkbutton(drinks_frame,text="mojito",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var14,width=7,command=mojito)
    mojito.grid(row=4,column=0,sticky=W)


    icetea=Checkbutton(drinks_frame,text="icetea",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var15,width=7,command=icetea)
    icetea.grid(row=5,column=0,sticky=W)


    coldcoffee=Checkbutton(drinks_frame,text="coldcoffee",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var16,width=7,command=coldcoffee)
    coldcoffee.grid(row=6,column=0,sticky=W)

    milkshake=Checkbutton(drinks_frame,text="milkshake",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var17,width=7,command=milkshake)
    milkshake.grid(row=7,column=0,sticky=W)

    fruitpunch=Checkbutton(drinks_frame,text="fruitpunch",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var18,width=7,command=fruitpunch)
    fruitpunch.grid(row=8,column=0,sticky=W)

    #entry variables for drinks

    text_coffee=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=coffee_e,bd=7,width=6)
    text_coffee.grid(row=0,column=1)

    text_coke=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=coke_e,bd=7,width=6)
    text_coke.grid(row=1,column=1)

    text_thumsup=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=thumsup_e,bd=7,width=6)
    text_thumsup.grid(row=2,column=1)

    text_sprite=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=sprite_e,bd=7,width=6)
    text_sprite.grid(row=3,column=1)

    text_mojito=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=mojito_e,bd=7,width=6)
    text_mojito.grid(row=4,column=1)

    text_icetea=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=icetea_e,bd=7,width=6)
    text_icetea.grid(row=5,column=1)

    text_coldcoffee=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=coldcoffee_e,bd=7,width=6)
    text_coldcoffee.grid(row=6,column=1)

    text_milkshake=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=milkshake_e,bd=7,width=6)
    text_milkshake.grid(row=7,column=1)

    text_fruitpunch=Entry(drinks_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=fruitpunch_e,bd=7,width=6)
    text_fruitpunch.grid(row=8,column=1)



    # icecream checkbuttons

    vanilla=Checkbutton(ice_frame,text="vanilla",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var19,width=10,command=vanilla)
    vanilla.grid(row=0,column=0,sticky=W)

    strawberry=Checkbutton(ice_frame,text="strawberry",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var20,width=10,command=strawberry)
    strawberry.grid(row=1,column=0,sticky=W)

    chocolate=Checkbutton(ice_frame,text="chocolate",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var21,width=10,command=chocolate)
    chocolate.grid(row=2,column=0,sticky=W)

    blackcurrent=Checkbutton(ice_frame,text="blackcurrent",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var22,width=10,command=blackcurrent)
    blackcurrent.grid(row=3,column=0,sticky=W)

    butterscotch=Checkbutton(ice_frame,text="butterscotch",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var23,width=10,command=butterscotch)
    butterscotch.grid(row=4,column=0,sticky=W)

    kesarpista=Checkbutton(ice_frame,text="kesarpista",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var24,width=10,command=kesarpista)
    kesarpista.grid(row=5,column=0,sticky=W)

    almondchoco=Checkbutton(ice_frame,text="almondchoco",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var25,width=10,command=almondchoco)
    almondchoco.grid(row=6,column=0,sticky=W)

    darkchocolate=Checkbutton(ice_frame,text="darkchocolate",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var26,width=10,command=darkchocolate)
    darkchocolate.grid(row=7,column=0,sticky=W)

    almondcarmel=Checkbutton(ice_frame,text="almondcarmel",font=("arial",18,"bold"),onvalue=1,offvalue=0,variable=var27,width=10,command=almondcarmel)
    almondcarmel.grid(row=8,column=0,sticky=W)



    #entries for icecreams

    text_vanilla=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=vanilla_e,bd=7,width=6)
    text_vanilla.grid(row=0,column=1)

    text_strawberry=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=strawberry_e,bd=7,width=6)
    text_strawberry.grid(row=1,column=1)

    text_chocolate=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=chocolate_e,bd=7,width=6)
    text_chocolate.grid(row=2,column=1)

    text_blackcurrent=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=blackcurrent_e,bd=7,width=6)
    text_blackcurrent.grid(row=3,column=1)

    text_butterscotch=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=butterscotch_e,bd=7,width=6)
    text_butterscotch.grid(row=4,column=1)

    text_kesarpista=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=kesarapista_e,bd=7,width=6)
    text_kesarpista.grid(row=5,column=1)

    text_almondchoco=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=almondchoco_e,bd=7,width=6)
    text_almondchoco.grid(row=6,column=1)

    text_darkchocolate=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=darkchocolate_e,bd=7,width=6)
    text_darkchocolate.grid(row=7,column=1)

    text_almondcarmel=Entry(ice_frame,font=("arial",18,"bold"),state=DISABLED,textvariable=almondcarmel_e,bd=7,width=6)
    text_almondcarmel.grid(row=8,column=1)



    #cost label

    labelcostfood=Label(cost_frame,text="   Cost Of Food   ",font=("arial",16,"bold"),bg="cyan")
    labelcostfood.grid(row=0,column=0)

    text_costfood=Entry(cost_frame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costoffoodvar)
    text_costfood.grid(row=0,column=1,padx=35)




    labelcostdrink=Label(cost_frame,text="  Cost Of Drinks  ",font=("arial",16,"bold"),bg="cyan")
    labelcostdrink.grid(row=1,column=0)


    text_costdrink=Entry(cost_frame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costofdrinkvar)
    text_costdrink.grid(row=1,column=1,padx=35)




    labelcostice=Label(cost_frame,text="Cost Of Icecream",font=("arial",16,"bold"),bg="cyan")
    labelcostice.grid(row=2,column=0)

    text_costice=Entry(cost_frame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=costoficevar)
    text_costice.grid(row=2,column=1,padx=35)


    labelsubtotal=Label(cost_frame,text="  SubTotal  ",font=("arial",16,"bold"),bg="cyan")
    labelsubtotal.grid(row=0,column=2)

    text_subtotal=Entry(cost_frame,font=(" arial ",16,"bold"),bd=6,width=14,state="readonly",textvariable=subtotalvar)
    text_subtotal.grid(row=0,column=3,padx=35)

    labelservicetax=Label(cost_frame,text="Service tax",font=("arial",16,"bold"),bg="cyan")
    labelservicetax.grid(row=1,column=2)

    text_servicetax=Entry(cost_frame,font=(" arial ",16,"bold"),bd=6,width=14,state="readonly",textvariable=servicetaxvar)
    text_servicetax.grid(row=1,column=3,padx=35)


    labeltotalcost=Label(cost_frame,text=" Total Cost ",font=("arial",16,"bold"),bg="cyan")
    labeltotalcost.grid(row=2,column=2)

    text_totalcost=Entry(cost_frame,font=("arial",16,"bold"),bd=6,width=14,state="readonly",textvariable=totalcostvar)
    text_totalcost.grid(row=2,column=3,padx=35)



    #buttons
    button_total=Button(button_frame,text="Total",font=("arial",14,"bold"),bg="cyan",bd=3,padx=3,command=totalcost)
    button_total.grid(row=0,column=0)


    button_receipt=Button(button_frame,text="Receipt",font=("arial",14,"bold"),bg="cyan",bd=3,padx=3,command=receipt)
    button_receipt.grid(row=0,column=1)

    button_save=Button(button_frame,text="Save",font=("arial",14,"bold"),bg="cyan",bd=3,padx=3,command=save)
    button_save.grid(row=0,column=2)


    button_reset=Button(button_frame,text="Reset",font=("arial",14,"bold"),bg="cyan",bd=3,padx=3,command=reset)
    button_reset.grid(row=0,column=3)

    button_send=Button(button_frame,text="Send",font=("arial",14,"bold"),bg="cyan",bd=3,padx=3,command=send)
    button_send.grid(row=0,column=4)

    #text area for receipt

    text_Receipt=Text(reciept_frame,font=("arial",12,"bold"),bd=3,width=42,height=14)
    text_Receipt.grid(row=0,column=0)


    #calculator
    def button_num(numbers):
        global value
        value=value+numbers
        cal_entry.delete(0,END)
        cal_entry.insert(END,value)

    def clear():
        global value
        value=""
        cal_entry.delete(0,END)

    def answer():
        global value
        cal_entry.delete(0,END)
        result=str(eval(value))
        cal_entry.insert(0,result)
        value=""












    cal_entry=Entry(cal_frame,font=("arial",16,"bold"),width=32,bd=4)
    cal_entry.grid(row=0,column=0,columnspan=4)

    b7=Button(cal_frame,text="7",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num('7'))
    b7.grid(row=1,column=0)

    b8=Button(cal_frame,text="8",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num('8'))
    b8.grid(row=1,column=1)

    b9=Button(cal_frame,text="9",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num('9'))
    b9.grid(row=1,column=2)

    bplus=Button(cal_frame,text="+",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("+"))
    bplus.grid(row=1,column=3)


    b4=Button(cal_frame,text="4",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num('4'))
    b4.grid(row=2,column=0)

    b5=Button(cal_frame,text="5",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num('5'))
    b5.grid(row=2,column=1)

    b6=Button(cal_frame,text="6",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num('6'))
    b6.grid(row=2,column=2)

    bminus=Button(cal_frame,text="-",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("-"))
    bminus.grid(row=2,column=3)

    b1=Button(cal_frame,text="1",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("1"))
    b1.grid(row=3,column=0)

    b2=Button(cal_frame,text="2",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("2"))
    b2.grid(row=3,column=1)

    b3=Button(cal_frame,text="3",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("3"))
    b3.grid(row=3,column=2)

    bmul=Button(cal_frame,text="*",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("*"))
    bmul.grid(row=3,column=3)

    bans=Button(cal_frame,text="ans",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=answer)
    bans.grid(row=4,column=0)


    bclear=Button(cal_frame,text="clear",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=clear)
    bclear.grid(row=4,column=1)

    b0=Button(cal_frame,text="0",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("0"))
    b0.grid(row=4,column=2)

    bdiv=Button(cal_frame,text="/",font=("arial",16,"bold"),fg="yellow",bg="red",bd=4,width=6,command=lambda:button_num("/"))
    bdiv.grid(row=4,column=3)

    #logoimage= PhotoImage(file="sender.png")
        #label_1=Label(root2,image=logoimage)
        #label_1.pack

    button_menu=Button(button_frame,text="Menu",font=("arial",14,"bold"),bg="cyan",bd=3,padx=5,command=menu)
    button_menu.grid(row=0,column=5)



    root.mainloop()
    login()

def login():
    screen=tkinter.Tk()
    screen.title ("login page")
    screen.config(bg="black")
    

    l0=Label(screen,text="LOGIN",font=("Elephant","50","bold"))
    l0.grid(row=0,column=1)


    imgvar=Image.open("food.ico")
    imgvar=ImageTk.PhotoImage(imgvar.resize((200,200)))
    img=Button(screen,image=imgvar)
    img.grid(row=0,column=0)

    l=Label(screen,text="username",font=("Candles","40","bold"))
    l.grid(row=1,column=0)


    l1=Label(screen,text="password",font=("candles","40","bold"))
    l1.grid(row=2,column=0)


    e=Entry(screen,width=35,borderwidth=5,font="bold")
    e.grid(row=1,column=1,padx=30,pady=40)

    e1=Entry(screen,width=35,borderwidth=5,font="bold",show="*")
    e1.grid(row=2,column=1,padx=30,pady=40)

    def restaurant():
        global user
        a=e.get()
        b=e1.get()
        c=(a,b)
        f= open("login.bin",'rb')
        data = pickle.load(f)
        for i in data:
                if c==i:
                 screen.destroy()
                 user = c[0]
                 restaurants()
                 break
        else:
            messagebox.showerror('ERROR','Wrong user id or password')


    def save():

        global id_entry
        global pwd_entry
        a=id_entry.get()
        b=pwd_entry.get()
        c= (a,b)
        with open("login.bin",'rb') as f:
            data = pickle.load(f)
        for i in data:
            if i[0] == c[0]:
                messagebox.showwarning('Login error','Account already exists!!')
                with open("login.bin",'wb') as f:
                    pickle.dump(data,f)
                break

        else:
            data.append(c)
            with open("login.bin",'wb') as f:
                pickle.dump(data,f)
            messagebox.showinfo('DONE','account created!!')


    def create():
        global id_entry
        global pwd_entry
        try:
            screen_2.destroy()
        except:
            pass
        screen_2=Toplevel()
        screen_2.title("Create account")
        screen_2.config(bg="black")
        screen_2.geometry("700x250")
        id=Label(screen_2,text="USER ID  ",font=("candles","20","bold"))
        id.grid(row=0,column=0)
        id_entry=Entry(screen_2,bd=9,relief= RIDGE,font=("arial",18,"bold"),width=25)
        id_entry.grid(row=0,column=1,padx=10,pady=10)

        pwd=Label(screen_2,text="PASSWORD",font=("candles","20","bold"))
        pwd.grid(row=1,column=0)
        pwd_entry=Entry(screen_2,bd=9,relief= RIDGE,font=("arial",18,"bold"),width=25)
        pwd_entry.grid(row=1,column=1,pady=10)

        confirm=Button(screen_2,text="CONFIRM",font=("candles","20","bold"),command=save)
        confirm.grid(row=2,column=1)


    
        screen_2.mainloop()




    b1=Button(screen,width=35,text="login",font="bold",command=restaurant)
    b1.grid(column=1,row=3,padx=25,pady=25)

    b2=Button(screen,width=35,text="create account",font="bold",command=create)
    b2.grid(row=3,column=0)


    screen.mainloop()

login()
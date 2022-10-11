from tkinter import*
root= Tk()
root.title("fibonacci seiries")
root.geometry("400x200")
result_show= Label(root)
entry= Entry(root)
result_sum= Label(root) 
def fibonacci():
    nom1= 0
    num2= 1
    sum=0
    i=1
    sum2= 0
    numberr= entry.get()
    while(i<=int(numberr)):
        result_show["text"]+=str(sum)+" "
        result_sum["text"]="the sum of the fibnacci series:"+str(sum2)
        i= i+1
        nom1=num2
        num2=sum
        sum= nom1+num2
        sum2= sum2+sum
    
btn= Button(root,text= "show fibonacci seiries",command=fibonacci)
entry.pack()
btn.pack()
result_show.pack()
result_sum.pack()
root.mainloop()
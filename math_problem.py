import tkinter as tk
from tkinter import PhotoImage,messagebox
from tkinter import ttk

main_application = tk.Tk()

main_application.title("Solve Math Question")
main_application.geometry('1500x800')

## ++++++++++++++++++++++++++++++= background image 

# Create a style for the button
style = ttk.Style()
style.configure('TButton', foreground='black', background='red')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   function  +++++++++++++++++++++++++++++++++++++++++++++++++++++
def exit_func(event = None):
    main_application.destroy()

def exit(_exit):
    exit_btn = ttk.Button(main_application, text= 'Exit Application ', width= 25 , command = _exit)
    exit_btn.pack(pady = 20, side= 'bottom' ) 

def back(_back):
    back_button = ttk.Button(main_application,text= 'Back '  , command= open_func )
    back_button.pack(side=  'bottom', pady= 20 )

def submit(_func_tab):
    submit_btn = ttk.Button(main_application, text= 'Submit', width= 10 , command = _func_tab )
    submit_btn.pack(pady = 10, side= 'bottom' )

def intro_label_func(str):
    intr_label = tk.Label(main_application,text= str, font= ('Helvetica', 30,'bold'))
    intr_label.pack()

# +++++++++++++++++++++++++++++++++++++ MathMathics problem function  +++++++++++++++++++++++++++
armstorng_var = tk.StringVar()
prime_num_var = tk.StringVar()
even_odd_var = tk.StringVar()
num2 = tk.StringVar()
num1 = tk.StringVar()
fact_var = tk.StringVar()
n_numvar = tk.StringVar()
square_var =tk.StringVar()
cube_var = tk.StringVar()
lcm_var1 = tk.StringVar()
lcm_var2 = tk.StringVar()

# even_odd functionality 
def even_odd_tab(event = None):
    _even_odd_var = even_odd_var.get()
    try:
        _even_odd_var = int(_even_odd_var)
        if _even_odd_var %2 == 0 :
                enter_label1= tk.Label(main_application,text= f'   {_even_odd_var} Even  Number ' )
                enter_label1.pack(pady=4)
        else :
                enter_label1= tk.Label(main_application,text= f'{_even_odd_var} Odd  Number'  )
                enter_label1.pack(pady=4)
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')

def even_odd_func( event = None):
    
    for widget in main_application.winfo_children():
        widget.destroy()

    intro_label_func('Check the number is even or odd')
    enter_label= tk.Label(main_application,text= 'Enter the Number to Check Even or Odd Number  ', font=  (  'Helvetica', 10 )  )
    enter_label.pack(pady= 15)
    
    even_entry = ttk.Entry(main_application,width= 30 , textvariable=even_odd_var )
    even_entry.pack(pady = 10)

    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(even_odd_tab)
    
##  prime number functionality 
def prime_number_tab(event= None ):
    _prime_num_var = prime_num_var.get()
    try:
        _prime_num_var= int(_prime_num_var)
        check_prime = any([True if  _prime_num_var%i== 0   else  False  for i in range(2 , _prime_num_var//2+1) ])
        if _prime_num_var== 1 :
                enter_label1= tk.Label(main_application,text= f'   {_prime_num_var} is not Prime  Number ' )
                enter_label1.pack(pady=4)
        
        elif check_prime:
                enter_label1= tk.Label(main_application,text= f'   {_prime_num_var} is not Prime  Number ' )
                enter_label1.pack(pady=4)
        else :
                enter_label1= tk.Label(main_application,text= f'{_prime_num_var} is prime  Number'  )
                enter_label1.pack(pady=4)
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')


def prime_number_func(event = None):
    
    for widget in main_application.winfo_children():
        widget.destroy()

    intro_label_func('Check the number is Prime or Not ')
    enter_label= tk.Label(main_application,text= 'Enter the Number ', font=  (  'Helvetica', 15 )  )
    enter_label.pack()
    
    even_entry = ttk.Entry(main_application,width=50 , textvariable=prime_num_var )
    even_entry.focus()
    even_entry.pack()

    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(prime_number_tab)


## armstrong functionality 
def armstrong_number_tab(event= None ):
    _armstrong_var = armstorng_var.get()
    try:
        __armstrong_var = int(_armstrong_var)   # if  check_num2 is not number then raise in error 
        c = 0 
        for i in _armstrong_var:
            c+=int(i)**3
            
        if c == __armstrong_var :
                enter_label1= tk.Label(main_application,text= f'  {_armstrong_var}  is  Armstrong   Number ' )
                enter_label1.pack(pady=4)
        else :
                enter_label1= tk.Label(main_application,text= f'  {_armstrong_var} is not a Armstrong  Number'  )
                enter_label1.pack(pady=4)
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')


def armstrong_number_func(event = None):
    for widget in main_application.winfo_children():
        widget.destroy()
    
    intro_label_func('Check wheater the number is armstrong number or not ')
    
    enter_label= tk.Label(main_application,text= 'Enter the Number ', font=  ( 'Helvetica', 15 )  )
    enter_label.pack()
    
    even_entry = ttk.Entry(main_application,width=50 , textvariable = armstorng_var )
    even_entry.focus()
    even_entry.pack()

    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(armstrong_number_tab)

##++++++++++++++++++++++++   HCF of two Number ++++++++++++++++++++++++++++++++

def HCF_Two_tab(event= None ):
    check_num1 = num1.get()
    check_num2 = num2.get()
    
    try:
        check_num_hcf1 = int(check_num1)
        check_num_hcf2 = int(check_num2)
        
        if check_num_hcf2>check_num_hcf1:
            max,min = check_num_hcf2,check_num_hcf1
        else :
            max,min = check_num_hcf1,check_num_hcf2
        
        while min  != 0 :
            re = max%min 
            max = min
            min = re 
        enter_label1= tk.Label(main_application,text= f'  HCF of { check_num_hcf2}and  {check_num_hcf1} is : {max} ' )
        enter_label1.pack(pady=4)
        
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')


def HCF_Two_func(event = None):
    
    for widget in main_application.winfo_children():
        widget.destroy()

    intro_label_func('Find the HCF of two number')
    enter_label1= tk.Label(main_application,text= 'Enter the  1st Number ', font=  (  'Helvetica', 15 )  )
    enter_label2= tk.Label(main_application,text= 'Enter the  2nd Number ', font=  (  'Helvetica', 15 )  )
    
    even_entry1 = ttk.Entry(main_application,width=50 , textvariable= num1 )
    even_entry2 = ttk.Entry(main_application,width=50 , textvariable= num2 )
    
    even_entry1.focus()
    enter_label1.pack()
    even_entry1.pack()
    enter_label2.pack()
    even_entry2.pack()
    
    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(HCF_Two_tab)

###++++++++ LCM function 

def lcm_func_tab(event = None):
    _lcm_var1 = lcm_var1.get()
    _lcm_var2 = lcm_var2.get()
    
    try:
        _lcm_var1 = int(_lcm_var1)
        _lcm_var2 = int(_lcm_var2)
        a = 0
        i = 1
        while  True:
            a = (_lcm_var2*i)
            if a%_lcm_var1 == 0 :
                break
            i+=1
        
        enter_label1= tk.Label(main_application,text= f'  LCM of { _lcm_var1}and  {_lcm_var2} is : {a} ' )
        enter_label1.pack(pady=4)
        
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')


def lcm_func(event = None):    
    for widget in main_application.winfo_children():
        widget.destroy()

    intro_label_func('Find the LCM of two number')

    enter_label= tk.Label(main_application,text= 'Enter the  1st Number ', font=  (  'Helvetica', 15 )  )
    enter_label.pack()
    
    even_entry = ttk.Entry(main_application,width=50 , textvariable= lcm_var1 )
    even_entry.focus()
    even_entry.pack()
    
    enter_label2= tk.Label(main_application,text= 'Enter the  2nd Number ', font=  (  'Helvetica', 15 )  )
    enter_label2.pack()
    
    even_entry2 = ttk.Entry(main_application,width=50 , textvariable= lcm_var2 )
    even_entry2.pack()
    
    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(lcm_func_tab)

##+++++++    factorial funtion
def factorial_func_tab( even = None ):
    _fact_var = fact_var.get()
    try:
        _fact_var = int(_fact_var)
        f = 1 
        for i in range (1,_fact_var+1):
            f*=i
        enter_label1= tk.Label(main_application,text= f' Factorial of {_fact_var} is {f} ' )
        enter_label1.pack(pady= 4 )
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')

def factorial_func(event = None ):
    for widget in main_application.winfo_children():
        widget.destroy()
        
    intro_label_func('Find the Factorial of a Number ')
    
    enter_label= tk.Label(main_application,text= 'Enter the  Number ', font=  (  'Helvetica', 15 )  )
    enter_label.pack()
    
    fact_entry = ttk.Entry(main_application,width=50 , textvariable= fact_var )
    fact_entry.focus()
    fact_entry.pack()
    
    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(factorial_func_tab)


## Natural Number 
def natural_func_tab( even = None ):
    _n_numvar = n_numvar.get()
    try:
        f = 0 
        _n_numvar = int(_n_numvar)
        for i in range (1,_n_numvar+1):
            f+=i
        enter_label1= tk.Label(main_application,text= f'  Sum of First  {_n_numvar} Natural Number  is :  {f} ' )
        enter_label1.pack(pady= 4 )
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')

def natural_func(event = None ):
    for widget in main_application.winfo_children():
        widget.destroy()   
    
    intro_label_func('Find the sum of Natural number')
    enter_label= tk.Label(main_application,text= 'Enter the Number ', font=  (  'Helvetica', 15 )  )
    enter_label.pack()
    
    natural_entry = ttk.Entry(main_application,width=50 , textvariable= n_numvar )
    natural_entry.focus()
    natural_entry.pack()
    
    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(natural_func_tab)

#++++++++ Square function 
def square_func_tab(event = None):
    _square_var =square_var.get()
    try:
        _square_var = int(_square_var)
        
        enter_label1= tk.Label(main_application,text= f' The square of {_square_var} is :-   {_square_var **2  }' )
        enter_label1.pack(pady= 4)
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')

def square_func(event = None):
    for widget in main_application.winfo_children():
        widget .destroy()
    
    intro_label_func('Find the Square of  number')
    
    enter_label= tk.Label(main_application,text= 'Enter the Number ', font=  (  'Helvetica', 15 )  )
    enter_label.pack()
    
    square_entry = ttk.Entry(main_application,width=50 , textvariable= square_var )
    square_entry.focus()
    square_entry.pack()
    
    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(square_func_tab)
    

###++++++ Cube  function 

def cube_func_tab(event = None):
    _cube_var = cube_var.get()
    try:
        f = 0 
        _cube_var = int(_cube_var)
        
        enter_label1= tk.Label(main_application,text= f' The  Cube  f {_cube_var} is :-   {_cube_var**3 }  ' )
        enter_label1.pack(pady=4 )
    except:
        messagebox.showerror("Error", 'Please !! , enter a number ')
    

def cube_func(event = None):
    for widget in main_application.winfo_children():
        widget.destroy()
    
    intro_label_func('Find the Cube of number')
    
    enter_label= tk.Label(main_application,text= 'Enter the  Number ', font=  (  'Helvetica', 15 )  )
    enter_label.pack()

    cube_entry = ttk.Entry(main_application,width=50 , textvariable= cube_var )
    cube_entry.focus()
    cube_entry.pack()
    ## button in function 
    exit(exit_func)
    back(open_func)
    submit(cube_func_tab)

## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  End Math Problem +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def open_func( event = None):
    for widget in main_application.winfo_children():
        widget.destroy()
    
    ## open  page label 
    select_label = tk.Label(main_application,text= 'Select Your math Problem', font=  (  'Helvetica', 30, 'bold')  )
    even_odd = ttk.Button(main_application,text= 'Check Even or Odd '  , command= even_odd_func )
    prime_number = ttk.Button(main_application,text= 'Check Prime Number  ' , command= prime_number_func)
    armstrong_number = ttk.Button(main_application,text= 'Check Armstrong Numbe' ,command= armstrong_number_func)
    LCM_label= ttk.Button(main_application,text= 'find LCM of two Number  '  , command= lcm_func )
    HCF_label= ttk.Button(main_application,text= 'Find HCF of Two Number ' , command=HCF_Two_func)
    Factorial_label = ttk.Button(main_application,text= 'Find the factorial ', command= factorial_func)
    square_number = ttk.Button(main_application,text= ' Find a square of Number', command= square_func)
    cube_number = ttk.Button(main_application,text= ' Find a Cube of a Number', command= cube_func)
    sum_n_number= ttk.Button(main_application,text= 'Sum of N Natural Number ' , command= natural_func)
    
    # add pack feature 
    select_label.pack()
    even_odd.pack(pady=18)
    prime_number.pack(pady=18 , padx= 18 )
    armstrong_number.pack(pady= 18  )
    LCM_label.pack(pady= 18  )
    HCF_label.pack(pady= 18       )
    Factorial_label.pack(pady= 18  )
    square_number.pack(pady= 18  )
    cube_number.pack(pady=18   )
    sum_n_number.pack(pady=18 ) 
    
    # exit button 
    exit_btn = ttk.Button(main_application, text= 'Exit Application ', width= 25 , command= exit_func)    
    exit_btn.pack(pady = 10, side= 'bottom' )

#++++++++++++++++++++++++++++++++++++++++++++ End Function +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

home_label = tk.Label(main_application,text= 'Welcome to Solve Math Question', font=  (  'Helvetica', 35, 'bold','italic')  )

#### home page label 
open_btn = ttk.Button(main_application, text= 'open', width= 10,  command= open_func)
exit(exit_func)

# home page pack 
home_label.pack()
open_btn.pack(pady= 150)

main_application.mainloop() 
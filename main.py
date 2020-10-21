# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:19:21 2020

@author: joedattoli
"""
"""
Created on Fri Oct  2 21:24:37 2020

@author: joedattoli
"""
import tkinter as tk
from datetime import datetime
import pandas as pd
from PIL import ImageTk,Image
       



def submit_to_full():
    print('start')
    df_full = pd.read_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_full.csv')
    df_temp = pd.read_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_temp.csv')
    
    df_full = df_full.append(df_temp, ignore_index = True)
    df_full.to_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_full.csv', index = False)
    print('finish')    

def temp_writer(info):
    for i in range(1,len(info)):
        if (info[i] == ''):
            info[i] = 0
        else:
            info[i] = int(info[i])
    
    app_dict = {'Player': info[0],'PA': info[1], 'AB': info[2], 'R': info[3], '1B': info[4],'2B': info[5], '3B': info[6],'HR': info[7],
                'BB': info[8],'HBP': info[9],'KL': info[10],'KS': info[11],'SB': info[12],'CS': info[13],'RBI': info[14],'SAC_BUNT': info[15],
                'SAC_FLY': info[16],'DP': info[17],'QUAB': info[18],'HHB': info[19],
                'PITCHES': info[20],'STRIKES': info[21],'TOT_SWINGS': info[22]}
    
    
    app_series = pd.Series(app_dict)
    #print(app_series)
    df = pd.read_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_temp.csv' )
    #print(df)
    df = df.append(app_series, ignore_index = True)
    df.to_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_temp.csv', index = False)




class App_Main_Window(tk.Frame):
    def __init__(self,parent):
        super(App_Main_Window,self).__init__(parent)
        
        self.NAME_label = tk.Label(self, text = 'NAME')
        self.PA_label = tk.Label(self, text = 'PA')
        self.AB_label = tk.Label(self, text = 'AB')
        self.R_label = tk.Label(self, text = 'R')
        self.SINGLE_label = tk.Label(self, text = '1B')
        self.DOUBLE_label = tk.Label(self, text = '2B')
        self.TRIPLE_label = tk.Label(self, text = '3B')
        self.HR_label = tk.Label(self, text = 'HR')
        self.BB_label = tk.Label(self, text = 'BB')
        self.HBP_label = tk.Label(self, text = 'HBP')
        self.KL_label = tk.Label(self, text = 'KL')
        self.KS_label = tk.Label(self, text = 'KS')
        self.SB_label = tk.Label(self, text = 'SB')
        self.CS_label = tk.Label(self, text = 'CS')
        self.RBI_label = tk.Label(self, text = 'RBI')
        self.SAC_label = tk.Label(self, text = 'SAC_BUNT')
        self.SACFLY_label = tk.Label(self, text = 'SAC_FLY')
        self.DP_label = tk.Label(self, text = 'DP')
        self.QUAB_label = tk.Label(self, text = 'QUAB')
        self.HHB_label = tk.Label(self, text = 'HHB')       
        self.PITCHES_label = tk.Label(self, text = 'PITCHES')
        self.STRIKES_label = tk.Label(self, text = 'STRIKES')
        self.TOT_SWINGS_label = tk.Label(self, text = 'TOT_SWINGS')  
        
        self.NAME_label.grid(row=1,column=0,padx=3)
        self.PA_label.grid(row=1,column=1,padx=3)
        self.AB_label.grid(row=1,column=2,padx=3)
        self.R_label.grid(row=1,column=3,padx=3)
        self.SINGLE_label.grid(row=1,column=4,padx=3)
        self.DOUBLE_label.grid(row=1,column=5,padx=3)
        self.TRIPLE_label.grid(row=1,column=6,padx=3)
        self.HR_label.grid(row=1,column=7,padx=3)
        self.BB_label.grid(row=3,column=1,padx=3)
        self.HBP_label.grid(row=3,column=2,padx=3)
        self.KL_label.grid(row=3,column=3,padx=3)
        self.KS_label.grid(row=3,column=4,padx=3)
        self.SB_label.grid(row=3,column=5,padx=3)
        self.CS_label.grid(row=3,column=6,padx=3)
        self.RBI_label.grid(row=3,column=7,padx=3)
        self.SAC_label.grid(row=5,column=1,padx=3)
        self.SACFLY_label.grid(row=5,column=2,padx=3)
        self.DP_label.grid(row=5,column=3,padx=3)
        self.QUAB_label.grid(row=5,column=4,padx=3)
        self.HHB_label.grid(row=5,column=5,padx=3)  
        self.PITCHES_label.grid(row=7,column=1,padx=3)
        self.STRIKES_label.grid(row=7,column=2,padx=3)
        self.TOT_SWINGS_label.grid(row=7,column=3,padx=3) 
        
        self.NAME_var = tk.StringVar()
        self.PA_var =  tk.StringVar()
        self.AB_var = tk.StringVar()
        self.R_var =  tk.StringVar()
        self.SINGLE_var = tk.StringVar()
        self.DOUBLE_var = tk.StringVar()
        self.TRIPLE_var = tk.StringVar()
        self.HR_var =  tk.StringVar()
        self.BB_var =  tk.StringVar()
        self.HBP_var =  tk.StringVar()
        self.KL_var =  tk.StringVar()
        self.KS_var =  tk.StringVar()
        self.SB_var =  tk.StringVar()
        self.CS_var =  tk.StringVar()
        self.RBI_var =  tk.StringVar()
        self.SAC_var =  tk.StringVar()
        self.SACFLY_var =  tk.StringVar()
        self.DP_var =  tk.StringVar()
        self.QUAB_var =  tk.StringVar()
        self.HHB_var =  tk.StringVar()
        self.PITCHES_var =  tk.StringVar()
        self.STRIKES_var =  tk.StringVar()
        self.TOT_SWINGS_var = tk.StringVar()
        
        self.NAME_entry = tk.Entry(self, textvariable =self.NAME_var )
        self.PA_entry = tk.Entry(self, textvariable =self.PA_var )
        self.AB_entry = tk.Entry(self, textvariable =self.AB_var )
        self.R_entry = tk.Entry(self, textvariable =self.R_var )
        self.SINGLE_entry = tk.Entry(self, textvariable = self.SINGLE_var )
        self.DOUBLE_entry = tk.Entry(self, textvariable = self.DOUBLE_var)
        self.TRIPLE_entry = tk.Entry(self, textvariable = self.TRIPLE_var)
        self.HR_entry = tk.Entry(self, textvariable = self.HR_var )
        self.BB_entry = tk.Entry(self, textvariable = self.BB_var)
        self.HBP_entry = tk.Entry(self, textvariable = self.HBP_var)
        self.KL_entry = tk.Entry(self, textvariable = self.KL_var)
        self.KS_entry = tk.Entry(self, textvariable = self.KS_var)
        self.SB_entry = tk.Entry(self, textvariable = self.SB_var)
        self.CS_entry = tk.Entry(self, textvariable = self.CS_var)
        self.RBI_entry = tk.Entry(self, textvariable =self.RBI_var )
        self.SAC_entry = tk.Entry(self, textvariable = self.SAC_var)
        self.SACFLY_entry = tk.Entry(self, textvariable = self.SACFLY_var)
        self.DP_entry = tk.Entry(self, textvariable = self.DP_var)
        self.QUAB_entry = tk.Entry(self, textvariable = self.QUAB_var)
        self.HHB_entry = tk.Entry(self, textvariable = self.HHB_var)
        self.PITCHES_entry = tk.Entry(self, textvariable =self.PITCHES_var)
        self.STRIKES_entry = tk.Entry(self, textvariable = self.STRIKES_var)
        self.TOT_SWINGS_entry = tk.Entry(self, textvariable = self.TOT_SWINGS_var)
        
        
        self.NAME_entry.grid(row=2,column=0,padx=3)
        self.PA_entry.grid(row=2,column=1,padx=3)
        self.AB_entry.grid(row=2,column=2,padx=3)
        self.R_entry.grid(row=2,column=3,padx=3)
        self.SINGLE_entry.grid(row=2,column=4,padx=3)
        self.DOUBLE_entry.grid(row=2,column=5,padx=3)
        self.TRIPLE_entry.grid(row=2,column=6,padx=3)
        self.HR_entry.grid(row=2,column=7,padx=3)
        self.BB_entry.grid(row=4,column=1,padx=3)
        self.HBP_entry.grid(row=4,column=2,padx=3)
        self.KL_entry.grid(row=4,column=3,padx=3)
        self.KS_entry.grid(row=4,column=4,padx=3)
        self.SB_entry.grid(row=4,column=5,padx=3)
        self.CS_entry.grid(row=4,column=6,padx=3)
        self.RBI_entry.grid(row=4,column=7,padx=3)
        self.SAC_entry.grid(row=6,column=1,padx=3)
        self.SACFLY_entry.grid(row=6,column=2,padx=3)
        self.DP_entry.grid(row=6,column=3,padx=3)
        self.QUAB_entry.grid(row=6,column=4,padx=3)
        self.HHB_entry.grid(row=6,column=5,padx=3)  
        self.PITCHES_entry.grid(row=8,column=1,padx=3)
        self.STRIKES_entry.grid(row=8,column=2,padx=3)
        self.TOT_SWINGS_entry.grid(row=8, column=3,padx=3)  
        
        self.submit_button =tk.Button(self, command = self.submit_choices, text = 'Submit Stats')
        self.submit_button.grid(row=8,column=6)
        
    def submit_choices(self):
        temp_writer(self.get_all())
        self.NAME_entry.delete(0 , tk.END)
        self.PA_entry.delete(0 , tk.END)
        self.AB_entry.delete(0 , tk.END)
        self.R_entry.delete(0 , tk.END)
        self.SINGLE_entry.delete(0 , tk.END)
        self.DOUBLE_entry.delete(0 , tk.END)
        self.TRIPLE_entry.delete(0 , tk.END)
        self.HR_entry.delete(0 , tk.END)
        self.BB_entry.delete(0 , tk.END)
        self.HBP_entry.delete(0 , tk.END)
        self.KL_entry.delete(0 , tk.END)
        self.KS_entry.delete(0 , tk.END)
        self.SB_entry.delete(0 , tk.END)
        self.CS_entry.delete(0 , tk.END)
        self.RBI_entry.delete(0 , tk.END)
        self.SAC_entry.delete(0 , tk.END)
        self.SACFLY_entry.delete(0 , tk.END)
        self.DP_entry.delete(0 , tk.END)
        self.QUAB_entry.delete(0 , tk.END)
        self.HHB_entry.delete(0 , tk.END)
        self.PITCHES_entry.delete(0 , tk.END)
        self.STRIKES_entry.delete(0 , tk.END)
        self.TOT_SWINGS_entry.delete(0 , tk.END)
        
            
    def get_all(self):
        return[self.NAME_var.get(),self.PA_var.get(),self.AB_var.get(),self.R_var.get(),self.SINGLE_var.get(),self.DOUBLE_var.get(),
               self.TRIPLE_var.get(),self.HR_var.get(), self.BB_var.get(), self.HBP_var.get(), self.KL_var.get(), self.KS_var.get(),
               self.SB_var.get(), self.CS_var.get(), self.RBI_var.get(), self.SAC_var.get(), self.SACFLY_var.get(), self.DP_var.get(),
               self.QUAB_var.get(), self.HHB_var.get(), self.PITCHES_var.get(), self.STRIKES_var.get(), self.TOT_SWINGS_var.get()]
    
        
if __name__ == "__main__":  
    
    root = tk.Tk()
    root.title("Offensive Stats Platform  v0.0.1 Pre-Alpha")
    canvas = tk.Canvas(root, width = 150, height = 150)  
    canvas.grid(row=0)  
    img = ImageTk.PhotoImage(Image.open(r"C:\Users\joedattoli\Documents\GitHub\radialdefensivechart\main_logo.png"))  
    canvas.create_image(75, 75, image=img) 
    app = App_Main_Window(root)
    app.grid(row =1)



    root.mainloop()
        
        
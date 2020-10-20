
"""
Created on Fri Oct  2 21:24:37 2020

@author: joedattoli
"""

import pandas as pd

#       print(time,self.get_player(),self.get_pos(),self.get_play(),self.get_direction(),self.get_speed(),self.get_bb(),self.get_base(),self.get_out(),get_align)
counting_stats = pd.DataFrame(columns = ['Player','PA', 'AB', 'R', '1B','2B', '3B','HR', 'BB','HBP','KL','KS','SB','CS','RBI','SAC_BUNT','SAC_FLY','DP','QUAB','HHB','PITCHES','STRIKES','TOT_SWINGS'])

counting_stats.to_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_full.csv', index = False)
counting_stats.to_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_backup.csv', index = False)
counting_stats.to_csv(r'C:\Users\joedattoli\Documents\gamechartexcelsheets\counting_stats_temp.csv', index = False)




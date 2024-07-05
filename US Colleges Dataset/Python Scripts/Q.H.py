import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
aaup_df = pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data', na_values=['*'])
usnews_df = pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data', na_values=['*'])

# Rename columns
aaup_df.columns = ['FICE','inst_name','Pin', 'inst_type', 'avg_full','avg_asc','avg_ass', 'avg_salary', 'avc_full','avc_asc','avc_ass','avg_comp', 'num_full','num_asc','num_ass','num_ins','num_faculty']
usnews_df.columns = ['FICE1','inst_name','Pin1', 'inst_type1', 'math_sat','verb_sat','sat','avg_act','fqmath','tqmath','fqverb','tqverb','fqact','tqact','num_cand','num_accept','num_enrol','pct_new_10','pct_new_25','num_full_ug','num_part_ug', 'instate_tuition','outstate_tuition','r&bcost','rcost','bcost','add_fee','bookcost','pers_exp','pct_fac_phd','pct_fac_termdeg','stu_fac_ratio','pct_alum','instexp_stu', 'grad_rate']

# Merge dataframes
merged_df = pd.merge(aaup_df, usnews_df, on='inst_name')

import pandas as pd
import matplotlib.pyplot as plt

# Select relevant columns
cost_df = usnews_df[usnews_df['inst_type1']==1][['inst_name', 'outstate_tuition', 'r&bcost', 'rcost', 'bcost', 'add_fee', 'bookcost', 'pers_exp']]
cost_df2 = usnews_df[usnews_df['inst_type1']==2][['inst_name', 'outstate_tuition', 'r&bcost', 'rcost', 'bcost', 'add_fee', 'bookcost', 'pers_exp']]
# Replace missing values with 0
cost_df = cost_df.replace('*', 0)
cost_df2 = cost_df2.replace('*', 0)
# Convert columns to float
cost_df = cost_df.astype({'outstate_tuition': float, 'r&bcost': float, 'rcost': float, 'bcost':float ,'add_fee':float, 'bookcost': float, 'pers_exp':float})
cost_df2 = cost_df2.astype({'outstate_tuition': float, 'r&bcost': float, 'rcost': float, 'bcost':float ,'add_fee':float, 'bookcost': float, 'pers_exp':float})
cost_df=cost_df.sum(axis='columns')
cost_df2=cost_df2.sum(axis='columns')
plt.subplot(2,1,1)
plt.hist(cost_df,bins=10)
plt.xlabel('Total Expenses of a student in public college($)')
plt.ylabel('Number of colleges')
plt.title('Average is $13923')
plt.show()
plt.subplot(2,1,2)
plt.hist(cost_df2,bins=10)
plt.xlabel('Total Expenses of a student in private college($)')
plt.ylabel('Number of colleges')
plt.title('Average is $20707')
plt.show()
print('Average value',cost_df.mean())
print('Average value',cost_df2.mean())
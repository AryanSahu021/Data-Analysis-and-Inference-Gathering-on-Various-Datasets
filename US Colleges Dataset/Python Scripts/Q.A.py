import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
aaup_df = pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/aaup.data', na_values=['*'])
usnews_df = pd.read_csv('http://lib.stat.cmu.edu/datasets/colleges/usnews.data', na_values=['*'])

# Rename columns
aaup_df.columns = ['FICE','inst_name','Pin', 'inst_type', 'avg_full','avg_asc','avg_ass', 'avg_salary', 'avc_full','avc_asc','avc_ass','avg_comp', 'num_full','num_asc','num_ass','num_ins','num_faculty']
usnews_df.columns = ['FICE','inst_name','Pin', 'inst_type', 'math_sat','verb_sat','sat','avg_act','fqmath','tqmath','fqverb','tqverb','fqact','tqact','num_cand','num_accept','num_enrol','pct_new_10','pct_new_25','num_full_ug','num_part_ug', 'instate_tuition','outstate_tuition','r&bcost','rcost','bcost','add_fee','bookcost','pers_exp','pct_fac_phd','pct_fac_termdeg','stu_fac_ratio','pct_alum','instexp_stu', 'grad_rate']

# Merge dataframes
merged_df = pd.merge(aaup_df, usnews_df, on='inst_name')

# Create scatterplot of college size vs. graduation rate
plt.scatter(merged_df['num_faculty'], merged_df['grad_rate'])
plt.xlabel('Number of Faculty')
plt.ylabel('Graduation Rate')
plt.title('Number of Faculty vs. Graduation Rate')
plt.show()
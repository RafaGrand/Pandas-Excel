from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import pandas as pd
#Use line below for disolay all rows of the DF
pd.set_option('display.max_rows',None)

file_path = '#YourPath'

df = pd.read_excel(file_path, header=0)
#Use line below if you want to only use some cols
#df_col_filter = pd.read_excel(file_path, header=0, usecols=[0,1,2,10,11,12], names=['A','B','C','D','E','F'])
#Use line below if you want to filter data that contains some string
#filter_df = df[df['A'].str.contains("#String") | df['B'].str.contains("#AnotherString")]

#Plot Pie 
colors  = ("dodgerblue","salmon", "palevioletred", "steelblue", "seagreen", "plum", "blue", "indigo", "beige", "yellow")

i = 0 #Counter

for col in df: 
    sizes = filter_df[col].value_counts()
    pie = filter_df[col].value_counts().plot(kind='pie',colors=colors,shadow=True,autopct='%1.1f%%',startangle=30,radius=1.5,
                                      center=(0.5,0.5),textprops={'fontsize':12},frame=False,labels=None,pctdistance=.65)
    labels = sizes.index.unique()
    plt.gca().axis("equal")
    plt.title(df.columns[i],weight='bold',size=14)
    plt.subplots_adjust(left=0.0,bottom=0.1,right=0.85)
    #plt.savefig(str(df.columns[i])+'.png',dpi=100,bbox_inches='tight') #Save Plots as PNG
    pie.set_ylabel('')
    plt.legend(labels,bbox_to_anchor=(0.5, -.2),
           bbox_transform=plt.gcf().transFigure)
    i = i+1
    plt.show()
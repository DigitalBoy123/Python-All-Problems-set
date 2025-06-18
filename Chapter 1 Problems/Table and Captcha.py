from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="User Data",style= "Purple")

table.add_column("Serials", style="green", justify="center")
table.add_column("Names" , style= "Yellow",)
table.add_column("Age", justify = "center", style= "Blue")
table.add_column("Marks", justify = "center", style= "red")
table.add_column("Grade", justify = "center", style= "Purple")
table.add_column("Percenetage", justify = "center")


table.add_row("1","Mohammad", "23","344","B","60%")
table.add_row("2","Ali khan", "34","440","B","55%")
table.add_row("4","Halim", "19","330","C","45%")
table.add_row("5","Naqib", "16","450","B","69%")
table.add_row("6","Jumad ullah", "18","490","A","95%")
table.add_row("7","Aziz khan", "24","210","C","50%")
table.add_row("8","Wakil", "27","150","D","30%")
table.add_row("9","Noor", "31","410","B","78%")
table.add_row("10","Majid khan", "30","299","C","47%")
table.add_row("11","Sudais", "17","170","C","20%")

console.print(table)







# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# data = np.random.rand(10,12)
# sns.heatmap(data, cmap = 'viridis')
# plt.show()
#using DataFrames lib from python
import pandas as pd
#film-making team work distribution
dtt = {
  "Name" = ["Ansh","Amar","Koushik","Govind","Rahul","Sandeep"],
  "Occupation" = ["Media & marketing","Travels Head","Employees Head","","Camera team head","Writer"]
}

dg = pd.DataFrame(dtt)
print(dg)

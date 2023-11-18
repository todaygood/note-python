import pandas as pd 


# Add new column to the DataFrame
tutors = ['William', 'Henry', 'Michael', 'John', 'Messi']
df2 = df.assign(TutorsAssigned=tutors)

# Add a multiple columns to the DataFrame
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon']
df2 =df.assign(MNCComp = MNCCompanies,TutorsAssigned=tutors )

# Derive New Column from Existing Column
df = pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x: x.Fee * x.Discount / 100)

# Add a constant or empty value to the DataFrame.
df = pd.DataFrame(technologies)
df2=df.assign(A=None,B=0,C="")

# Add New column to the existing DataFrame
df = pd.DataFrame(technologies)
df["MNCCompanies"] = MNCCompanies

# Add new column at the specific position
df = pd.DataFrame(technologies)
df.insert(0,'Tutors', tutors )

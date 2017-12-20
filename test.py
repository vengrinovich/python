import datetime
import pandas as pd 

# this below is the same as above but using a simple example;
x = [('2002-05-01', 968), ('2002-04-01', 155), ('2002-04-01', 155), ('2003-07-01', 578), ('2003-01-01', 973)]

# creates an dataframe where each values in sublist a is a sepate row with column names year & column
df = pd.DataFrame(data = x, columns=['year','number'])
print df

# makes sure that the date column is in the right datetime format
# so letter you can easily extract date, month or year from it
df['year'] = pd.to_datetime(df['year'])

# groups the values month-year in the first column, uses strftime values for month and year
# then sums the values of grouped items, sorts them and returns
dff = df.groupby(df['year'].dt.strftime('%m-%Y'))['number'].sum().sort_values()

print dff
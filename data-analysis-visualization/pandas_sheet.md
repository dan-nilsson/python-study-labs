## Pandas Cheat Sheet

### Basis
#### Shape. (rows, cols)
df.shape
#### Info.  entries, cols, names, value_set
df.info()
#### Columns
df.columns   
#### Various Info
df.describe()   
df.dtype   
df.nunique()   
df.unique()   
df.tolist()   
df.duplicated().sum()   
### Options
#### Display
pd.set_option('display.max_columns', val)   
pd.set_option('display.max_rows', val)
#### Limit
df.head(val)   
df.tail(val)   
default=5
### Indexing
#### Set Index on Read
pd.read_csv(index_col='col')
#### Sort Index row, inplace for perm
df.sort_index(inplace=True)
#### loc can now grab row by column value
df.loc('index_row_val')
#### index of mask match
df[mask].index   
df.drop(index=df[mask].index)
### Filter
#### Output
df['col']   
df[['col','col2']]   
df.iloc[int]   
df.loc[index]   
df.iloc/loc[[1,2,3], col_index]   
#### Slice. start/stop:incl
df.loc[0:2, 'col':'col2']
#### Compare
df[col].value_counts()   
df[col].mean()    
df[col].apply(len)   
df.applymap(len)   
#### Mask, &=AND |=OR
df['col'] == val   
df['col'] >= 0   
df['col].isin([vals_in_col])   
df['col'].str.contains('str', na=False)   
#### Filter by mask, ~=invers
df[mask]   
df.loc[mask, 'col']   
df.loc[mask, ['col','col2']]   
### Columns
#### Columns
df.columns = ['new_name','new_2']   
df.columns = [x.upper() for x in df.columns]   
df.columns = df.columns.str.replace(' ','_')   
df.rename(columns={'current': 'new'}, inplace=True)
### Data Operations
#### Data update
df.loc[i] = [val, val, val...]    
df.loc[i, [col, col2]] = [val,val...]    
df.loc[i, col] = val   
df[col].str.lower()   
df[col] = df[col].apply(func)   
.apply(lambda x: x.lower())   
df[col].map({'Yes': True, 'No': False})    
.map not matched default NaN.   
df[col].replace({'Yes': True, 'No': False})   
#### Data change
df['full_name'] = df['first] + ' ' + df['last']   
df.drop(columns=['first','last'], inplace=True)   
df[['first','last']] = df['full_name'].str.split(' ', expand=True)   
df.append({...} ignore_index=True)   
df.append(df2, ignore_index=True, sort=False)   
df.drop(index=val, inplace=True)   
#### String Operations
str.strip(char)    
str.lower()   
str.upper()   
str.title()   
#### Cast
pd.to_datetime(df, errors='coerce')   
df.astype(float)   
### Duplicates
#### Info and Drop
df.duplicated().sum()   
df[df.duplicated(keep=False)].head(6)   
df.drop_duplicates().reset_index(drop=True)   
### Final
#### Drop Tables and Save Clean
df.drop(columns='empty_col')   
df_clean.to_csv('data/clean.csv', index=False)   

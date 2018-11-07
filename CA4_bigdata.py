
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[28]:



def read_file(any_file):
    # use strip to strip out spaces and trim the line.
    return [line.strip() for line in open(any_file, 'r')]

def get_commits(data):
    sep = 72*'-'
    commits = []
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip().split(' ')[0],
                'time': details[2].strip().split(' ')[1],
                'number_of_lines': int(details[3].strip().split(' ')[0])
            }
            change_file_end_index = data.index('', index + 1)
            commit['changed_path'] = data[index + 3 : change_file_end_index]
            commit['comment'] = data[change_file_end_index + 1 : 
                    change_file_end_index + 1 + commit['number_of_lines']]
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            index = len(data)
    return commits

def save_commits(commits, any_file):
    my_file = open(any_file, 'w')
    my_file.write("revision,author,date,time,number_of_lines,comment\n")
    for commit in commits:
        my_file.write(commit['revision'] + ',' + commit['author'] +
                ',' + commit['date'] + ',' + commit['time'] + ',' +
				str(commit['number_of_lines']) + ',' + ' '.join(commit['comment']) + '\n')
    my_file.close()

if __name__ == '__main__':
#    open the file - and read all of the lines.
    changes_file = 'changes.txt'
    data = read_file(changes_file)
    print (len(data))
    commits = get_commits(data)
    save_commits(commits, 'changes.csv')


# In[29]:


    df=pd.DataFrame(commits)


# In[30]:


    print(df.head())


# In[31]:


    print(df.columns)


# In[32]:


    df['date'] = pd.to_datetime(df['date'])
    df['time'] = pd.to_timedelta(df['time'])


# In[33]:


    name_lines=df.loc[:,['author','number_of_lines']]
    tot_lines = name_lines.groupby(['author']).sum()
    tot_lines.at['Dave','number_of_lines']


# In[34]:


    print(tot_lines)


# In[35]:


    tot_lines.plot(kind="bar")


# In[36]:


    #name_time=df.loc[:,['author','time']]
    #name_time.groupby(['author']).describe()




# In[37]:


    date_lines=df.loc[:,['date','number_of_lines']]
    tot_date=date_lines.groupby(['date']).sum()


# In[38]:


    print(tot_date.sort_values('number_of_lines', ascending=False).head())


# In[39]:


# Avarage number of realeases per day
    release_no=date_lines.groupby(['date']).count()
    print(release_no['number_of_lines'].mean())


# In[40]:


    print(df['number_of_lines'].mean())


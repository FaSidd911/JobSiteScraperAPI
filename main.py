import pandas as pd

datadf = pd.read_csv('data_dump.csv')
datadf['salary'] = datadf['salary'].map(lambda x: x.rstrip(' PA.').lstrip('aAbBcC'))
datadf['salary'] = datadf['salary'].str.replace(',','')
splitdata= datadf['salary'].str.split(' - ', expand = True)
splitdata = splitdata[splitdata[0].astype(str).str.isnumeric()]
splitdata = splitdata[splitdata[1].astype(str).str.isnumeric()]
datadf = pd.concat([datadf,splitdata], axis=1)
datadf.dropna(inplace=True)
datadf['avg'] = (datadf[0].astype(int) + datadf[1].astype(int))/2

def FetchJob(x):
    job = datadf[datadf['jobTitle'].str.contains(x, case = False)]
    mode  =job['avg'].mode()[0]
    median  =job['avg'].median()
    mean  =round(job['avg'].mean())
    count = len(job)
    max_sal = job['avg'].max()

    return {'Mean salary':mean,
             'Median Salary':median,
             'Mode Salary':mode,
             'Max salary offerede': max_sal,
             'No. Of Job Openings' :count}


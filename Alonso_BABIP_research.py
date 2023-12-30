import pandas as pd 
import plotly.express as px

data = pd.read_excel("season_end.xlsx")

data.head()

data.info()
data = data[data['AB'] > 200]
data = data[data['HR'] > 20]
data


def BABIP_calculation(data):
    ''' calculates an BABIP (power metric) for each hitter '''
    '''
    args: data = a dataframe that stores our data
    
    returns: data [BABIP] = a column that can be added to our dataframe with an ISO calculution
        
    '''
    data['BABIP'] = (data['H']- data['AVG'])/(data['AB'] - data['SO'] - data['HR']+ data['SF'])
    data['BABIP'].astype('float64')
    data['BABIP'] = data['BABIP'].apply(lambda x: round(x,3))
    return data['BABIP']
data['BABIP'] = BABIP(data)
data 


# In[43]:


def ISO_calculation(data):
    ''' calculates an ISO (power metric) for each hitter '''
    '''
    args: data = a dataframe that stores our data
    
    returns: data [ISO] = a column that can be added to our dataframe with an ISO calculution
        
    '''
    data['ISO'] = (data['SLG']- data['BA'])
    data['ISO'].astype('float64')
    data['ISO'] = data['ISO'].apply(lambda x: round(x,3))
    return data['ISO']
data['ISO'] = ISO_calculation(data)
data 



scatter_plot2 = px.scatter(data, x = data['HR'], y=data['BABIP'], color = 'Name', 
                          title= "2023 Scatter Plot of BABIP vs HR<br><sup> Min 20 HRs, 200 ABs</sup>")
scatter_plot2





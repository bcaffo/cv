## Old figure 1
temp = dat
temp = temp.assign(Count = 1)
temp = temp.rename(columns = {'total' : 'Citations'})

fig = px.bar(temp, x = 'Publication Year', 
                 y = 'Count',
                 color = 'Document Title',
                 hover_data = ['Publication Year', 'Document Title', 'Journal Title', 'Authors', 'Citations'])

fig = fig.update_layout({
    'plot_bgcolor' : 'rgba(0, 0, 0, 0)',
    'paper_bgcolor' : 'rgba(0, 0, 0, 0)'})

fig.update_layout(showlegend=False)

## Static image
#Image(fig.to_image(format="png", width=400, height=250, scale=2))

fig.show()


## Create a temporary copy of the dataset and work with that
temp = dat
temp = temp.rename(columns = {'total' : 'Citations'})
## Add one to citations for the scaling factor otherwise the points don't plot
temp = temp.assign(Citations1 = temp['Citations'] + 1) 
temp = temp.sort_values('Publication Year')

year = temp['Publication Year'].to_list()
Count = []
for i in range(len(year)):
    if i == 0:
        position = 0
    elif year[i] == year[i-1]:
        position += 1
    else :
        position = 0
    Count.append(position)
temp = temp.assign(Count = Count)


## Set the journals so that if they have 3 or fewer publications, it's just "other"
journals = dat['Journal Title'].value_counts().reset_index()
topJournals = journals['index'][journals['Journal Title'] > 3].unique()
notInTop = [j not in topJournals for j in temp['Journal Title']]
temp['Journal'] = temp['Journal Title']
temp.loc[notInTop, 'Journal'] = 'Other'



fig = px.scatter(temp, x = 'Publication Year', 
                 y = 'Count',
                 color = 'Journal',
                 size = 'Citations1',
                 hover_data = ['Publication Year', 'Document Title', 'Journal Title', 'Authors', 'Citations'])

fig = fig.update_layout({
    'plot_bgcolor' : 'rgba(0, 0, 0, 0)',
    'paper_bgcolor' : 'rgba(0, 0, 0, 0)'})

fig.update_traces(marker=dict(sizemin=2)),
#                              line=dict(width=2,
#                                        color='DarkSlateGrey'))#,
#                  selector=dict(mode='markers')
#                 )

#fig.update_layout(showlegend=False)

## Static image
#Image(fig.to_image(format="png", width=400, height=250, scale=2))

fig.show()
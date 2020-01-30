import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

df = pd.read_csv('https://gist.githubusercontent.com/aguileralorenzo/466a9459a42c2695858cc3e649e68cbe/raw/dec45a320fa5e25025ca3fb591a74dee0666b2d7/climate-change-excel-4-6-mb-', usecols=['name', 'group', 'year', 'value'])

df.head(3)
end_year = 2007
dff = (df[df['year'].eq(end_year)]
       .sort_values(by='value', ascending=True)
       .head(10))

ax.barh(dff['name'], dff['value'])
colors = dict(zip(
    ['Europe', 'Asie', 'Amerique Nord',
     'Amerique Latine', 'Océanie'],
    ['#00C2FF', '#aa0bff', '#F03a0a', '#e4FF00',
     '#aacc00', '#00bb5f']
))
group_lk = df.set_index('name')['group'].to_dict()


ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])

for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
    ax.text(value, i, name, ha='right')
    ax.text(value, i - .25, group_lk[name], ha='right')
    ax.text(value, i, value, ha='left')

ax.text(1, 0.4, end_year, transform=ax.transAxes, size=46, ha='right')

def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max() / 200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value - dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value - dx, i - .25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value + dx, i, f'{value:,.0f}', size=14, ha='left', va='center')

    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(0, 1.06, 'Emissions CO2 (KtCO2)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'Emissions totales de CO2 de 1990 à 2007',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(1, 0, 'Ynov Equipe 6', transform=ax.transAxes, ha='right',
            color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
    plt.box(False)

import matplotlib.animation as animation
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1990, 2007))
HTML(animator.to_jshtml())

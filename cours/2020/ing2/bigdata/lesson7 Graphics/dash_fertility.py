import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

START = 'Start'
STOP  = 'Stop'

def get_data():
    incomes = pd.read_excel('data/GDPpercapitaconstant2000US.xlsx', index_col=0).round()
    children = pd.read_excel('data/fertility.xlsx', index_col=0)
    population = pd.read_excel('data/population.xlsx', index_col=0).round()
    continent = pd.read_csv('data/countries_continent.csv', index_col=0)
    idx = (list(set(incomes.index) & set(children.index) 
        & set(population.index) & set(continent.index)))
    idx.sort()
    df = pd.concat({'incomes': incomes.loc[idx, '1960':'2010'],
            'population': population.loc[idx, '1960':'2010'],
            'children': children.loc[idx, '1960':'2010']}, axis='columns')
    df = df.swaplevel(0,1,axis='columns').sort_index(axis=1)
    continent = continent.loc[idx,:] 
    return df, continent

continent_colors = {'Asia':'yellow', 'Europe':'green', 'Africa':'brown',
                    'Oceania':'blue', 'Americas':'red'}
df, continent = get_data()
years = df.columns.levels[0]

app = dash.Dash()
app.layout = html.Div(children=[
    html.H3(children='World Stats'),

    html.Div('Move the mouse over a bubble to get information about the country'), 

    html.Div([
        html.Div([ dcc.Graph(id='main-graph'), ], style={'width':'90%', }),

        html.Div([
            dcc.Checklist(
                id='crossfilter-which-continent',
                options=[{'label': i, 'value': i} for i in sorted(continent_colors.keys())],
                values=sorted(continent_colors.keys()),
                labelStyle={'display':'block'},
            ),
            html.P(id='placeholder'), # used when a callback should not act on another component
            html.Div('X scale'),
            dcc.RadioItems(
                id='crossfilter-xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Log',
                labelStyle={'display':'block'},
            )
        ], style={'width': '10%', 'float':'right'}),
    ], style={
        'padding': '0px 50px', 
        'display':'flex',
        'justifyContent':'center'
    }),

    html.Div([
            dcc.Slider(
                id='crossfilter-year-slider',
                min=years[0],
                max=years[-1],
                value=years[0],
                step = 1,
                marks={str(year): str(year) for year in years[::5]},
            ),
            dcc.Interval(
                id='auto-stepper',
                interval=60*60*1000, # in milliseconds
                n_intervals=0    # change by itself every interval
            ),
            html.Button(
                STOP,   # for some reason loading the page makes a click!
                id='button-start-stop', 
                style={'margin-left':'30'},
            ),
    ], style={
        'padding': '0px 50px', 
        'display':'flex',
        'justifyContent':'center'
    }),

    html.P(),
    html.Div(id='div-country'),

    html.Div([
        dcc.Graph(id='x-time-series', 
                  style={'width':'33%', 'display':'inline-block'}),
        dcc.Graph(id='y-time-series',
                  style={'width':'33%', 'display':'inline-block', 'padding-left': '0.5%'}),
        dcc.Graph(id='pop-time-series',
                  style={'width':'33%', 'display':'inline-block', 'padding-left': '0.5%'}),
    ], style={ 'display':'flex', 'justifyContent':'center', }),

], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(240, 240, 240)',
         'padding': '10px 50px 10px 50px',
         }
)

def traces(df, which_continent, year):
    res = []
    for c in which_continent:
        dfc = df[year][continent.region == c]
        res.append(
            go.Scatter(
                 x = dfc['incomes'],
                 y = dfc['children'],
                 mode = 'markers',
                 marker = dict( size = np.sqrt(dfc['population']/1E5),
                                color = continent_colors[c],
                              ),
                 text = dfc.index)
        )
    return res

@app.callback(
    dash.dependencies.Output('main-graph', 'figure'),
    [ dash.dependencies.Input('crossfilter-which-continent', 'values'),
      dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
      dash.dependencies.Input('crossfilter-year-slider', 'value')])
def update_graph(which_continent, xaxis_type, year):
    return {
        'data': traces(df, which_continent, year),
        'layout': go.Layout(
            xaxis = dict(title='GDP per Capita (US $)',
                         type= 'linear' if xaxis_type == 'Linear' else 'log',
                         range=(0,55000) if xaxis_type == 'Linear' 
                                         else (np.log10(50), np.log10(55000)) 
                        ),
            yaxis = dict(title='Child per woman', range=(0,9)),
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest',
            showlegend=False,
        )
    }


def create_time_series(country, what, axis_type, title):
    return {
        'data': [go.Scatter(
            x=years,
            y=df.loc[country, (years, what)],
            mode='lines+markers',
        )],
        'layout': {
            'height': 225,
            'margin': {'l': 50, 'b': 20, 'r': 10, 't': 20},
            'yaxis': {'title':title,
                      'type': 'linear' if axis_type == 'Linear' else 'log'},
            'xaxis': {'showgrid': False}
        }
    }


def get_country(hoverData):
    if hoverData == None:  # init value
        return df.index.values[np.random.randint(len(df))]
    return hoverData['points'][0]['text']

@app.callback(
    dash.dependencies.Output('div-country', 'children'),
    [dash.dependencies.Input('main-graph', 'hoverData')])
def country_chosen(hoverData):
    return get_country(hoverData)

# graph incomes vs years
@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('main-graph', 'hoverData'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_type):
    country = get_country(hoverData)
    return create_time_series(country, 'incomes', xaxis_type, 'GDP per Capita (US $)')

# graph children vs years
@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('main-graph', 'hoverData'),])
def update_x_timeseries(hoverData):
    country = get_country(hoverData)
    return create_time_series(country, 'children', 'linear', 'Child per woman')

# graph population vs years
@app.callback(
    dash.dependencies.Output('pop-time-series', 'figure'),
    [dash.dependencies.Input('main-graph', 'hoverData'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
def update_pop_timeseries(hoverData, xaxis_type):
    country = get_country(hoverData)
    return create_time_series(country, 'population', xaxis_type, 'Population')

# start and stop the movie
@app.callback(
    dash.dependencies.Output('button-start-stop', 'children'),
    [dash.dependencies.Input('button-start-stop', 'n_clicks')],
    [dash.dependencies.State('button-start-stop', 'children')])
def button_on_click(n_clicks, text):
    if text == START:
        return STOP
    else:
        return START

# this one is triggered by the previous one because we cannot have 2 outputs
# in the same callback
@app.callback(
    dash.dependencies.Output('auto-stepper', 'interval'),
    [dash.dependencies.Input('button-start-stop', 'children')])
def button_on_click(text):
    if text == START:    # then it means we are stopped
        return 60*60*1000  # just one event an hour
    else:
        return 0.5*1000 

# see if it should move the slider for simulating a movie
@app.callback(
    dash.dependencies.Output('crossfilter-year-slider', 'value'),
    [dash.dependencies.Input('auto-stepper', 'n_intervals')],
    [dash.dependencies.State('crossfilter-year-slider', 'value'),
     dash.dependencies.State('button-start-stop', 'children')]) 
def on_interval(n_intervals, year, text):
    if text == STOP:  # then we are running
        if year == years[-1]:
            return years[0]
        else:
            return year + 1
    else:
        return year  # nothing changes


if __name__ == '__main__':
    app.run_server()

import dash, datetime, math
import pandas_datareader.data as web
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go

#1a1c23
#b2b2b2
#22252b
#b5b5b5
#1E1E1E
#d8d8d8

start_date = datetime.datetime(2000, 1, 1)
end_date = datetime.datetime.today()

df = pd.read_csv('stock_name.csv')

# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_scripts = external_scripts, external_stylesheets = external_stylesheets)

app.config.suppress_callback_exceptions = True

app.title = "STOCK APP"

colors = {
   'background': '#1E1E1E',
   'text': '#FDFEFE'
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
                html.Div(
                    style={'padding-right':'20px','width':'10','float':'right','font-size':'20px'},
                    children=[
                        dcc.Link('OFFLINE', href='/page-2'),
                        html.Div(style={'padding-right':'20px','display':'inline-block'}),
                        dcc.Link('ONLINE', href='/page-1'),
                    ]),
                html.Div([
                    html.Div(
                        style = {'backgroundColor': '#1a1c23', 'max-width': '100%'},
                        className = 'app-header',
                        children=[
                            html.Div('S&P 500 STOCK ANALYSIS', className = 'app-header--title'),
                        ]),
                    html.Div(
                        className='card1',
                        children = [
                            html.Div(
                                className="slidingbackground",
                                children=[
                                    html.Img(src='//logo.clearbit.com/google.com',style={'padding':'30px','padding-top':'70px'}),
                                    html.Img(src='//logo.clearbit.com/microsoft.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/facebook.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/amazon.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/apple.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/walmart.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/intel.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/netflix.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/jnj.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/ebay.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/nike.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/starbucks.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/boeing.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/accenture.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/abbvie.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/abiomed.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/activision.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/aes-corp.com',style={'padding':'30px','padding-top':'80px'}),
                                    html.Img(src='//logo.clearbit.com/abbott.com',style={'padding':'30px','padding-top':'80px'}),

                                   html.Img(src='//logo.clearbit.com/photoshop.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/advanceautoparts.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/advancedmd.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/agilent.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/alexion.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/alliantenergy.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/apachecorp.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/autodesk.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/baxter.com',style={'padding':'30px','padding-top':'80px'}),

                                   html.Img(src='//logo.clearbit.com/blackrock.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/brown-forman.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/campbells.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='https://logo.clearbit.com/carmax.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/cbs.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/cisco.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/coca-colacompany.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/cognizant.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/dteenergy.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/ea.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/equinix.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/ford.com',style={'padding':'30px','padding-top':'80px'}),

                                   html.Img(src='//logo.clearbit.com/fox.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/generalmills.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/harley-davidson.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/hersheys.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/idexcorp.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/jpmorganchase.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/nvidia.com',style={'padding':'30px','padding-top':'80px'}),

                                   html.Img(src='//logo.clearbit.com/borgwarner.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/bostonproperties.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/schwab.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/chevron.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/cigna.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/cimarex.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/thecloroxcompany.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/comcast.co',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/conocophillips.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/corteva.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/drhorton.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/devonenergy.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/gd.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/hasbro.com',style={'padding':'30px','padding-top':'80px'}),

                                   html.Img(src='//logo.clearbit.com/hormel.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/idexcorp.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/illumina.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/mcdonalds.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/mckesson.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/microchip.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/mondelezinternational.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/nrg.com',style={'padding':'30px','padding-top':'80px'}),

                                   html.Img(src='//logo.clearbit.com/xylem.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/kimberly-clark.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/kraftheinzcompany.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/xerox.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/xilinx.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/zoetis.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/zionsbancorp.com',style={'padding':'30px','padding-top':'80px'}),
                                   html.Img(src='//logo.clearbit.com/westerndigital.com',style={'padding':'30px','padding-top':'80px'}),
                               ]
                            )
                        ]
                    ),
                ]),
            ])

##################################ONLINE#######################################

page_1_layout = html.Div(
            style   =   {'overflow-x':'hidden','overflow-y':'hidden' ,'background-color': '#1a1c23'},
            children=[
            html.Div(
                style={'padding-right':'20px','width':'10','float':'right','font-size':'15px'},
                children=[
                    dcc.Link('OFFLINE', href='/page-2'),
                    html.Div(style={'padding-right':'20px','display':'inline-block'}),
                    dcc.Link('HOME', href='/'),
                ]
            ),

            html.Div(
                style = {'backgroundColor': '#1a1c23', 'max-width': '100%'},

                children = [
                    html.H1('S&P 500 STOCK ANALYSIS [ONLINE]', style = {'color': '#FDFEFE', 'font-size':'32px',}),

                    html.Label('COMPANY', style = {'color': '#FDFEFE','float': 'left','font-size':'20px',}),

                    html.Label('OTHER S&P 500 OPTIONS', style = {'color': '#FDFEFE', 'font-size':'20px', 'padding-left':'1370px '}),

                    html.Br(),
                    html.Div([
                        dcc.Dropdown(
                            id = 'stock-ticker-input',
                            options = [{'label': i[0], 'value': i[1]} for i in zip(df['Company'].unique(), df['Symbol'].unique())],
                            placeholder = 'Enter TICKER',
                            style = {'backgroundColor': '#1E1E1E', 'font-size':'15px', 'color': 'black'}
                        )
                    ],style={'width': '40%', 'padding': '5px, 10px, 12px', 'display': 'inline-block', 'backgroundColor': '#1a1c23', 'font-size':'15px' }),

                    html.Div([
                        html.Button(children = 'S&P 500 COMPARISION', id = 'button3', type = 'submit', n_clicks = 0)
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right','text-color':'#FDFEFE' }),

                    html.Div([
                        html.Button(children = 'S&P 500 CORRELATION', id = 'button1', type = 'submit')
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right','text-color':'white' }),

                    html.Div([
                        html.Button(children = 'S&P 500 SECTORS', id = 'button2', type = 'submit', n_clicks = 0)
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right','text-color':'#FDFEFE' }),

                    html.Div([
                        html.Button(children = 'S&P 500', id = 'button4', type = 'submit', n_clicks = 0)
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right','text-color':'#FDFEFE' }),

                    html.Br(),
                    html.Div([
                        html.Button(children = 'RESET', id = 'reset_button', type = 'submit', n_clicks = 0)
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'left','text-color':'#FDFEFE' }),

                    html.Br(),
                    html.Div(id = 'ticker-input'),
                    html.Div([
                            dcc.Dropdown(
                                id = 'ticker-input-compare',
                            )
                    ],style={'visibility':'hidden'}),
                    html.Br(),
                    html.Div(id = 'graph1'),
                    html.Div(id = 'graph2'),
                    html.Div(id = 'graph3'),
                    html.Div(id = 'graph4'),
                    html.Div(id = 'heatmap'),
                    html.Div(id = 'pie-chart'),
                    html.Div(id = 'snp500'),
                ]
        )
    ])

##################################OFFLINE#######################################

page_2_layout = html.Div(
            style = {'overflow-x':'hidden','overflow-y':'hidden' ,'background-color': '#1a1c23'},
            children =[
            html.Div(
                style={'padding-right':'20px','width':'10','float':'right','font-size':'15px'},
                children=[
                    dcc.Link('ONLINE', href='/page-1'),
                    html.Div(style={'padding-right':'20px','display':'inline-block'}),
                    dcc.Link('HOME', href='/'),
                ]
            ),

            html.Div(
                style = {'backgroundColor': '#1a1c23', 'max-width': '100%'},

                children = [
                    html.H1('S&P 500 STOCK ANALYSIS [OFFLINE]', style = {'color': '#FDFEFE', 'font-size':'32px',}),

                    html.Label('COMPANY', style = {'color': '#FDFEFE','float': 'left','font-size':'20px',}),

                    html.Label('OTHER S&P 500 OPTIONS', style = {'color': '#FDFEFE', 'font-size':'20px', 'padding-left':'1370px '}),

                    html.Br(),
                    html.Div([
                        dcc.Dropdown(
                            id = 'stock-ticker-input_off',
                            options = [{'label': i[0], 'value': i[1]} for i in zip(df['Company'].unique(), df['Symbol'].unique())],
                            placeholder = 'Enter TICKER',
                            style = {'backgroundColor': '#1E1E1E', 'font-size':'15px', 'color': 'black'}
                        )
                    ],style={'width': '40%', 'padding': '5px, 10px, 12px', 'display': 'inline-block', 'backgroundColor': '#1a1c23', 'font-size':'15px' }),

                    html.Div([
                        html.Button(children = 'S&P 500 COMPARISION', id = 'button3_off', type = 'submit')
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right', 'title':'Correlation b/w S&P 500','text-color':'#FDFEFE' }),

                    html.Div([
                        html.Button(children = 'S&P 500 CORRELATION', id = 'button1_off', type = 'submit')
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right', 'title':'Correlation b/w S&P 500','text-color':'white' }),

                    html.Div([
                        html.Button(children = 'S&P 500 SECTORS', id = 'button2_off', type = 'submit')
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right', 'title':'Correlation b/w S&P 500','text-color':'#FDFEFE' }),

                    html.Div([
                        html.Button(children = 'S&P 500', id = 'button4_off', type = 'submit', n_clicks = 0)
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'right','text-color':'#FDFEFE' }),

                    html.Br(),
                    html.Div([
                        html.Button(children = 'RESET', id = 'reset_button_off', type = 'submit', n_clicks = 0)
                    ], style = {'padding-right': '1px', 'display': 'inline-block', 'backgroundColor': 'black', 'font-size':'12px', 'float': 'left','text-color':'#FDFEFE' }),

                    html.Br(),
                    html.Div(id = 'ticker-input_off'),
                    html.Div([
                            dcc.Dropdown(
                                id = 'ticker-input-compare_off',
                            )
                    ],style={'visibility':'hidden'}),

                    html.Br(),
                    html.Div(id = 'graph5'),
                    html.Div(id = 'graph6'),
                    html.Div(id = 'graph7'),
                    html.Div(id = 'heatmap_off'),
                    html.Div(id = 'pie-chart_off'),
                    html.Div(id = 'snp500_off'),
                ]
        )
    ])

#################################PAGE CALLBACKS################################
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/':
        return index_page
    else:
        return '404 URL NOT FOUND!!'

#######################################################################

############################ONLINE CALLBACKS###########################

#######################################################################
@app.callback(
    Output('graph1','children'),
    [Input('stock-ticker-input', 'value')])

def update_graph(tickers):
    if tickers is None:
        return None
    else:
        dff = web.DataReader(tickers, 'yahoo', start_date, end_date)
        dff.reset_index(inplace=True)
        dff.set_index("Date", inplace=True)

        forecast_col = 'Adj Close'
        dff.fillna(-99999, inplace = True)
        forecast_out = int(math.ceil(0.01 * len(dff)))

        dff['Prediction'] = dff[forecast_col].shift(-forecast_out)

        X = np.array(dff.drop(['Prediction'],1))
        X = preprocessing.scale(X)
        X_predict = X[-forecast_out:]
        X = X[:-forecast_out]

        y_close = dff['Adj Close']
        dff.dropna(inplace = True)
        y = np.array(dff['Prediction'])

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

        clf = svm.SVR(kernel = 'poly')
        clf.fit(X_train, y_train)
        accuracy = clf.score(X_test, y_test)
        forecast_set = clf.predict(X_predict)
        print(f'Accuracy: {accuracy},\n\nNo. of Days in future: {forecast_out}')

        last_date = y_close.index[-1]
        forecast_date = last_date + datetime.timedelta(days = 1)
        forecast_index = []
        for value in forecast_set:
            if forecast_date.weekday() < 5:
                forecast_index.append(forecast_date)
            else :
                forecast_date += datetime.timedelta(days = (8 - forecast_date.isoweekday()))
                forecast_index.append(forecast_date)
            forecast_date += datetime.timedelta(days = 1)
        forecast_series = pd.Series(forecast_set, index = forecast_index)
        #print(forecast_series)

        trace1 = go.Scatter(
                        x = dff.index,
                        y = y_close,
                        name = 'Current')

        trace2 = go.Scatter(
                        x = forecast_index,
                        y = forecast_series,
                        name = 'Prediction')

        data = [trace1, trace2]

        layout = dict(
                title = tickers,
                xaxis=dict(
                    rangeselector=dict(
                        buttons=[
                            dict(count = 1,
                                    label =" 1m",
                                    step = "month",
                                    stepmode = "backward"),
                            dict(count = 6,
                                    label = "6m",
                                    step = "month",
                                    stepmode = "backward"),
                            dict(count = 1,
                                    label = "YTD",
                                    step = "year",
                                    stepmode = "todate"),
                            dict(count = 1,
                                    label = "1y",
                                    step = "year",
                                    stepmode = "backward"),
                            dict(step = "all")
                        ]
                    ),
                    rangeslider = dict(visible=True),
                    title = 'Date',
                    showticklabels = True,
                    fixedrange = False
                ),
                yaxis=dict(
                    title = 'Price',
                    showticklabels=True,
                    fixedrange=False
                ),
                showgrid=False,
                plot_bgcolor = '#1a1c23',
                paper_bgcolor = '#1a1c23',
                font = {'color':'#7FDBFF'}
            )

        return html.Div([
                    html.Div([
                        dcc.Graph(
                            id = 'graph-plot',
                            figure={
                                'data': data,
                                'layout': layout,
                            }
                        ),
                    ],style = {'padding': '2px','width': '90%', 'height':'auto'})
                ])

@app.callback(
    Output('graph2','children'),
    [Input('stock-ticker-input', 'value')])

def update_figure(tickers):
    if tickers is None:
        return None
    else:
        dff = web.DataReader(tickers, 'yahoo', start_date, end_date)
        dff.reset_index(inplace=True)
        dff.set_index("Date", inplace=True)

        trace1 = go.Candlestick(
                    x = dff.index,
                    open = dff['Open'],
                    close = dff['Close'],
                    high = dff['High'],
                    low = dff['Low'],
                    increasing = {'line': {'color':'#380aab'}},
                    decreasing = {'line': {'color':'#03fc90'}})

        trace_vol = go.Bar(
                        x = dff.index,
                        y = dff['Volume'],
                        name = 'Volume'
                    )

        return html.Div([
                    html.Div([
                        dcc.Graph(
                            figure = go.Figure(
                                data = [trace1],
                                layout = go.Layout(
                                    xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    yaxis=dict(title = 'Price', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    plot_bgcolor='#1a1c23',
                                    paper_bgcolor='#1a1c23',
                                    font= {'color':'#7FDBFF',}
                                )
                            )
                        )
                    ],style = {'display': 'inline-block', 'width': '50%', 'height':'auto','float':'left'}),

                html.Div([
                        dcc.Graph(
                            figure = go.Figure(
                                data = [trace_vol],
                                layout = go.Layout(
                                    xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    yaxis=dict(title = 'Volume', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    hovermode='closest',
                                    plot_bgcolor='#1a1c23',
                                    paper_bgcolor='#1a1c23',
                                    font= {'color':'#7FDBFF',}
                                )
                            )
                        )
                ],style = {'display': 'inline-block', 'width': '50%', 'height':'auto','float':'left'}),
            ])

@app.callback(
    Output('graph3','children'),
    [Input('stock-ticker-input', 'value')])

def ohlc(tickers):
    today_date = datetime.datetime.today()
    tomorrow = today_date + datetime.timedelta(days = 1)
    yesterday = today_date - datetime.timedelta(days = 30)

    if tickers is None:
        return None
    else:
        dff = web.DataReader(tickers, 'yahoo', yesterday, today_date)
        dff.reset_index(inplace=True)
        dff.set_index('Date', inplace=True)

        trace_open = go.Scatter(
                        x = dff.index,
                        y = dff['Open'],
                        name = 'Open'
                    )
        trace_high = go.Bar(
                        x = dff.index,
                        y = dff['High'],
                        name = 'High',
                    )
        trace_low = go.Bar(
                        x = dff.index,
                        y = dff['Low'],
                        name = 'Low'
                    )
        trace_close = go.Scatter(
                        x = dff.index,
                        y = dff['Close'],
                        name = 'Close',
                    )

        return html.Div([
                dcc.Graph(
                    figure = go.Figure(
                        data = [trace_open, trace_high, trace_low, trace_close],
                        layout = go.Layout(
                            xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                            yaxis=dict(title = 'O-H-L-C', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                            hovermode='closest',
                            plot_bgcolor='#1a1c23',
                            paper_bgcolor='#1a1c23',
                            font= {'color':'#7FDBFF',}
                        )
                    )
                )
        ],style = {'display': 'inline-block', 'width': '50%', 'height':'auto'})
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('ticker-input', 'children'),
    [Input('button3', 'n_clicks')])

def show_and_use_dropdown(clicked):
        if clicked is None:
            clicked = 0
        if clicked>0:
            return html.Div([
                    dcc.Dropdown(
                        id = 'ticker-input-compare',
                        options = [{'label': i[0], 'value': i[1]} for i in zip(df['Company'].unique(), df['Symbol'].unique())],
                        placeholder = 'Enter Company TICKERS',
                        multi = True,
                        style = {'backgroundColor': '#1E1E1E', 'font-size':'15px'}
                    )
            ],style={'width': '20%', 'display': 'block', 'float':'right', 'backgroundColor': '#1a1c23', 'font-size':'15px'})

@app.callback(
    Output('button3', 'n_clicks'),
    [Input('reset_button','n_clicks')])

def reset(reset):
    return 0
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('graph4','children'),
    [Input('ticker-input-compare', 'value')])

def stock_comparision(tickers):
    if tickers is None:
        return None
    else:
        tick_list = []
        for tick in tickers:
            #tick_list.append(tick)
            dff = web.DataReader(tick, 'yahoo', start_date, end_date)
            dff.reset_index(inplace=True)
            dff.set_index("Date", inplace=True)

            trace = go.Scatter(
                    x = dff.index,
                    y = dff['Adj Close'],
                    name = tick
                    )
            tick_list.append(trace)
        data = tick_list
        layout = go.Layout(
                    title = 'Stock Comparision',
                    xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                    yaxis=dict(title = 'Price', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                    plot_bgcolor='#1a1c23',
                    paper_bgcolor='#1a1c23',
                    font= {'color':'#7FDBFF',}
                )

        return html.Div([
                    dcc.Graph(
                        figure = {
                            'data': data,
                            'layout': layout,
                        }
                    )
                ],style = {'display': 'inline-block', 'width': '70%', 'height':'auto','float':'center'})
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('heatmap','children'),
    [Input('button1', 'n_clicks')])

def corr_graph(clicked):
    if clicked is None:
        clicked = 0

    if clicked>0:
        all_stock_df = pd.read_csv('stock_corr_data.csv')
        close_val_per_day = pd.DataFrame()

        for name, group in all_stock_df.groupby('Name'):
            if close_val_per_day.empty:
                close_val_per_day = group.set_index('Date')[ ['Close'] ].rename(columns = {'Close' : name})
            else:
                close_val_per_day = close_val_per_day.join(group.set_index('Date')[ ['Close'] ].rename(columns = {'Close' : name}))

        close_val_per_day_corr = close_val_per_day.corr()

        labels = [c[:3] for c in close_val_per_day_corr.columns]
        return html.Div([
                dcc.Graph(
                    id = 'heatmap-graph',
                    figure = {
                        'data': [go.Heatmap(
                                    x = labels,
                                    y = labels,
                                    z = close_val_per_day_corr,
                                    colorscale = 'Viridis'
                                )],
                        'layout': go.Layout(
                                    xaxis = dict(title = 'COMPANIES'),
                                    yaxis = dict(title = 'COMPANIES'),
                                    plot_bgcolor = '#1a1c23',
                                    paper_bgcolor = '#1a1c23',
                                    font = {'color':'#7FDBFF',}
                                )
                    }
                )
        ], style = {'width': '1000px', 'height':'10000px', 'display': 'inline-block', 'float': 'left'} )

@app.callback(
    Output('button1', 'n_clicks'),
    [Input('reset_button','n_clicks')])

def reset(reset):
    return 0
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('pie-chart', 'children'),
    [Input('button2','n_clicks')])

def pie_graph(clicked):
    if clicked is None:
        clicked = 0

    if clicked>0:
        df1=pd.read_csv('sector.csv')
        df1.set_index('Symbol',inplace=True)

        Industrials=df1[df1['Sector']=='Industrials'].count()
        ind=Industrials['Sector']

        Health=df1[df1['Sector']=='Health Care'].count()
        h=Health['Sector']

        It=df1[df1['Sector']=='Information Technology'].count()
        i=It['Sector']

        Cd=df1[df1['Sector']=='Consumer Discretionary'].count()
        c=Cd['Sector']

        uti=df1[df1['Sector']=='Utilities'].count()
        u=uti['Sector']

        Fi=df1[df1['Sector']=='Financials'].count()
        f=Fi['Sector']

        Mt=df1[df1['Sector']=='Materials'].count()
        m=Mt['Sector']

        Re=df1[df1['Sector']=='Real Estate'].count()
        r=Re['Sector']

        cs=df1[df1['Sector']=='Consumer Staples'].count()
        co=cs['Sector']

        e=df1[df1['Sector']=='Energy'].count()
        en=e['Sector']

        tele=df1[df1['Sector']=='Telecommunication Services'].count()
        t=tele['Sector']

        li=[ind,h,i,c,u,f,m,r,co,en,t]
        le=['Industrials','Health Care','Information Technology','Consumer Discretionary','Utilities','Financials','Materials'
              ,'Real Estate','Consumer Staples','Energy','Telecommunication Services']

        fig = go.Figure(data=[go.Pie(labels=le, values=li, hole=.3)])

        return html.Div([
                        html.Div([
                            dcc.Graph(

                               figure={
                                        'data': [{
                                            'hole': 0.5,
                                            'labels': [
                                                        'Industrials',
                                                        'Health Care',
                                                        'Information Technology',
                                                        'Consumer Discretionary', 'Utilities', 'Financials', 'Materials',
                                                        'Real Estate',
                                                        'Consumer Staples',
                                                        'Energy',
                                                        'Telecommunication',
                                                        ],
                                             'type': 'pie',
                                             'values': [
                                            ind, h, i, c, u, f, m, r, co, en, t
                                                       ]}
                                        ],
                                         'layout': {
                                            'direction': 'clockwise',
                                            ''
                                            'title': 'S & P 500 sectors',
                                            'pull': ['1', '0', '0', '0', '1'],
                                            'plot_bgcolor':'#1a1c23',
                                            'paper_bgcolor':'#1a1c23',
                                            'font': {'color':'#7FDBFF'}
                                   }
                        })],style = {'width': '700px', 'height':'700px','text-align':'center', 'text-color': '#FDFEFE', 'display': 'inline-block'}),
                ])

@app.callback(
    Output('button2', 'n_clicks'),
    [Input('reset_button','n_clicks')])

def reset(reset):
    return 0
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('snp500', 'children'),
    [Input('button4','n_clicks')])

def combine_graph(clicked):
    if clicked is None:
        clicked = 0

    if clicked > 0:
        snp_df = pd.read_csv('snp500.csv')
        snp_df.reset_index(inplace=True)
        snp_df.set_index('Date', inplace=True)

        trace_close = go.Scatter(
                        x = snp_df.index,
                        y = snp_df['Adj Close'],
                        name = 'S&P 500 Close'
                    )

        trace_close_100ma = go.Scatter(
                            x = snp_df.index,
                            y = snp_df['Adj Close'].rolling(100).mean(),
                            name = '100 Days Moving Average'
                        )

        trace_close_200ma = go.Scatter(
                            x = snp_df.index,
                            y = snp_df['Adj Close'].rolling(200).mean(),
                            name = '200 Days Moving Average'
                        )

        trace_close_300ma = go.Scatter(
                            x = snp_df.index,
                            y = snp_df['Adj Close'].rolling(300).mean(),
                            name = '300 Days Moving Average'
                        )

        return html.Div([
                        html.Div([
                            dcc.Graph(
                                figure = go.Figure(
                                    data = [trace_close, trace_close_100ma, trace_close_200ma, trace_close_300ma],
                                    layout = go.Layout(
                                        xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                        yaxis=dict(title = 'Adj Close', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                        plot_bgcolor='#1a1c23',
                                        paper_bgcolor='#1a1c23',
                                        font= {'color':'#7FDBFF',}
                                    )
                                )
                            )
                    ],style = {'display': 'inline-block', 'width': '80%', 'height':'auto','float':'left'}),
            ])

@app.callback(
    Output('button4', 'n_clicks'),
    [Input('reset_button','n_clicks')])

def reset(reset):
    return 0
#######################################################################

############################OFFLINE CALLBACKS##########################

#######################################################################
@app.callback(
    Output('graph5','children'),
    [Input('stock-ticker-input_off', 'value')])

def update_graph(tickers):
    if tickers is None:
        return None
    else:
        df = pd.read_csv('sp500.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index("Date", inplace=True)

        data = df.copy()[df['Symbol'] == tickers]       #.copy(): to avoid getting # WARNINGs

        #-------------------FEATURES------------------------
        data['HL_PCT'] = (data['High'] - data['Close'])/data['Close'] * 100.0
        data['PCT_Change'] = (data['Close'] - data['Open'])/data['Open'] * 100.0
        data = data[['Close','HL_PCT','PCT_Change','Volume',]]
        #print('TABLE: ')
        #print(data.tail(50))
        #print('\n')
        #-------------------LABEL------------------------
        forecast_col = 'Close'
        data.fillna(-99999, inplace = True)
        forecast_out = int(math.ceil(0.02 * len(data))) # rounding up the decimal val
                                                        # predicting 1% of the dataframe
        #print(forecast_out)                            # no. of days in the future
        data['Prediction'] = data[forecast_col].shift(-forecast_out)


        X = np.array(data.drop(['Prediction'],1))       #FEATURES
        X = preprocessing.scale(X)
        X_predict = X[-forecast_out:]
        X = X[:-forecast_out]

        y_close = data['Close']
        data.dropna(inplace = True)

        y = np.array(data['Prediction'])                #LABELS

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2) # testing over 20% of data

        clf = svm.SVR(kernel = 'linear')             # n_jobs = -1 -> threading; default = 1
        clf.fit(X_train, y_train)
        accuracy = clf.score(X_test, y_test)
        forecast_set = clf.predict(X_predict)
        print(f'Accuracy: {accuracy},\n\nNo. of Days in future: {forecast_out}')

        last_date = y_close.index[-1]
        forecast_date = last_date + datetime.timedelta(days = 1)
        forecast_index = []
        for value in forecast_set:
            if forecast_date.weekday() < 5:
                forecast_index.append(forecast_date)
            else :
                forecast_date += datetime.timedelta(days = (8 - forecast_date.isoweekday()))
                forecast_index.append(forecast_date)
            forecast_date += datetime.timedelta(days = 1)
        forecast_series = pd.Series(forecast_set, index = forecast_index)
        #print(forecast_series)

        trace1 = go.Scatter(
                        x = data.index,
                        y = y_close,
                        name = 'Current')

        trace2 = go.Scatter(
                        x = forecast_index,
                        y = forecast_series,
                        name = 'Prediction')

        data = [trace1, trace2]

        layout = dict(
                title = tickers,
                xaxis=dict(
                    rangeselector=dict(
                        buttons=[
                            dict(count = 1,
                                    label =" 1m",
                                    step = "month",
                                    stepmode = "backward"),
                            dict(count = 6,
                                    label = "6m",
                                    step = "month",
                                    stepmode = "backward"),
                            dict(count = 1,
                                    label = "YTD",
                                    step = "year",
                                    stepmode = "todate"),
                            dict(count = 1,
                                    label = "1y",
                                    step = "year",
                                    stepmode = "backward"),
                            dict(step = "all")
                        ]
                    ),
                    rangeslider = dict(visible=True),
                    title = 'Date',
                    showticklabels = True,
                    fixedrange = False
                ),
                yaxis=dict(
                    title = 'Price',
                    showticklabels=True,
                    fixedrange=False
                ),
                showgrid=False,
                plot_bgcolor = '#1a1c23',
                paper_bgcolor = '#1a1c23',
                font = {'color':'#7FDBFF'}
            )

        return html.Div([
                    html.Div([
                        dcc.Graph(
                            id = 'graph-plot',
                            figure={
                                'data': data,
                                'layout': layout,
                            }
                        )
                    ],style = {'padding': '5px','width': '90%', 'height':'auto'})
                ])

@app.callback(
    Output('graph6','children'),
    [Input('stock-ticker-input_off', 'value')])

def update_figure(tickers):
    if tickers is None:
        return None
    else:
        df = pd.read_csv('sp500.csv')
        df.reset_index(inplace=True)
        df.set_index("Date", inplace=True)

        dff = df.copy()[df['Symbol'] == tickers]

        trace1 = go.Candlestick(
                    x = dff.index,
                    open = dff['Open'],
                    close = dff['Close'],
                    high = dff['High'],
                    low = dff['Low'],
                    increasing = {'line': {'color':'#380aab'}},
                    decreasing = {'line': {'color':'#03fc90'}})

        trace_vol = go.Bar(
                        x = dff.index,
                        y = dff['Volume'],
                        name = 'Volume'
                    )


        return html.Div([
                    html.Div([
                        dcc.Graph(
                            figure = go.Figure(
                                data = [trace1],
                                layout = go.Layout(
                                    xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    yaxis=dict(title = 'Price', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    plot_bgcolor='#1a1c23',
                                    paper_bgcolor='#1a1c23',
                                    font= {'color':'#7FDBFF',}
                                )
                            )
                        )
                    ],style = {'display': 'inline-block', 'width': '50%', 'height':'auto','float':'left'}),

                html.Div([
                        dcc.Graph(
                            figure = go.Figure(
                                data = [trace_vol],
                                layout = go.Layout(
                                    xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    yaxis=dict(title = 'Volume', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                    hovermode='closest',
                                    plot_bgcolor='#1a1c23',
                                    paper_bgcolor='#1a1c23',
                                    font= {'color':'#7FDBFF',}
                                )
                            )
                        )
                ],style = {'display': 'inline-block', 'width': '50%', 'height':'auto','float':'left'}),
            ])

@app.callback(
    Output('ticker-input_off', 'children'),
    [Input('button3_off', 'n_clicks')])

def show_and_use_dropdown(clicked):
        if clicked is None:
            clicked = 0
        if clicked > 0:
            return html.Div([
                    dcc.Dropdown(
                        id = 'ticker-input-compare_off',
                        options = [{'label': i[0], 'value': i[1]} for i in zip(df['Company'].unique(), df['Symbol'].unique())],
                        placeholder = 'Enter Company TICKERS',
                        multi = True,
                        style = {'backgroundColor': '#1E1E1E', 'font-size':'15px'}
                    )
            ],style={'width': '20%', 'display': 'block', 'float':'right', 'backgroundColor': '#1a1c23', 'font-size':'15px'})

@app.callback(
    Output('button3_off', 'n_clicks'),
    [Input('reset_button_off','n_clicks')])

def reset(reset):
    return 0
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('graph7','children'),
    [Input('ticker-input-compare_off', 'value')])

def stock_comparision(tickers):
    if tickers is None:
        return None
    else:
        tick_list = []
        for tick in tickers:
            #tick_list.append(tick)
            df = pd.read_csv('sp500.csv')
            df.reset_index(inplace=True)
            df.set_index("Date", inplace=True)

            dff = df.copy()[df['Symbol'] == tick]

            trace = go.Scatter(
                    x = dff.index,
                    y = dff['Close'],
                    name = tick
                    )
            tick_list.append(trace)
        data = tick_list
        layout = go.Layout(
                    title = 'Stock Comparision',
                    xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                    yaxis=dict(title = 'Price', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                    plot_bgcolor='#1a1c23',
                    paper_bgcolor='#1a1c23',
                    font= {'color':'#7FDBFF',}
                )

        return html.Div([
                    dcc.Graph(
                        figure = {
                            'data': data,
                            'layout': layout,
                        }
                    )
                ],style = {'display': 'inline-block', 'width': '70%', 'height':'auto','float':'center'})
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('heatmap_off','children'),
    [Input('button1_off', 'n_clicks')])

def corr_graph(clicked):
    if clicked is None:
        clicked = 0

    if clicked>0:
        all_stock_df = pd.read_csv('stock_corr_data.csv')
        close_val_per_day = pd.DataFrame()

        for name, group in all_stock_df.groupby('Name'):
            if close_val_per_day.empty:
                close_val_per_day = group.set_index('Date')[ ['Close'] ].rename(columns = {'Close' : name})
            else:
                close_val_per_day = close_val_per_day.join(group.set_index('Date')[ ['Close'] ].rename(columns = {'Close' : name}))

        close_val_per_day_corr = close_val_per_day.corr()

        labels = [c[:3] for c in close_val_per_day_corr.columns]
        return html.Div([
                dcc.Graph(
                    id = 'heatmap-graph',
                    figure = {
                        'data': [go.Heatmap(
                                    x = labels,
                                    y = labels,
                                    z = close_val_per_day_corr,
                                    colorscale = 'Viridis'
                                )],
                        'layout': go.Layout(
                                    xaxis = dict(title = 'COMPANIES'),
                                    yaxis = dict(title = 'COMPANIES'),
                                    plot_bgcolor = '#1a1c23',
                                    paper_bgcolor = '#1a1c23',
                                    font = {'color':'#7FDBFF',}
                                )
                    }
                )
        ], style = {'width': '1000px', 'height':'10000px', 'display': 'inline-block', 'float': 'left'} )

@app.callback(
    Output('button1_off', 'n_clicks'),
    [Input('reset_button_off','n_clicks')])

def reset(reset):
    return 0
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('pie-chart_off', 'children'),
    [Input('button2_off','n_clicks')])

def pie_graph(clicked):
    if clicked is None:
        clicked = 0

    if clicked>0:
        df1=pd.read_csv('sector.csv')
        df1.set_index('Symbol',inplace=True)

        Industrials=df1[df1['Sector']=='Industrials'].count()
        ind=Industrials['Sector']

        Health=df1[df1['Sector']=='Health Care'].count()
        h=Health['Sector']

        It=df1[df1['Sector']=='Information Technology'].count()
        i=It['Sector']

        Cd=df1[df1['Sector']=='Consumer Discretionary'].count()
        c=Cd['Sector']

        uti=df1[df1['Sector']=='Utilities'].count()
        u=uti['Sector']

        Fi=df1[df1['Sector']=='Financials'].count()
        f=Fi['Sector']

        Mt=df1[df1['Sector']=='Materials'].count()
        m=Mt['Sector']

        Re=df1[df1['Sector']=='Real Estate'].count()
        r=Re['Sector']

        cs=df1[df1['Sector']=='Consumer Staples'].count()
        co=cs['Sector']

        e=df1[df1['Sector']=='Energy'].count()
        en=e['Sector']

        tele=df1[df1['Sector']=='Telecommunication Services'].count()
        t=tele['Sector']

        li=[ind,h,i,c,u,f,m,r,co,en,t]
        le=['Industrials','Health Care','Information Technology','Consumer Discretionary','Utilities','Financials','Materials'
              ,'Real Estate','Consumer Staples','Energy','Telecommunication Services']

        fig = go.Figure(data=[go.Pie(labels=le, values=li, hole=.3)])

        return html.Div([
                        html.Div([
                            dcc.Graph(

                               figure={
                                        'data': [{
                                            'hole': 0.5,
                                            'labels': [
                                                        'Industrials',
                                                        'Health Care',
                                                        'Information Technology',
                                                        'Consumer Discretionary', 'Utilities', 'Financials', 'Materials',
                                                        'Real Estate',
                                                        'Consumer Staples',
                                                        'Energy',
                                                        'Telecommunication',
                                                        ],
                                             'type': 'pie',
                                             'values': [
                                            ind, h, i, c, u, f, m, r, co, en, t
                                                       ]}
                                        ],
                                         'layout': {
                                            'direction': 'clockwise',
                                            ''
                                            'title': 'S & P 500 sectors',
                                            'pull': ['1', '0', '0', '0', '1'],
                                            'plot_bgcolor':'#1a1c23',
                                            'paper_bgcolor':'#1a1c23',
                                            'font': {'color':'#7FDBFF'}
                                   }
                        })],style = {'width': '700px', 'height':'700px','text-align':'center', 'text-color': '#FDFEFE', 'display': 'inline-block'}),
                ])

@app.callback(
    Output('button2_off', 'n_clicks'),
    [Input('reset_button_off','n_clicks')])

def reset(reset):
    return 0
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@app.callback(
    Output('snp500_off', 'children'),
    [Input('button4_off','n_clicks')])

def combine_graph(clicked):
    if clicked is None:
        clicked = 0

    if clicked > 0:
        snp_df = pd.read_csv('snp500.csv')
        snp_df.reset_index(inplace=True)
        snp_df.set_index('Date', inplace=True)

        trace_close = go.Scatter(
                        x = snp_df.index,
                        y = snp_df['Adj Close'],
                        name = 'S&P 500 Close'
                    )

        trace_close_100ma = go.Scatter(
                            x = snp_df.index,
                            y = snp_df['Adj Close'].rolling(100).mean(),
                            name = '100 Days Moving Average'
                        )

        trace_close_200ma = go.Scatter(
                            x = snp_df.index,
                            y = snp_df['Adj Close'].rolling(200).mean(),
                            name = '200 Days Moving Average'
                        )

        trace_close_300ma = go.Scatter(
                            x = snp_df.index,
                            y = snp_df['Adj Close'].rolling(300).mean(),
                            name = '300 Days Moving Average'
                        )

        return html.Div([
                        html.Div([
                            dcc.Graph(
                                figure = go.Figure(
                                    data = [trace_close, trace_close_100ma, trace_close_200ma, trace_close_300ma],
                                    layout = go.Layout(
                                        xaxis=dict(title = 'Date', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                        yaxis=dict(title = 'Adj Close', showticklabels=True, fixedrange=False, showgrid = False, showline = False),
                                        plot_bgcolor='#1a1c23',
                                        paper_bgcolor='#1a1c23',
                                        font= {'color':'#7FDBFF',}
                                    )
                                )
                            )
                    ],style = {'display': 'inline-block', 'width': '80%', 'height':'auto','float':'left'}),
            ])

@app.callback(
    Output('button4_off', 'n_clicks'),
    [Input('reset_button_off','n_clicks')])

def reset(reset):
    return 0






if __name__ == '__main__':
    app.run_server(debug = True, port = 7791)

import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from ModulationPlotter import ModulationPlotter

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Modulação Interativa"),

    # Sliders para ajustar os parâmetros
    html.Label("Índice de Modulação (m_mod):"),
    dcc.Slider(
        id='m_mod-slider',
        min=0.1, max=1.0, step=0.001, value=0.6,
        marks={i: str(i) for i in np.arange(0.1, 1.1, 0.1)}
    ),

    html.Label("Frequência da Portadora (f_car) em Hz:"),
    dcc.Slider(
        id='f_car-slider',
        min=1000, max=10000, step=500, value=2000,
        marks={i: str(i) for i in range(1000, 10500, 500)}
    ),

    html.Label("Duração do Sinal (duration) em segundos:"),
    dcc.Slider(
        id='duration-slider',
        min=0.001, max=0.01, step=0.001, value=0.005,
        marks={i: str(round(i, 3)) for i in np.arange(0.001, 0.011, 0.001)}
    ),

    html.Label("Frequência de Modulação (f_mod) em Hz:"),
    dcc.Slider(
        id='f_mod-slider',
        min=1.0, max=500, step=10, value=160.0,
        marks={i: str(i) for i in np.arange(1.0, 500, 10)}
    ),

    html.Label("Fase de Modulação (phase_mod) em radianos:"),
    dcc.Slider(
        id='phase_mod-slider',
        min=0, max=2*np.pi, step=0.1, value=0*np.pi,
        marks={i: f"{i:.1f}" for i in np.arange(0, 2*np.pi+0.1, 0.5)}
    ),

    dcc.Graph(id='modulation-graph')
])

@app.callback(
    Output('modulation-graph', 'figure'),
    [
        Input('m_mod-slider', 'value'),
        Input('f_car-slider', 'value'),
        Input('duration-slider', 'value'),
        Input('f_mod-slider', 'value'),
        Input('phase_mod-slider', 'value')
    ]
)
def update_graph(m_mod, f_car, duration, f_mod, phase_mod):
    # Criar uma instância da classe ModulationPlotter com os valores atualizados
    plotter = ModulationPlotter(m_mod=m_mod, f_car=f_car, duration=duration, f_mod=f_mod, phase_mod=phase_mod)
    figure = plotter.plot()

    # Adicionar barras verticais interativas
    x_data = np.linspace(0, duration, 100)  # Exemplo de dados x
    annotations = []

    for x in [0.002, 0.004]:  # Exemplos de posições das barras verticais
        annotations.append(
            dict(
                x=x,
                y=1,  # Ajuste o valor de y conforme necessário
                xref='x',
                yref='paper',
                text='X: {:.3f}'.format(x),
                showarrow=True,
                arrowhead=2,
                ax=0,
                ay=-40
            )
        )

    # Atualizar o layout com as barras verticais interativas
    figure.update_layout(
        annotations=annotations
    )

    return figure

# Rodar o servidor Dash
if __name__ == '__main__':
    app.run_server(debug=True)

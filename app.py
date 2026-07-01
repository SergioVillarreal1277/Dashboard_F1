'''
Integrantes del grupo:
Esquivel, Kevin 8-1023-1678
Simmons, Abigail 8-1020-2416 
Solis, Luis 8-1026-948 
Villarreal, Sergio 20-14-7997
'''


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# cargar datos
fia         = pd.read_csv("vista_fia.csv")
patrocin    = pd.read_csv("vista_patrocinador.csv")
piloto      = pd.read_csv("vista_piloto.csv")

app = Dash(__name__)

escuderias  = sorted(fia["escuderia"].dropna().unique())
temporadas  = sorted(piloto["temporada"].dropna().unique())

# colores
FONDO       = "#1e1e2e"
TARJETA     = "#2a2a3e"
ROJO        = "#e10600"
BLANCO      = "white"
GRIS        = "#aaaaaa"

def tema():
    return dict(
        plot_bgcolor=TARJETA,
        paper_bgcolor=TARJETA,
        font_color=BLANCO,
        margin=dict(t=50, b=40, l=40, r=20)
    )

app.layout = html.Div(
    style={"backgroundColor": FONDO, "minHeight": "100vh",
           "fontFamily": "Segoe UI, sans-serif"},
    children=[

        # header
        html.Div(
            style={"backgroundColor": ROJO, "padding": "20px 40px"},
            children=[
                html.H1("Formula 1",
                        style={"color": BLANCO, "margin": "0",
                               "fontSize": "28px", "letterSpacing": "2px"})
            ]
        ),

        # subtitulo
        html.Div(
            style={"padding": "20px 40px 0px"},
            children=[
                html.P("Análisis de rendimiento — Base de datos F1",
                       style={"color": GRIS, "fontSize": "15px", "margin": "0"})
            ]
        ),

        # filtros
        html.Div(
            style={"padding": "20px 40px", "display": "flex", "gap": "30px"},
            children=[
                html.Div([
                    html.Label("Escudería:", style={"color": GRIS, "fontSize": "13px"}),
                    dcc.Dropdown(
                        id="dd-escuderia",
                        options=[{"label": e, "value": e} for e in escuderias],
                        placeholder="Todas",
                        clearable=True,
                        style={"width": "280px"}
                    )
                ]),
                html.Div([
                    html.Label("Temporada:", style={"color": GRIS, "fontSize": "13px"}),
                    dcc.Dropdown(
                        id="dd-temporada",
                        options=[{"label": str(t), "value": t} for t in temporadas],
                        placeholder="Todas",
                        clearable=True,
                        style={"width": "220px"}
                    )
                ])
            ]
        ),

        # fila 1
        html.Div(
            style={"padding": "0 40px", "display": "grid",
                   "gridTemplateColumns": "1fr 1fr", "gap": "20px"},
            children=[
                html.Div(style={"backgroundColor": TARJETA, "borderRadius": "12px",
                                "padding": "15px", "boxShadow": "0 4px 20px rgba(0,0,0,0.4)"},
                         children=[dcc.Graph(id="g-victorias")]),

                html.Div(style={"backgroundColor": TARJETA, "borderRadius": "12px",
                                "padding": "15px", "boxShadow": "0 4px 20px rgba(0,0,0,0.4)"},
                         children=[dcc.Graph(id="g-nacionalidad")])
            ]
        ),

        # fila 2
        html.Div(
            style={"padding": "20px 40px 40px", "display": "grid",
                   "gridTemplateColumns": "1fr 1fr", "gap": "20px"},
            children=[
                html.Div(style={"backgroundColor": TARJETA, "borderRadius": "12px",
                                "padding": "15px", "boxShadow": "0 4px 20px rgba(0,0,0,0.4)"},
                         children=[dcc.Graph(id="g-patrocinadores")]),

                html.Div(style={"backgroundColor": TARJETA, "borderRadius": "12px",
                                "padding": "15px", "boxShadow": "0 4px 20px rgba(0,0,0,0.4)"},
                         children=[dcc.Graph(id="g-puntos")])
            ]
        )
    ]
)

# callbacks

@app.callback(Output("g-victorias", "figure"), Input("dd-escuderia", "value"))
def victorias(escuderia):
    df = fia.copy()
    if escuderia:
        df = df[df["escuderia"] == escuderia]
    ag = df.groupby("escuderia")["victorias"].sum().reset_index()
    ag = ag.sort_values("victorias", ascending=False)
    fig = px.bar(ag, x="escuderia", y="victorias",
                 title="Victorias por Escudería",
                 color="escuderia",
                 color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(**tema(), showlegend=False)
    return fig

@app.callback(Output("g-nacionalidad", "figure"), Input("dd-escuderia", "value"))
def nacionalidad(escuderia):
    df = fia.copy()
    if escuderia:
        df = df[df["escuderia"] == escuderia]
    ag = df["nacionalidad"].value_counts().reset_index()
    ag.columns = ["nacionalidad", "cantidad"]
    fig = px.pie(ag, names="nacionalidad", values="cantidad",
                 title="Pilotos por Nacionalidad",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(**tema())
    return fig

@app.callback(Output("g-patrocinadores", "figure"), Input("dd-escuderia", "value"))
def patrocinadores(escuderia):
    df = patrocin.copy()
    if escuderia:
        df = df[df["escuderia_patrocinada"] == escuderia]
    ag = df.groupby("sector_industria")["mi_inversion"].sum().reset_index()
    ag = ag.sort_values("mi_inversion", ascending=True)
    fig = px.bar(ag, x="mi_inversion", y="sector_industria",
                 orientation="h",
                 title="Inversión por Sector",
                 color="sector_industria",
                 color_discrete_sequence=px.colors.qualitative.Safe)
    fig.update_layout(**tema(), showlegend=False)
    return fig

@app.callback(Output("g-puntos", "figure"), Input("dd-temporada", "value"))
def puntos(temporada):
    df = piloto.copy()
    if temporada:
        df = df[df["temporada"] == temporada]
    ag = df.groupby("piloto")["puntos_obtenidos"].sum().reset_index()
    ag = ag.sort_values("puntos_obtenidos", ascending=False).head(10)
    fig = px.bar(ag, x="puntos_obtenidos", y="piloto",
                 orientation="h",
                 title="Top 10 Pilotos por Puntos",
                 color="puntos_obtenidos",
                 color_continuous_scale="Reds")
    fig.update_layout(**tema())
    return fig

if __name__ == "__main__":
    app.run(debug=True)
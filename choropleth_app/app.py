#-----------------------------------------------------------------------------------------------
# This app shows the ultramarathon participation and performance of the countries of the world.
# For simplification purposes, all countries not existing anymore were omitted.
#-----------------------------------------------------------------------------------------------

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

AGGREGATED_PATH = "../data/choropleth_data.csv"
DOMINANCE_PATH = "../data/dominance_data.csv"

# Load data

_data = pd.read_csv(AGGREGATED_PATH)
YEARS = sorted(_data["year"].unique().astype(int).tolist())

_dominance = pd.read_csv(DOMINANCE_PATH)

# App layout

app = Dash(__name__)

def make_dominance_figure():
    fig = px.line(
        _dominance,
        x="year", y="finishers_smooth", color="country_name",
        hover_data={"finishers": True, "finishers_smooth": ":.0f"},
        labels={"year": "Year", "finishers_smooth": "Finishers (3-yr avg)", "country_name": "Country"},
        title="Top 10 Countries by Ultra-Marathon Finishers Over Time (1970–2022)",
        color_discrete_sequence=px.colors.qualitative.Bold,
    )
    for decade in [1980, 1990, 2000, 2010, 2020]:
        fig.add_vline(x=decade, line_dash="dot", line_color="gray", opacity=0.5)
        fig.add_annotation(x=decade, y=1, yref="paper", text=str(decade),
                           showarrow=False, font=dict(size=10, color="gray"), yanchor="top")
    fig.update_layout(
        hovermode="closest",
        xaxis=dict(title="Year", dtick=5),
        yaxis=dict(title="Number of Finishers (3-yr rolling avg)"),
        title_font_size=18, height=500,
        plot_bgcolor="white", paper_bgcolor="white",
        legend_title_text="Country",
    )
    fig.update_xaxes(showgrid=True, gridcolor="#f0f0f0")
    fig.update_yaxes(showgrid=True, gridcolor="#f0f0f0")
    return fig


app.layout = html.Div([
    # Viz 1: Choropleth
    html.H2(
        "Average 50km Ultra-Marathon Speed by Country",
        style={"textAlign": "center", "marginBottom": "4px"}
    ),
    dcc.Graph(id="choropleth", style={"height": "600px"}),
    html.Div([
        dcc.Slider(
            id="year-slider",
            min=YEARS[0],
            max=YEARS[-1],
            step=1,
            value=YEARS[-1],
            marks={y: str(y) for y in YEARS if y % 5 == 0},
            tooltip={"placement": "bottom", "always_visible": True},
        )
    ], style={"width": "80%", "margin": "0 auto 32px auto"}),

    html.Hr(style={"borderColor": "#e0e0e0"}),

    # Viz 2: National dominance line chart
    html.H2(
        "Top 10 Countries by Ultra-Marathon Finishers Over Time",
        style={"textAlign": "center", "marginBottom": "4px"}
    ),
    dcc.Graph(id="dominance", figure=make_dominance_figure(), style={"height": "500px"}),

], style={"fontFamily": "sans-serif", "maxWidth": "1200px", "margin": "0 auto", "padding": "24px"})

# ---------------------------------------------------------------------------
# Callback
# ---------------------------------------------------------------------------

@app.callback(Output("choropleth", "figure"), Input("year-slider", "value"))
def update_map(year):
    df_year = _data[_data["year"] == year]
    fig = px.choropleth(
        df_year,
        locations="iso3",
        locationmode="ISO-3",
        color="avg_speed",
        color_continuous_scale="Plasma",
        range_color=[6, 14],
        hover_name="country_name",
        hover_data={"avg_speed": ":.2f", "finishers": True, "iso3": False},
        labels={"avg_speed": "Avg Speed (km/h)", "finishers": "Finishers"},
    )
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            showcountries=True,
            countrycolor="lightgrey",
            projection_type="natural earth",
        ),
        dragmode=False,
        margin=dict(l=0, r=0, t=10, b=0),
        coloraxis_colorbar=dict(
            title=dict(text="Avg Speed<br>(km/h)"),
        ),
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True, port=5050)

import plotly.express as px
import pandas as pd

# source data extracted from JSON structure provided by the user
dataset = {
    "title": "Millionaires Per Capita by Country",
    "metric": "Millionaires per 1,000 adults",
    "regions": {
        "Europe": [
            { "country": "Switzerland", "code": "CHE", "value": 145.6 },
            { "country": "Netherlands", "code": "NLD", "value": 82.9 },
            { "country": "Denmark", "code": "DNK", "value": 74.6 },
            { "country": "Norway", "code": "NOR", "value": 74.5 },
            { "country": "Sweden", "code": "SWE", "value": 55.8 },
            { "country": "Belgium", "code": "BEL", "value": 55.0 },
            { "country": "France", "code": "FRA", "value": 50.6 },
            { "country": "United Kingdom", "code": "GBR", "value": 45.8 },
            { "country": "Germany", "code": "DEU", "value": 37.2 },
            { "country": "Spain", "code": "ESP", "value": 28.3 },
            { "country": "Italy", "code": "ITA", "value": 25.9 },
            { "country": "Russia", "code": "RUS", "value": 3.6 }
        ],
        "Asia Pacific": [
            { "country": "Hong Kong", "code": "HKG", "value": 96.1 },
            { "country": "Australia", "code": "AUS", "value": 85.2 },
            { "country": "Singapore", "code": "SGP", "value": 62.1 },
            { "country": "Taiwan", "code": "TWN", "value": 37.3 },
            { "country": "South Korea", "code": "KOR", "value": 28.1 },
            { "country": "Japan", "code": "JPN", "value": 24.9 },
            { "country": "China", "code": "CHN", "value": 5.3 },
            { "country": "India", "code": "IND", "value": 0.8 }
        ],
        "North America": [
            { "country": "United States", "code": "USA", "value": 84.8 },
            { "country": "Canada", "code": "CAN", "value": 59.9 },
            { "country": "Mexico", "code": "MEX", "value": 4.0 }
        ],
        "Middle East": [
            { "country": "Saudi Arabia", "code": "SAU", "value": 12.6 }
        ],
        "South America": [
            { "country": "Brazil", "code": "BRA", "value": 2.5 }
        ]
    },
    "notes": "Selected countries are the top 25 countries by number of millionaires.",
    "source": [
        "UBS Global Wealth Report 2025",
        "The World Bank"
    ],
    "publisher": "Visual Capitalist",
    "collaborators": {
        "research_writing": "Niccolo Conte",
        "art_direction_design": "Sabrina Lam"
    },
    "branding": {
        "voronoi_tagline": "Where Data Tells the Story"
    }
}

# flatten the JSON into a list of tuples that pandas can consume
data = []
for region, countries in dataset["regions"].items():
    for entry in countries:
        data.append((entry["country"], entry["code"], entry["value"]))

df = pd.DataFrame(data, columns=["Country","ISO","Value"])

fig = px.choropleth(
    df, locations="ISO", color="Value",
    hover_name="Country",
    color_continuous_scale="Viridis",
    title="Millionaires per 1,000 Adults (by Country)"
)

fig.update_layout(coloraxis_colorbar=dict(title="Millionaires/1k"))
fig.write_html("plot.html", auto_open=False)
# fig.show()
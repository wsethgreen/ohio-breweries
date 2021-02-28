import plotly.express as px
from data_mining import ohio_brew_df

# Create the scatter plot
fig = px.scatter_mapbox(ohio_brew_df, lat=ohio_brew_df.latitude, lon=ohio_brew_df.longitude, 
                        size=ohio_brew_df.latitude, size_max=6, zoom=6, mapbox_style="carto-positron", 
                        hover_name=ohio_brew_df.name, title="Ohio Breweries", 
                        center={'lat': 40.30017, 'lon': -82.58862}, width=750, text=ohio_brew_df.street)

#fig.show()

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

pio.write_html(fig, file='templates/ohio_brew_map.html', auto_open=False)


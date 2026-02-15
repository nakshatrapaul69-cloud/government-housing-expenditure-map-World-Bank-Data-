import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
data=pd.read_csv(r"govt exp on housing.csv")
focused_data=data.loc[:,#rows
                     #cloumns
                      ["REF_AREA_LABEL","TIME_PERIOD","OBS_VALUE","UNIT_TYPE_LABEL",]]
focused_data = focused_data.dropna()
focused_data=focused_data[focused_data["UNIT_TYPE_LABEL"]!="Ratio"]
focused_data["OBS_VALUE"] = focused_data["OBS_VALUE"] / 1_000_000_000
focused_data=focused_data.dropna()
focused_data = focused_data[focused_data["OBS_VALUE"] != 0]
focused_data=focused_data[focused_data["REF_AREA_LABEL"]!="Chile"]
#yearly
year_clean = (
    focused_data
    .groupby(["REF_AREA_LABEL", "TIME_PERIOD"], as_index=False)["OBS_VALUE"]
    .mean()
)

fig = px.choropleth(
    year_clean,
    locations="REF_AREA_LABEL",
    locationmode="country names",
    color="OBS_VALUE",
    hover_name="REF_AREA_LABEL",
    animation_frame="TIME_PERIOD",   
    color_continuous_scale="Blues",
    title="Government Housing Expenditure Over Time (Billion USD)"
)

fig.show()
fig.write_html("output_map.html")








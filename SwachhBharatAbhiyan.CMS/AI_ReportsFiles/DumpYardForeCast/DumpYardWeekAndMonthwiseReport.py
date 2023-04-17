# Run python DumpYardWeekAndMonthwiseReport.py --server 202.65.157.254 --database LIVEAdvanceJinturGhantaGadi --ulbname Jintur --hostname localhost --filename Analysis1 --ReportTitle "Analysis1"

import pymssql
import pandas as pd
import argparse
import os
from datetime import datetime
import plotly.graph_objs as go
import calendar
import warnings
warnings.filterwarnings("ignore")

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ip", "--server", required=True, help="Server IP address")
ap.add_argument("-db", "--database", required=True, help="Database name")
ap.add_argument("-ulbname", "--ulbname", required=True, help="name of the ULB")
ap.add_argument("-hostname", "--hostname", required=True, help="name of the ULB")
ap.add_argument("-filename", "--filename", required=True, help="name of the File")
ap.add_argument("-ReportTitle", "--ReportTitle", required=True, help="name of the ULB")
args = vars(ap.parse_args())

# HostName
hostname = args["hostname"]
# Directory
directory = args["ulbname"]
# Filename
filename = args["filename"]
# Report Title
reporttitle = args["ReportTitle"]
if hostname == "localhost":

    # Parent Directory path
    parent_dir = "D:/Rohit/ICTSBMCMS(AI_GIS_BC)/ICTSBMCMS/SwachhBharatAbhiyan.CMS/Images/AI"

else:

    # Parent Directory path
    parent_dir = "D:/AdvancePublish/ICTSBMCMS_AI/Images/AI"

# Path
path = os.path.join(parent_dir, directory)

try:
    os.mkdir(path)
except OSError as error:
    print(error)

server = args["server"]
database = args["database"]


# Fetch data from server
def df_server(server, database):
    ## Read data from server through query
    # Server details
    conn = pymssql.connect(server=server, user='appynitty',
                           password='BigV$Telecom', database=database)
    # Query
    df = pd.read_sql_query("select distinct(cast(gcdate as Date)) gcDate ,COUNT(distinct(houseid)) as House_Count ,isnull(SUM(totalGcWeight),0) As Total_Weight,isnull(SUM(totaldryWeight),0) As Total_Dry_Weight,isnull(SUM(totalwetWeight),0) As Total_Wet_Weight from GarbageCollectionDetails where EmployeeType is null and gctype is not null group by cast(gcdate as Date) order by cast(gcdate as Date) asc;",
                           conn)
    
    return df
df = df_server(server=server, database=database)

df.rename(columns = {'gcDate':'Date'}, inplace = True)
df['Weekday']=[calendar.day_name[(datetime.strptime(str(i), '%Y-%m-%d')).weekday()] for i in df['Date']]
df['Month']=[calendar.month_name[(datetime.strptime(str(i), '%Y-%m-%d')).month] for i in df['Date']]

fig = go.Figure()

# Adding Traces

fig = go.Figure()
fig.add_trace(go.Bar(x=df['Month'],y=df['Total_Weight'],
                name='Total',
                marker_color='rgb(102, 0, 0)'
                ))
fig.add_trace(go.Bar(x=df['Month'],
                y=df['Total_Dry_Weight'],
                name='Dry',
                marker_color='rgb(50,102,255)'
                ))
fig.add_trace(go.Bar(x=df['Month'],
                y=df['Total_Wet_Weight'],
                name='Wet',
                marker_color='rgb(0, 102, 0)'
                ))
fig.add_trace(go.Bar(x=df['Weekday'],y=df['Total_Weight'],
                name='Total',
                visible=False,
                marker_color='rgb(102, 0, 0)'
                ))
fig.add_trace(go.Bar(x=df['Weekday'],
                y=df['Total_Dry_Weight'],
                name='Dry',
                visible=False,
                marker_color='rgb(50,102,255)'
                ))
fig.add_trace(go.Bar(x=df['Weekday'],
                y=df['Total_Wet_Weight'],
                name='Wet',
                visible=False,
                marker_color='rgb(0, 102, 0)'
                ))
fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Monthwise",
                     method="update",
                     args=[{"visible": [True, True, True, False,False,False]},
                           {"title": "Monthwise Waste Weight"}]),
                dict(label="Weekwise",
                     method="update",
                     args=[{"visible": [False,False,False, True,True,True]},
                           {"title": "Weekwise Waste Weight"
                            }])]))])
fig.update_layout(
    title='Monthwise Waste Weight',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Weight(MT)',
        titlefont_size=16,
        tickfont_size=14),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.update_layout(
    yaxis_title="Weight in MT",
    
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="Black"
    )
)

config = {
        'toImageButtonOptions': {
            'format': 'png',  # one of png, svg, jpeg, webp
            'filename': filename
            # 'height': 500,
            # 'width': 700,
            # 'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
        }
    }
fig.write_html(path + "/DumpYardWeeklyMonthly.html", config=config)
# fig.write_html("WeeklyMonthly.html", config=config)

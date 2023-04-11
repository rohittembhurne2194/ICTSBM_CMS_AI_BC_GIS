# Run python Analysis_deploy1.py --server 202.65.157.254 --database LIVEAdvanceJinturGhantaGadi --ulbname Jintur --hostname localhost --filename Analysis1 --ReportTitle "Analysis1"

import pymssql
import pandas as pd
import argparse
import os
from datetime import datetime
import plotly.graph_objs as go
import calendar

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

    # parent_dir = "D:/ICTSBMCMS-AI-BC-GIS/ICTSBMCMS/SwachhBharatAbhiyan.CMS/Images/AI"
else:

    # Parent Directory path
    parent_dir = "D:/Publish/ICTSBMCMS_AI_BC_GIS/Images/AI"

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
    df = pd.read_sql_query("select distinct(cast(gcdate as Date)) gcDate ,COUNT(distinct(houseid)) as House_Count ,isnull(SUM(totalGcWeight),0) As Total_Weight,isnull(SUM(totaldryWeight),0) As Total_Dry_Weight,isnull(SUM(totalwetWeight),0) As Total_Wet_Weight from GarbageCollectionDetails where EmployeeType is null and gcDate is not null group by cast(gcdate as Date) order by cast(gcdate as Date) asc;",
                           conn)
    
    return df
df = df_server(server=server, database=database)

df.rename(columns = {'gcDate':'Date'}, inplace = True)
df['Weekday']=[calendar.day_name[(datetime.strptime(str(i), '%Y-%m-%d')).weekday()] for i in df['Date']]
df['Month']=[calendar.month_name[(datetime.strptime(str(i), '%Y-%m-%d')).month] for i in df['Date']]

fig = go.Figure()

# Adding Traces

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=list(df.Total_Weight),
               name="Total_Weight",
               line=dict(color="#33CFA5")))

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=[df.Total_Weight.mean()] * len(df.index),
               name="Total_Weight Average",
               visible=False,
               line=dict(color="#33CFA5", dash="dash")))

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=list(df.Total_Dry_Weight),
               name="Total_Dry_Weight",
               line=dict(color="#F06A6A")))

fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=[df.Total_Dry_Weight.mean()] * len(df.index),
               name="Total_Dry_Weight Average",
               visible=False,
               line=dict(color="#F06A6A", dash="dash")))
fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=list(df.Total_Wet_Weight),
               name="Total_Wet_Weight",
               line=dict(color="burlywood"))),
fig.add_trace(
    go.Scatter(x=list(df.Date),
               y=[df.Total_Wet_Weight.mean()] * len(df.index),
               name="Total_Wet_Weight Average",
               visible=False,
               line=dict(color="burlywood", dash="dash")))

fig.update_layout(paper_bgcolor="blanchedalmond")
fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Total_Weight",
                     method="update",
                     args=[{"visible": [True, True, False, False,False,False]},
                           {"title": "Garbage Weight Analysis"
                            }]),
                dict(label="Dry_Weight",
                     method="update",
                     args=[{"visible": [False,False,True, True,False,False]},
                           {"title": "Garbage Weight Analysis"
                            }]),
                dict(label="Wet_Weight",
                     method="update",
                     args=[{"visible": [False,False,False,False, True, True]},
                           {"title": "Garbage Weight Analysis"
                            }]),
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, True, True,True,True]},
                           {"title": "Garbage Weight Analysis"
                            }]),
                
                
            ]),
        )
    ])

# title
fig.update_layout(title_text="Garbage Weight Analysis")
fig.update_layout(paper_bgcolor="white")

config = {
        'toImageButtonOptions': {
            'format': 'png',  # one of png, svg, jpeg, webp
            'filename': filename
            # 'height': 500,
            # 'width': 700,
            # 'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
        }
    }
fig.write_html(path + "/DumpYardDayWise.html", config=config)
#fig.write_html("Jintur1.html", config=config)

# Run python forecast_deply_1.py -ip 124.153.94.110 -db LIVEAdvanceAppynittyGhantaGadi -ulbname ITDepartment -hostname localhost -filename DumpYardForecast -ReportTitle "IT Department"
import pymssql
import pandas as pd
import argparse
import os
from datetime import date
import holidays
from sklearn.ensemble import RandomForestRegressor
import plotly.graph_objs as go


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
    parent_dir = "D:/AdvancePublish/ICTSBMCMS_AI_BC_GIS/Images/AI"

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
    df = pd.read_sql_query(
        'select distinct(cast(gcdate as Date)) gcDate , isnull(SUM(totalGcWeight),0) As Total_Weight from GarbageCollectionDetails group by cast(gcdate as Date)  having SUM(totalGcWeight)>0 order by cast(gcdate as Date) asc;',
        conn)
    df.set_index('gcDate', inplace=True)
    df.index = pd.to_datetime(df.index)
    # print(df.describe())
    return df


# server = "202.65.157.253"
# database = "LIVEAdvanceKurkhedaGhantaGadi"
df = df_server(server=server, database=database)

if df['Total_Weight'].count() <= 10:  # Plot No Enough Samples
    # Plot No Enough Samples
    layout = go.Layout(
        title='Garbage Generation Forecast of ' + database,
        xaxis={"title": "Date"},
        yaxis={"title": "Total_Weight"},
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

    fig = go.Figure(layout=layout)

    annotation = {
        'text': 'No Enough Samples',  # text
        'showarrow': False,  # would you want to see arrow
        'font': {'size': 20, 'color': 'orange'}  # font style
    }
    fig.add_annotation(annotation)
    fig.write_html(path + "/DumpYardforecast.html", config=config)

else:
    # Drop NaN
    df.dropna(inplace=True)
    # Cut-off limit
    df = df[df['Total_Weight'] < 20]

    if not df.index.is_monotonic:
        df = df.sort_index()

    # Split the Data into dummy variables
    df_features = (
        df
        # .assign(hour = df.index.hour)
        # .assign(day = df.index.day)
        .assign(month=df.index.month)
        .assign(day_of_week=df.index.dayofweek)
        .assign(week_of_year=df.index.week)
    )


    def onehot_encode_pd(df, cols):
        for col in cols:
            dummies = pd.get_dummies(df[col], prefix=col)
            df = pd.concat([df, dummies], axis=1).drop(columns=col)
        return df


    df_features = onehot_encode_pd(df_features, ['month', 'day_of_week', 'week_of_year'])

    # Required columns
    req_cols = ['Total_Weight', 'month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6', 'month_7', 'month_8',
                'month_9', 'month_10', 'month_11', 'month_12',
                'day_of_week_0', 'day_of_week_1', 'day_of_week_2', 'day_of_week_3', 'day_of_week_4', 'day_of_week_5',
                'day_of_week_6',
                'week_of_year_1', 'week_of_year_2', 'week_of_year_3', 'week_of_year_4', 'week_of_year_5',
                'week_of_year_6', 'week_of_year_7', 'week_of_year_8',
                'week_of_year_9', 'week_of_year_10', 'week_of_year_11', 'week_of_year_12', 'week_of_year_13',
                'week_of_year_14', 'week_of_year_15',
                'week_of_year_16', 'week_of_year_17', 'week_of_year_18', 'week_of_year_19', 'week_of_year_20',
                'week_of_year_21', 'week_of_year_22', 'week_of_year_23',
                'week_of_year_24', 'week_of_year_25', 'week_of_year_26',
                'week_of_year_27', 'week_of_year_28', 'week_of_year_29',
                'week_of_year_30', 'week_of_year_31', 'week_of_year_32',
                'week_of_year_33', 'week_of_year_34', 'week_of_year_35',
                'week_of_year_36', 'week_of_year_37', 'week_of_year_38',
                'week_of_year_39', 'week_of_year_40', 'week_of_year_41',
                'week_of_year_42', 'week_of_year_43', 'week_of_year_44',
                'week_of_year_45', 'week_of_year_46', 'week_of_year_47',
                'week_of_year_48', 'week_of_year_49', 'week_of_year_50',
                'week_of_year_51', 'week_of_year_52', 'week_of_year_53', ]


    # Create missing columns in the training data if not present
    def create_miss_col(df_features, req_cols):
        for col in req_cols:
            if col not in df_features.columns:
                df_features[col] = 0
        return df_features


    df_features = create_miss_col(df_features, req_cols)

    us_holidays = holidays.IND()


    def is_holiday(date):
        date = date.replace(hour=0)
        return 1 if (date in us_holidays) else 0


    def add_holiday_col(df, holidays):
        return df.assign(is_holiday=df.index.to_series().apply(is_holiday))


    df_features = add_holiday_col(df_features, us_holidays)


    def feature_label_split(df, target_col):
        y = df[[target_col]]
        X = df.drop(columns=[target_col])
        return X, y


    X, y = feature_label_split(df_features, 'Total_Weight')

    X_train = X.values
    y_train = y.values

    # Modeling
    randforest = RandomForestRegressor(n_estimators=5000, oob_score=True, random_state=100)
    randforest.fit(X_train, y_train)

    # Forecasting
    start_date = date.today()
    index = pd.date_range(start=start_date, freq='D', periods=60)
    df_forecast = pd.DataFrame(index=index)

    # Split the Data into dummy variables
    df_forecast = (
        df_forecast
        # .assign(hour = df.index.hour)
        # .assign(day = df.index.day)
        .assign(month=df_forecast.index.month)
        .assign(day_of_week=df_forecast.index.dayofweek)
        .assign(week_of_year=df_forecast.index.week)
    )

    # Onehot encoding
    df_forecast = onehot_encode_pd(df_forecast, ['month', 'day_of_week', 'week_of_year'])

    # Create missing columns
    df_forecast = create_miss_col(df_forecast, req_cols)

    # Adding Holidays
    df_forecast = add_holiday_col(df_forecast, us_holidays)
    df_forecast = df_forecast.drop(columns='Total_Weight')

    # Forecasting features
    X_forecast = df_forecast.values

    # Forecasting
    forecast_tree = randforest.predict(X_forecast)

    # Plot Forecasting
    data = []

    value = go.Scatter(
        x=df_features.index[-30:],
        y=df_features['Total_Weight'][-30:].values,
        mode="lines",
        name="Real_Weight",
        marker={"color": "blue"},
    )
    data.append(value)

    forecast = go.Scatter(
        x=df_forecast.index,
        y=forecast_tree,
        mode="lines",
        name="Forecast_Weight",
        marker={"color": "red"},
    )
    data.append(forecast)

    if df_features.index[-1] == df_forecast.index[0]:
        work_prog = go.Scatter(
            x=[df_features.index[-1], df_forecast.index[0]],
            y=[df_features['Total_Weight'][-1], forecast_tree[0]],
            mode="lines",
            line={"dash": "dot"},
            name="Work_in_Progress",
            marker={"color": "black"},
        )
        data.append(work_prog)
    else:
        no_work = go.Scatter(
            x=[df_features.index[-1], df_forecast.index[0]],
            y=[df_features['Total_Weight'][-1], forecast_tree[0]],
            mode="lines",
            line={"dash": "dot"},
            name="No_Work",
            marker={"color": "black"},
        )
        data.append(no_work)

    layout = go.Layout(
        title='Garbage Generation Forecast of ' + reporttitle,
        xaxis={"title": "Date"},
        yaxis={"title": "Total_Weight"},
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
    fig = go.Figure(data=data, layout=layout)
    fig.write_html(path + "/DumpYardforecast.html", config=config)
    # graph_name = "database + "_Forecast.html"
    # fig.write_html(graph_name)
    # iplot(fig)

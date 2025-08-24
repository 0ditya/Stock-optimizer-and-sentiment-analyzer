import requests #HTTP requests
import json # handling json data
import streamlit as st #web apps
import pandas as pd

from environs import Env #environment variable work

env = Env()
env.read_env()

# @st.cache
def get_tickerlist():
    #get request to fetch ticker list
    response = requests.get(f"{env('HOST')}/Tickerlist_provider?datatype=tickerlist")

    response_json = response.json() #convert to json

    companyTicker = pd.read_json(response_json["myData"])
    #read into pandas
    return companyTicker


# @st.cache #fetch and plots stock data
def get_plot(selection: str, plottype: str):

    assert plottype in ["scatter", "returns", "histogram"]
    #checks if plots is valid
    response = requests.get(
        f"{env('HOST')}/Stockticker_provider?plottype={plottype}&selection={selection}"
    )
    #get request to fetch
    blub = response.json() #convert to json

    fig = json.loads(blub["plot"]) # load plot

    return fig


if __name__ == "__main__":
    print(get_tickerlist())

    print(get_plot("ADS.DE", "scatter"))

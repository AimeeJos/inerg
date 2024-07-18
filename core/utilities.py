"""Functions to process xls files"""

import pandas as pd
from core.models import ProductionData


def add_to_database(production_data):
    """Add data to the database"""
    if not ProductionData.objects.filter(well_no=production_data["well_no"]).exists():
        p = ProductionData.objects.create(**production_data)
        print(p)


def calculate_sum_of_columns(col_name):
    """Calculate the sum of a column in a dataframe"""
    total = pd.to_numeric(col_name).sum()
    return total


def filter_data_by_well_no(well_no, df):
    """Filter data by well number"""
    filtered_df = df[df["API WELL  NUMBER"] == int(well_no)]
    return filtered_df


def create_production_data_object(df):
    """Create a production data object"""
    production_data = {}
    for well_no in df["API WELL  NUMBER"]:
        print("--------------------------------")
        production_data = {}
        production_data["well_no"] = well_no
        filtered_df = filter_data_by_well_no(well_no, df)
        total_oil = calculate_sum_of_columns(filtered_df["OIL"])
        production_data["oil"] = total_oil
        total_gas = calculate_sum_of_columns(filtered_df["GAS"])
        production_data["gas"] = total_gas
        total_brine = calculate_sum_of_columns(filtered_df["BRINE"])
        production_data["brine"] = total_brine
        # print(production_data)
        add_to_database(production_data)


def read_data(file):
    print(file)
    df = pd.read_excel(file, engine="xlrd")
    print(df.head())

    create_production_data_object(df)

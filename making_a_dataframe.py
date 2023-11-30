import pandas as pd
import finance

record = finance.get_record()

def create_df(record):

    biggest_df = pd.DataFrame()

    # Loops through each piece of data
    for i in range(len(record)):
        print(i)
        datapoint = record[i]

        # Puts each different dictionary into a DataFrame
        state_df = pd.DataFrame({i : {"State": datapoint["State"]}}, columns=[i])
        year_df = pd.DataFrame({i : {"Year": datapoint["Year"]}}, columns=[i])
        details_df = pd.DataFrame({i : datapoint["Details"]})
        totals_df = pd.DataFrame({i : datapoint["Totals"]})

        # Puts all of these dataframes together
        big_df = pd.concat([state_df, year_df, totals_df, details_df], axis=0)

        # Turns big_df into a row
        big_df = big_df.transpose()

        # Adds row to bigger_df
        biggest_df = pd.concat([biggest_df, big_df], axis=0)

    print(biggest_df)

    # Returns File
    return biggest_df

df = create_df(record)
df.to_csv("data/uncivilized.csv")
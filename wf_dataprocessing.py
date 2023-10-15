import pandas as pd


def preprocess(inputfile):
    df=pd.read_csv(inputfile) 

    # Convert the "Date" column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    print(len(df))
    # Filter data for years after 2019
    df = df[df['Date'].dt.year >= 2019]

    #to know number of records(data)
    print(len(df))

    #to show number of null values in our dataset
    print(df.isnull().sum())

    #Updating Missing location description rows as Unknows
    # (location description is where the crime occurs like parking lot, appartment etc.,)
    df['Location Description'].fillna('Unknown', inplace=True)

    #without coordinates we cannot analize the data so removing those lines of data
    df = df.dropna(subset=['X Coordinate','Ward','Community Area'])

    print(len(df))
    print(df.isnull().sum())
    # Save the preprocessed data to a new CSV file
    df.to_csv('./data_processed/preprocessed_crime_data.csv', index=False)
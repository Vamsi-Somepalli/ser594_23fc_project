import pandas as pd
import hashlib


def preprocess(inputfile):
    '''Preprocess a CSV file containing crime data, including filtering, cleaning, and saving the result.

    Parameters:
    inputfile (str): The path to the input CSV file containing crime data.

    Returns:
    None'''

    #READING csv file using pandas
    df=pd.read_csv(inputfile) 

    #tofind MS5
    csv_content = df.to_csv(index=False).encode()
    file_md5_hash = calculate_md5_hash(csv_content)
    print("MD5 code:",file_md5_hash)

    # Convert the "Date" column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    print("No of records before preprocessing",len(df))

    # Filter data for years after 2019
    df = df[df['Date'].dt.year >= 2019]

    #to know number of records(data)
    

    #to show number of null values in our dataset
    #print(df.isnull().sum())

    #Updating Missing location description rows as Unknows
    # (location description is where the crime occurs like parking lot, appartment etc.,)
    df['Location Description'].fillna('Unknown', inplace=True)

    #without coordinates we cannot analize the data so removing those lines of data
    df = df.dropna(subset=['X Coordinate','Ward','Community Area'])
    print("No of records after preprocessing",len(df))
    # print(len(df))
    # print(df.isnull().sum())
    # Save the preprocessed data to a new CSV file
    df.to_csv('./data_processed/preprocessed_crime_data.csv', index=False)


def calculate_md5_hash(csvdata):
    md5_hash = hashlib.md5()
    md5_hash.update(csvdata)
    return md5_hash.hexdigest()
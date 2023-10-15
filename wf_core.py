import wf_dataprocessing
import wf_visualization




if __name__ == '__main__':
    filename="data_original/Crimes_-_2001_to_Present.csv"
    wf_dataprocessing.preprocess(filename)
    processed_file="data_processed/preprocessed_crime_data.csv"
    wf_visualization.visualization(processed_file)
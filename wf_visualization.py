import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



def visualization(processed_file):
    '''Generate various visualizations and statistics from a processed CSV file containing crime data.

    Parameters:
    processed_file (str): The path to the processed CSV file.

    Returns:
    None'''
    
    data=pd.read_csv(processed_file)

    #summary file content
    Qualitative=['Primary Type','Year','Arrest','Domestic','Location Description' ]
    with open('./data_processed/summary.txt', 'w') as file:
        file.write("Qualitative Features:\n\n")
        for feature in Qualitative:
            # Number of categories
            num_categories = len(data[feature].unique())
            
            # Most frequent category and its count
            most_frequent = data[feature].value_counts().idxmax()
            most_frequent_count = data[feature].value_counts().max()
            
            # Least frequent category and its count
            least_frequent = data[feature].value_counts().idxmin()
            least_frequent_count = data[feature].value_counts().min()
            
            # Write the results to the text file
            file.write(f"Feature: {feature}\n")
            file.write(f"Number of Categories: {num_categories}\n")
            file.write(f"Most Frequent Category: {most_frequent} (Count: {most_frequent_count})\n")
            file.write(f"Least Frequent Category: {least_frequent} (Count: {least_frequent_count})\n\n")
    Quantitative=['Beat', 'Ward', 'District', 'Community Area']
    with open('./data_processed/summary.txt', 'a') as file:
        file.write("\n\nQuantitative Feature Statistics:\n\n")
        for feature in Quantitative:
            # Calculate the statistics
            min_value = data[feature].min()
            max_value = data[feature].max()
            median_value = data[feature].median()
            
            # Append the results to the text file
            file.write(f"Feature: {feature}\n")
            file.write(f"Minimum Value: {min_value}\n")
            file.write(f"Maximum Value: {max_value}\n")
            file.write(f"Median Value: {median_value}\n\n")
    #Corelation matrix
    CorelationMatrix=data[Quantitative].corr()
    
    CorelationMatrix.to_csv('./data_processed/correlations.txt', sep='\t')
    

    #Visualization
    #catagerizing 
    crime_counts = data["Primary Type"].value_counts()
    crime_counts_sorted = crime_counts.sort_values(ascending=False)
    #print(crime_counts_sorted)
    # Create a logarithmic scale for the y-axis
    log_counts = np.log10(crime_counts_sorted.values)
    # Create a bar plot with a logarithmic y-axis and labels inside the bars
    plt.figure(figsize=(10, 6))
    sns.barplot(x=crime_counts_sorted.index, y=log_counts)
    plt.xlabel("Primary Crime Type")
    plt.ylabel("Number of crimes log10(count)")
    plt.title("Distribution of Crime Types (Log Scale)")
    plt.xticks([])#removing xlabels

    for i, label in enumerate(crime_counts_sorted.index):
        plt.text(i, log_counts[i] / 2, label, ha="center", va="center", rotation=90, fontsize=6, color="white")
    plt.tight_layout()
    plt.savefig('./visuals/Crime_Categories.png')
    plt.show()


    data["Date"] = pd.to_datetime(data["Date"])
    data.set_index("Date", inplace=True)
    crime_counts_by_weekly = data.resample("W").size()
    plt.figure(figsize=(12, 6))
    plt.plot(crime_counts_by_weekly.index, crime_counts_by_weekly.values)
    plt.xlabel("Date")
    plt.ylabel("Number of Crimes")
    plt.title("Crime Trends Over Time  on a weekly basis")
    plt.tight_layout()
    plt.savefig('./visuals/Weekly_Trends.png')
    plt.show() 

    crime_counts_by_month = data.resample("M").size()
    #print(crime_counts_by_month)
    plt.figure(figsize=(12, 6))
    plt.plot(crime_counts_by_month.index, crime_counts_by_month.values)
    plt.xlabel("Date")
    plt.ylabel("Number of Crimes")
    plt.title("Crime Trends Over Time  on a Monthly basis")
    plt.tight_layout()
    plt.savefig('./visuals/Montly_Trends.png')
    plt.show()

    # Arrest vs. Non-Arrest: Pie chart
    arrest_counts = data['Arrest'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(arrest_counts, labels=arrest_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Arrest vs. Non-Arrest')
    plt.savefig('./visuals/Arrested_pie.png')
    plt.legend(['Non-Arrest', 'Arrest'], loc='lower right')
    plt.show()


    plt.figure(figsize=(6, 6))
    plt.bar(arrest_counts.index, arrest_counts.values, color=['blue', 'red'])

    plt.xlabel('Arrest')
    plt.ylabel('Number of Incidents')
    plt.title('Arrest vs. Non-Arrest Incidents')

    plt.xticks([0, 1], ['Not Arrested', 'Arrested'])
    plt.savefig('./visuals/Arrest_barchart.png')
    plt.show()


    domestic_counts = data['Domestic'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(domestic_counts, labels=domestic_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Domestic vs. Non-Domestic Incidents')
    plt.savefig('./visuals/isdomestic_pie.png')
    # Add a legend
    plt.legend(['Non-Domestic', 'Domestic'], loc='lower right')
    plt.show()


    year_column = data['Year']

    # Create a histogram
    plt.figure(figsize=(10, 6))
    plt.hist(year_column, bins=range(min(year_column), max(year_column) + 1),width=0.8, alpha=0.7, edgecolor='black')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('Histogram of Year')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('./visuals/Histogram_years.png')
    plt.show()


    # Create scatter plots for all pairs of selected features

    for i in range(len(Quantitative)):
        for j in range(i + 1, len(Quantitative)):
            feature1 = Quantitative[i]
            feature2 = Quantitative[j]

            plt.figure(figsize=(8, 6))
            plt.scatter(data[feature1], data[feature2], alpha=0.5)
            plt.xlabel(feature1)
            plt.ylabel(feature2)
            plt.title(f'Scatter Plot: {feature1} vs {feature2}')
            plt.grid(True)
            plt.savefig(f'./visuals/ScatterPlot_{feature1}vs{feature2}.png')
            plt.show()
    
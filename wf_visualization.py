import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



def visualization(processed_file):
    data=pd.read_csv(processed_file)

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
    plt.savefig('./visuals/Arrested_.png')
    plt.legend(['Non-Arrest', 'Arrest'], loc='lower right')
    plt.show()

    domestic_counts = data['Domestic'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(domestic_counts, labels=domestic_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Domestic vs. Non-Domestic Incidents')
    plt.savefig('./visuals/isdomestic.png')
    # Add a legend
    plt.legend(['Non-Domestic', 'Domestic'], loc='lower right')
    plt.show()
import matplotlib.pyplot as plt
import numpy as np
import csv


__author__ = "Vamsi Krishna Somepalli"
__date__ = "10/08/2023"
__assignment = "SER594: Homework 3 Q3 Programming"


def do_stuff(input_filename):
    data=[]
    with open(input_filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    for row in data:
        row['Total_Views']=clean_views(row['Total_Views'])#preprocess total views
        row['Publish_Date']=clean_PublishDate(row['Publish_Date'])#preprocess publish date
    #Line plot
    #todetermine chanels with more than 10 videos
    channels={} #dict that stores chanel names as key and no of vides as value
    for row in data:
        channel_Name=row['Channel_Name']
        if channel_Name in channels:
            channels[channel_Name]+=1
        else:
            channels[channel_Name]=1
    topchannels=[]
    for channelName,noOfVideos in channels.items():
        if(noOfVideos>10):
            topchannels.append(channelName)
    channels_to_plot=topchannels[:3]#just picking first three
    colors = ["r", "b", "g"]  # Useing red, blue, gree for three channels
    plt.figure()
    for i, channel in enumerate(channels_to_plot):#enumerate is to get both index and value
        channel_data = []
        for row in data:
            if(row['Channel_Name'] == channel):
                channel_data.append(row)
        publish_date=[]
        total_views=[]
        for row in channel_data:
            publish_date.append(row['Publish_Date'])
            total_views.append(row['Total_Views'])
        publish_date = np.array(publish_date)
        total_views = np.array(total_views)
        plt.plot(publish_date, total_views, label=channel, color=colors[i])#line plot by defalult
    plt.title('Total Views vs Publish Date for Three Channels')
    plt.xlabel('Publish Date (in days)')
    plt.ylabel('Total Views')
    plt.grid(True)
    plt.legend()
    plt.savefig('hw03_Somepalli_image1lineplot.png')
    plt.show()

    #scatter plot
    plt.figure()
    publishDate=[]
    totalViews=[]
    for row in data:
        publishDate.append(row['Publish_Date'])
        totalViews.append(row['Total_Views'])
    publish_Date=np.array(publishDate)
    total_Views=np.array(totalViews)
    plt.scatter(publish_Date,total_Views)           
    plt.title('Total Views vs Publish Date (All Data Points)')
    plt.xlabel('Publish Date (in days)')
    plt.ylabel('Total Views')
    plt.grid(True)
    plt.savefig('hw03_Somepalli_image2scatterplot.png')
    plt.show()
    #Barchart
    Channel_Frequency={}
    for row in data:
        channel_link = row['Channel_Link']
        if channel_link in Channel_Frequency:
            Channel_Frequency[channel_link]+=1
        else:
             Channel_Frequency[channel_link]=1
    sorted_channel_frequency=sorted(Channel_Frequency.items(),key=lambda x: x[1], reverse=True)
    productive_channel_names=[]
    productive_channel_counts=[]
    for i in range(5):
        productive_channel_names.append(sorted_channel_frequency[i][0])
        productive_channel_counts.append(sorted_channel_frequency[i][1])
    plt.figure(figsize=(10, 6))
    plt.bar(productive_channel_names, productive_channel_counts)
    plt.title('Five Most Productive Channels')
    plt.xlabel('Channel Link')
    plt.ylabel('Number of Videos')
    plt.xticks(rotation=45, ha='right')
    plt.savefig('hw03_Somepalli_image3barchart.png')
    plt.show()

    print(publishDate)
 #histograms
    plt.figure(figsize=(10, 6))
    plt.hist(publish_Date, bins=20, edgecolor='k')
    plt.title('Histogram of Video Ages')
    plt.xlabel('Publish Date (in days)')
    plt.ylabel('Frequency')
    plt.savefig('hw03_lastname_image4histogram.png')
    plt.show()


def clean_views(view):
    if 'K views' in view:#replacing K with times 1000
        return float(view.replace('K views',""))*1000
    elif 'M views' in view:#replacing M with times 1000000
         return float(view.replace('M views',""))*1000000
    elif 'No views' in view:#replacing No views with 0
        return float(view.replace('No views',"0"))
    elif 'views' in view:#Removing views string(views without K/M)
        return float(view.replace(' views',""))
    elif 'view' in view:#replacing view from 1view
        return float(view.replace(' view',""))
    else:#replacing anything with Zero
        return float(0)

def clean_PublishDate(date):
    if 'Streamed' in date:
        if 'year' in date:
            return int(date.split(' ')[1])*365 #assuming  1 year=365days
        elif 'month' in date:
            return int(date.split(' ')[1])*30 #assuming  1 month=30days
        elif 'week' in date:
            return int(date.split(' ')[1])*7
        elif 'day' in date:
            return int(date.split(' ')[1])
        else:
            return 0
    elif 'year' in date:
        return int(date.split(' ')[0])*365
    elif 'month' in date:
        return int(date.split(' ')[0])*30
    elif 'week' in date:
        return int(date.split(' ')[0])*7
    elif 'day' in date:
        return int(date.split(' ')[0])
    else:
        return 0 #asssuming any value other than this is zero ex: 20 hours as zero days


if __name__ == '__main__':
    filename = "HW03_Kaggle_Youtube_DataScience.csv"
    do_stuff(filename)

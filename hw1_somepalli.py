__author__ = "TODO"
__date__ = "TODO"
__assignment = "SER*94: Homework 1 Programming"


def smooth(data, cutoff=4):
    """
    Applies smoothing to a list containing integer data using Pascal's Triangle technique from HW PDF.
    :param dat: the original numerical data to smooth.
    :param cutoff: the minimum required value for something to count as a max.
    :return: a tuple containing: smoothed, smoothed_stable, maximums, maximum difference
    """

    # TODO
    smoothed=[None]*len(data)
    stablesmoooth=[None]*len(data)
    pascal_triangle=[1,10,45,120,210,252,210,120,45,10,1]
    last=len(data)-1
    for i in range(len(data)-6):
        if(i<=5):#edge smothing
            temp = int(len(pascal_triangle)/2)-i           
            pascal=pascal_triangle[temp:]
            Sum_pascal=sum(pascal)
            buffer=sum(data[j] * pascal[j] for j in range(len(pascal))) / Sum_pascal
            smoothed[i]=buffer
            stablesmoooth[i]=round(buffer*10)
            buffer1=sum(data[last-k]*pascal[k] for k in range(len(pascal)))/Sum_pascal
            smoothed[last-i]=buffer1
            stablesmoooth[last-i]=round(buffer1*10)
        else:#smothed middle
            pascal_sum=sum(pascal_triangle)
            buffer2 = sum(data[j + i - 5] * pascal_triangle[j] for j in range(len(pascal_triangle))) / pascal_sum
            smoothed[i] = buffer2
            stablesmoooth[i]=round(buffer2*10)
    #Find maximums without palteaus
    Maximums=["-"]*len(stablesmoooth)
    for i in range(len(stablesmoooth)):
        if(stablesmoooth[i]>cutoff): 
            if(i==0):
                if(stablesmoooth[i]>stablesmoooth[i+1]):
                   Maximums[i]="X"
            elif(i==len(stablesmoooth)-1):
                if(stablesmoooth[i]>stablesmoooth[i-1]):
                    Maximums[i]="X"
            else:
                if(stablesmoooth[i]>stablesmoooth[i+1] and stablesmoooth[i]>stablesmoooth[i-1]):
                    Maximums[i]="X"
    #Find maximums with palteaus
    plateaus=[]
    start = -1
    for i in range(1, len(stablesmoooth) - 1):
        if stablesmoooth[i] > stablesmoooth[i - 1] and stablesmoooth[i] == stablesmoooth[i + 1]:
            if start == -1:
                start = i
        elif start != -1 and stablesmoooth[i] > stablesmoooth[i + 1]:
            end = i+1
            plateaus.append(start)
            plateaus.append(end)
            start = -1
    max_with_plateau=sum(plateaus)//2
    Maximums[max_with_plateau]="X"
    #Find the margin of error
    error=[]
    for i in range(len(data)):
        abs_value=abs(data[i]-smoothed[i])
        error.append(abs_value)
    max_error=max(error)

    
    return smoothed, stablesmoooth,Maximums, max_error


if __name__ == '__main__':
    # feel free to change anything here, this code block will not be graded.

    # sample input
    data = [6, 3, 3, 5, 3, 5, 4, 5, 4, 3, 2, 2, 2, 2, 3, 4, 4, 6, 5, 5, 7, 7, 5, 7, 7, 7, 6, 5, 5, 5]

    smooth_result = smooth(data)

    print(smooth_result[0])
    print(smooth_result[1])
    print("".join(smooth_result[2]))
    print(smooth_result[3])

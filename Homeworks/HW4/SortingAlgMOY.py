## HW4

# 2 different sorting algorithms (ones from class just with different complexities)
# O(n^2) and O(nlogn)

#graph with -Vertical axis in time - Horizontal axis is N size of set to sort - one line for each algorithm = label everything
# https://visualgo.net/bn/sorting
# https://betterexplained.com/articles/sorting-algorithms/#Radix_sort_BestAvgWorst_ON

# Graphing in python https://plot.ly/python/
#py.show() 
#bubble sort
#x=[4,2,1]


#index list of numbers [0]  [1].
#if [0] > [1] switch then repeat

#x[0]>x[1]

#BubbleSort

import random
import timeit
import pylab as py

random_l = random.sample(range(10), 10)

listn= [2,1,3]
def BubbleSort(listn):
	for i in range(0,len(listn)):
		for j in range(i+1, len(listn)): #range(1,len(listn)):
			if listn[i]>listn[j]:
				listn[i], listn[j] = listn[j], listn[i]
	return listn

BubbleSort(random_l)
BubbleSort(listn)




def SelectionSort(listn):
	i = 0
	while i<len(listn):
		minim = min(listn[i:])
		minim_index = listn.index(minim)
		listn[i],listn[minim_index] = listn[minim_index],listn[i]
		i+=1
	return listn



### time

# https://stackoverflow.com/questions/8220801/how-to-use-timeit-module


def simulation(n,it):
    t_BubbleSort = []
    t_SelectionSort = []
    for i in range(it):
        sim = random.sample(range(n),n)
        start_time = timeit.default_timer() 
        BubbleSort(sim)
        mid_time = timeit.default_timer() 
        SelectionSort(sim)    
        end_time = timeit.default_timer()
        t_BubbleSort.append(mid_time - start_time)
        t_SelectionSort.append(end_time - mid_time)
    return sum(t_BubbleSort)/len(t_BubbleSort), sum(t_SelectionSort)/len(t_SelectionSort) #average




t_BubbleSort = []
t_SelectionSort = []


# 1-99


for i in range(2,100):
    all_times = simulation(i,10) 
    t_BubbleSort.append(all_times[0])
    t_SelectionSort.append(all_times[1])



def MakeFigure(BubbleX1,BubbleY1,SelectionX1,SelectionY2):
    py.plot(BubbleX1, BubbleY1, label = 'BubbleSort')
    py.plot(SelectionX1, SelectionY2, label = 'SelectionSort')
    py.xlabel('Size of Sample')
    py.ylabel('Average Time')
    py.legend()



MakeFigure(range(2,100), t_BubbleSort, range(2,100), t_SelectionSort)
py.savefig('MoyGraphSort.png')




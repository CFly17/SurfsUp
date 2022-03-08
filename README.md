# Surfs_Up

## Analysis Overview
In this analysis we compare the temperature data between two different months, June and December, over the course of about seven years to determine the viability of opening up a surf shop. 

Fortunately, the Pandas environment allows us to call upon a dataframe with the .describe() method

Here we can see the start and end points for the December dataset:

![image](https://user-images.githubusercontent.com/87148145/157146100-61a5fbe8-9022-47ec-9de4-3b25607a9719.png) ![image](https://user-images.githubusercontent.com/87148145/157146066-64dc2899-ca8d-47a6-933d-05b1149adb59.png)

And the June dataset:

![image](https://user-images.githubusercontent.com/87148145/157146791-210fb87d-a31b-4b99-a0a0-4179df561581.png) ![image](https://user-images.githubusercontent.com/87148145/157146812-81980365-6bc0-4936-b7f5-97df9a9ff8ee.png)


The data is not perfect (what data is?!): June has earlier and later datapoints by about a year. 

But it's enough to analyze. 


## Results
* Curiously enough, the average temperature for June and December wasn't that much different! I highly doubt that tried-and-true surfers would make much fuss about a 4-degree difference, especially when the temperature is still in the 70's:


![June_data](https://user-images.githubusercontent.com/87148145/157147242-31b806cf-9b03-4933-b9f4-a82bf57ceda2.PNG) ![December_data](https://user-images.githubusercontent.com/87148145/157147244-7ab51ba5-20c2-43a0-9e8c-b07d98f3d67b.PNG)



* However, we must follow this point with the notable minimums: December can be nearly 30 degrees colder than the highest temperatures of Summer. 

* Finally, it would be interesting to perform an analysis on surfing interest in sub-60 degree weather. The other factor that might play here is temperament of the surfers: If it was under 60 degrees yesterday, do I really want to take a chance and go out to the water today, even if the forecast says it will be warmer?
 

## Summary
To summarize, the current datasets do not lineup perfectly (they are off by about a year) but they provide us a good snapshot of average temperatures over the course of 6-7 years. Noteably, the average temperature doesn't vary by more than four degrees! That should be no problem if you're willing to wade throug the ocean in the first place.

I would recommend checking the weather of certain weather stations -- I believe there were over half a dozen involved in the first analysis. That might look like this, tacked on to the June or December month queries:

    filter(Measurement.station == 'USC00519281')

Furthermore, each station has different counts (ranging from 511 datapoints to 2772 datapoints, a significant range). I would highly suggest looking at these month comparison charts, putting into context the robustness of the weather station data. That query might look like th following:

    func.count(Measurement.station)


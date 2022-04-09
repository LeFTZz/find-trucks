# **Find Food Trucks** 🌮

## **Summary**

A Python FastApi which supports the input of a latitude, a longitude and the amount of food trucks you need and outputs the nearest food trucks for you.

A Jupyter Notebook version also available [here](https://github.com/LeFTZz/find-trucks/blob/main/notebook.ipynb)

Data source is located [here](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat/data) 

## **Motivation**

Our San Francisco team loves to eat. They are also a team that loves variety, so they also like to discover new places to eat. In fact, we have a particular affection for food trucks. One of the great things about Food Trucks in San Francisco is that the city releases a list of them as open data. It would be good to have the all the information you need for the food trucks in hand wherever you are!

By carrying out this project I am to make it possible for us to find a food truck no matter where our work takes us in the city

## Demo

Bellow is a basic demo of the proposed web api which I used Python FastApi to implement:

Please checkout on this 45 seconds [demo](https://user-images.githubusercontent.com/48968790/162579975-2bd574eb-67d6-44c0-b6dd-300e1e81f3dd.mp4) video.

A less clear version:

![demo](https://user-images.githubusercontent.com/48968790/162579799-656f699c-2058-4b55-b38b-2fa2f96fceec.gif)

## **Detailed Design**

### **Overview**

There are two ways provided to retrieve the data.

1. Jupyter NoteBook
2. Swagger UI for Web api (to be deployed)

For both implementations, I followed the below steps to fetch data:

- Read data from csv file [here](https://github.com/LeFTZz/find-trucks/blob/main/Mobile_Food_Facility_Permit.csv)
- Clean data where the license status isn’t `Approved` and have no information of latitude and longitude
- Calculate the distance between the input position and all available trucks positions
- Sort and return the top K location

The solution is to return all of the information we have for a truck which makes it possible for displaying more detailed data on the front-end. I used geopandas package to help me calculate distance in a neater way.

## **Alternatives**

### CLI Script

Similar to API and Jupyter Notebook we could create a shell script or python script that would allow users to fetch data directly from their console. When comparing this with API and NoteBook, there’re still something different.

***Advantages***

- Provides quicker development cycle
- Could provide an easier workflow to add and make changes than other methods if done right

***Disadvantages***

- Would require the user to have a working laptop with correct environment installed for running shell.
- Less visual feature compared to swagger UI page
- Would require the user to be an engineer and knowledge on shell.

### Vue Web application

With frontend website available it would be a little bit easier to access and fetch the result than an API. It may attract more users into using it as when hosted on somewhere you can directly share the link with each other and may be able to handle some more functions such as login, save favorite food trucks.

 ***Advantages***

- Provides a nicer looking interface to use
- Could be able to support more user-wise functionality
- Removes the barrier to use it for non-engineers

***Disadvantages***

- Would require some time spent on the UI design

## **Unresolved Issues**

#### Error handling

With the current design I didn’t put error handling function due to limited time I spent on this project. A possible enhancement would be add error handle logic for cases like invalid input, no data available

#### Unit testing

Unit tests are good thing to have in a project especially for an project like this which might be scaling in the future or have new engineers working on it. Adding unit tests would reduce the possibility of accidentally breaking some functions.

## **Future Possibilities**

**Website**

An API isn’t the best way of display informations. We could consider using frameworks like Vue or React to generate a front end application so it would be more user friendly.



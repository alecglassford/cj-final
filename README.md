# Biking in the rain != fun

This title may change depending on what the data reveals.

## Elevator pitch

The city of Seattle has set up bike counters at several spots throughout the city and has been keeping track of how many bicycles pass by each hour for the last several years. This app compares the number of bicycles that pass through each of 10 locations; visualizes how ridership has changed between April 2014, 2015, and 2016; and considers the effect of weather on the number of bicycles on the road.

## Inspirations and prior work

* [Seattle Spokane Street Bicycle Counter](http://www.seattle.gov/transportation/bikecounter_spokane.htm)
    * A map showing where this bicycle counter is, customizable timerange, display of bicycle counts during this timerange, graphs of these numbers over time (by day, week, or month) with stacked bars that separate eastbound and westbound
* [Seattle Spokane Street Bicycle Counter (detail)](http://www.seattle.gov/transportation/bikecounter_fremont.htm#detail)
    * Similar to above at a different location, but the detail includes some more aggregate data embedded as a Tableau Workbook: comparisons between months in several different graph forms, ridership by day of the week, and, notably, a couple of customizable graphs of weather vs bike numbers: can use precipitation, windspeed, etc. and see one graph comparing the variables (weather, ridership) directly as a scatter and another which plots each variable over the course of a week
* [2015 Fremont Bridge bike counts have broken records every month so far](http://www.seattlebikeblog.com/2015/04/10/2015-fremont-bridge-bike-counts-have-broken-records-every-month-so-far/)
    * Trying to tell a narrative with this data: a simple graph with a set of bars for each month; each set has 3 bars, 1 each for the past 3 years of ridership. Clearly shows that the most recent bars in 2015 beat the previous years' numbers for each month.
* [Fremont Bridge smashes bike count record (for real this time) + Bike use rises all over town](http://www.seattlebikeblog.com/2014/05/14/fremont-bridge-smashes-bike-count-record-for-real-this-time-bike-use-rises-all-over-town/)
    * Ridership plotted over several months for a couple of counters, small multiples (bar charts) for each bike counter that show ridership numbers over last 4 months (broken down by direction of biking in each month)
* [Is Seattle Really Seeing an Uptick In Cycling?](https://jakevdp.github.io/blog/2014/06/10/is-seattle-really-seeing-an-uptick-in-cycling/)
    * An iPython notebook that does statistical analyses of the effects of different factors (# daylight hours, precipitation, etc.) - very detailed walkthrough that dives into how different environmental factors affect ridership

## Data sources

1. [10 up to date hourly bicycle counters](https://data.seattle.gov/browse?limitTo=datasets&utf8=%E2%9C%93&q=bicycle%20counter&sortBy=last_modified)at different locations in Seattle, form the Seattle open data portal
2. [The Dark Sky Forecast API](https://developer.forecast.io/docs/v2#time_call) which gives a nice summary of weather data from a location at a certain point of time, including many metrics (precipitation intensity, wind speed, temperature, moon phase, etc.) and nice categorical summaries of the weather at the time (rain, partly-cloudy-day, clear, etc.)

## Slimming the data

I'm using the hourly data from each of 10 locations from the last 3 Aprils (2014, 2015, 2016). This gives 10 locations * 3 years * 31 days * 24 hours = 22,320 data points. Comparing year over year probably gives the most intelligible data over time, and April is a month that likely has a variety of weather (and is recent). I'm currently planning to use shared weather data between the 10 locations point, assuming (perhaps wrongly, but I don't think the data necessarily has better resolution than this) that the weather is roughly the same throughout the city of Seattle at any time (i.e. only 2,320 weather data points).

## Joining the data

The bicycle counts and weather will be joined by the date-time attribute.

## New categorical variable

The weather data gives some nice categories of weather already (see above), but I think a more coarse grained binary category of precipitation/no-precipitation will be revealing.

## New continuous variable

For any given time, how does each location compare to the others? I.e. a ranking from 1 to 10 of how busy it is.

## Filtering options

Filter by weather. Filter by day of the week. Filter by time of day. Filter/sort by location. Sort by year.

## Views

The atomic view will be the time point (e.g. 11am on April 3 - will show data for all locations and all 3 years at that time). In the filtering view you'll be able to see rows for each year separately though.

## Visualizations

Probably a map to let you filter by location. Several different charts for different types of queries. In the atomic view, charts of ridership year over year.

## Deployment

Hopefully with Frozen-Flask

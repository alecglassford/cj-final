# Concept and documentation

## App name: ["231 drought maps show just how thirsty California has become"](http://www.latimes.com/local/lanow/la-me-g-california-drought-map-htmlstory.html) by the LA Times

## Elevator Pitch

The drought in California has become a widespread and longterm problem. This simple visualization shows the extent of drought (maps have regions ratings ranging from normal to "exceptional drought") throughout California from 2012 through the present, week by week, giving a sense of the drought's evolution and also its timescale.

## Inspirations and Prior work

* [U.S. Drought Monitor](http://droughtmonitor.unl.edu/Home.aspx) from the National Drought Mitigation Center/University of Nebraska Lincoln
    * The source of data for the LA Times app (as well as other apps below). Has raw GIS data available
    * Has its own map of U.S. drought, can zoom in by state (e.g. California) and also access old maps, but the focus of the display is on present situation
    * Not necessarily "sleek"—more interested in being a comphrensive source of information about drought throughout the country
* [Esri Drought Tracker](http://livingatlas.arcgis.com/drought/)
    * Javascript map of the U.S., with the same data as the U.S. Drought Monitor's map (^) but is more interactive: can drag, zoom, click
    * Clicking on a county leads to a pop up with a somewhat confusing chart over time (actually a pair: one that's year over year, another that covers the previous 8 weeks). They show what percentage of the county as drought levels of dry/moderate/severe/extreme/exceptional. This is somewhat confusing since most counties are entirely of one category, so much of the chart is at 100% or 0% at all points.
    * When the charts come up, however, a bar also pops up at the bottom of the screen which shows similar situation but in a much more legible stacked bar portion, with a slide that lets you move throughout time (transforming the entire map as you do). This feature seems much more helpful than the charts pop-up
* [California's Long Challenge With Drought](http://graphics.wsj.com/californias-long-challenge-with-drought/) by the Wall Street Journal
    * The first portion of this app is similar to above (with same data source, it seems), but zoomed in just on California: a map that shows different drought levels throughout the state, with a slider that lets you progress through time (notably only through November 2015). Nice feature of circles showing affected population
    * Also integrates other data sources: Storage levels of various reservoirs throughout the state at three different time points, charts of precipitation levels and temperature by month over a 100+ year period
* [How the Drought is Shrinking California's Reservoirs](http://ww2.kqed.org/lowdown/2014/03/18/into-the-drought-californias-shrinking-reservoirs/) by KQED
    * A similar map of reservoirs as the WSJ app (from the same data source, it seems) this one with more time points and a scroll bar that takes you through them (you can also hit "play" to watch the map move through time in a little animation)
    * Also provides charts of reservoir capacity over time for each reservoir
* [How Has the Drought Affected California's Water Use?](http://www.nytimes.com/interactive/2015/04/01/us/water-use-in-california.html) by the New York Times
    * A large map of California with three different choices of visualization (tabs to select which one you want): change in water consumption, by community between two fixed dates; sizes of proposed water cuts by different districts; daily water use per capita by community with two choices for dates
    * Detail info boxes prelayered over certain bubles on the map to provide specific information and context

## Data

As described above, data is from [U.S. Drought Monitor](http://droughtmonitor.unl.edu/Home.aspx). It's updated weekly, and probably processed through some pipeline that gathers only the California GIS data and redraws the California map to the LA Times style specifications and outputs a PNG for each weekly map (the regions are the same as the Drought Monitor maps but the coloring is slightly different).

I don't think this dataset meets all the requirements for the project (creating a categorical variable, creating a continuous variable, joining datasets). Oops.

## Filtering options

Oops also doesn't apply here. I just picked an app that I thought told an important story in a great way. :(


## Visualizations (Maps)

The innovation of this app over others is its display of all maps from 2012 to the present on a single page, so viewers can engage with the drastic change over time (and the temporal extent of intense drought conditions) in a very striking way.

This is bolstered by the apparent auto-updates every week.

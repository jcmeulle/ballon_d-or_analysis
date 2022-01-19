# Ballon D'Or Analysis

This repository holds all the code for my side project using clustering to analyze the relative abilities of the 2021 Ballon D'Or candidates.
Soon, I'll add a Github article to talk about my findings and visualizations.

## Files

The "players" folder contains each player's statistics for the season.

In "fbrefmarkdown," I clean and merge the player data into a single dataframe, then do the analysis.

In "pltstuff", I make some plotly radar charts to profile each cluster. These are hosted on my plotly account.

In "fbclust.twb", I make the Tableau visualization of the clusters. It is also hosted online on my Tableau public account.

## Project Intro

The Ballon D'or is the biggest award in international soccer. Every winter, it is awarded to the overall "best" player in the world. This year's award was given on November 29, and coincidentally, around then I learned about clustering in my master's program. When we talked about k-means clustering, I  wondered if the algorithm could tell between the "types" of soccer players.

For this project, I took data from FBRef, a website with all kinds of per-match data on soccer players, on each of the 30 nominees for the 2021 Ballon D'Or. Then, I used R, Python, and Tableau to restructure, analyze, and visualize the data.

I clustered the players with k-means clustering so I could get a few groups of players that made sense in a soccer context before profiling them by these groups.

## Clustering

To actually cluster the players, I used k-means on normalized data. I tried some different numbers of clusters and looked at them in terms of soccer sense and mathematical sense. 6 clusters ended up making sense both soccer-wise and by the gap statistic!

Here's how the clusters looked after plotting them in Tableau:

<iframe src="https://public.tableau.com/app/profile/jack.meullenet/viz/fbclust/Sheet2"></iframe>

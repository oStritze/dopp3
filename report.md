# Report

## Which datasets did you choose? Why?
- Total Population by Sex: https://population.un.org/wpp/Download/Standard/CSV/ (Subgroup Population, File: All variants (CSV, 19.39 MB))
- Fragile State index: https://fragilestatesindex.org/excel/ 2006-2019
- Period Indicatiors: https://population.un.org/wpp/Download/Standard/CSV/ (Period Indicators, File: Medium variant (most used) (CSV, 2.41 MB))

We stated the assumption that, the state stability index of a country correlates with the migration of a country. To prove that assumption, we need three different datasets: (1) A dataset, containing the total population of a country from 1950 - 2019; (2) A dataset, in which the total ranking of a state, and other factors like the security apparatus and public services are available in numbers. The data reach from 2006 - 2019. (3) A dataset, which contains multiple indicators of a countries population, e.g. the birth- and deathrate. Interesting for us, in this dataset, is the relative migration of a country. The data is available from 1950 - 2019.
With these three datasets, we can compute the correlation between a country's migration-rate and various stability indicators of a country.

## How did you clean/transform the data? Why?

The population, and population indicators datasets had estimations for the years after 2019. We dropped them because we want to estimate them ourself. We also had to drop the years prior o 2006, because the state stability index were only available for the years 2006 - 2019.

The cleaning process included date formatting, removing unnecessary columns and aggregating population data in an interval.

As the final preparation we merged the three dataset.

## How did you solve the problem of missing values? Why?

We had none

## What question did you ask of the data? Why were these good questions?

(1) Are there typical characteristics of refugee origin and destination countries?



(2) Can countries that will produce large numbers of refugees be predicted?


## What were the answers to these questions? How did you obtain them? Do the answers make sense?

We assumed that, state stability and population growth rate are strongly correlated to a country's migration rate. This assumption is an obvious one and we selected the most important features of our trained model and gained the insight that indeed, the growth rate and economy are the most influencal parameters. To obtain this insight, we trained a RandomForestClassifier and a RidgeClassifier on the data with the migration as target variable.
TODO: Inser bild mit den wichtigsten features 



##  Were there any difficulties in analysing the data? What were the key insights contained?

## Which Data Science tools and techniques were learned during this exercise?

Search for data:
Data cleaning:
Model training:
Performance measure:

Python:
Jupyter:
Pandas:
SKLearn:


## How was the work divided up between the members of the group?


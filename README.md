# dopp3
## Question 14:  
What is the most accurate overview of flows of refugees between countries that can be obtained? Are there typical characteristics of refugee origin and destination countries? Are there typical characteristics of large flows of refugees? Can countries that will produce large numbers of refugees be predicted? Can refugee flows be predicted?

## Main Questions that we want to answer
- Datasets used:
    - state stability index: clean/fragile_states_index.csv
    - united nations: period_indicator_medium.csv
    - populations_dataset: clean/population_by_age.csv
1.  Are there typical characteristics of refugee origin and destination countries?
    - We understand that this question tries to specify why people go from a to b
    - Refugees are not refugees because of economic reasons alone, must be something else (that is what Hanbury said)
2. Can countries that will produce large numbers of refugees be predicted?
    - We understand that this question tries to identify features which are important for migration

## How we answer questions?
- use relative number for immigration/migration numbers (total divided by number of inhabitants)
1. Merge state stability index with new UN dataset (period_indicators_medium) and total population dataset. 
    - merge population_by_age.csv with population_total.csv 
    - Make a feature selection/PCA, for migration and immigration countries (may have different features)
2. Classify same data and test/train different models for classification (with 10fold CV). No regression, only classification
    - define variable to predict 
    - from number of migrants/immigrants, define a scale (0-1 or 0,1,2,3,4,5) for migration (high/medium/ low numbers)


---
**NOTE**

Please Comment code appropriately 

---


## TODOs
### Prepare Data
- [x] Choose Datasets
- [x] Prepare Datasets (michi, oli)
- [x] Merge Datasets 
- [x] Check what to do with missing values, if there
- [x] Check what to do with outliers, if there
- [ ] Fix missing countries
- [ ] Rerun analysis with new fixed data set
### Explore Data
#### Task 1 
- [ ] make some findings and statements
- [x] statistical moments, means, etc?
- [x] simple visualizations (corr heatmap, ...)
- [x] PCA / feature analysis (raphael)
#### Task 2 Model Data Classifier
- [ ] try different models 
- [ ] find best model with CV and parameter tuning (gridsearch)
### Visualize Data 
- [ ] some interesting visualizations
### Finalize Hand in 
- [ ] finalize Jupyter Notebook + Data (final hand-in must be in this form)
### Presentation 
- 10 mins 
- audience is data scientists (students)
### Write Report (max 2 pages) 
- Intended for Management
- Key Findings and why they make sense + visualizations


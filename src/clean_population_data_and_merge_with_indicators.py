import streamlit as st
import pandas as pd
import numpy as np


# read cleaned population_total data
pop_total = pd.read_csv("../data/clean/population_total.csv", sep=",", na_values='')
pop_total.set_index(['Year', 'Country'], inplace=True)
st.write(pop_total)
#print(pop_total[pop_total['PopTotal']<0])

# read cleaned population_per_age group data
pop_per_age = pd.read_csv("../data/clean/population_per_age.csv", sep=",", na_values='')
pop_per_age.set_index(['Year', 'Country'], inplace=True)
# drop code since it's not available for merges later anyway
pop_per_age.drop(columns="Code", inplace=True)

# create 3 df's for each group and sum the values for each year and country
pop_per_age_young = pop_per_age.query('AgeGrp in ["0-4", "5-9", "10-14", "15-19"]').sum(level=['Year', 'Country'])
pop_per_age_young.rename(columns={"PopMale": "PopMale_0-19", "PopFemale": "PopFemale_0-19", "PopTotal" : "PopTotal_0-19"}, inplace=True)
pop_per_age_mid = pop_per_age.query('AgeGrp in ["20-24", "25-29", "30-34", "35-39", "40-44", "45-49","50-54", "55-59"]').sum(level=['Year', 'Country'])
pop_per_age_mid.rename(columns={"PopMale": "PopMale_20-59", "PopFemale": "PopFemale_20-59", "PopTotal" : "PopTotal_20-59"}, inplace=True)
pop_per_age_old = pop_per_age.query('AgeGrp in ["60-64", "65-69", "70-74", "75-79", "80-84", "85-89", "90-94", "95-99", "100+"]').sum(level=['Year', 'Country'])
pop_per_age_old.rename(columns={"PopMale": "PopMale_60+", "PopFemale": "PopFemale_60+", "PopTotal" : "PopTotal_60+"}, inplace=True)

# merge all groups to one big df
pop_with_groups = pop_per_age_young.merge(pop_per_age_mid, left_index=True, right_index=True)
pop_with_groups = pop_with_groups.merge(pop_per_age_old, left_index=True, right_index=True)
pop_total_with_groups = pop_total.merge(pop_with_groups, left_index=True, right_index=True)

# load indicators dataset
indicators = pd.read_csv("../data/raw/WPP2019_Period_Indicators_Medium.csv", sep=",", na_values=''
# ,dtype={"Deaths":"int64", "DeathsMale":"int64", "DeathsFemale":"int64", "NetMigrations":"int64"}
 )
# convert readable per 1000 values to ints
indicators[["Births", "Deaths", "DeathsMale", "DeathsFemale", "NetMigrations"]] = (indicators[["Births", "Deaths", "DeathsMale", "DeathsFemale", "NetMigrations"]].fillna(0) * 1000 / 5).astype("int64")
#indicators['RelMigrations'] = indicators[]
indicators_pop = indicators.merge(pop_total_with_groups, left_on=['MidPeriod','Location'], right_on=['Year','Country'])
indicators_pop["RelMigrations"] = indicators_pop["NetMigrations"]/indicators_pop["PopTotal"]
indicators_pop.drop(columns=['VarID', 'Variant'], inplace=True)
indicators_pop.rename(columns={"Location" : "Country"}, inplace=True)
st.write(indicators_pop)

# save df
indicators_pop.to_csv(index=False, path_or_buf="../data/clean/population_indicators.csv")

# read fragile states data
fragile_states = pd.read_csv("../data/clean/fragile_states_index.csv", sep=",", na_values='')
st.write(fragile_states.shape)
st.write(fragile_states)
st.write(indicators_pop.shape)
full_set = indicators_pop.merge(fragile_states, left_on=['Country','MidPeriod'], right_on=['country','year'])

query_result = full_set.query("Time == '2005-2010'")
full_set.loc[query_result.index, "change_from_previous_year"] = pd.Series(0, index=query_result.index)
previous = query_result
for years in ["2010-2015", "2015-2020"]:
    query_result = full_set.query("Time == '" + years + "'")
    full_set.loc[query_result.index, "change_from_previous_year"] = \
        (query_result.set_index("Country")["total"] - previous.set_index("Country")["total"]).round(1).fillna(0).to_numpy()
    previous = full_set.loc[query_result.index, :]
st.write(full_set.shape)
st.write(full_set)
full_set.to_csv(index=False, path_or_buf="../data/clean/full_set.csv")

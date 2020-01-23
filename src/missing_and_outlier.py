import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats
import streamlit as st

if __name__ == '__main__':
	full_df = pd.read_csv("../data/clean/full_set.csv")
	st.markdown("# Missing Values")
	st.write(full_df.isnull().any())

	st.markdown("# Boxplots and Histograms")
	st.markdown("## Drop useless columns")
	drop_cols = ["LocID", "Country", "Time", "MidPeriod", "Code", "Unnamed: 0", "country", "year", "ranking"]
	st.write(drop_cols)
	small_df = full_df.drop(columns=drop_cols)

	st.markdown("## Plot those with more than 3 outliers")
	plot_cols = [column for column in small_df.columns if len([y for stat in boxplot_stats(small_df[column]) for y in stat['fliers']]) > 3]
	st.write(plot_cols)
	_, axes = plt.subplots(nrows=len(plot_cols), ncols=2, figsize=(10, 150))
	for i, column in enumerate(plot_cols):
		small_df.boxplot(column=column, ax=axes[i][0])
		small_df.hist(column=column, ax=axes[i][1])
	st.pyplot()

	st.markdown("## Print rows of max outliers")
	max_indices = small_df[plot_cols].idxmax(axis=0)
	for column in ["Deaths", "DeathsMale", "DeathsFemale", "CNMR", "GrowthRate", "RelMigrations", "change_from_previous_year"]:
		st.write(column + " with mean " + str(round(full_df[column].mean())), full_df.loc[max_indices[column], :])

	st.write("Correlation of CNMR to", full_df[["GrowthRate", "RelMigrations"]].corrwith(full_df["CNMR"]).sort_values(ascending=False))
	st.write("Correlation of GrowthRate to", full_df[["RelMigrations"]].corrwith(full_df["GrowthRate"]).sort_values(ascending=False))
	st.write("All outliers seem to be correct ones (no incorrect values). "
			 "Outliers regarding the deaths belong to Lesotho, which seems reasonable, since it's an unstable country. "
			 "The outliers in Growth rate, CNMR, and RelMigration all correlate to each other and all belong to Qatar. "
			 "Thus the probability of correctness of the data is high.")
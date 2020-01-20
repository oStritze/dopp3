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
	drop_cols = ["LocID", "Country", "Time", "MidPeriod", "Code", "Unnamed: 0", "country", "year", "ranking"] \
				+ [pop_col for pop_col in full_df.columns if "Pop" in pop_col]
	st.write(drop_cols)
	full_df.drop(columns=drop_cols, inplace=True)

	st.markdown("## Plot those with more than 3 outliers")
	plot_cols = [column for column in full_df.columns if len([y for stat in boxplot_stats(full_df[column]) for y in stat['fliers']]) > 3]
	st.write(plot_cols)
	_, axes = plt.subplots(nrows=len(plot_cols), ncols=2, figsize=(10, 150))
	for i, column in enumerate(plot_cols):
		full_df.boxplot(column=column, ax=axes[i][0])
		full_df.hist(column=column, ax=axes[i][1])
	st.pyplot()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats
import streamlit as st
import seaborn as sns

def plot_heat_map_quarter(x1, x2, y1, y2):
	plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False, labeltop=True)
	ax = sns.heatmap(corr.iloc[x1:x2, y1:y2], vmin=-1, vmax=1, center=0,
					 cmap=sns.diverging_palette(20, 220, n=200), square=True)
	ax.set_xticklabels(ax.get_xticklabels(), rotation=-45, horizontalalignment='right', fontsize=14)
	ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=14)
	st.pyplot()

if __name__ == '__main__':
	full_df = pd.read_csv("../data/clean/full_set.csv")
	st.markdown("# Descriptive Statistics")
	st.markdown("## Drop useless columns")
	drop_cols = ["LocID", "Country", "Time", "MidPeriod", "Code", "Unnamed: 0", "country", "year", "ranking"]
	st.write(drop_cols)
	small_df = full_df.drop(columns=drop_cols)

	st.markdown("## Print statistics")
	st.write(small_df.describe())

	st.markdown("## Plot heat map")
	corr = small_df.corr()
	plt.figure(figsize=(20, 20))
	plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, bottom=False, top=False, labeltop=True)
	ax = sns.heatmap(corr.iloc[:, :], vmin=-1, vmax=1, center=0,
					 cmap=sns.diverging_palette(20, 220, n=200), square=True)
	ax.set_xticklabels(ax.get_xticklabels(), rotation=-45, horizontalalignment='right', fontsize=10)
	ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
	st.pyplot()
	st.write("The heat map shows that there are some bigger blocks in which the variable are strongly correlated to each other, "
			 "e.g. TFR, NRR, CBR, Birth (all describe some birth statistics). An interesting observation for the population "
			 "is that the numbers in age group 0-19 strongly correlate to each other but have also string anticorrelation "
			 "to the numbers in age group 60+, i.e. high number of young means low older people and vice versa. But there "
			 "are some variables which are independet from most of the others, like CNMR, NetMigration, RelMigration, PopTotal. "
			 "Also interesting, that a high fragile state index correlates with high TFR, high ratio of young population, "
			 "and low olders.")

	st.markdown("## Scatter plots")
	plt.scatter(x=full_df["GrowthRate"], y=full_df["RelMigrations"])
	plt.xlabel("GrowthRate")
	plt.ylabel("RelMigrations")
	st.pyplot()

	plt.scatter(x=full_df["PopMale_20-59"], y=full_df["RelMigrations"])
	plt.xlabel("PopMale_20-59")
	plt.ylabel("RelMigrations")
	st.pyplot()
	st.markdown("`RelMigrations` and `PopMale_20-59` have the highest feature importance according to our tests. "
				"This can also be expressed by the two scatter plots. A high value for both variables indicate high migration.")
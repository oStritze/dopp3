import pandas as pd
import numpy as np
import os


def prepare_total_pop():
    with open(os.getcwd() + "/../data/raw/population/WPP2019_TotalPopulationBySex.csv") as f:
        total_pop = pd.read_csv(f, engine="python")
    print(total_pop.columns)

    print("shape", total_pop.shape)
    total_pop = total_pop[total_pop["Time"] < 2020]
    print("shape", total_pop.shape)

    print("Variant values", total_pop["Variant"].unique())
    print("MidPeriod values", total_pop["MidPeriod"].unique())
    total_pop.drop(columns=["VarID", "Variant", "MidPeriod"], inplace=True)

    total_pop.columns = ["Code", "Country", "Year", "PopMale", "PopFemale", "PopTotal"]
    total_pop.set_index(["Country", "Year"], inplace=True)

    total_pop[["PopMale", "PopFemale", "PopTotal"]] = (total_pop[["PopMale", "PopFemale", "PopTotal"]].fillna(0) * 1000).astype(int)
    return total_pop


def prepare_age_pop():
    with open(os.getcwd() + "/../data/raw/population/WPP2019_PopulationByAgeSex_Medium.csv") as f:
        age_pop = pd.read_csv(f, engine="python")
    print(age_pop.columns)

    print("shape", age_pop.shape)
    age_pop = age_pop[age_pop["Time"] < 2020]
    print("shape", age_pop.shape)

    print("Variant values", age_pop["Variant"].unique())
    print("MidPeriod values", age_pop["MidPeriod"].unique())
    age_pop.drop(columns=["VarID", "Variant", "MidPeriod", "AgeGrpStart", "AgeGrpSpan"], inplace=True)

    age_pop.columns = ["Code", "Country", "Year", "AgeGrp", "PopMale", "PopFemale", "PopTotal"]
    print("AgeGrp values", age_pop["AgeGrp"].unique())
    age_pop.set_index(["Country", "Year", "AgeGrp"], inplace=True)

    age_pop[["PopMale", "PopFemale", "PopTotal"]] = (age_pop[["PopMale", "PopFemale", "PopTotal"]].fillna(0) * 1000).astype(int)
    return age_pop


if __name__ == '__main__':
    total_pop = prepare_total_pop()
    age_pop = prepare_age_pop()

    print(total_pop.head(2))
    print(age_pop.head(2))


    total_pop.to_csv("./../data/clean/population_total.csv")
    age_pop.to_csv("./../data/clean/population_per_age.csv")
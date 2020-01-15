import pandas as pd

years = list(range(2006,2020))

dfs = []
for year in years:
    df = pd.read_excel("../data/raw/fragile_states_index/fragile_states_index_" + str(year) + ".xlsx")
    df = df.assign(Year=[str(s).split('-')[0] for s in df['Year']])
    df = df.assign(Rank=[str(s)[:-2] for s in df['Rank']])
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True, sort=False)

df.columns = ['country', 'year', 'ranking', 'total', 'security_apparatus',
       'factionalized_elites', 'group_grievance', 'economy',
       'economic_inequality', 'human_flight_and_brain_drain',
       'state_legitimacy', 'public_services', 'human_rights',
       'demographic_pressures', 'refugees_and_idps',
       'external_intervention', 'change_from_previous_year']

df.to_csv("../data/clean/fragile_states_index.csv")
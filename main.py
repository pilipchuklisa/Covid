import pandas as pd
import matplotlib.pyplot as plt

confirmed_url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'
deaths_url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'
recovered_url = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'

confirmed_df = pd.read_csv(confirmed_url)

countries = confirmed_df['Country/Region'].unique().tolist()
categories = ['Confirmed', 'Recovered', 'Deaths']

print("List of available countries:")
for country in countries:
    print(country)

selected_country = input("Enter the country: ")
selected_category = input("Enter the category (Confirmed/Recovered/Deaths): ")

if selected_category == 'Confirmed':
    df_country = confirmed_df[confirmed_df['Country/Region'] == selected_country]
elif selected_category == 'Recovered':
    recovered_df = pd.read_csv(recovered_url)
    df_country = recovered_df[recovered_df['Country/Region'] == selected_country]
elif selected_category == 'Deaths':
    deaths_df = pd.read_csv(deaths_url)
    df_country = deaths_df[deaths_df['Country/Region'] == selected_country]

df_category = df_country.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long']).sum()

df_daily_increase = df_category.diff().fillna(df_category.iloc[0]).astype(int)

plt.figure(figsize=(12, 8))
plt.plot(df_category.index, df_category.values, label=selected_category)
plt.plot(df_daily_increase.index, df_daily_increase.values, label='Daily Increase')
plt.title(f"{selected_country} - {selected_category}")
plt.xlabel("Date")
plt.ylabel("# of Cases")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

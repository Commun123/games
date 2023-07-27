import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('vgsales.csv')

def get_top_selling_games_by_platform_and_year(platform, year):
    filtered_data = data[(data['Platform'] == platform) & (data['Year'] == year)]
    top_selling_games = filtered_data.nlargest(10, 'Global_Sales')
    return top_selling_games

def main():
    st.title('Top Selling Video Games by Platform and Year')

    platform_list = data['Platform'].unique()
    platform = st.selectbox('Select Platform', platform_list)

    year_list = data['Year'].unique()
    year = st.selectbox('Select Year', year_list)

    if st.button('Show Top Selling Games'):
        top_selling_games = get_top_selling_games_by_platform_and_year(platform, year)
        st.dataframe(top_selling_games)

        # Plot bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(top_selling_games['Name'], top_selling_games['Global_Sales'])
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Game Name')
        plt.ylabel('Global Sales (in millions)')
        plt.title(f'Top Selling Games in {year} - {platform}')
        st.pyplot()

if __name__ == '__main__':
    main()

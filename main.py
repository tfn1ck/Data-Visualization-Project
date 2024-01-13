import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px

bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:brown']


def load_data():
    return pd.read_csv('./Crypto.csv', parse_dates=['Date']).copy()


# PATH = load_data()


def get_volume_chart_all():
    PATH = load_data()
    columns_to_plot = ['Volume (BTC)', 'Volume (ETH)', 'Volume (USDT)', 'Volume (BNB)']

    PATH.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 8))
    sns.set(style="darkgrid")

    for column in columns_to_plot:
        plt.plot(PATH.index, PATH[column], label=column)

    plt.title('Cryptocurrency Trading Volumes Comparison')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    plt.show()


def get_closing_chart_all():
    PATH = load_data()
    columns_to_plot = ['Close (BTC)', 'Close (ETH)', 'Close (USDT)', 'Close (BNB)']

    PATH.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 8))
    sns.set(style="darkgrid")

    for column in columns_to_plot:
        plt.plot(PATH.index, PATH[column], label=column)

    plt.title('Cryptocurrency Closing Values Comparison')
    plt.xlabel('Date')
    plt.ylabel('Close')
    plt.legend()
    plt.show()


def get_BTC_chart_volume():
    PATH = load_data()
    columns_to_plot = ['Volume (BTC)']
    PATH.set_index('Date', inplace=True)
    df_yearly = PATH[columns_to_plot].resample('Y').sum()

    plt.figure(figsize=(10, 8))
    sns.set_palette("pastel")
    sns.set(style="darkgrid")

    years = df_yearly.index.year

    plt.bar(years, df_yearly['Volume (BTC)'], color=bar_colors)
    plt.title('Yearly Cryptocurrency Trading Volume for BTC')
    plt.xlabel('Year')
    plt.ylabel('Total Volume (BTC)')
    plt.show()


def get_ETH_chart_volume():
    PATH = load_data()
    columns_to_plot = ['Volume (ETH)']
    PATH.set_index('Date', inplace=True)
    df_yearly = PATH[columns_to_plot].resample('Y').sum()

    plt.figure(figsize=(10, 8))
    sns.set_palette("pastel")
    sns.set(style="darkgrid")

    years = df_yearly.index.year

    plt.bar(years, df_yearly['Volume (ETH)'], color=bar_colors)
    plt.title('Yearly Cryptocurrency Trading Volume for ETH')
    plt.xlabel('Year')
    plt.ylabel('Total Volume (ETH)')
    plt.show()


def get_USDT_chart_volume():
    PATH = load_data()
    columns_to_plot = ['Volume (USDT)']
    PATH.set_index('Date', inplace=True)
    df_yearly = PATH[columns_to_plot].resample('Y').sum()

    plt.figure(figsize=(10, 8))
    sns.set_palette("pastel")
    sns.set(style="darkgrid")

    years = df_yearly.index.year

    plt.bar(years, df_yearly['Volume (USDT)'], color=bar_colors)
    plt.title('Yearly Cryptocurrency Trading Volume for USDT')
    plt.xlabel('Year')
    plt.ylabel('Total Volume (USDT)')
    plt.show()


def get_BTC_chart_Close():
    PATH = load_data()
    columns_to_plot = ['Close (BTC)']

    PATH.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 8))
    sns.set_palette("husl")
    sns.set(style="darkgrid")
    plt.plot(PATH.index, PATH[columns_to_plot], label='Close (BTC)', color='forestgreen', linewidth=2)

    plt.title('Cryptocurrency Closing Values for BTC')
    plt.xlabel('Date')
    plt.ylabel('Closing Value (BTC)')
    plt.legend()
    plt.show()


def get_ETH_chart_Close():
    PATH = load_data()
    columns_to_plot = ['Close (ETH)']

    PATH.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 8))
    sns.color_palette("tab10")
    sns.set(style="darkgrid")
    plt.plot(PATH.index, PATH[columns_to_plot], label='Close (ETH)', color='coral', linewidth=2,)

    plt.title('Cryptocurrency Closing Values for ETH')
    plt.xlabel('Date')
    plt.ylabel('Closing Value (ETH)')
    plt.legend()
    plt.show()


def get_USDT_chart_Close():
    PATH = load_data()
    columns_to_plot = ['Close (USDT)']

    PATH.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 8))
    sns.set_palette("husl")
    sns.set(style="darkgrid")
    plt.plot(PATH.index, PATH[columns_to_plot], label='Close (USDT)', color='dodgerblue', linewidth=2)

    plt.title('Cryptocurrency Closing Values for USDT')
    plt.xlabel('Date')
    plt.ylabel('Closing Value (USDT)')
    plt.legend()
    plt.show()


def get_BNB_chart_volume():
        PATH = load_data()
        columns_to_plot = ['Volume (BNB)']
        PATH.set_index('Date', inplace=True)
        df_yearly = PATH[columns_to_plot].resample('Y').sum()

        plt.figure(figsize=(10, 8))
        sns.set_palette("pastel")
        sns.set(style="darkgrid")

        years = df_yearly.index.year

        plt.bar(years, df_yearly['Volume (BNB)'], color=bar_colors)
        plt.title('Yearly Cryptocurrency Trading Volume for BNB')
        plt.xlabel('Year')
        plt.ylabel('Total Volume (BNB)')
        plt.show()


def get_BNB_chart_Close():
    PATH = load_data()
    columns_to_plot = ['Close (BNB)']

    PATH.set_index('Date', inplace=True)

    plt.figure(figsize=(10, 8))
    sns.set_palette("husl")
    sns.set(style="darkgrid")
    plt.plot(PATH.index, PATH[columns_to_plot], label='Close (BNB)', color='fuchsia', linewidth=2)

    plt.title('Cryptocurrency Closing Values for BNB')
    plt.xlabel('Date')
    plt.ylabel('Closing Value (BNB)')
    plt.legend()
    plt.show()


def get_volume_pie_chart():
    PATH = load_data()
    columns_to_plot = ['Volume (BTC)', 'Volume (ETH)', 'Volume (USDT)', 'Volume (BNB)']
    total_volumes = PATH[columns_to_plot].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(total_volumes, labels=total_volumes.index, autopct='%1.1f%%', startangle=90)
    plt.title('Cryptocurrency Trading Volumes Distribution')
    plt.show()


if __name__ == '__main__':
    running = True
    print("**********CRYPTO CURRENCY DATA ANALYSIS**********\n")
    print("*****THIS ANALYSIS IS BASED ON VOLUME & CLOSING NUMBERS OF CRYPTO COINS OVER THE YEARS*****\n")

    while running:
        try:
            choice = int(input("----PLEASE CHOOSE ONE AMONG THE FOLLOWING TO VIEW----\n"
                               "1. SHOW ALL VOLUME COMPARISON\n2. SHOW ALL CLOSING COMPARISON\n"
                               "3. SHOW BTC VOLUME CHART\n4. SHOW BTC CLOSING CHART\n"
                               "5. SHOW ETH VOLUME CHART\n6. SHOW ETH CLOSING CHART\n"
                               "7. SHOW USDT VOLUME CHART\n8. SHOW USDT CLOSING CHART\n"
                               "9. SHOW BNB VOLUME CHART\n10. SHOW BNB CLOSING CHART\n"
                               "11. SHOW THE VOLUME PIE CHART\n "
                               "0. PRESS 0 TO EXIT\nENTER YOUR CHOICE FROM ABOVE:- "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if choice == 1:
            get_volume_chart_all()
        elif choice == 2:
            get_closing_chart_all()
        elif choice == 3:
            get_BTC_chart_volume()
        elif choice == 4:
            get_BTC_chart_Close()
        elif choice == 5:
            get_ETH_chart_volume()
        elif choice == 6:
            get_ETH_chart_Close()
        elif choice == 7:
            get_USDT_chart_volume()
        elif choice == 8:
            get_USDT_chart_Close()
        elif choice == 9:
            get_BNB_chart_volume()
        elif choice == 10:
            get_BNB_chart_Close()
        elif choice == 11:
            get_volume_pie_chart()
        elif choice == 0:
            print("Thank you for Viewing the Project :)")
            running = False
        else:
            print("Invalid choice. Please enter a valid option.")

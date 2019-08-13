import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Are you excited to explore bikesahring data? /n Which city's data would you like to see? New York, Chicago, Washington (Choose one):").lower()
        if city not in ('new York', 'chicago', 'washington'):
            print("\n(ERROR) Make sure you are using a capital letter for the first letter in each city: Ex. (N)ew (Y)ork.\n")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to see? January, February, March, April, May, June or All (Choose one):").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("\n(ERROR) Make sure you are using a capital letter for the first letter in each month: Ex. (J)une")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day would you like to see? Sunday, Monday, Tuesday,        Wednesday, Thursday, Friday, Saturday, or All (Choose one):").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
             print("\n(ERROR) Make sure you are using a capital letter for the first letter in each day: Ex. (S)unday")
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    elif day != 'all':
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day) + 1
        df = df[df['day'] == day]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('This is the most common month')
    common_month = df['month'].value_counts().max()
    print ('Most Common Month:', common_month)


    # TO DO: display the most common day of week
    print('This is the most common day of the week')
    common_day = df['Day_of_week'].value_counts().max()
    print ('Most Common Day:', common_day)

    # TO DO: display the most common start hour
    print('This is the most common start hour')
    common_hour = df['Hour'].value_counts().max()
    print ('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('This is the most used start station')
    most_used_station = df['Start Station'].value_counts().max()
    print('Most common station:', most_used_station)

    # TO DO: display most commonly used end station
    print('This is the most used start station')
    most_used_station = df['Start Station'].value_counts().max()
    print('Most common station:', most_used_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('This is the most used end station')
    most_used_start_and_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most Used End Station:', most_used_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('This is the total travel time')
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time was:', total_travel_time)


    # TO DO: display mean travel time
    print('This is the average travel time')
    average_travel_time = df['Trip Duration'].mean()
    print('Avergae travel time:', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('This is a count of all user types')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    print('This is a count of all user types')
    try:
        gender = df['Gender'].value_counts()
        print("Counts of gender:", gender)
    except KeyError:
        print("Data Unavailable")

    # TO DO: Display earliest, most recent, and most common year of birth
    print('This is a display of the earliest, most recent, and most common YOB')
    try:
        earliest_year = int(df['Birth Year'].min())
        print('Earliest birth year:', earliest_year)
    except KeyError:
        print("Data Unavailable")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_5_lines(df):

    rowindex = 0

    more_rows = input("\nShould we display more data? Enter 'yes' or 'no' \n")

    while True:
        if more_rows == 'no':
           return

        elif more_rows == 'yes':
            print(df[rowindex: rowindex + 5])
            rowindex = rowindex + 5
            more_rows = input("\nWant to see more data? Input: 'yes' or 'no' \n").lower()

    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_5_lines(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":

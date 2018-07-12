# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:30:24 2018

@author: Kroening
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    allowed_cities = ['chicago', 'new york city', 'washington']
    allowed_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    allowed_weekdays = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        city = input('Please enter a city (chicago, new york city or washington): ')
        if city.lower() not in allowed_cities:
            print("There's no data for " + city + ". Please try again!")
            continue
        else:
            print("Ok, let's analyze the data of " + city + "!")
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter the data by month? To do so, enter a month (january, february, march, april, may, june). Type "all" for no filter: ')
        if month.lower() not in allowed_months:
            print("There's no data for " + month + ". Please try again!")
            continue
        elif month.lower() == 'all':
            print('Ok, no filter for months!')
            break
        else:
            print("Ok, let's analyze the data of " + month + "!")
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Would you like to filter the data by day? To do so, enter a weekday (monday, tuesday, wednesday, thursday, friday, saturday, sunday). Type "all" for no filter: ')
        if day.lower() not in allowed_weekdays:
            print("There's no data for " + day + ". Please try again!")
            continue
        elif day.lower() == 'all':
            print('Ok, no filter for weekdays!')
            break
        else:
            print("Ok, let's analyze the data of " + day + "s!")
            break

    print('-'*40)
    return city, month, day

def load_data(city, month='all', day='all'):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a DataFrame
    df = pd.read_csv(CITY_DATA.get(city))

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: ' + months[common_month-1])

    # TO DO: display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    print('The most common day of the week is: ' + str(common_weekday))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour of the week is: ' + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is: ' + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station is: ' + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    common_station_combination = df['route'].mode()[0]
    print('The most common combination is: ' + common_station_combination)
    #print('The most common end station is: ' + common_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() # total travel time in seconds
    total_min, total_sec  = divmod(total_travel_time,60)
    total_hour, total_min  = divmod(total_min,60)
    print("The total travel time is: {} hours, {} minutes and {} seconds".format(total_hour, total_min, round(total_sec)))

    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    mean_min, mean_sec = divmod(mean_travel_time,60)
    mean_hour, mean_min = divmod(mean_min,60)
    print("The average travel time is: {} hours, {} minutes and {} seconds".format(mean_hour, mean_min, round(mean_sec)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:")
    print(user_types)

    # TO DO: Display counts of gender (no gender data for Washington)
    if "Gender" in df:
        gender = df['Gender'].dropna(axis=0).value_counts()
        print("\nGender of users:")
        print(gender)
    else:
        print("\nThere's no data for gender.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = int(df['Birth Year'].dropna(axis=0).min())
        recent_birth_year = int(df['Birth Year'].dropna(axis=0).max())
        common_birth_year = int(df['Birth Year'].dropna(axis=0).mode()[0])
        print("\nBirth year of users:")
        print("Earliest birth year: " + str(earliest_birth_year))
        print("Most recent birth year: " + str(recent_birth_year))
        print("Most common birth year: " + str(common_birth_year))
    else:
        print("\nThere's no data for age.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

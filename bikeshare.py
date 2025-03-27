"""
Explore US Bikeshare Data

A command-line interactive tool for exploring bikeshare system usage patterns.
Analyzes travel times, popular stations, user demographics, and provides raw data exploration.

Features:
- Filter data by city, month and day
- Display time/station/trip duration statistics
- Show user demographics
- Interactive raw data exploration

Example:
    $ python bikeshare.py
    > Enter city (chicago, new york city, washington): chicago
    > Enter month (all, january-june): all
    > Enter day (all, monday-sunday): all
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Explore US Bikeshare Data

    A command-line interactive tool for exploring bikeshare system usage patterns.
    Analyzes travel times, popular stations, user demographics, and provides raw data exploration.

    Features:
    - Filter data by city, month and day
    - Display time/station/trip duration statistics
    - Show user demographics
    - Interactive raw data exploration

    Example:
        $ python bikeshare.py
        > Enter city (chicago, new york city, washington): chicago
        > Enter month (all, january-june): all
        > Enter day (all, monday-sunday): all
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city you want see data for Chicago , New York City or Washington : ')
    city = city.casefold()
    while city not in CITY_DATA:
      city = input('Invalid city name.Please Try Again!')
      city = city.casefold()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Enter the month from January to June OR Enter "all" for no month filter : ')
    month = month.casefold()
    while month not in months:
        month = input('Invalid month name.Please Try Again!')
        month = month.casefold()
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Enter the day from Monday to Sunday OR Enter "all" for no day filter : ')
    day = day.casefold()
    while day not in days:
        day = input('Invalid day name.Please Try Again!')
        day = day.casefold()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads and filters bikeshare data based on user inputs.
    
    Args:
        city (str): Validated city name from get_filters()
        month (str): Validated month filter from get_filters()
        day (str): Validated day filter from get_filters()
    
    Returns:
        pd.DataFrame: Filtered dataframe with additional temporal columns:
            - month (int): 1-6 representing January-June
            - day_of_week (str): Monday-Sunday
            - hour (int): 0-23 (created in time_stats())
    
    Notes:
        - Original CSV columns expected: 
          ['Start Time', 'End Time', 'Trip Duration', 'Start Station', 
           'End Station', 'User Type', 'Gender', 'Birth Year']
        - Washington dataset lacks Gender/Birth Year columns
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """
    Analyzes temporal patterns in bike usage with statistical mode.
    
    Args:
        df (pd.DataFrame): Filtered dataframe from load_data()
    
    Statistics Calculated:
        1. Most common travel month (1-6 mapped to January-June)
        2. Most frequent weekday (0-6 mapped to Monday-Sunday)
        3. Peak start hour (0-23 in 24h format)
    
    Time Complexity: O(n) for mode calculations
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Popular Month:', months[common_month-1])

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    common_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Most Popular Day:', days[common_day])


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Popular Start Station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Popular End Station: ', df['End Station'].mode()[0])
    

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start and End Station Trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types,'\n')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:    
        gender = df['Gender'].value_counts()
        print(gender,'\n')
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays raw data in chunks of 5 rows upon user request."""
    """
    Paginates raw data display in 5-row increments.
    
    Args:
        df (pd.DataFrame): Dataframe to display
        
    Flow Control:
        - Starts from index 0
        - Continues until user declines or EOF
        - Maintains position between requests
        
    Example:
        >>> display_data(df)
        Do you want to see the first 5 rows? [yes/no]: yes
        [Displays rows 0-4]
        Do you want to see the next 5 rows? [yes/no]: no
    """
    start_loc = 0
    while True:
        if start_loc == 0:
            prompt = '\nDo you want to see the first 5 rows of data? Enter yes or no.\n'
        else:
            prompt = '\nDo you want to see the next 5 rows of data? Enter yes or no.\n'
        
        answer = input(prompt).lower()
        
        if answer != 'yes':
            break
        
        if start_loc >= len(df):
            print('There is no more data to display.')
            break
        
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df) 

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

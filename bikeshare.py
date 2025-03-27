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
    def validate_input(prompt, options):
        while True:
            user_input = input(prompt).casefold()
            if user_input in options:
                return user_input
            print(f"Invalid input. Please choose from: {', '.join(options)}")

    city_prompt = '''\nChoose a city:
    - Chicago
    - New York City
    - Washington\n>>> '''
    month_prompt = '''\nFilter by month (all, january-june):\n>>> '''
    day_prompt = '''\nFilter by day (all, monday-sunday):\n>>> '''

    city = validate_input(city_prompt, CITY_DATA.keys())
    month = validate_input(month_prompt, ['all', 'january', 'february', 'march', 'april', 'may', 'june'])
    day = validate_input(day_prompt, ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
    
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
    
    def filter_by_month(df, month):
    
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month_idx = months.index(month) + 1
            return df[df['month'] == month_idx]
        return df

    def filter_by_day(df, day):
        
        if day != 'all':
            return df[df['day_of_week'] == day.title()]
        
    df = filter_by_month(df, month)
    
    df = filter_by_day(df, day)    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    time_features = df['Start Time'].dt
    df['month'] = time_features.month
    df['day_of_week'] = time_features.day_name()  
    df['hour'] = time_features.hour

    print(f"Most Popular Month: {df['month'].mode().iloc[0]}")
    print(f"Most Popular Day: {df['day_of_week'].mode().iloc[0]}")
    print(f"Most Popular Hour: {df['hour'].mode().iloc[0]}")


    
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

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
    print('Hello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter a city either Chicago, New York City or Washington: \n").lower()
    while city not in ['chicago', 'new york city', 'washington','all']:
        city = input("City name is invalid! Enter either Chicago, New York City or Washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nPlease input a month January thru June or all to apply no month filter:\n ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        month = input("Month is invalid! Enter a month January thru June or All: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nPlease input day of week, Monday - Sunday or all to apply no day filter:\n ").lower()
    while day not in ['monday', 'tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        day = input("Day is invalid! Enter All or a day of the week spelled out ").lower()

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

    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #convert Start Time data to Date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    pop_month = df['month'].mode()[0]
    print('The most popular month traveled:\n',pop_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    pop_day_of_week = df['day_of_week'].mode()[0]
    print('The most popular day of the week traveled:\n',pop_day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print('The most popular hour traveled:\n',pop_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_strt_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:',pop_strt_station)

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:',pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    pop_strt_end_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)
    print('\nThe most common start and end stations are:\n', pop_strt_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration'].sum())/60
    print('Total travel time in seconds is:\n',total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('Average travel time in seconds is:\n',avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('The total # of users types are:\n',User_Types)


    # TO DO: Display counts of gender
    try:
        print("\nThe counts by gender are:")
        print(df['Gender'].value_counts())
    except:
        print('There are is no gender data for Washington.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        Earliest_birthday = df['Birth Year'].min()
        print('\nThe earliest birthyear is\n ', Earliest_birthday)

        Latest_birthday = df['Birth Year'].max()
        print('The latest birthyear is\n ', Latest_birthday)

        Most_common_birthday = df['Birth Year'].mode()[0]
        print('The most common birthyear is\n ', Most_common_birthday)
    except:
        print('There are is no birth data for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_five(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data.lower() != 'no':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('Do you wish to continue?: ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_five(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

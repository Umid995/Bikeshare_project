'''Created on Mon June 27 15:01:46 2022

@author: umidkarimov'''



import time
import pandas as pd
import numpy as np

# uploding csv data files to dataframe
df = pd.read_csv(r'//Users//umidkarimov//Downloads//all-project-files//chicago.csv')
df = pd.read_csv(r'//Users//umidkarimov/Downloads//all-project-files//new_york_city.csv')
df = pd.read_csv(r'//Users//umidkarimov//Downloads//all-project-files//washington.csv')

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
    # get user input for city (chicago, new york city, washington). 
    global city
    city = input('Enter the name of city :').lower()
    name_of_cities = ['washington', 'chicago', 'new york city']
    while city not in name_of_cities:
        print('Invalid name of city, please check the name')
        city = input('Enter the name of city :').lower()
        
    

    # get user input for month (all, january, february, ... , june)
    month = input('Enter the name of month :').lower()
    months = ['all', 'january', 'feburary', 'march', 'april', 'may', 'june']
    while month not in months:
        print('Invalid name of month, please check the name')
        month = input('Enter the name of month :').lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('Enter name of day :').lower()
    days = ['all', 'monday', 'thuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days: 
        print('Invalid name of day, please check the name')
        day = input('Enter the name of day :').lower()
        
        
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
    df['day_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    

    if month != 'all':
       months = ['january','feburary', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
       df = df[df['month'] == month]
       
    if day != 'all':
       df = df[df['day_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    # display the most common month
   
    common_month = df['month'].mode()[0]
    print('Most common travel month  : {} ' .format(common_month))
    


    # display the most common day of week
   
    common_day = df['day_week'].mode()[0]
    print('Most common travel day  : {} ' .format(common_day))
    


    # display the most common start hour
    
    common_hour = df['hour'].mode()[0]
    print('Most common travel hour : {} ' .format(common_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    
  

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common travel start station  {} :' .format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common travel end station  {}  :' .format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('The most frequent combination of start and end station trip {} :' .format(common_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time : {}' .format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time : {}' .format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser types :\n {}'.format(user_types))


    # Display counts of gender
    # gender data not available in washington 
    
    if city == 'washington' :
       print('Not information about gender')
   
    else:
       gender = df['Gender'].value_counts()
       print('gender :\n {}'.format(gender))
        


    # Display earliest, most recent, and most common year of birth
    # birth year not available for washington
    if city == 'washington' :
        print('Not information about birth year')
    
    else :
      earliest = df['Birth Year'].min() 
      print('The age of the oldest user : {}'.format(earliest))
    
      recent = df['Birth Year'].max()
      print('The age of the youngest user : {}'.format(recent))
     
      common_year_of_birth = df['Birth Year'].mode()[0]
      print('Common year of birth users : {}'.format(common_year_of_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
def row_data(df):
    #show 5 row data
        x = 0
        y = 5
        data = input('Are you want to see five line of raw data ? Enter yes or no :' ).lower()
        if data == 'yes':
            print(df.iloc[x:y]) 
        while True :   
            datas = input('Are you want to see next five line of raw data ? Enter yes or no :').lower ()
            if datas == 'yes' :
             x += 5
             y += 5
             print(df.iloc[x:y])
            
            else :
               break
         


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    


from s_and_l import get_info 

objl = save_and_load ()
tt = objl.get_info()


hashtag_value = tt['dead_line'] / 20 
days_passed = 0  

# Function to save the current state of the loading bar
def save_bar(bar, saved_bars):
    saved_bars += bar  
    return saved_bars

# Function to display the loading bar
def display_loading_bar(days):
    global days_passed
    days_passed += days 

    # Calculate the number of '#' 
    hashtag = days_passed // hashtag_value
    if hashtag > tt:
        hashtag = tt  
    bar = '#' * hashtag + '_' * (tt - hashtag)
    tt['loadin_b'] = bar
    print(f'\r[{bar}] Days Passed: {days_passed}', end='')



    print("\nTask completed!")

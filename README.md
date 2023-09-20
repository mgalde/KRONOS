# Kronos Project

## Overview

The Kronos Project is an ongoing effort to recreate the KRONOS interface from the movie "The Incredibles". The ultimate goal is not only to replicate the visual and interactive aspects of the interface but also to connect it to an external database, allowing for real-world applications.

## Sections

### Initialization

The application starts in fullscreen mode, displaying a password screen. The user is prompted to enter the password to access the main interface.

### Menu Options

Once the correct password ("KRONOS") is entered, the user is presented with a menu containing several options. These options can be navigated using the up and down arrow keys on the keyboard. The currently selected option is visually highlighted.

### Option Screens

Each menu option leads to its own unique screen:

- **ISLAND OPERATIONS**: Displays a white rectangle covering 80% of the screen with the title "ISLAND OPERATIONS" in the upper right corner.
  
- **FINANCES**: Similar to the "ISLAND OPERATIONS" screen but with an additional thick black line in the middle of the white rectangle.
  
- **OMNIDROID METATRINING**: Displays a white circle in the center of the screen. Inside the circle, the current time is shown, along with a countdown to October 31, 2023.

### Resetting

At any point, pressing the `<BackSpace>` key will reset the application to the password screen.

## Functions Breakdown

- `__init__`: Initializes the main application window and sets up the initial screen.
  
- `init_password_screen`: Sets up the password entry screen.
  
- `enable_password_entry`: Enables the password entry after a short delay.
  
- `on_focus_in` and `on_key_press`: Handle the behavior of the password entry field.
  
- `check_password`: Checks if the entered password is correct and transitions to the main menu if it is.
  
- `draw_background_rectangle`: Draws the background for the main menu options.
  
- `display_options`: Displays the main menu options on the screen.
  
- `select_option_up` and `select_option_down`: Handle the navigation of the menu options using the arrow keys.
  
- `update_option_colors`: Updates the visual indication of the currently selected menu option.
  
- `reset_to_password_screen`: Resets the application to the password entry screen.
  
- `select_current_option`: Handles the selection of a menu option and transitions to the corresponding screen.
  
- `island_operations_screen`, `finances_screen`, and `omnidroid_metatrining_screen`: Set up the individual screens for each menu option.

## Future Work

The project is still in progress. The next steps include refining the user interface, adding more features and interactivity, and connecting the application to an external database for real-world data storage and retrieval.

## Note

This project is inspired by the movie "The Incredibles" and is intended for educational and entertainment purposes only.

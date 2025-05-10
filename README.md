# Water Reminder

A lightweight Python script that sends you desktop notifications at regular intervals to remind you to drink water, with a sound alert.

## Features

- Desktop notifications using [`plyer`](https://plyer.readthedocs.io/en/latest/)
- Sound alert using [`pygame`](https://www.pygame.org/)
- Easy-to-use CLI to set reminder frequency (in hours)
- Simple and clean code structure

## Repository Structure

Water_reminder/ ├── main.py              # The main script 
                └── waterdrip.mp3        # Audio file for notification sound

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/himanshu0154/Water_reminder.git
    cd Water_reminder

2. Install dependencies
    
    ```bash
    pip install pygame plyer

3. run the script 

    ```bash
    python main.py

# Usage

* When prompted, enter how frequently (in hours) you want the water reminder to pop up.

    * Example: 0.5 for every 30 minutes.


* You’ll get a desktop notification and a sound alert at your chosen interval.


# Example Output

how frequently do you want the notification to pop up (in hours): 1
Notification will appear every 1.0 hour(s).

# License

This project is licensed under the MIT License

Author 

[himanshu0154](https://github.com/himanshu0154)
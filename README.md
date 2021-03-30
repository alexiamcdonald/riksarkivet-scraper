# Riksarkivet Scraper
Scrapes riksarkivet for information on historical people from https://sok.riksarkivet.se/person

Makes it easier to see all the results for a person without having to click through everything.

## Requirements

Install Python 3
[Click here if you need to install python 3](https://www.python.org/downloads/)

Afterwards you'll need to add the following Requirements by typing into the terminal:

`pip3 install beautifulsoup4`

and

`pip3 install requests`


## How to use

To search a person type their first name and their second name with a +.

In this example I've used "Peter Tottie":

`python3 scraper.py peter+tottie`

## What does it return?
- Namn
- Yrke
- Hemort
- Hemförsamling
- Civilstånd
- Anhöriga info
- Årtal
- Arkiv
- Volym
- Register
- Upprättad av
- Anhörigs namn

## Any issues

You can post any issues you have [here](https://github.com/alexiamcdonald/riksarkivet-scraper/issues)

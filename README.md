# hiking-webscraper
Simple Python Webscraper that collects data from www.wellingtonregionaltrails.com and convert into a csv

Current working feature:
- Goes to https://www.wellingtonregionaltrails.com/trails/search?q=&location=&use=&difficulty=14&distance=&type=&start=0&_=1673510890038
- Collects the name, location and distance from each trail
- Writes each trail into a csv file

Future feature:
- There are 103 results. A single page only load 20 results at a time. Will want to make it go through the next page and collect the data until the last page.

Problems encountered and fixes:
1. Getting a lot of NoneType error when trying to extract information

Fix: Found out that the data hasn't loaded yet when requesting the page. NoneType error occuring because the html tags hasn't been loaded in yet.

2. The page uses JavaScript to load the content, so it doesn't appear when just using requests.

Fix: Used Selenium to load a browser and waits for the page to load until a certain class within a div finishes loading before we can start interpreting data.

3. \u0101 error when writing the data into the csv

Fix: Figured out it was a unicode character not supported. Specified encoding UTF-8 that supports \u0101

4. Current problem: the script manage to click on the "load more" button 4 times but is still only returning the first 20 trails instead of the expected 80 trails
## Election night scraper for Texas Governor's Race
<b>By:</b> <em>Ari Sen & Jun Kai Teoh</em>

The repository contains a Python notebook which scrapes the Texas Secretary of State's Office, retrieves a JSON file with the results, parses that JSON into a Pandas dataframe and then saves that dataframe as a CSV file. 

The scraper is run roughly once every 10 minutes using GitHub Actions.

Every time the Texas Secretary of State's Office updates its results it generates a new JSON file. The url path to this new file contains a three-digit number which iterates by one with each update. So we wrote code to test increasingly larger three-digit numbers until no JSON file is returned, then save the last working three digit number in a text file. On the next run the Python script reads this text file and starts testing urls at that number.

The raw CSV file is linked to the following Datawrapper map: https://www.datawrapper.de/_/WVH0c/

You can see it embeded on <em>The Dallas Morning News</em> website, in the following stories:
- <a href="https://www.dallasnews.com/news/elections/2022/11/08/election-day-voting-in-texas-live-midterms-coverage-results-across-dallas-fort-worth/">Live Election Day results in Texas: Abbott, Paxton win, Prop A passes</a>
- <a href="https://www.dallasnews.com/news/politics/2022/11/08/greg-abbott-beto-orourke-in-texas-governors-race-election-day-finale/">Greg Abbott defeats Beto O’Rourke in Texas governor’s race</a>
- <a href="https://www.dallasnews.com/news/politics/2022/11/09/abbott-victory-confirms-pundits-forecasts/">Abbott victory confirms pundits’ forecasts</a>

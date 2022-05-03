<h1>Brazilian stocks data scraper</h1>

![screenshot](https://user-images.githubusercontent.com/47046552/166299837-966948d8-059c-4b9a-bfb8-d5f6dfc1a6c0.png)

<h2>About</h2>
This project scrapes and stores the following data associated with stocks from the Brazilian market:

- Name
- Price
- Sector
- Price/profit
- Net worth

It is composed of three modules:
1. A web crawler/scraper focused in Brazilian stocks data. It uses <a href='https://www.fundamentus.com.br/detalhes.php?papel='>this link</a> to get stock acronyms and to create a list of individual stock information links. Then it uses the links to scrape data from two sources: <a href='https://www.fundamentus.com.br/'>Fundamentus</a> and <a href='https://br.financas.yahoo.com/'>Brazilian Yahoo Finances</a>. It also has a script to upload data to the server. (The crawling/scraping code is located in folder "/stock_info_scraper")
2. A Node.js backend to store the scraped data.
3. A frontend developed using React and MaterialUI where it is possible to search for a stock acronym.

<h2>Setup</h2>

1. Install Postgres: `sudo apt install postgresql`
2. Start Postgres: `sudo service start posgresql`
3. Make sure you are using Node 16
4. Go to /backend/config/database.js and set Postgres configs
5. Go to /backend, run ```npm install``` and then ```npm start```
6. Now you should see the server running and queries in terminal from the database being created
7. (optional) Create a virtual environment for Python
8. Go to /stock_info_scraper and run ```pip install -r requirements.txt```
9. Go back to root folder and run ```Python3 scrape_and_upload.py```
10. After the last step is completed to /frontend, run ```npm install``` and then ```npm start```. When a browser window is popped, project setup has finished.

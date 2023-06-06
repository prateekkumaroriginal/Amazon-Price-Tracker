# Amazon Price Tracker
This Python program tracks the price of a specific product on Amazon and sends an email alert if the price drops below a certain threshold.

## Note
To use it effectively, you should deploy it on a cloud service like Google's <a href="https://cloud.google.com/run/?userloc_9303169-network_g">Cloud Run</a>.

## Setup
1. Clone the repository or download the Python file.
2. Set the necessary environment variables:
   - `EMAIL`: Your Gmail email address.
   - `PASSWORD`: Your Gmail password or an app password if you have 2-step verification enabled.
3. Set the `EXPECTED_PRICE` variable to the desired price threshold.
4. Replace the `URL` variable with the URL of the Amazon product you want to track.

## Usage
1. Run the Python script in your terminal or IDE.
2. The program will send a GET request to the Amazon web page and retrieve the HTML content.
3. It will extract the price and product name from the HTML using web scraping techniques.
4. If the price is less than or equal to the `EXPECTED_PRICE`, an email alert will be sent using the provided Gmail account.
5. Check your email inbox for the price drop alert.

## Note
Ensure that you have allowed access for less secure apps in your Gmail account settings to send emails using `SMTP`.

## Tech Stack
Language: Python <br>
Libraries: `requests`, `BeautifulSoup`, `smtplib`, `os`

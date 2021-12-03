# Automated Birthday Wisher

Sends automated email birthday wishes when today = birthday in csv.
Day 32 Python Bootcamp


## Usage
Use the smtplib library to send email birthday wishes when today matches birthday
in CSV file.

1. Create a .env in root folder with this info:
    1. MY_EMAIL = "your-email-address-goes-here"
    2. MY_PASSWORD = "your-email-password"
    3. SMTP = 'smtp-for-your-email-provider'
2. Update CSV with correct birthday info. Example layout in CSV.
3. Depending on email provider you're using to send the emails (),
you may have to change security settings so emails will send.

Project can be uploaded to cloud and run through a cron job.

## License
[MIT](https://choosealicense.com/licenses/mit/)
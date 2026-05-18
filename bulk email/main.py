import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
PASSWORD = os.getenv('PASSWORD')

recipients = [
    {'email': 'hotbite43@gmail.com', 'company': 'France P26'},
    # {'email': 'shafiabbasmundol@gmail.com', 'company': 'Abaya Palace Shop'},
]

SUBJECT = "Elevate {company}'s Digital Presence with a Custom Website"

PLAIN_BODY = """\
Dear Team at {company},

I hope this message finds you well. My name is Muheeb Ahmed, and I’m a web developer specializing in creating custom, responsive websites that help companies like yours stand out and attract the right clients.

I came across {company} on the Yello UAE directory and was impressed by the wide range of services you provide — from investment support and startup funding to strategic consulting. Your offerings are dynamic and expansive, and I believe your online presence should reflect that.

A professionally built website could help your business:
✅ Clearly present your services and investment offerings
✅ Build credibility with potential partners and investors
✅ Improve visibility through search engines
✅ Enable lead generation and client inquiries directly through your site

I'd love to offer you a free consultation to discuss how a modern website can help scale your business and establish a stronger digital presence.

Please let me know a convenient time for a quick call or meeting.

Looking forward to hearing from you.

Best regards,
Muheeb Ahmed
📞 0322 2831086
"""

HTML_BODY = """\
<html>
  <body>
    <p>Dear Team at <b>{company}</b>,<br><br>
       I hope this message finds you well. My name is <b>Muheeb Ahmed</b>, and I’m a web developer specializing in creating custom, responsive websites that help companies like yours stand out and attract the right clients.<br><br>
       I came across <b>{company}</b> on the Yello UAE directory and was impressed by the wide range of services you provide — from investment support and startup funding to strategic consulting. Your offerings are dynamic and expansive, and I believe your online presence should reflect that.<br><br>

       A professionally built website could help your business:<br>
       ✅ Clearly present your services and investment offerings<br>
       ✅ Build credibility with potential partners and investors<br>
       ✅ Improve visibility through search engines<br>
       ✅ Enable lead generation and client inquiries directly through your site<br><br>

       I'd love to offer you a free consultation to discuss how a modern website can help scale your business and establish a stronger digital presence.<br><br>

       Please let me know a convenient time for a quick call or meeting.<br><br>

       Looking forward to hearing from you.<br><br>

       Best regards,<br>
       <b>Muheeb Ahmed</b><br>
       📞 0322 2831086
    </p>
  </body>
</html>
"""

# Logging config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email sending function
def send_bulk_email():
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        logging.info("Logged in to SMTP server successfully.")

        for person in recipients:
            email = person['email']
            company = person.get('company', 'Your Company')

            msg = MIMEMultipart('alternative')
            msg['From'] = SENDER_EMAIL
            msg['To'] = email
            msg['Subject'] = SUBJECT.format(company=company)

            plain_text = PLAIN_BODY.format(company=company)
            html_text = HTML_BODY.format(company=company)

            msg.attach(MIMEText(plain_text, 'plain'))
            msg.attach(MIMEText(html_text, 'html'))

            try:
                server.sendmail(SENDER_EMAIL, email, msg.as_string())
                logging.info(f"Email sent to {email} ({company})")
            except Exception as e:
                logging.error(f"Failed to send email to {email}: {e}")

        server.quit()
        logging.info("All emails sent successfully.")

    except Exception as e:
        logging.critical(f"SMTP connection or login failed: {e}")

if __name__ == '__main__':
    send_bulk_email()

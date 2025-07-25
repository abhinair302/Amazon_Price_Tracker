# 🛒 Amazon Price Tracker (with Email Alerts)
This Python script tracks the price of a product on Amazon and sends an email notification if the price drops below a set target.
---
# 🚀 Features
- Scrapes live product price and title from Amazon.

- Compares the current price to a user-defined target price.

- Sends an automated email alert if the price is below the threshold.

- Uses .env file to securely store credentials.

- Lightweight, fast, and easily customizable.

---

# 📦 Requirements
- Python 3.x

- requests

- beautifulsoup4

- python-dotenv

---

# 🔐 Environment Variables
Create a .env file in the root directory with your email and SMTP server details:
```
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

---
# 💡 Notes
- Amazon may block your IP if you scrape too frequently — use responsibly.

- Gmail users must enable "App Passwords" if using 2FA.

- This script is for personal/educational use only.

---
# 🙏 Thank You
Thank you for checking out this project!
If you found it useful or learned something new, feel free to ⭐️ star the repo or share it with others.

Happy coding! 💻✨

--Abhijeet--

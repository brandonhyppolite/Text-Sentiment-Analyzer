# Text-Sentiment-Analyzer
🧠 Sentiment Analyzer
A lightweight web application that analyzes text sentiment using AWS Comprehend, built with HTML, Tailwind CSS, JavaScript, and AWS Lambda.

📌 What It Does
Enter any text, and the app will detect the sentiment — Positive, Negative, Neutral, or Mixed — along with confidence scores for each.
You can either try the live version using Brandon’s deployed backend or set up your own with AWS.

⚡ Try It Instantly (No Setup Needed)
Clone or download this repository.

Open index.html in your browser.

Enter any sentence and click "Check Sentiment".

The app will send a request to the deployed AWS Lambda API and return the sentiment result.

✅ No AWS setup required — uses the hosted API provided in this repo.

🛠️ Want to Deploy Your Own?
If you want to build and deploy your own backend, follow the steps below:

🔧 Backend (AWS Lambda + API Gateway)
Create a Lambda function in AWS using Python.

Paste in the lambda_function.py code provided in this repo.

Add permissions for AWS Comprehend (use AWSLambdaBasicExecutionRole + ComprehendFullAccess).

Create an API Gateway:

Create a REST API.

Add a POST method to /analyze, pointing to your Lambda.

Enable CORS for both POST and OPTIONS.

Deploy your API and grab the Invoke URL.

🌐 Frontend (Optional Changes)
In index.html, replace this line with your own URL:

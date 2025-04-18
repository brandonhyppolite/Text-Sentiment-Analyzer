# 🧠 Sentiment Analyzer

A simple, serverless web app that detects sentiment in text using **AWS Comprehend** via **AWS Lambda** and **API Gateway**.

Built with:
- 🔹 HTML
- 🔹 Tailwind CSS
- 🔹 JavaScript (Fetch API)
- 🔹 AWS Lambda (Python)
- 🔹 AWS Comprehend

---

## 🌐 Live Demo (No Setup Needed)

1. Clone or download this repository.
2. Open `index.html` in your browser.
3. Type a sentence and click **"Check Sentiment"**.
4. Get instant results — sentiment and confidence scores — using the deployed AWS Lambda API.

> ✅ No AWS configuration needed. The app uses a hosted endpoint.

---

## 🛠️ Deploy Your Own Version (Optional)

Want to deploy your own AWS backend? Follow these steps:

### 1. Set Up AWS Lambda
- Go to AWS Lambda → Create a new function.
- Choose Python as your runtime.
- Paste the code from `lambda_function.py`.
- Add permissions:
  - `AWSLambdaBasicExecutionRole`
  - `ComprehendFullAccess`

### 2. Connect via API Gateway
- Create a new REST API.
- Add a resource: `/analyze`
- Add a method: `POST` (linked to your Lambda)
- Enable **CORS** on both `POST` and `OPTIONS` methods.
- Deploy the API (e.g., stage name: `prod`)
- Copy the **Invoke URL**

### 3. Update Frontend (Optional)
Open `index.html` and update the fetch URL:

```js
fetch("https://your-api-id.execute-api.region.amazonaws.com/prod/analyze", {

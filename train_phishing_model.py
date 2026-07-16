import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack
import pickle

# ------------------------------
# 1️⃣ Safe URLs (~500)
# ------------------------------
safe_urls = [
    # Indian Government
    "https://www.india.gov.in",
    "https://www.mca.gov.in",
    "https://www.incometaxindia.gov.in",
    "https://www.uidai.gov.in",
    "https://www.rbi.org.in",
    "https://www.nic.in",
    "https://www.eci.gov.in",
    "https://www.aicte-india.org",
    "https://www.irctc.co.in",
    "https://www.pgportal.gov.in",

    # Indian Banks
    "https://www.icicibank.com",
    "https://www.sbi.co.in",
    "https://www.hdfcbank.com",
    "https://www.axisbank.com",
    "https://www.kotak.com",
    "https://www.bankofbaroda.in",
    "https://www.pnbindia.in",
    "https://www.idfcfirstbank.com",
    "https://www.indusind.com",
    "https://www.canarabank.com",

    # Private/Tech Companies
    "https://www.tcs.com",
    "https://www.infosys.com",
    "https://www.wipro.com",
    "https://www.reliance.com",
    "https://www.amazon.in",
    "https://www.flipkart.com",
    "https://www.google.co.in",
    "https://www.microsoft.com",
    "https://www.facebook.com",
    "https://www.linkedin.com",
]

# Duplicate to reach ~500 safe URLs
safe_urls = safe_urls * 17  # 30 * 17 = 510

# ------------------------------
# 2️⃣ Phishing URLs (~500)
# ------------------------------
phish_bases = [
    "http://login-{}-secure.com",
    "http://{}-account-update.com",
    "https://secure-{}-verify.com",
    "http://{}-alert-login.com",
    "http://verify-{}-account.com",
]

phish_targets = ["bank", "paypal", "google", "facebook", "apple", "amazon", "hdfc", "icici", "sbi", "axis"]

phishing_urls = []
for i in range(500):
    base = random.choice(phish_bases)
    target = random.choice(phish_targets)
    phishing_urls.append(base.format(target))

# ------------------------------
# 3️⃣ Combine URLs and Labels
# ------------------------------
urls = safe_urls + phishing_urls
labels = [0]*len(safe_urls) + [1]*len(phishing_urls)

# Shuffle dataset
combined = list(zip(urls, labels))
random.shuffle(combined)
urls, labels = zip(*combined)

# Create DataFrame
df = pd.DataFrame({"url": urls, "label": labels})

# ------------------------------
# 4️⃣ Feature Engineering
# ------------------------------
def extract_numeric_features(url_list):
    features = []
    for url in url_list:
        url = url.lower()
        url_len = len(url)
        num_dots = url.count('.')
        num_hyphens = url.count('-')
        has_https = 1 if url.startswith("https") else 0
        num_digits = sum(c.isdigit() for c in url)
        features.append([url_len, num_dots, num_hyphens, has_https, num_digits])
    return features

X_numeric = extract_numeric_features(df["url"])
scaler = StandardScaler()
X_numeric_scaled = scaler.fit_transform(X_numeric)

# Convert URLs into numeric features using CountVectorizer
vectorizer = CountVectorizer()
X_text = vectorizer.fit_transform(df["url"])

# Combine text features + numeric features
X = hstack([X_text, X_numeric_scaled])
y = df["label"]

# ------------------------------
# 5️⃣ Train/Test Split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ------------------------------
# 6️⃣ Train Model
# ------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model accuracy on test set:", model.score(X_test, y_test))

# ------------------------------
# 7️⃣ Save Model, Vectorizer, Scaler
# ------------------------------
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Training complete. Model, vectorizer, and scaler saved.")

from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model dan scaler
model = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load dataset untuk analitik cluster
df = pd.read_csv("Mall_Customers.csv")

# Profil masing-masing cluster
cluster_info = {
    0: {
        "name": "Moderate Customer",
        "label": "Balanced Segment",
        "description": "Pelanggan dengan pendapatan dan tingkat belanja yang relatif sedang.",
        "action": "Berikan promo umum, loyalty program, dan penawaran produk yang sesuai kebutuhan."
    },
    1: {
        "name": "High Income - High Spending",
        "label": "High Value Customer",
        "description": "Pelanggan dengan pendapatan tinggi dan tingkat belanja yang tinggi.",
        "action": "Berikan program loyalitas, penawaran premium, dan akses promo eksklusif."
    },
    2: {
        "name": "Young High-Spending Customer",
        "label": "Active Spender",
        "description": "Pelanggan relatif muda dengan pendapatan lebih rendah tetapi tingkat belanja tinggi.",
        "action": "Gunakan promo menarik, bundling produk, dan kampanye yang mendorong pembelian berulang."
    },
    3: {
        "name": "High Income - Low Spending",
        "label": "Low Engagement",
        "description": "Pelanggan dengan pendapatan tinggi tetapi tingkat belanja rendah.",
        "action": "Gunakan penawaran personal, produk premium, dan strategi re-engagement."
    },
    4: {
        "name": "Low Income - Low Spending",
        "label": "Budget Conscious",
        "description": "Pelanggan dengan pendapatan dan tingkat belanja yang relatif rendah.",
        "action": "Gunakan promo hemat, diskon, bundling ekonomis, dan voucher."
    }
}

# Hitung jumlah pelanggan setiap cluster
cluster_counts = df["Cluster"].value_counts().sort_index() if "Cluster" in df.columns else None

# Kalau dataset belum memiliki kolom Cluster,
# prediksi ulang menggunakan model yang sudah dilatih
if cluster_counts is None:
    X_all = df[["Annual Income (k$)", "Spending Score (1-100)"]]
    X_all_scaled = scaler.transform(X_all)
    df["Cluster"] = model.predict(X_all_scaled)
    cluster_counts = df["Cluster"].value_counts().sort_index()

# Profil cluster
cluster_profile = df.groupby("Cluster")[
    ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
].mean().round(2)

# Data untuk halaman analitik
cluster_overview = []

for cluster_id in range(5):
    count = int(cluster_counts.get(cluster_id, 0))
    percentage = round((count / len(df)) * 100, 1)

    cluster_overview.append({
        "id": cluster_id,
        "name": cluster_info[cluster_id]["name"],
        "label": cluster_info[cluster_id]["label"],
        "description": cluster_info[cluster_id]["description"],
        "action": cluster_info[cluster_id]["action"],
        "count": count,
        "percentage": percentage,
        "age": cluster_profile.loc[cluster_id, "Age"],
        "income": cluster_profile.loc[cluster_id, "Annual Income (k$)"],
        "spending": cluster_profile.loc[cluster_id, "Spending Score (1-100)"]
    })


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        income = float(request.form["income"])
        spending = float(request.form["spending"])

        data = pd.DataFrame(
            [[income, spending]],
            columns=["Annual Income (k$)", "Spending Score (1-100)"]
        )

        data_scaled = scaler.transform(data)

        cluster = int(model.predict(data_scaled)[0])

        result = {
            "cluster": cluster,
            "name": cluster_info[cluster]["name"],
            "label": cluster_info[cluster]["label"],
            "description": cluster_info[cluster]["description"]
        }

    return render_template(
        "index.html",
        result=result,
        clusters=cluster_overview
    )


if __name__ == "__main__":
    app.run(debug=True)
\# Customer Segmentation menggunakan K-Means Clustering



\## Deskripsi Project



Project ini merupakan implementasi Machine Learning untuk melakukan segmentasi pelanggan menggunakan algoritma K-Means Clustering.



Segmentasi dilakukan berdasarkan dua karakteristik utama pelanggan, yaitu:



\- Annual Income (k$)

\- Spending Score (1-100)



Hasil clustering digunakan untuk mengelompokkan pelanggan ke dalam beberapa segmentasi berdasarkan karakteristik pendapatan dan perilaku belanja.



\## Dataset



Dataset yang digunakan adalah Mall Customers Dataset.



Dataset memiliki beberapa atribut:



\- CustomerID

\- Gender

\- Age

\- Annual Income (k$)

\- Spending Score (1-100)



Dalam proses clustering, fitur yang digunakan adalah:



\- Annual Income (k$)

\- Spending Score (1-100)



CustomerID tidak digunakan karena hanya merupakan identitas pelanggan.



Gender dan Age tidak digunakan sebagai fitur utama clustering, tetapi Age digunakan dalam proses profiling untuk memahami karakteristik setiap cluster.



\## Metode



Tahapan pengembangan model:



1\. Data Understanding

2\. Data Preprocessing

3\. Feature Selection

4\. Standardisasi menggunakan StandardScaler

5\. Menentukan jumlah cluster menggunakan Elbow Method

6\. Pemodelan menggunakan K-Means Clustering

7\. Profiling dan interpretasi cluster

8\. Evaluasi menggunakan Silhouette Score

9\. Export model dan scaler menggunakan Joblib

10\. Deployment menggunakan Flask



\## Pemilihan Jumlah Cluster



Berdasarkan hasil Elbow Method, digunakan:



\*\*K = 5\*\*



Model kemudian melakukan clustering terhadap data pelanggan menjadi lima kelompok.



\## Hasil Clustering



\### Cluster 0 — Moderate Customer



Pelanggan dengan pendapatan dan tingkat belanja yang relatif sedang.



\### Cluster 1 — High Income - High Spending



Pelanggan dengan pendapatan tinggi dan tingkat belanja yang tinggi.



\### Cluster 2 — Young High-Spending Customer



Pelanggan relatif muda dengan pendapatan lebih rendah tetapi memiliki tingkat belanja yang tinggi.



\### Cluster 3 — High Income - Low Spending



Pelanggan dengan pendapatan tinggi tetapi tingkat belanja yang rendah.



\### Cluster 4 — Low Income - Low Spending



Pelanggan dengan pendapatan dan tingkat belanja yang relatif rendah.



\## Evaluasi Model



Evaluasi clustering dilakukan menggunakan Silhouette Score.



Hasil evaluasi:



\*\*Silhouette Score = 0.555\*\*



Nilai tersebut menunjukkan bahwa cluster yang terbentuk memiliki pemisahan yang cukup baik berdasarkan Annual Income dan Spending Score.



\## Model



Model yang digunakan:



\- K-Means Clustering

\- StandardScaler



Model disimpan dalam format:



\- `kmeans\_model.pkl`

\- `scaler.pkl`



Format `.pkl` digunakan agar model yang telah dilatih dapat digunakan kembali tanpa melakukan proses training dari awal.



\## Aplikasi



Project ini menggunakan Flask sebagai backend untuk membuat aplikasi sederhana.



User dapat memasukkan:



\- Annual Income

\- Spending Score



Kemudian aplikasi akan memproses data tersebut menggunakan model K-Means dan menampilkan cluster pelanggan yang sesuai.



Aplikasi juga menampilkan informasi karakteristik setiap cluster berdasarkan hasil profiling dataset.



\## Struktur Project



```text

customer-segmentation/

│

├── app.py

├── kmeans\_model.pkl

├── scaler.pkl

├── Mall\_Customers.csv

├── customer\_segmentation.ipynb

├── README.md

│

└── templates/

&#x20;   └── index.html


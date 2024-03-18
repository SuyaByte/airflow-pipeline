# airflow-pipeline

This project implements a Wikipedia data pipeline using Apache Airflow, Amazon EC2, and Amazon S3. The pipeline extracts data from a Wikipedia page, processes it using Python, and stores it in an S3 bucket. An overview of the process:

Data Extraction: Utilizing BeautifulSoup and pandas, data is extracted from a Wikipedia page and structured into a dataframe. This extraction process is encapsulated into a reusable function.

Data Storage: Extracted data is stored as a CSV file initially.

Airflow Orchestration: An EC2 instance is set up to run Airflow. A Python script (DAG) is created, importing the ETL function for data extraction and saving.

Airflow Execution: The DAG is monitored in Airflow to ensure proper execution.

S3 Integration: The pipeline can be modified to save data directly to an S3 bucket instead of a local CSV file. However, prior creation of the S3 bucket is necessary.

This project serves as a template for building robust data pipelines, providing flexibility in data extraction, processing, and storage while leveraging powerful orchestration tools like Airflow and scalable storage solutions like Amazon S3.

## Acknowledgement
[Youtuber Darshil Parmar](https://www.youtube.com/@DarshilParmar)


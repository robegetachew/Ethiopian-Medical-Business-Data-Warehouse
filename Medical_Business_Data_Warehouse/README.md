# 🎉 Welcome to the Ethiopian Medical Business Data Warehouse DBT Project! 🇪🇹

## 📊 **Project Overview**
This project is designed to process and analyze data related to the Ethiopian medical business domain. It utilizes **DBT (Data Build Tool)** to transform raw data into a structured format suitable for analytics and reporting.

## 🚀 **Running the DBT Project**
To run this DBT project, follow these steps:

### 1. **Install DBT**
Make sure you have DBT installed. You can install it using pip:

```
pip install dbt
```

### 2. **Set up your environment**
Ensure that your database connection settings are configured correctly in the profiles.yml file. This file is usually located in the ~/.dbt/ directory on your local machine.

### 3. **Run the transformations**
Once DBT is installed and configured, you can run all the transformations defined in this project by using the following command:

```
dbt run
```
This command will execute all the models in the project and create the final tables or views in your data warehouse.

### 4. **Check the DBT status**
Use the following command to check if DBT is configured correctly and that the connection to the database is successful:

```
dbt debug
```
This will run a diagnostic check on your DBT environment and provide feedback on the connection status, missing configurations, or potential issues.

### 5. **View the documentation**
To view the generated documentation for your project (e.g., tables, columns, tests), you can use the following command:

```
dbt docs generate
```

This command will create the documentation for your models, sources, and tests. To view the generated documentation in your browser, use the following command:

```
dbt docs serve
```

This will launch a local web server and open the documentation in your default browser. You can view all the models, sources, and tests in the project, along with details on the data transformations.


## ⚙️ **Running this project**
To run this DBT project, make sure you have the following prerequisites:

+ DBT installed on your machine or server.
+ A connection to your data warehouse (e.g., Postgres).
+ The raw data source and necessary permissions set up to allow transformations.
  
## 🗂️ **Project Structure**
+ Models: All transformation logic is stored in the models directory.
+ Sources: The source data tables can be configured in the sources.yml file.
+ Tests: Data tests to ensure data integrity can be found in the tests directory.
+ Documentation: Automatically generated documentation for the project can be found in the dbt docs serve output.
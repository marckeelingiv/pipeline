# The What and the Why of Data Engineering
- Oil Analogy

# Type A vs B Data Engineer
- Type A (abstractor)
    - Uses off the shelf tools to accomplish objectives whenever possible
- Type B (builder)
    - Often builds systems from scratch using only code

# What is Clickhouse? 
- Open-source, columnar database management system (DBMS) 
- Designed for high-performance analytics and data processing
- Specifically optimized for handling large volumes of data and executing complex analytical queries 
- Organizes data in a columnar format (each column of a table is stored separately) 
    - Columnar storage approach allows for efficient compression and retrieval of specific columns, resulting in improved query performance and reduced storage requirements.  
- Can scale horizontally across multiple servers, enabling distributed query execution and fault tolerance
- Suitable for big data analytics, data warehousing, and time-series data analysis.  
- Supports a wide range of data formats
    - structured
    - semi-structured
    - unstructured
- Provides various built-in functions and SQL-like query language for data manipulation, aggregation, filtering, and joining.  
   
Overall, ClickHouse is a powerful database solution for organizations that deal with large-scale data analytics, where speed, scalability, and efficient storage are critical requirements.

# What is Airbyte?
A powerful open-source tool for data integration that simplifies the process of collecting, transforming, and transferring data from various sources to multiple destinations. It provides flexibility, scalability, and ease of use, making it a valuable asset for businesses in managing their data integration needs.

# What is DBT?
DBT, which stands for Data Build Tool
 - Open-source software tool used in the field of data engineering. 
 - Designed to help you manage and transform your data in a structured and scalable manner.
    - define and organize your data models (building blocks for your data pipelines)
- Provides a set of features and functionalities that make it easier to create, test, and maintain your data models
    - Incremental builds, which allow you to only update the parts of your data that have changed, making the process more efficient.
- Promotes collaboration and reproducibility
- Allows multiple data engineers to work on the same project concurrently, while ensuring that everyone is using the same set of rules and best practices. 
    - This helps to reduce errors and inconsistencies in your data pipelines.


# Building-a-CDC-with-Azure-CosmosDB-and-Redpanda

This project demonstrates how to set up a Change Data Capture (CDC) pipeline using Azure CosmosDB and Redpanda. It's designed to capture modifications in real-time from a database table in Azure CosmosDB and stream these changes to a Redpanda topic. This setup is particularly useful for scenarios requiring quick data access and updates, such as in financial trading or real-time analytics.

## Overview

Azure Cosmos DB is a fully managed NoSQL database service provided by Microsoft, known for its global distribution, horizontal scaling, and low-latency access. Redpanda is a streaming data platform that is API-compatible with Apache Kafka but designed to be simpler and faster.

In this project, we leverage Azure Cosmos DB's Change Feed feature and Redpanda to create a CDC system that captures every data modification in the Cosmos DB and streams it to Redpanda in real-time. This system is particularly valuable for applications that rely on up-to-the-minute data to make crucial decisions, such as trading platforms and online gaming.

## Prerequisites

Before starting, ensure you have the following installed and set up:

- Docker and Docker Compose (for running Redpanda)
- Python 3.10.12 or higher (for interacting with Azure Cosmos DB)
- An Azure account (to use Azure Cosmos DB)
- The Azure Cosmos DB Python SDK (installed via `pip`)

## Setup Instructions

### Setting Up Azure Cosmos DB

1. Create an Azure Cosmos DB account through the Azure portal.
2. Choose Azure Cosmos DB for NoSQL and follow the prompts to create your database instance.

### Running a Redpanda Cluster

1. Use Docker Compose to spin up a Redpanda cluster on your local machine.
2. Create a `docker-compose.yml` file based on the Redpanda documentation and run it.

### Configuring the Environment

Set up the necessary Python environment and install the Azure Cosmos DB Python SDK using pip. Organize your project directory with folders for source code, configuration files, and plugins necessary for integrating Redpanda with Azure CosmosDB.

### Implementing CDC with Azure CosmosDB and Redpanda

1. **Create a Database and Table in Cosmos DB**: Use the provided Python script to create a database, a container (table), and populate it with sample data.
2. **Set Up Redpanda to Connect to Azure Cosmos DB**: Configure Kafka Connect to interface with Redpanda and set up a source connector for Azure Cosmos DB to enable CDC.

### Consuming Change Data

Use Kafka's tools to consume messages from the Redpanda topic, reflecting the changes captured from the Cosmos DB.

## Usage

After setting up, you can run the provided Python script to insert or update data in the Azure Cosmos DB. The changes will automatically be captured and streamed to the specified Redpanda topic, which you can monitor using Kafka's console consumer tool.

For detailed commands and configuration specifics, refer to the respective sections above.


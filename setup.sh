#!/bin/bash

# Create the Streamlit credentials file
mkdir -p ~/.streamlit/
echo "[general]" > ~/.streamlit/credentials.toml
echo "email = \"tanmay5tj@gmail.com\"" >> ~/.streamlit/credentials.toml

# Create the Streamlit config file
echo "[server]" > ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "port = $PORT" >> ~/.streamlit/config.toml

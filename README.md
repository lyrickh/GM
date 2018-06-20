# MG

Reads in a file of json objects to be converted in to Impressions and stored in the RAM - data will not persist between 
runs

## Installation Instructions

1. cd to the project directory (MG)
2. run cmd "docker build -t python-mg ."
3. run cmd "docker run -d -p 5000:5000 python-mg"
4. The application is now running on http://127.0.0.1:5000/ !
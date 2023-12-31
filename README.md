# monitoringapp

Cloud Native Resource Monitoring Python App on K8s!

Memory Monitoring App using Flask and Psutil
docker pull flavian92/my-flask-app
This DevOps project aims to develop a Python application that monitors CPU and memory usage using Flask and the Psutil library. 
The application provides real-time insights into the system's resource utilization and allows users to track the performance of their machine.
Key Features:
CPU and Memory Monitoring: The Python app utilizes the Psutil library to collect data on CPU and memory usage.
Flask Web Interface: The application is built with Flask, a lightweight web framework, to provide a user-friendly interface for displaying the monitoring data.
Real-time Updates: The app continuously collects and updates the CPU and memory metrics to reflect the system's current status.
Dockerization: The project includes a Dockerfile that enables easy deployment and containerization of the Python application.
Python 3.9 and Buster: The Dockerfile specifies the base image as Python 3.9 on the Buster (Debian 10) operating system.
Pip3 Dependency Management: The Dockerfile installs project dependencies using pip3, ensuring all required packages are included in the container.
Benefits:
Efficient Monitoring: The app offers an efficient and centralized way to monitor CPU and memory usage in real-time.
Scalability: Dockerization allows for easy scalability and deployment across different environments.
Portability: The Docker container can be deployed on various platforms without worrying about specific system dependencies.
Simplified Dependency Management: Using pip3 to manage dependencies ensures the required packages are installed consistently.
By implementing this DevOps project, you can effectively monitor and analyze the CPU and memory utilization of your system, facilitating performance optimization and resource management. hashtag#devops hashtag#data hashtag#docker hashtag#management hashtag#project hashtag#python hashtag#scalability 

Part 1: Deploying the Flask application locally

Step 1: Clone the code
Clone the code from the repository:

git clone <repository_url>
Step 2: Install dependencies
The application uses the psutil and Flask, Plotly, boto3 libraries. Install them using pip:

pip3 install -r requirements.txt
Step 3: Run the application
To run the application, navigate to the root directory of the project and execute the following command:

python3 app.py
This will start the Flask server on localhost:5000. Navigate to http://localhost:5000/ on your browser to access the application.
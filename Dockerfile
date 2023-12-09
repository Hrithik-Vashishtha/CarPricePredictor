FROM ubuntu
WORKDIR /home/ubuntu/Kushmanda_Assignment/

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt install -y python3 python3-pip mysql-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    service mysql start && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Configure MySQL
RUN service mysql start && \
    mysql -e "CREATE USER 'hrithik'@'localhost' IDENTIFIED BY 'hrithik@12345';" && \
    mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'hrithik'@'localhost' WITH GRANT OPTION;" && \
    mysql -e "FLUSH PRIVILEGES;"

# Update MySQL configuration to bind to all interfaces
RUN sed -i 's/bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/' /etc/mysql/mysql.conf.d/mysqld.cnf

# Expose ports
EXPOSE 3306
EXPOSE 5000

# Set the entry point
CMD ["bash", "entrypoint.sh"]

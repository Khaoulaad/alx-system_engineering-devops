#!/bin/bash

# Install nginx if not already installed
sudo apt-get update -y
sudo apt-get install -y nginx

# Create a custom 404 page with the required content
echo '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>Ceci n\'est pas une page</p>
</body>
</html>' | sudo tee /var/www/html/404.html

# Configure Nginx to use the custom 404 page
sudo sed -i '/listen 80 default_server;/a \\n\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo systemctl restart nginx

# Display a message indicating the script has completed successfully
echo "Nginx configured with a custom 404 page."

# End of script


#!/usr/bin/env bash
# bash script that sets up your web servers for deployment

if ! command -v nginx &> /dev/null; then
	sudo apt update
	sudo apt install -y nginx
fi

web_static_dir="/data/web_static"
test_dir="$web_static_dir/releases/test"
shared_dir="$web_static_dir/shared"
current_dir="$web_static_dir/current"

sudo mkdir -p "$web_static_dir" "$test_dir" "$shared_dir"
echo "Holberton School" | sudo tee "$test_dir/index.html"
if [ -L "$current_dir" ]; then
	sudo rm -rf $current_dir
fi
sudo ln -s $test_dir $current_dir
sudo chown -R ubuntu: $web_static_dir

#update Nginx configuration
config="server_name _;\n\tlocation \/hbnb_static {\n\t\talias $current_dir\;\n\t}"
sudo sed -i "s#server_name _;#$config#" /etc/nginx/sites-available/default

sudo service nginx restart

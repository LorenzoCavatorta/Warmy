#http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html

#then http://www.rabbitmq.com/install-debian.html
echo 'deb http://www.rabbitmq.com/debian/ testing main' |  sudo tee /etc/apt/sources.list.d/rabbitmq.list

wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get install rabbitmq-server

sudo rabbitmqctl add_user admin password
sudo rabbitmqctl add_vhost test
sudo rabbitmqctl set_user_tags lollo test_tag
sudo rabbitmqctl set_user_tags admin test_tag
sudo rabbitmqctl set_permissions -p test admin ".*" ".*" ".*"
sudo rabbitmq-server
sudo rabbitmqctl stop
sudo rabbitmq-server
 

bash clearlogs.sh &

php -S 0.0.0.0:8000 index.php &

while :
do
	phantomjs admin_simulate_job.js 
	sleep 7
	echo "yo"
done

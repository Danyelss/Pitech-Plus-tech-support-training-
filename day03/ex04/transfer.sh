#check connection
gcloud compute ssh my-vm-eu --zone=europe-west1-b --command="ps -ejH"
#copy image
gcloud compute scp ~/weeknd.jpg ~/weeknd.jpg  my-vm-us:~/ --zone=us-central1-c


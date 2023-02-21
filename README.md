# sample_flask_services

* Comment or uncomment blueprint prefix based on requirement.

     File ```service_1/run_server.py```
     
     ```app.register_blueprint(app_api,url_prefix="/c1")```

     File ```service_2/run_server.py```
     
     ```app.register_blueprint(app_api,url_prefix="/c2")```
     

* Do docker build from root directory itself

 ```sudo docker build -t service_0:latest -f service_0/Dockerfile .```

 ```sudo docker build -t service_1:latest -f service_1/Dockerfile .```

 ```sudo docker build -t service_2:latest -f service_2/Dockerfile .```

* Then tag and push the docker images to respective container registry.

* Update the correct image uri to the yaml deployment file present inside each folder
   * service_0/service_0.yaml
   * service_1/service_1.yaml
   * service_2/service_2.yaml

* (If required) Update Port type & service names in those YAML files

* Then use those YAML files for deploying the services

* Create required load balancer and other related things.

* Finally make changes and run the ingress.yaml file



Health Checks

 [Google cloud health check](https://cloud.google.com/load-balancing/docs/health-check-concepts?authuser=1#example "Google cloud health check") 

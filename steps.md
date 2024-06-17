
# Steps  

## Creating an Local API
```bash
python3 -m venv venv 
source venv/bin/activate
pip3 install .
```

### Test 
```bash
streamlit run main.py 
```


## Containerization
Build first image **toml**.
```bash
docker build -t car-api:v2 .
```

Run image.
```bash
docker run -it --rm -P car-api:v2
```

## Deploying on Kubernetes

### Installation 
- Install minikube Link: https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download
- Install kubernetes: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/


Start a minikube cluster.
```bash
minikube start
```

Get all objects across all namespaces.
```bash
kubectl get all -A
```

List images.
```bash
minikube image list
```

Load an image.
```bash
minikube image load car-api:v2
```

Create a deployment.
```bash
kubectl create deploy car-deploy --image=cool-api:v2
```

Create a service.
```bash
kubectl expose deploy/car-deploy --name=cool-service --target-port=8501 --port=1234
```
- `8501`: the port number where the application is running. When a request comes to this service, it would be forwarded to this port in one of the ports 
- `1234`: the port on the service in mv 


Launch a service 
```bash 
minikube service car-service
```
- Get the port number when running this command 
    

## Scale up on Kubernetes 

```bash
kubectl scale deploy/car-deploy --replicas=3
```
- replicas = 3: the total pod would be 3 so would create 2 new pods as there is already one


Get logs of 3 replicas 
- Open 3 terminals. In every terminal, type `kubectl logs -f PODFULLNAME1`

Launch the service 

```bash
minikube service car-service
```
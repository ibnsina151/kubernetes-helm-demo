# kubernetes-helm-demo

## Prerequisites
It's assumed that you have already booted a cluster in GKE and you are connected with it using gcloud connect command and helm is installed on your local machine.


1. First build two docker container with different tags using the following command `docker build . -t tag_of_the_container`
2. Push the container to remote container hub `docker push tag_of_the_container`
3. We used two container named `server` and `client` to form an ingress network

#### Install nginx-ingress controller in your kubernetes cluster 
```
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
helm init
```

### If you want to use only kubernetes cluster without helm
4. Change the image location in `k8s/deployments/server-deployment.yaml` under `spec.template.spec.containers[0].image`
5. Do the same for `k8s/deployments/client-deployment.yaml`
6. Now apply all the deployments using `kubectl apply -f k8s/deployments`
7. Apply all the services using `kubectl apply -f k8s/services`

### If you want to use only kubernetes cluster with helm
4. go to the charts folder using `cd kubernetes-helm-demo/` and run `helm dep up` to updated all the charts mentioned in `requirements.yaml`
5. Replace all the `image.server` and `images.client` values in `values.yaml`
6. Check the syntax using `helm template -f Chart.yaml .`
7. Install the chart file using `helm install -f Chart.yaml .`


### After Works
8. Access the loadbalancer ip from google console.
9. Accessing `/` will give 404 error. Please access `http://ip/server` or `http://ip/client`

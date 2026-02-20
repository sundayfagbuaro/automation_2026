# Directory Structure
gitops-lab/
│
├── bootstrap/
│   └── root-app.yaml
│
├── apps/
│   ├── ingress.yaml
│   ├── nfs-csi.yaml
│   └── monitoring.yaml
│
└── values/
    ├── ingress-values.yaml
    ├── nfs-csi-values.yaml
    └── monitoring-values.yaml


# Install Argocd
kubectl create namespace argocd

kubectl apply -n argocd -f \
https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl get pods -n argocd

# Expose Argocd UI
kubectl port-forward svc/argocd-server -n argocd 8080:443

# Get The Default Password
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d

# Connect from the web with user - admin and the reyreived password
https://localhost:8080

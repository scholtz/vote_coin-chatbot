kubectl create namespace chat-bot
kubectl create secret generic settings-secret --from-literal=token=mytoken -n chat-bot
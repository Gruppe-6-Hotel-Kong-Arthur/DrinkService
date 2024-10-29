# DrinkService


```bash
docker build -t drinks_service . && docker image prune -f
```

```bash
docker run -d \        
  -p 5006:5006 \
  --name drinks_service \
  --network microservice-network \
  drinks_service
```

docker run -d -p 5004:5004 --name drinks_service --network microservice-network drinks_service

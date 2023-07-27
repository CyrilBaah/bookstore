# Variables
NAMESPACE = default
DEPLOYMENT = bookstore
SERVICE = bookstore
LOCALPORT := 8000
REMOTEPORT := 8000

# Targets
.PHONY: build push_image create_cluster

build:
	docker build -t cyrilbaah/bookstore .

push_image:
	docker push cyrilbaah/bookstore:latest

logs:
	kubectl logs -f deployments/$(DEPLOYMENT) -n $(NAMESPACE)

create_cluster:
	kind create cluster --config=workerNodes.yml
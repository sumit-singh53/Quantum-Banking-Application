# Quantum Banking Application Makefile
# Comprehensive build, test, and deployment automation

.PHONY: help install test security-scan build deploy clean
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
NC := \033[0m # No Color

# Project configuration
PROJECT_NAME := quantum-banking
DOCKER_REGISTRY := ghcr.io
NAMESPACE := quantum-banking
MONITORING_NAMESPACE := monitoring
LOGGING_NAMESPACE := logging

# Service list
SERVICES := user-service account-service payments-service kms-service fraud-service compliance-service anomaly-service notification-service api-gateway

help: ## Show this help message
	@echo "$(BLUE)Quantum Banking Application$(NC)"
	@echo "$(BLUE)=============================$(NC)"
	@echo ""
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies and setup development environment
	@echo "$(BLUE)Installing dependencies...$(NC)"
	@pip install --upgrade pip
	@pip install bandit safety semgrep pytest pytest-cov pytest-django
	@pip install docker-compose
	@echo "$(GREEN)Dependencies installed successfully$(NC)"

test: ## Run all tests
	@echo "$(BLUE)Running all tests...$(NC)"
	@python tests/infrastructure/test_runner.py --type all --verbose
	@echo "$(GREEN)All tests completed$(NC)"

test-service-mesh: ## Run service mesh tests
	@echo "$(BLUE)Running service mesh tests...$(NC)"
	@python tests/infrastructure/test_runner.py --type service-mesh --verbose

test-monitoring: ## Run monitoring tests
	@echo "$(BLUE)Running monitoring tests...$(NC)"
	@python tests/infrastructure/test_runner.py --type monitoring --verbose

test-security: ## Run security tests
	@echo "$(BLUE)Running security tests...$(NC)"
	@python tests/infrastructure/test_runner.py --type security --verbose

test-devsecops: ## Run DevSecOps pipeline tests
	@echo "$(BLUE)Running DevSecOps tests...$(NC)"
	@python tests/infrastructure/test_runner.py --type devsecops --verbose

security-scan: ## Run comprehensive security scan
	@echo "$(BLUE)Running security scan...$(NC)"
	@if [ -f scripts/security-scan.sh ]; then \
		bash scripts/security-scan.sh; \
	else \
		echo "$(YELLOW)Security scan script not found, using Docker Compose...$(NC)"; \
		docker-compose --profile security -f docker-compose.security.yml run --rm bandit-scanner; \
		docker-compose --profile security -f docker-compose.security.yml run --rm safety-scanner; \
		docker-compose --profile security -f docker-compose.security.yml run --rm pqc-auditor; \
	fi
	@echo "$(GREEN)Security scan completed$(NC)"

security-scan-docker: ## Run security scan using Docker Compose
	@echo "$(BLUE)Running security scan with Docker...$(NC)"
	@docker-compose --profile security -f docker-compose.security.yml up --abort-on-container-exit
	@echo "$(GREEN)Docker security scan completed$(NC)"

build: ## Build all Docker images
	@echo "$(BLUE)Building Docker images...$(NC)"
	@for service in $(SERVICES); do \
		echo "Building $$service..."; \
		docker build -t $(PROJECT_NAME)/$$service:latest services/$$service/ || exit 1; \
	done
	@echo "$(GREEN)All images built successfully$(NC)"

build-service: ## Build specific service (usage: make build-service SERVICE=user-service)
	@if [ -z "$(SERVICE)" ]; then \
		echo "$(RED)Error: SERVICE parameter required$(NC)"; \
		echo "Usage: make build-service SERVICE=user-service"; \
		exit 1; \
	fi
	@echo "$(BLUE)Building $(SERVICE)...$(NC)"
	@docker build -t $(PROJECT_NAME)/$(SERVICE):latest services/$(SERVICE)/
	@echo "$(GREEN)$(SERVICE) built successfully$(NC)"

push: ## Push Docker images to registry
	@echo "$(BLUE)Pushing images to registry...$(NC)"
	@for service in $(SERVICES); do \
		echo "Pushing $$service..."; \
		docker tag $(PROJECT_NAME)/$$service:latest $(DOCKER_REGISTRY)/$(PROJECT_NAME)/$$service:latest; \
		docker push $(DOCKER_REGISTRY)/$(PROJECT_NAME)/$$service:latest || exit 1; \
	done
	@echo "$(GREEN)All images pushed successfully$(NC)"

deploy-namespace: ## Create Kubernetes namespaces
	@echo "$(BLUE)Creating Kubernetes namespaces...$(NC)"
	@kubectl apply -f k8s/namespace.yaml
	@kubectl create namespace $(MONITORING_NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	@kubectl create namespace $(LOGGING_NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	@kubectl create namespace jaeger-system --dry-run=client -o yaml | kubectl apply -f -
	@echo "$(GREEN)Namespaces created$(NC)"

deploy-secrets: ## Deploy secrets and configmaps
	@echo "$(BLUE)Deploying secrets and configmaps...$(NC)"
	@kubectl apply -f k8s/secrets.yaml
	@kubectl apply -f k8s/configmaps.yaml
	@echo "$(GREEN)Secrets and configmaps deployed$(NC)"

deploy-infrastructure: ## Deploy infrastructure components (databases, message queues)
	@echo "$(BLUE)Deploying infrastructure components...$(NC)"
	@kubectl apply -f k8s/postgres.yaml
	@kubectl apply -f k8s/redis.yaml
	@kubectl apply -f k8s/kafka.yaml
	@kubectl apply -f k8s/vault.yaml
	@echo "$(GREEN)Infrastructure components deployed$(NC)"

deploy-services: ## Deploy application services
	@echo "$(BLUE)Deploying application services...$(NC)"
	@kubectl apply -f k8s/user-service.yaml
	@kubectl apply -f k8s/account-service.yaml
	@kubectl apply -f k8s/
	@echo "$(GREEN)Application services deployed$(NC)"

deploy-istio: ## Deploy Istio service mesh configuration
	@echo "$(BLUE)Deploying Istio service mesh...$(NC)"
	@kubectl apply -f k8s/istio/
	@echo "$(GREEN)Istio service mesh deployed$(NC)"

deploy-monitoring: ## Deploy monitoring stack (Prometheus, Grafana, Jaeger)
	@echo "$(BLUE)Deploying monitoring stack...$(NC)"
	@kubectl apply -f k8s/monitoring/
	@echo "$(GREEN)Monitoring stack deployed$(NC)"

deploy: deploy-namespace deploy-secrets deploy-infrastructure deploy-services deploy-istio deploy-monitoring ## Deploy complete application
	@echo "$(GREEN)Complete deployment finished$(NC)"

undeploy: ## Remove all deployed resources
	@echo "$(BLUE)Removing deployed resources...$(NC)"
	@kubectl delete namespace $(NAMESPACE) --ignore-not-found=true
	@kubectl delete namespace $(MONITORING_NAMESPACE) --ignore-not-found=true
	@kubectl delete namespace $(LOGGING_NAMESPACE) --ignore-not-found=true
	@kubectl delete namespace jaeger-system --ignore-not-found=true
	@echo "$(GREEN)Resources removed$(NC)"

logs: ## Show logs for all services
	@echo "$(BLUE)Showing service logs...$(NC)"
	@kubectl logs -n $(NAMESPACE) -l app=user-service --tail=50
	@kubectl logs -n $(NAMESPACE) -l app=account-service --tail=50

logs-service: ## Show logs for specific service (usage: make logs-service SERVICE=user-service)
	@if [ -z "$(SERVICE)" ]; then \
		echo "$(RED)Error: SERVICE parameter required$(NC)"; \
		echo "Usage: make logs-service SERVICE=user-service"; \
		exit 1; \
	fi
	@echo "$(BLUE)Showing logs for $(SERVICE)...$(NC)"
	@kubectl logs -n $(NAMESPACE) -l app=$(SERVICE) --tail=100 -f

port-forward-prometheus: ## Port forward Prometheus (localhost:9090)
	@echo "$(BLUE)Port forwarding Prometheus to localhost:9090$(NC)"
	@kubectl port-forward -n $(MONITORING_NAMESPACE) svc/prometheus 9090:9090

port-forward-grafana: ## Port forward Grafana (localhost:3000)
	@echo "$(BLUE)Port forwarding Grafana to localhost:3000$(NC)"
	@kubectl port-forward -n $(MONITORING_NAMESPACE) svc/grafana 3000:3000

port-forward-jaeger: ## Port forward Jaeger (localhost:16686)
	@echo "$(BLUE)Port forwarding Jaeger to localhost:16686$(NC)"
	@kubectl port-forward -n jaeger-system svc/jaeger-query 16686:16686

port-forward-kibana: ## Port forward Kibana (localhost:5601)
	@echo "$(BLUE)Port forwarding Kibana to localhost:5601$(NC)"
	@kubectl port-forward -n $(LOGGING_NAMESPACE) svc/kibana 5601:5601

status: ## Show deployment status
	@echo "$(BLUE)Deployment Status$(NC)"
	@echo "$(BLUE)=================$(NC)"
	@echo ""
	@echo "$(YELLOW)Namespaces:$(NC)"
	@kubectl get namespaces | grep -E "($(NAMESPACE)|$(MONITORING_NAMESPACE)|$(LOGGING_NAMESPACE)|jaeger-system)" || echo "No quantum banking namespaces found"
	@echo ""
	@echo "$(YELLOW)Services:$(NC)"
	@kubectl get pods -n $(NAMESPACE) 2>/dev/null || echo "No services deployed"
	@echo ""
	@echo "$(YELLOW)Monitoring:$(NC)"
	@kubectl get pods -n $(MONITORING_NAMESPACE) 2>/dev/null || echo "No monitoring stack deployed"

health-check: ## Run health checks on all services
	@echo "$(BLUE)Running health checks...$(NC)"
	@for service in $(SERVICES); do \
		echo "Checking $$service..."; \
		kubectl get pods -n $(NAMESPACE) -l app=$$service --no-headers 2>/dev/null | \
		awk '{print "  " $$1 ": " $$3}' || echo "  $$service: Not deployed"; \
	done

clean: ## Clean up Docker images and containers
	@echo "$(BLUE)Cleaning up Docker resources...$(NC)"
	@docker system prune -f
	@docker image prune -f
	@echo "$(GREEN)Cleanup completed$(NC)"

clean-reports: ## Clean up test and security reports
	@echo "$(BLUE)Cleaning up reports...$(NC)"
	@rm -rf reports/
	@echo "$(GREEN)Reports cleaned$(NC)"

dev-setup: install ## Setup development environment
	@echo "$(BLUE)Setting up development environment...$(NC)"
	@mkdir -p reports/security reports/tests
	@echo "$(GREEN)Development environment ready$(NC)"

dev-start: ## Start development services with Docker Compose
	@echo "$(BLUE)Starting development services...$(NC)"
	@docker-compose up -d postgres redis kafka vault
	@echo "$(GREEN)Development services started$(NC)"

dev-stop: ## Stop development services
	@echo "$(BLUE)Stopping development services...$(NC)"
	@docker-compose down
	@echo "$(GREEN)Development services stopped$(NC)"

lint: ## Run code linting
	@echo "$(BLUE)Running code linting...$(NC)"
	@for service in $(SERVICES); do \
		if [ -d "services/$$service" ]; then \
			echo "Linting $$service..."; \
			bandit -r services/$$service/ -f txt || true; \
		fi; \
	done
	@echo "$(GREEN)Linting completed$(NC)"

format: ## Format code (if formatters are available)
	@echo "$(BLUE)Formatting code...$(NC)"
	@for service in $(SERVICES); do \
		if [ -d "services/$$service" ] && command -v black >/dev/null 2>&1; then \
			echo "Formatting $$service..."; \
			black services/$$service/ || true; \
		fi; \
	done
	@echo "$(GREEN)Code formatting completed$(NC)"

docs: ## Generate documentation
	@echo "$(BLUE)Generating documentation...$(NC)"
	@echo "# Quantum Banking Application" > docs/README.md
	@echo "" >> docs/README.md
	@echo "Generated on: $$(date)" >> docs/README.md
	@echo "$(GREEN)Documentation generated$(NC)"

benchmark: ## Run performance benchmarks
	@echo "$(BLUE)Running performance benchmarks...$(NC)"
	@echo "$(YELLOW)Benchmark functionality not yet implemented$(NC)"

integration-test: ## Run integration tests
	@echo "$(BLUE)Running integration tests...$(NC)"
	@python tests/infrastructure/test_runner.py --type all --save-report
	@echo "$(GREEN)Integration tests completed$(NC)"

ci: security-scan test build ## Run CI pipeline (security scan, tests, build)
	@echo "$(GREEN)CI pipeline completed successfully$(NC)"

cd: ci deploy ## Run CD pipeline (CI + deploy)
	@echo "$(GREEN)CD pipeline completed successfully$(NC)"

# Development shortcuts
up: dev-start ## Alias for dev-start
down: dev-stop ## Alias for dev-stop
ps: status ## Alias for status
restart: dev-stop dev-start ## Restart development services
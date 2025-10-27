# Quantum Banking Application Setup Guide

## Quick Start

### Prerequisites
- Docker Desktop with Docker Compose
- Node.js 18+ (for frontend development)
- kubectl (for Kubernetes deployment)
- istioctl (for service mesh)

### Development Setup

1. **Clone and Setup**
   ```bash
   # Generate SSL certificates (Linux/Mac)
   ./scripts/generate-ssl-certs.sh
   
   # Or on Windows, run the equivalent PowerShell commands
   # See scripts/generate-ssl-certs.sh for certificate generation steps
   ```

2. **Start Infrastructure**
   ```bash
   # Start all services
   docker-compose up -d
   
   # Initialize databases and Kafka topics
   ./scripts/init-databases.sh
   
   # Or use the Makefile
   make setup
   make start
   make init-db
   ```

3. **Access Services**
   - API Gateway: http://localhost:8080
   - User Service: http://localhost:8001
   - Account Service: http://localhost:8002
   - Payments Service: http://localhost:8003
   - Fraud Service: http://localhost:8004
   - Compliance Service: http://localhost:8005
   - KMS Service: http://localhost:8006
   - Anomaly Service: http://localhost:8007
   - Notification Service: http://localhost:8008
   - Vault UI: http://localhost:8200
   - Frontend: http://localhost:3000

### Production Deployment

1. **Kubernetes with Istio**
   ```bash
   # Deploy to Kubernetes
   ./scripts/deploy-k8s.sh
   
   # Or use the Makefile
   make deploy
   ```

## Project Structure

```
quantum-banking-app/
├── services/                    # Microservices
│   ├── api-gateway/            # Nginx API Gateway
│   ├── user-service/           # Authentication & User Management
│   ├── account-service/        # Account Core Operations
│   ├── payments-service/       # Payment Processing
│   ├── fraud-service/          # Fraud Detection
│   ├── compliance-service/     # KYC/AML Compliance
│   ├── kms-service/           # Key Management Service
│   ├── anomaly-service/       # Anomaly Detection
│   └── notification-service/   # Multi-channel Notifications
├── frontend/                   # React Frontend
├── k8s/                       # Kubernetes Manifests
│   ├── istio/                 # Istio Service Mesh Config
│   ├── namespace.yaml         # Namespaces
│   ├── secrets.yaml           # Secrets
│   ├── configmaps.yaml        # ConfigMaps
│   ├── postgres.yaml          # PostgreSQL StatefulSets
│   ├── redis.yaml             # Redis StatefulSet
│   ├── kafka.yaml             # Kafka StatefulSet
│   ├── vault.yaml             # Vault StatefulSet
│   └── *-service.yaml         # Service Deployments
├── scripts/                   # Setup Scripts
│   ├── init-databases.sh      # Database Initialization
│   ├── generate-ssl-certs.sh  # SSL Certificate Generation
│   └── deploy-k8s.sh          # Kubernetes Deployment
├── config/                    # Configuration Files
│   ├── redis/                 # Redis Configuration
│   └── vault/                 # Vault Configuration
├── docker-compose.yml         # Development Environment
├── Makefile                   # Build Automation
├── README.md                  # Project Overview
└── ARCHITECTURE.md            # Detailed Architecture
```

## Key Features Implemented

### Infrastructure
✅ **Microservices Architecture**: 9 services with domain separation
✅ **Docker Containers**: Multi-stage builds with security scanning
✅ **Kubernetes Manifests**: Production-ready with Istio service mesh
✅ **PostgreSQL per Service**: Encrypted databases with SSL
✅ **Redis Caching**: Session management and caching
✅ **Kafka Event Streaming**: Asynchronous communication
✅ **HashiCorp Vault**: Secrets management with HSM support

### Security
✅ **Post-Quantum Cryptography**: Kyber-768 + Dilithium-3 ready
✅ **Zero-Trust Networking**: Istio mTLS between services
✅ **Phantom Token Architecture**: Opaque tokens with PQC-JWT
✅ **SSL/TLS Encryption**: End-to-end encryption
✅ **Network Policies**: Kubernetes network segmentation
✅ **Security Headers**: OWASP recommended headers

### Development Experience
✅ **Docker Compose**: Complete development environment
✅ **Makefile**: Automated build and deployment
✅ **Health Checks**: Service health monitoring
✅ **Logging**: Structured logging configuration
✅ **Scripts**: Automated setup and initialization

### Frontend Ready
✅ **React 18 + TypeScript**: Modern frontend stack
✅ **Premium Dark Theme**: Tailwind CSS with gradients
✅ **PWA Capabilities**: Progressive web app features
✅ **Build Pipeline**: Vite with optimized builds

## Next Steps

1. **Implement Service Logic**: Add business logic to each microservice
2. **Database Migrations**: Create Django models and migrations
3. **API Endpoints**: Implement REST APIs for each service
4. **Frontend Components**: Build React components with dark theme
5. **Testing**: Add unit and integration tests
6. **Monitoring**: Set up Prometheus and Grafana
7. **CI/CD Pipeline**: Implement DevSecOps pipeline

## Commands Reference

```bash
# Development
make setup          # Initial setup
make start          # Start all services
make stop           # Stop all services
make logs           # View logs
make status         # Service status

# Database
make init-db        # Initialize databases
make migrate        # Run migrations
make backup         # Backup databases

# Testing
make test           # Run all tests

# Deployment
make deploy         # Deploy to Kubernetes
make clean          # Clean up containers

# Monitoring
make monitor        # Monitor services
```

## Troubleshooting

### Common Issues
1. **Port Conflicts**: Ensure ports 3000, 5432-5439, 6379, 8001-8008, 8080, 8200, 29092 are available
2. **Docker Memory**: Increase Docker memory limit to at least 8GB
3. **SSL Certificates**: Generate certificates before starting services
4. **Vault Initialization**: Wait for Vault to be ready before accessing secrets

### Windows Specific
- Use PowerShell or WSL2 for script execution
- Docker Desktop must be running
- Enable Kubernetes in Docker Desktop for local deployment

This infrastructure provides a solid foundation for implementing the quantum banking application with modern microservices architecture and post-quantum cryptography security.
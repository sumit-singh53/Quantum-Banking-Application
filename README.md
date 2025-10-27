# 🏦 Quantum Banking Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-blue.svg)](https://kubernetes.io/)
[![Post-Quantum](https://img.shields.io/badge/Post--Quantum-Kyber768%20%7C%20Dilithium3-purple.svg)](https://csrc.nist.gov/projects/post-quantum-cryptography)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://www.docker.com/)
[![Security](https://img.shields.io/badge/Security-Zero--Trust-red.svg)](https://www.nist.gov/publications/zero-trust-architecture)
[![Compliance](https://img.shields.io/badge/Compliance-GDPR%20%7C%20PCI--DSS-green.svg)](https://gdpr.eu/)

**A next-generation fintech platform combining traditional banking with quantum-safe cryptography**

The Quantum Banking Application is an enterprise-grade microservices platform that revolutionizes financial technology by integrating **post-quantum cryptography** (Kyber-768 & Dilithium-3) with modern banking operations. Built for the quantum computing era, it provides secure payments, biometric authentication, AI-powered fraud detection, and GDPR-compliant data protection.

## Architecture Overview

This application implements a complete microservices architecture with domain separation:

### Core Banking Domain
- **Account Core Service** (Port 8002): Account balances and core operations
- **Payments Service** (Port 8003): Payment processing with Saga pattern
- **Compliance Service** (Port 8005): KYC/AML and regulatory compliance

### Security Domain  
- **User Service** (Port 8001): Authentication and user management
- **Key Management Service** (Port 8006): PQC key lifecycle management
- **API Gateway** (Port 8080): Entry point with phantom token introspection

### Intelligence Domain
- **Fraud Service** (Port 8004): Real-time fraud detection
- **Anomaly Detection Service** (Port 8007): Batch ML processing
- **Notification Service** (Port 8008): Multi-channel notifications

### Frontend & Validation
- **React Frontend** (Port 3000): Premium gradient dark theme interface
- **Auth Validation System**: Comprehensive authentication flow testing

## 🚀 Key Features

### 🔐 Quantum-Safe Security
- **Post-Quantum Cryptography**: Kyber-768 key encapsulation + Dilithium-3 digital signatures
- **Hybrid Encryption**: Seamless migration from classical to quantum-safe algorithms
- **Zero-Trust Architecture**: mTLS between all microservices with phantom token pattern
- **Biometric Authentication**: WebAuthn integration with fingerprint/face recognition
- **Cryptographic Agility**: Easy algorithm swapping for future quantum threats

### 🏛️ Enterprise Banking Features
- **Real-time Payments**: Instant transfers with Saga pattern for distributed transactions
- **AI Fraud Detection**: Machine learning algorithms for real-time risk assessment
- **Regulatory Compliance**: GDPR, PCI-DSS, and SOX compliance with audit trails
- **Multi-channel Notifications**: Email, SMS, and push notifications
- **Account Management**: Real-time balance updates with transaction history

### 🎨 Premium User Experience
- **Dark Gradient Theme**: Neumorphism + glassmorphism design with neon accents
- **3D Crypto Visualization**: Live PQC operations with D3.js animations
- **AI Banking Assistant**: Context-aware chatbot with voice interface
- **Responsive Design**: Mobile-first approach with PWA capabilities
- **Accessibility**: WCAG 2.2 compliant with screen reader support

### 📊 Advanced Analytics
- **PQC Performance Metrics**: Real-time cryptographic operation benchmarks
- **Fraud Heat Maps**: Geographic and temporal fraud pattern visualization
- **Compliance Dashboards**: Regulatory reporting and audit trail management
- **Business Intelligence**: Transaction analytics and user behavior insights

## 🏗️ Technology Stack

### Backend Microservices
- **Framework**: Django 4.2 with Django REST Framework
- **Databases**: PostgreSQL per service with field-level encryption
- **Caching**: Redis Cluster for session management and high-performance caching
- **Message Broker**: Apache Kafka for event streaming and async processing
- **API Gateway**: Nginx with OpenResty for phantom token introspection
- **Security**: HashiCorp Vault for secrets management with HSM integration

### Frontend & User Interface
- **Framework**: React 18 with TypeScript and feature-based architecture
- **State Management**: Redux Toolkit with RTK Query for API caching
- **Styling**: Tailwind CSS with custom gradient themes and animations
- **Charts**: D3.js and Recharts for interactive data visualization
- **Testing**: Vitest, React Testing Library, and Cypress for E2E testing

### Infrastructure & DevOps
- **Containerization**: Docker with multi-stage builds and security scanning
- **Orchestration**: Kubernetes with Istio service mesh for traffic management
- **Monitoring**: Prometheus + Grafana with custom business metrics
- **Tracing**: OpenTelemetry + Jaeger for distributed request tracing
- **CI/CD**: DevSecOps pipeline with automated security scanning (Bandit, Trivy, OWASP ZAP)

### Post-Quantum Cryptography
- **Key Encapsulation**: Kyber-768 for secure key exchange
- **Digital Signatures**: Dilithium-3 for authentication and integrity
- **Hybrid Mode**: Dual encryption (PQC + classical) during migration period
- **Key Management**: Automated rotation with 90-day lifecycle policies
- **Performance**: Optimized implementations with hardware acceleration support

## Quick Start

### Prerequisites
```bash
# Required tools
docker --version          # Docker 20.10+
docker-compose --version  # Docker Compose 2.0+
kubectl version           # Kubernetes 1.25+
node --version           # Node.js 18+
python --version         # Python 3.11+
```

### Development Setup
```bash
# 1. Clone and setup
git clone <repository-url>
cd quantum-banking-app

# 2. Start infrastructure
docker-compose up -d

# 3. Initialize databases
./scripts/init-databases.sh

# 4. Start frontend
cd frontend && npm install && npm run dev

# 5. Run authentication validation
cd auth-validation
pip install -r requirements.txt
python run_validation.py --mode validate --environment dev
```

### Production Deployment
```bash
# Complete system deployment
./scripts/deploy-complete-system.sh

# Or step-by-step
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/
```

### Authentication Flow Validation
```bash
# Run comprehensive validation
cd auth-validation
python run_validation.py --mode validate --environment staging

# Continuous monitoring
python run_validation.py --mode monitor

# Generate compliance report
python run_validation.py --mode compliance
```

## Services

| Service | Port | Description | Status |
|---------|------|-------------|--------|
| API Gateway | 8080 | Entry point with phantom token introspection | ✅ Complete |
| User Service | 8001 | Authentication and user management | ✅ Complete |
| Account Core Service | 8002 | Account balances and core operations | ✅ Complete |
| Payments Service | 8003 | Payment processing with Saga pattern | ✅ Complete |
| Fraud Service | 8004 | Real-time fraud detection | ✅ Complete |
| Compliance Service | 8005 | KYC/AML and regulatory compliance | ✅ Complete |
| Key Management Service | 8006 | PQC key lifecycle management | ✅ Complete |
| Anomaly Detection Service | 8007 | Batch ML processing | ✅ Complete |
| Notification Service | 8008 | Multi-channel notifications | ✅ Complete |
| Frontend | 3000 | React application with premium dark theme | ✅ Complete |
| Auth Validation System | - | Authentication flow validation framework | ✅ Complete |

## 🔒 Advanced Security Architecture

### Post-Quantum Cryptography Implementation
```
┌─────────────────────────────────────────────────────────────┐
│                 Quantum-Safe Security Layer                 │
├─────────────────────────────────────────────────────────────┤
│ • Kyber-768: Key Encapsulation Mechanism (KEM)             │
│ • Dilithium-3: Digital Signature Algorithm                 │
│ • Hybrid Encryption: PQC + Classical (Migration Period)    │
│ • Crypto-Agile Framework: Algorithm Swapping Capability    │
│ • CBOM: Cryptographic Bill of Materials Tracking           │
└─────────────────────────────────────────────────────────────┘
```

### Zero-Trust Security Model
- **Phantom Token Pattern**: Opaque tokens with PQC-signed JWT introspection
- **Mutual TLS (mTLS)**: Certificate-based authentication between all services
- **Network Segmentation**: Kubernetes network policies with Istio service mesh
- **Principle of Least Privilege**: Minimal required permissions for each service
- **Continuous Verification**: Real-time security posture assessment

### Data Protection & Privacy
- **Field-Level Encryption**: PQC encryption for PII and financial data
- **Encryption at Rest**: Database-level encryption with key rotation
- **GDPR Compliance**: Right to be forgotten with cryptographic erasure
- **Data Minimization**: Collect only necessary data with purpose limitation
- **Audit Trail**: Tamper-proof logging with digital signatures

### Authentication & Authorization
- **Multi-Factor Authentication**: Biometric (WebAuthn) + traditional factors
- **Role-Based Access Control (RBAC)**: Granular permission management
- **Session Management**: Secure session handling with Redis clustering
- **Device Trust**: Device fingerprinting and risk-based authentication
- **Adaptive Security**: Dynamic security controls based on risk assessment

## 🛠️ Development Guide

### Local Development Setup

#### Prerequisites Installation
```bash
# Install required tools
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs python3.11 python3-pip

# Verify installations
docker --version          # Docker 20.10+
kubectl version --client  # Kubernetes 1.25+
node --version            # Node.js 18+
python3 --version         # Python 3.11+
```

#### Quick Start (Development)
```bash
# 1. Clone repository
git clone https://github.com/sumit-singh53/Quantum-Banking-Application.git
cd Quantum-Banking-Application

# 2. Start infrastructure services
docker-compose up -d postgres redis kafka

# 3. Initialize databases
./scripts/init-databases.sh

# 4. Start all microservices
./scripts/start-services.sh

# 5. Launch frontend
cd frontend
npm install
npm run dev

# 6. Run authentication validation
cd ../auth-validation
pip install -r requirements.txt
python run_validation.py --mode validate --environment dev
```

#### Service-by-Service Development
```bash
# Start individual services for development
cd services/user-service
python manage.py runserver 8001

cd services/account-service  
python manage.py runserver 8002

cd services/payments-service
python manage.py runserver 8003

# Run service tests
python manage.py test
pytest --cov=apps --cov-report=html
```

### Testing Strategy

#### Frontend Testing
```bash
cd frontend

# Unit tests with Vitest
npm run test

# Component testing with React Testing Library
npm run test:components

# E2E testing with Cypress
npm run test:e2e

# Visual regression testing
npm run test:visual
```

#### Backend Testing
```bash
# Unit tests for each service
cd services/user-service
python manage.py test apps.authentication.tests
python manage.py test apps.users.tests

# Integration tests
pytest tests/integration/

# Load testing with Locust
cd tests/load
locust -f locustfile.py --host=http://localhost:8080
```

#### Security Testing
```bash
# PQC algorithm validation
cd tests/security
python test_pqc_performance.py
python test_crypto_agility.py

# Penetration testing
cd tests/security
python run_security_tests.py --target=http://localhost:8080

# Compliance validation
cd auth-validation
python run_validation.py --mode compliance --generate-report
```

### Code Quality & Standards

#### Pre-commit Hooks
```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Manual run
pre-commit run --all-files
```

#### Code Formatting
```bash
# Python (Black + isort)
black services/
isort services/

# TypeScript (Prettier + ESLint)
cd frontend
npm run lint:fix
npm run format
```

#### Security Scanning
```bash
# Python security scan
bandit -r services/ -f json -o security-report.json

# Container security scan  
trivy image quantum-banking:latest

# Dependency vulnerability scan
safety check --json
npm audit --audit-level=moderate
```

### Performance Optimization

#### Database Optimization
```sql
-- Index optimization for high-frequency queries
CREATE INDEX CONCURRENTLY idx_transactions_user_date 
ON transactions(user_id, created_at DESC);

-- Partitioning for large tables
CREATE TABLE transactions_2024 PARTITION OF transactions
FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```

#### Caching Strategy
```python
# Redis caching for frequently accessed data
@cache_result(timeout=300)  # 5 minutes
def get_account_balance(account_id):
    return Account.objects.get(id=account_id).balance

# Application-level caching
@lru_cache(maxsize=1000)
def get_user_permissions(user_id):
    return UserPermission.objects.filter(user_id=user_id)
```

### Monitoring & Debugging

#### Local Monitoring Stack
```bash
# Start monitoring services
docker-compose -f docker-compose.monitoring.yml up -d

# Access dashboards
open http://localhost:3001  # Grafana (admin/admin)
open http://localhost:9090  # Prometheus
open http://localhost:16686 # Jaeger
```

#### Debug Configuration
```python
# Django debug settings
DEBUG = True
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'quantum_banking': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

### API Documentation

#### Interactive API Docs
- **Swagger UI**: `http://localhost:8080/docs/`
- **ReDoc**: `http://localhost:8080/redoc/`
- **Postman Collection**: `docs/api/quantum-banking.postman_collection.json`

#### Service Documentation
- [User Service API](services/user-service/README.md)
- [Account Service API](services/account-service/README.md)  
- [Payments Service API](services/payments-service/README.md)
- [Fraud Service API](services/fraud-service/README.md)
- [Compliance Service API](services/compliance-service/README.md)

## 🚀 Production Deployment

### Kubernetes Deployment

#### Prerequisites
```bash
# Install Kubernetes tools
kubectl version --client
helm version
istioctl version

# Verify cluster access
kubectl cluster-info
kubectl get nodes
```

#### Complete System Deployment
```bash
# 1. Deploy infrastructure components
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secrets/
kubectl apply -f k8s/configmaps/

# 2. Deploy databases and message brokers
kubectl apply -f k8s/infrastructure/
kubectl wait --for=condition=ready pod -l app=postgresql --timeout=300s

# 3. Deploy microservices
kubectl apply -f k8s/services/
kubectl wait --for=condition=ready pod -l app=user-service --timeout=300s

# 4. Deploy frontend and API gateway
kubectl apply -f k8s/frontend/
kubectl apply -f k8s/gateway/

# 5. Configure Istio service mesh
kubectl apply -f k8s/istio/
```

#### Automated Deployment Script
```bash
# One-command deployment
./scripts/deploy-complete-system.sh --environment=production

# With custom configuration
./scripts/deploy-complete-system.sh \
  --environment=production \
  --replicas=3 \
  --enable-monitoring=true \
  --enable-backup=true
```

### Cloud Provider Deployments

#### AWS EKS Deployment
```bash
# Create EKS cluster
eksctl create cluster --name quantum-banking --region us-west-2 --nodes 3

# Deploy with AWS-specific configurations
kubectl apply -f k8s/aws/
kubectl apply -f k8s/aws/load-balancer.yaml
kubectl apply -f k8s/aws/rds-integration.yaml
```

#### Azure AKS Deployment  
```bash
# Create AKS cluster
az aks create --resource-group quantum-banking --name quantum-banking-cluster

# Deploy with Azure-specific configurations
kubectl apply -f k8s/azure/
kubectl apply -f k8s/azure/application-gateway.yaml
kubectl apply -f k8s/azure/cosmos-integration.yaml
```

#### Google GKE Deployment
```bash
# Create GKE cluster
gcloud container clusters create quantum-banking --num-nodes=3

# Deploy with GCP-specific configurations
kubectl apply -f k8s/gcp/
kubectl apply -f k8s/gcp/cloud-sql-proxy.yaml
kubectl apply -f k8s/gcp/cloud-armor.yaml
```

### Environment Configuration

#### Production Environment Variables
```bash
# Core application settings
ENVIRONMENT=production
DEBUG=false
SECRET_KEY=<secure-random-key>
DATABASE_URL=postgresql://user:pass@host:5432/db

# Post-Quantum Cryptography settings
PQC_ENABLED=true
KYBER_KEY_SIZE=768
DILITHIUM_VARIANT=3
HYBRID_MODE=false

# Security settings
VAULT_URL=https://vault.company.com
HSM_ENABLED=true
MTLS_ENABLED=true
RATE_LIMIT_ENABLED=true

# Monitoring and observability
PROMETHEUS_ENABLED=true
JAEGER_ENABLED=true
LOG_LEVEL=INFO
METRICS_ENABLED=true
```

#### Secrets Management
```yaml
# HashiCorp Vault integration
apiVersion: v1
kind: Secret
metadata:
  name: quantum-banking-secrets
type: Opaque
data:
  database-password: <base64-encoded>
  jwt-secret: <base64-encoded>
  pqc-private-key: <base64-encoded>
  vault-token: <base64-encoded>
```

### Monitoring & Observability

#### Prometheus Metrics
```yaml
# Custom business metrics
quantum_banking_transactions_total{service="payments", status="success"}
quantum_banking_pqc_operations_duration_seconds{algorithm="kyber768"}
quantum_banking_fraud_detection_accuracy{model="ml_v2"}
quantum_banking_user_sessions_active{region="us-west"}
```

#### Grafana Dashboards
- **Business Overview**: Transaction volumes, user growth, revenue metrics
- **Technical Performance**: Response times, error rates, throughput
- **Security Monitoring**: Authentication failures, fraud alerts, PQC performance
- **Infrastructure Health**: CPU, memory, disk usage, network traffic

#### Alerting Rules
```yaml
# Critical alerts
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "High error rate detected"

- alert: PQCPerformanceDegradation  
  expr: quantum_banking_pqc_operations_duration_seconds > 2.0
  for: 10m
  labels:
    severity: warning
  annotations:
    summary: "PQC operations taking longer than expected"
```

### Backup & Disaster Recovery

#### Database Backup Strategy
```bash
# Automated daily backups
kubectl create cronjob postgres-backup \
  --image=postgres:15 \
  --schedule="0 2 * * *" \
  -- pg_dump -h postgres-service quantum_banking > /backup/$(date +%Y%m%d).sql

# Point-in-time recovery setup
kubectl apply -f k8s/backup/postgres-pitr.yaml
```

#### Multi-Region Deployment
```bash
# Primary region (us-west-2)
kubectl config use-context us-west-2
kubectl apply -f k8s/production/

# Secondary region (us-east-1) 
kubectl config use-context us-east-1
kubectl apply -f k8s/disaster-recovery/
```

## 🤝 Contributing

We welcome contributions to the Quantum Banking Application! Please follow our contribution guidelines:

### Development Workflow
1. **Fork the repository** and create your feature branch
   ```bash
   git checkout -b feature/quantum-enhancement
   ```

2. **Follow coding standards** and run tests
   ```bash
   # Python code formatting
   black services/
   isort services/
   
   # TypeScript formatting  
   cd frontend && npm run lint:fix
   
   # Run comprehensive tests
   ./scripts/run-all-tests.sh
   ```

3. **Security validation** before committing
   ```bash
   # Security scans
   bandit -r services/
   npm audit --audit-level=moderate
   
   # PQC algorithm validation
   python tests/security/validate_pqc.py
   ```

4. **Commit with conventional format**
   ```bash
   git commit -m "feat(pqc): add Kyber-1024 support for enhanced security"
   git commit -m "fix(auth): resolve WebAuthn timeout issue"
   git commit -m "docs(api): update payment service documentation"
   ```

5. **Create Pull Request** with detailed description
   - Describe the changes and motivation
   - Include test results and security scan reports
   - Reference any related issues
   - Add screenshots for UI changes

### Contribution Areas
- **🔐 Post-Quantum Cryptography**: Algorithm implementations, performance optimizations
- **🏦 Banking Features**: New financial products, payment methods, compliance features  
- **🎨 User Interface**: Design improvements, accessibility enhancements, mobile optimization
- **🔍 Security**: Vulnerability fixes, security feature enhancements, audit improvements
- **📊 Analytics**: New metrics, dashboard improvements, reporting features
- **🧪 Testing**: Test coverage improvements, performance testing, security testing
- **📚 Documentation**: API documentation, deployment guides, troubleshooting guides

### Code Review Process
1. **Automated Checks**: All PRs must pass CI/CD pipeline
2. **Security Review**: Security team review for crypto and auth changes
3. **Architecture Review**: Senior developer review for significant changes
4. **Testing Validation**: QA team validation for user-facing features
5. **Final Approval**: Maintainer approval and merge

### Community Guidelines
- **Be Respectful**: Treat all contributors with respect and professionalism
- **Be Constructive**: Provide helpful feedback and suggestions
- **Be Collaborative**: Work together to improve the project
- **Follow Standards**: Adhere to coding standards and best practices
- **Security First**: Always consider security implications of changes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Post-Quantum Cryptography algorithms: Kyber-768 and Dilithium-3
- NIST Post-Quantum Cryptography Standardization
- Open source community for various libraries and tools

## Contact

- Repository: [sumit-singh53/Quantum-Banking-Application](https://github.com/sumit-singh53/Quantum-Banking-Application)
- Issues: [GitHub Issues](https://github.com/sumit-singh53/Quantum-Banking-Application/issues)
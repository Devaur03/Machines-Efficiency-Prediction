# Machine Efficiency Prediction Project

A comprehensive DevOps and GitOps pipeline project that predicts machine efficiency using machine learning models, containerized with Docker, and deployed on Kubernetes with ArgoCD for continuous deployment.

## 🚀 Project Overview

This project demonstrates a complete end-to-end DevOps pipeline that:
- Analyzes machine operational data to predict efficiency status
- Builds and deploys ML models using Jenkins CI/CD
- Containerizes applications with Docker
- Implements GitOps practices with ArgoCD
- Deploys on Kubernetes infrastructure

## 📸 Project Documentation

### Screenshots Gallery
All project screenshots are organized in the `GitOps-Project-Screenshots/` directory:

| Component | Screenshot | Description |
|-----------|------------|-------------|
| **Jenkins Pipeline start** | ![Jenkins Pipeline](static\j1.png)| Complete CI/CD pipeline with initial stage |
| **Jenkins Pipeline finish** | ![GitHub](static\j9.png) | Complete CI/CD pipeline with last stage |
| **DockerHub Repository** | ![DockerHub](static\d_hub.png) | Docker images with tags and push timestamps |
| **GCP VM Instance** | ![GCP VM](static\vm_instance.png) | Running VM with external IP and open ports |
| **ArgoCD Application** | ![ArgoCD App](static\argo_cd.png) | Healthy and synced GitOps application |
| **Running Application** | ![App Browser](static\ap.png) | Live application accessible via browser |
| **Terminal Commands** | ![Terminal](static\t1.png) | Kubernetes and Docker commands execution |
| **Docker Containers** | ![Terminal](static\t2.png) | Kubernetes and Docker commands execution |

### 🎥 Video Demonstration
Watch the complete project walkthrough and demonstration (CLICK ON THE IMAGE):

[![Machine Efficiency Prediction - DevOps Pipeline Demo](static\ap.png)](https://youtu.be/U7jJznH_eSs)

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   GitHub Repo   │───▶│   Jenkins CI    │───▶│   DockerHub     │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       ▼                       │
         │              ┌─────────────────┐              │
         │              │   Build & Test  │              │
         │              │                 │              │
         │              └─────────────────┘              │
         │                                               │
         ▼                                               ▼
┌─────────────────┐                            ┌─────────────────┐
│   ArgoCD GitOps │◀───────────────────────────│  Kubernetes     │
│                 │                            │  Deployment     │
└─────────────────┘                            └─────────────────┘
```

## 🛠️ Technology Stack

### DevOps & Infrastructure
- **CI/CD**: Jenkins with Blue Ocean
- **GitOps**: ArgoCD
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Minikube)
- **Cloud Platform**: Google Cloud Platform (GCP)
- **Version Control**: Git/GitHub

### Machine Learning & Development
- **Language**: Python
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Web Framework**: Flask/FastAPI
- **Data Processing**: Pandas, NumPy

## 📁 Project Structure

```
Machines-Efficiency-Prediction/
├── src/
│   ├── app.py                 # Main application
│   ├── model.py              # ML model implementation
│   ├── data_preprocessing.py  # Data processing utilities
│   └── requirements.txt      # Python dependencies
├── manifests/
│   ├── deployment.yaml       # Kubernetes deployment
│   ├── service.yaml         # Kubernetes service
│   └── namespace.yaml       # Kubernetes namespace
├── Dockerfile               # Container configuration
├── Jenkinsfile             # Jenkins pipeline configuration
├── data/
│   └── machine_data.csv    # Training dataset
├── tests/
│   └── test_app.py         # Unit tests
├── README.md
└── LICENSE
```

## 🚀 Getting Started

### Prerequisites
- Docker installed
- Kubernetes cluster (Minikube recommended)
- Jenkins with required plugins
- ArgoCD installed
- GitHub account with PAT
- DockerHub account

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Machines-Efficiency-Prediction.git
   cd Machines-Efficiency-Prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r src/requirements.txt
   ```

3. **Run the application locally**
   ```bash
   python src/app.py
   ```

### Docker Deployment

1. **Build Docker image**
   ```bash
   docker build -t devaur003/gitops-project:latest .
   ```

2. **Run container**
   ```bash
   docker run -p 8080:8080 devaur003/gitops-project:latest
   ```

### Kubernetes Deployment

1. **Apply manifests**
   ```bash
   kubectl apply -f manifests/
   ```

2. **Check deployment status**
   ```bash
   kubectl get all -n argocd
   ```

3. **Access the application**
   ```bash
   kubectl port-forward svc/my-service 9090:8080 -n argocd
   ```

## 🔄 CI/CD Pipeline

### Jenkins Pipeline Stages
1. **Checkout**: Pull code from GitHub repository
2. **Build**: Create Docker image
3. **Test**: Run unit tests
4. **Push**: Push image to DockerHub
5. **Deploy**: Trigger ArgoCD sync (optional)

### GitOps with ArgoCD
- **Repository**: Connected to GitHub repo
- **Application**: `gitopsapp`
- **Sync Policy**: Automatic or manual
- **Target**: Kubernetes cluster

## 📊 Model Performance

The machine efficiency prediction model analyzes multiple operational parameters to determine:
- **Efficiency Status**: High/Medium/Low efficiency classification
- **Predictive Maintenance**: Proactive maintenance recommendations
- **Operational Optimization**: Performance improvement suggestions

## 🔧 Configuration

### Jenkins Credentials
- `gitops-dockerhub-token`: DockerHub authentication
- `github-token`: GitHub Personal Access Token

### ArgoCD Configuration
- **Repository URL**: GitHub repository
- **Target Revision**: `mybch` branch
- **Path**: `manifests/`
- **Destination**: Kubernetes cluster

## 🌐 Access Points

- **Application**: `http://<external-ip>:30863` (NodePort)
- **ArgoCD UI**: `http://<external-ip>:8080`
- **Jenkins**: `http://<external-ip>:8080`

## 📝 Screenshots Documentation

For complete project documentation, screenshots are organized as:
```
GitOps-Project-Screenshots/
├── 1-Jenkins/
├── 2-DockerHub/
├── 3-GCP-VM/
├── 4-ArgoCD/
├── 5-Terminal/
├── 6-Browser-App/
└── 7-GitHub/
```

## 🧪 Testing

Run tests using:
```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Dev**
- GitHub: [@Devaur03](https://github.com/Devaur03)
- DockerHub: [devaur003](https://hub.docker.com/u/devaur003)

## 🙏 Acknowledgments

- Thanks to the open-source community for amazing tools
- Jenkins and ArgoCD communities for excellent documentation
- Kubernetes community for robust orchestration platform

## 📞 Support

If you have any questions or need help, please:
1. Check the documentation above
2. Search existing [Issues](https://github.com/yourusername/Machines-Efficiency-Prediction/issues)
3. Create a new issue if needed

---

⭐ **Star this repository if it helped you!**
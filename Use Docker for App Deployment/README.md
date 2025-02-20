# Docker
## Differences between virtualisation and containerisation
| Feature          | Virtualization 🖥️       | Containerization 📦     |
|-----------------|----------------------|----------------------|
| Definition      | Runs multiple OSes on a hypervisor. | Runs lightweight apps using shared OS. |
| Isolation      | Each VM has its own OS. | Containers share the host OS. |
| Resource Usage  | High (each VM includes a full OS). | Low (containers share the OS kernel). |
| Performance    | Slower (full OS overhead). | Faster (directly runs on the host OS). |
| Startup Time   | Minutes (loads entire OS). | Seconds (only starts the app). |
| Portability    | Limited (large VM images). | Highly portable (runs anywhere). |
| Use Case       | Running multiple OS environments. | Microservices, cloud apps, CI/CD. |
| Tools         | VMware, VirtualBox, Hyper-V. | Docker, Kubernetes, Podman. |

### What's Included in a Container vs. Virtual Machine?
| Component       | Container 📦              | Virtual Machine 🖥️          |
|----------------|-------------------------|-------------------------|
| Kernel         | Shared with the host OS  | Separate for each VM    |
| Operating System | Not included (uses host OS) | Full OS (Windows, Linux, etc.) |
| Libraries & Dependencies | Included for the app only | Included with the full OS |
| Application    | Runs inside the container | Runs inside the VM |
| Hypervisor     | ❌ Not needed              | ✅ Required to manage VMs |

### Benefits of Each (Virtual Machines vs. Containers)
🖥️ Virtual Machines (VMs) Benefits<br>
✅ Full Isolation:

Each VM has its own OS, providing strong security.
Ideal for running different OSes on one machine (e.g., Windows and Linux).<br>
✅ Better for Legacy Apps:

Great for apps that require a specific OS or system dependencies.<br>
✅ Stable & Reliable:

Works well in traditional enterprise environments.<br>
✅ Supports GUI-based Applications:

Unlike containers, VMs can run full desktop environments.<br>
📦 Container Benefits<br>
✅ Lightweight & Fast:

Starts in seconds (no OS boot required).<br>
Uses fewer resources since multiple containers share the same OS.<br>
✅ Highly Portable:

"Build once, run anywhere" (works the same across different environments).<br>
✅ Better for Microservices & Cloud:

Works well for DevOps, CI/CD, and modern cloud applications.<br>
✅ Scalability & Efficiency:<br>
Uses less memory and CPU compared to VMs, allowing more apps per server.

## Microservices
### What are they?
Microservices are a software architecture style where an application is broken down into small, independent services that communicate with each other. Each microservice:<br>
✔️ Handles a specific function (e.g., authentication, payment, inventory).<br>
✔️ Communicates via APIs (usually REST or gRPC).<br>
✔️ Can be developed, deployed, and scaled independently.<br>

### How Are Microservices Made Possible?
1. Containers & Orchestration
   * Docker: Packages microservices into isolated, portable containers.
   * Kubernetes: Manages, scales, and orchestrates microservices across multiple servers.
2. API Communication
   * RESTful APIs or gRPC: Allows microservices to talk to each other.
   * Message Brokers (Kafka, RabbitMQ): Helps in asynchronous communication.
3. DevOps & CI/CD
   * Continuous Integration/Continuous Deployment (CI/CD): Automates testing and deployment.
   * Infrastructure as Code (IaC) (Terraform, Ansible): Automates cloud/server provisioning.
4. Cloud & Scalability
   * Cloud Services (AWS, Azure, GCP): Provides managed services to deploy microservices.
   * Service Discovery (Eureka, Consul): Helps services locate each other dynamically.

## Docker- What is it
### What is it?
Docker is a containerization platform that allows developers to package applications and their dependencies into lightweight, portable containers. These containers can run on any environment (local, cloud, or on-premise) without compatibility issues.

🔹 Key Features:<br>
✅ Portability – "Write once, run anywhere"<br>
✅ Lightweight – Uses fewer resources than virtual machines<br>
✅ Fast Deployment – Containers start in seconds<br>
✅ Scalability – Easily scale applications across multiple servers<br>

### Alternatives
* Podman
* LXC (Linux Containers)
* Singularity 

### Success story: Netflix
Netflix needed to:

Scale services rapidly across different cloud environments.<br>
Improve developer productivity.<br>
Reduce deployment time for thousands of microservices.<br>
🔹 The Docker Solution:<br>
✅ Microservices with Docker: Netflix broke down its monolithic app into microservices, each running in Docker containers.<br>
✅ Consistent Environment: Developers could create identical local environments to production using Docker.<br>
✅ Scalability with Kubernetes: Containers were managed and scaled dynamically.<br>
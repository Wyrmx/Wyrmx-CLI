![Wyrmx-logo](https://github.com/user-attachments/assets/9aa1ec6b-1e2b-466e-8399-8044c60275c2)


# 🐉 Wyrmx CLI

**Wyrmx CLI** is the official command-line interface for **Wyrmx** — a modern, AI-assisted web framework built on **FastAPI** and **Uvicorn**.  

With Wyrmx CLI, you can scaffold, generate, and manage full-stack or microservice projects without the usual setup headaches. From controllers and services to models and schemas, everything is automated so you can focus on building your application, not boilerplate.  

---

## 📋 Prerequisites  
Before installing Wyrmx CLI, make sure you have:  
- **Python 3.13** installed  
- **pipx** (to install Wyrmx CLI globally)  
- **Poetry** installed globally (for dependency management)  

---

## ⚡ Installation  


Install Wyrmx CLI globally with:  

```bash
pipx install wyrmx-cli
```

Verify installation

```bash
wyrmx --help
```

## ✨ Quick Start  

Create a new project:

```bash 
wyrmx new <project-name>
cd <project-name>
```

Generate Common modules: 

```bash 
# Controllers / Services / Models / Schemas

wyrmx generate:controller <controller-name> 
wyrmx generate:service <service-name>
wyrmx generate:model <model-name>
wyrmx generate:schema <schema-name>
```

Run the server:

```bash
wyrmx run # defaults to http://127.0.0.1:8000
```

##  🚀 Features

###  🧠 AI-Enhanced Code Generation (in development)

Integrates LLMs via MCP to generate boilerplate directly in your project—no copy-pasting from chat windows.

###  ⚙️ Project Scaffolding

Spin up complete Wyrmx project structures with FastAPI + Uvicorn in seconds.

###  🛠 Modular Code Generation

Generate controllers, services, models, schemas via simple CLI commands.

### 🔧 HTTP Decorators

Decorators for request methods and paths—skip repetitive endpoint wiring.

### 📦 Build & Manage Projects

Alembic + SQLAlchemy for migrations and ORM usage

Poetry for dependency management

Pyright for pre-execution type checking

Pytest for testing, out of the box

### 🖥 Developer-Friendly CLI

No need to activate a venv each time—the CLI handles workflows.

Create boilerplate, run servers, and manage migrations with clear, concise commands.
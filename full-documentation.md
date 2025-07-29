## 1. Introduction

**Wyrmx CLI** is the official command-line interface for **Wyrmx**, a modern, AI-assisted web framework built on **FastAPI** and **Uvicorn**.  

Designed to streamline web development, Wyrmx CLI helps developers scaffold projects, generate boilerplate code, manage database migrations, and run servers—all directly from the terminal. With Wyrmx CLI, repetitive tasks like creating controllers, services, models, and schemas are automated, allowing you to focus on building the core functionality of your application.

Key highlights include:

- **Full Project Scaffolding**: Quickly create a new Wyrmx project with the correct folder structure, configurations, and dependencies.
- **Modular Code Generation**: Generate controllers, services, models, schemas, payloads, and responses using simple CLI commands.
- **Database Migrations**: Manage your database schema using Alembic and SQLAlchemy with commands for creating, applying, and rolling back migrations.
- **Developer-Friendly Workflow**: No need to manually activate virtual environments or copy boilerplate code—everything is handled seamlessly.
- **AI-Assisted Boilerplate Generation** *(in development)*: Integrate LLMs via MCP to generate reusable code templates directly in your project.

Whether you are building REST APIs, full-stack applications, or microservices, Wyrmx CLI accelerates development while ensuring best practices and maintainable code.


## 2. Prerequisites

Before using Wyrmx CLI, ensure your system meets the following requirements:

- **Python 3.13**: Wyrmx CLI requires Python 3.13 or higher. You can check your Python version with:

```bash
python --version
```

- **Pipx**: Used to install Wyrmx CLI globally so it can be run from anywhere. To install pipx:

```bash 
python -m pip install --user pipx
python -m pipx ensurepath
```

- **Poetry**: For dependency management and project builds. Recommended to install via pipx for global access:

```bash
pipx install poetry
```

> **Note: Make sure Python, pipx, and Poetry are correctly added to your system PATH to avoid any issues running Wyrmx commands.**


## 3. Installation

After ensuring the prerequisites are installed, you can install Wyrmx CLI globally using **pipx**:

```bash
pipx install wyrmx-cli
```

Once installed, verify that Wyrmx CLI is working correctly:

```bash
wyrmx --help
```

You should see the CLI usage instructions along with the list of available commands and options.

## 4. Architecture

Wyrmx follows a modular and structured architecture that separates responsibilities across different layers, making your codebase clean, maintainable, and scalable. The main components are:

- **Controller**: Handles incoming HTTP requests and routes them to the appropriate service. Responsible for request validation and returning responses.


- **Service**: Contains the business logic of the application. Controllers call services to execute core operations.

- **Model**: Manages data access and interactions with the database. Services use models to query or persist data.


- **Schema**: Represents database tables using SQLAlchemy models. Ensures a structured mapping between your Python objects and database tables.


- **Payload**: Pydantic classes representing the HTTP request body for each API endpoint. Used to validate and parse incoming request data.


- **Response**: Pydantic classes representing the HTTP response body for each API endpoint. Used to structure the data sent back to clients.


This separation of concerns ensures that each layer has a specific responsibility, promoting clean, testable, and reusable code.



## 5. CLI Overview
Wyrmx CLI provides a powerful command-line interface to interact with your projects. All commands are organized into three main categories:

### Global Options


| Option | Description |
|--------|-------------|
| `--version`, `-v` | Show Wyrmx CLI version |
| `--help` | Show CLI help and available commands |


### Command Categories

1. **Project Commands**
   - `new`: Create a new Wyrmx project with the proper folder structure and configuration.
   - `build`: Build and compile the Wyrmx project.
   - `run`: Start the Wyrmx server.
   - `test`: Run unit tests using Pytest.

2. **Code Generation Commands**
   - `generate:controller` (`gc`): Generate a new controller.
   - `generate:service` (`gs`): Generate a new service.
   - `generate:model` (`gm`): Generate a new data model.
   - `generate:schema` (`gsc`): Generate a new database schema.
   - `generate:payload` (`gp`): Generate a Pydantic request payload.
   - `generate:response` (`gr`): Generate a Pydantic response body.

3. **Database Migration Commands**
   - `migration:make`: Create a new database migration based on your current schemas.
   - `migration:apply`: Apply all pending migrations.
   - `migration:rollback`: Rollback the database schema to a previous state.
   - `migration:edit`: Open a migration file in an editor to modify it manually.

> The CLI provides shortcuts for many commands (e.g., `gc` for `generate:controller`) to speed up development.


## 6. Commands Reference

Wyrmx CLI commands are grouped into project management, code generation, and database migration. Each command comes with examples and shortcuts where applicable.

---

### Project Commands

#### `wyrmx new <project_name>`
Create a new Wyrmx project with the default folder structure, configuration files, and dependencies.

Example : 

```bash
wyrmx new app
cd app
```

#### `wyrmx build`

Build and compile your Wyrmx project. This step ensures type checking and prepares your project for deployment.

```bash
wyrmx build
```

#### `wyrmx run`

Start the Wyrmx server. By default, it runs on http://127.0.0.1:8000.

```bash
wyrmx run
```

#### `wyrmx test`

Run unit tests using Pytest.

```bash
wyrmx test
```

---

### Code Generation Commands


#### `wyrmx generate:controller <name> (gc)`

Generate a new controller file with default boilerplate.

```bash
wyrmx generate:controller user
# or using shortcut
wyrmx gc user
```

#### `wyrmx generate:service <name> (gs)`

Generate a service module for business logic.

```bash
wyrmx generate:service user
# or using shortcut
wyrmx gs user
```

#### `wyrmx generate:model <name> (gm)`
Generate a data model for database interactions.

```bash
wyrmx generate:model user
# or using shortcut
wyrmx gm user
```

#### `wyrmx generate:schema <name> (gsc)`
Generate a SQLAlchemy schema for the database table.

```bash
wyrmx generate:schema user
# or using shortcut
wyrmx gsc user
```

#### `wyrmx generate:payload <name> (gp)`
Generate a Pydantic class for HTTP request bodies.

```bash
wyrmx generate:payload create-user
wyrmx gp create-user
```

#### `wyrmx generate:response <name> (gr)`
Generate a Pydantic class for HTTP response bodies.

```bash
wyrmx generate:response create-user
wyrmx gr create-user
```


#### `wyrmx migration:make <name>`

Create a new database migration based on your current schemas.

```bash
wyrmx migration:make create_users_table
```

#### `wyrmx migration:apply`

Apply all pending database migrations.

```bash
wyrmx migration:apply
```

#### `wyrmx migration:rollback`

Rollback or downgrade the database schema to a previous state.

```bash
wyrmx migration:rollback
```

#### `wyrmx migration:edit <migration_hash>`

Open and edit a migration file manually in your default editor.

```bash
wyrmx migration:edit 2cd5dca62538
```

## 7. Quick Start Guide

This guide walks you through creating a new Wyrmx project, generating modules, running the server, and applying database migrations.


### Step 1: Create a New Project

```bash
wyrmx new my-app
cd my-app
```

This layout separates controllers, services, models, schemas, payloads, and responses for clean architecture.

```.
├── alembic.ini
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
    ├── app_module.py
    ├── conftest.py
    ├── controllers
    ├── main.py
    ├── migrations
    │   ├── engine.py
    │   ├── env.py
    │   ├── README
    │   ├── script.py.mako
    │   └── versions
    ├── models
    ├── payloads
    ├── responses
    ├── schemas
    └── services
```

### Step 2: Create a New Project

Create a controller, service, model, schema, payload, and response:


#### Controller

Create a controller for handling HTTP requests:

```bash
wyrmx gc user
```

Generated controller (`src/controllers/user_controller/user_controller.py`):

```python
from wyrmx_core import controller

@controller('user')
class UserController:

    def __init__(self):
        pass

    # Add your methods here
```

Generated test (`src/controllers/user_controller/test_user_controller.py`):

```python
import pytest
from src.controllers.user_controller.user_controller import UserController

class TestUserController:

    @pytest.fixture(autouse=True)
    def setup(self): self.controller = UserController()
```

#### Service

Create a service for business logic:

```bash
wyrmx gs user
```
Generated service (`src/services/user_service/user_service.py`):

```python
from wyrmx_core import service

@service
class UserService:

    def __init__(self):
        pass

    # Add your methods here
```

Generated test (`src/services/user_service/test_user_service.py`)

```python
import pytest
from src.services.user_service.user_service import UserService

class TestUserService:

    @pytest.fixture(autouse=True)
    def setup(self): self.service = UserService()
```

#### Model
Create a model for database interactions:

```bash
wyrmx gm user
```

Generated model (`src/models/user_model/user_model.py`)

```python
from wyrmx_core import model
from wyrmx_core.db import Model

@model
class User(Model):

    __schema__ = None  # Bind the schema that corresponds to this model

    def __init__(self):
        pass

    # Add your methods here
```

Generated test (`src/models/user_model/test_user_model.py`)

```python
import pytest
from wyrmx_core.db import Model
from src.models.user_model.user_model import User

class TestUser:

    @pytest.fixture(autouse=True)
    def setup(self, db_session):
        Model.bindSession(db_session)
        self.model = User()
```

#### Schema

Create a database schema:

```bash
wyrmx gsc user
```

Generated schema (`src/schemas/user_schema.py`):

```python
from wyrmx_core.db import DatabaseSchema
from wyrmx_core import schema

@schema
class UserSchema(DatabaseSchema):

    __tablename__ = 'User'

    # Define columns here
```

#### Payload

Create a Pydantic class for HTTP request bodies:

```bash
wyrmx gp create_user
```
Generated payload (`src/payloads/create_user_payload.py`):

```python
from wyrmx_core import payload
from pydantic import BaseModel

@payload
class CreateUserPayload(BaseModel):
    pass
```


#### Response

Create a Pydantic class for HTTP response bodies:

```bash
wyrmx gr create_user
```
Generated response (`src/responses/create_user_response.py`):

```python
from wyrmx_core import response
from pydantic import BaseModel

@response
class CreateUserResponse(BaseModel):
    pass
```







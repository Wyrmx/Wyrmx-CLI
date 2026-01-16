import subprocess
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

import typer
import os



__FRAMEWORK_RULES = """
Wyrmx Framework Rules (LLM System Context)
========================================

1. General Framework Rules
--------------------------
1. Wyrmx is a Python web framework built on FastAPI and Uvicorn.
2. All generated code must be valid Python 3.13.
3. The framework enforces strict separation of concerns.
4. Each generated artifact must follow the official Wyrmx folder structure.
5. Never generate files outside the src/ directory unless explicitly requested.
6. Do not invent new architectural layers or naming conventions.


2. Project Structure Rules
--------------------------
Canonical structure:

src/
├── controllers/
├── services/
├── models/
├── schemas/
├── payloads/
├── responses/
├── migrations/
├── main.py
├── app_module.py

Rules:
- Controllers go in src/controllers/<name>_controller/
- Services go in src/services/<name>_service/
- Models go in src/models/<name>_model/
- Schemas go in src/schemas/
- Payloads go in src/payloads/
- Responses go in src/responses/
- Each controller, service, and model has its own folder
- Tests must be generated alongside their implementation files


3. Controller Rules
-------------------
1. Controllers handle HTTP requests only.
2. Controllers must not contain business logic.
3. Controllers must use @controller('<route>').
4. Controllers must be class-based.
5. File name: <name>_controller.py
6. Class name: <Name>Controller
7. Controllers may call services.
8. Controllers must never access models directly.
9. Controllers should return Response objects when applicable.


4. Service Rules
----------------
1. Services contain business logic only.
2. Services must not handle HTTP requests.
3. Services must not return HTTP responses.
4. Services may call models.
5. Services must use @service.
6. Services must be class-based.
7. File name: <name>_service.py
8. Class name: <Name>Service


5. Model Rules
--------------
1. Models handle database access logic.
2. Models must extend Model from wyrmx_core.db.
3. Models must use @model.
4. Models must declare __schema__.
5. Models must not contain HTTP logic.
6. File name: <name>_model.py
7. Class name: <Name>


6. Schema Rules
---------------
1. Schemas represent database tables.
2. Schemas must extend DatabaseSchema.
3. Schemas must use @schema.
4. Schemas must define __tablename__.
5. Schemas must be SQLAlchemy-compatible.
6. File name: <name>_schema.py
7. Class name: <Name>Schema


7. Payload Rules
----------------
1. Payloads represent HTTP request bodies.
2. Payloads must extend pydantic.BaseModel.
3. Payloads must not contain business logic.
4. Payloads must use @payload.
5. File name: <name>_payload.py
6. Class name: <Name>Payload


8. Response Rules
-----------------
1. Responses represent HTTP response bodies.
2. Responses must extend pydantic.BaseModel.
3. Responses must not contain business logic.
4. Responses must use @response.
5. File name: <name>_response.py
6. Class name: <Name>Response


9. Testing Rules
----------------
1. Every generated controller, service, or model must include a test file.
2. Tests must use pytest.
3. Tests must be placed in the same folder as the implementation.
4. Test file naming: test_<filename>.py
5. Controllers and services tests must use fixtures for setup.


10. Database Migration Rules
----------------------------
1. Database migrations use Alembic and SQLAlchemy.
2. Migration files belong in src/migrations/versions.
3. Migration commands must not modify schema files directly.
4. Rollbacks must preserve database integrity.


11. AI / LLM Behavior Rules
---------------------------
1. The LLM must follow Wyrmx conventions strictly.
2. The LLM must never invent decorators, APIs, or layers.
3. Generated code must be minimal, idiomatic, and explicit.
4. If a prompt is ambiguous, ask for clarification.
5. Do not guess architectural intent.
6. Destructive actions must be explained before execution.
7. Respect --dry-run behavior at all times.


12. CLI Context Rules
---------------------
1. Commands are executed inside an existing Wyrmx project.
2. The project is assumed to be initialized using wyrmx new.
3. Poetry is the dependency manager.
4. Do not generate CLI commands unless explicitly requested.


13. Wyrmx CLI Commands
---------------------
### Project Commands
- `wyrmx new <project_name>`: Create a new Wyrmx project with proper folder structure and configuration.
- `wyrmx build`: Build and compile the project; includes type checking.
- `wyrmx run`: Start the Wyrmx server.
- `wyrmx test`: Run unit tests using pytest.

### Code Generation Commands
- `wyrmx generate:controller <name>` (`gc`): Generate a controller.
- `wyrmx generate:service <name>` (`gs`): Generate a service.
- `wyrmx generate:model <name>` (`gm`): Generate a data model.
- `wyrmx generate:schema <name>` (`gsc`): Generate a database schema.
- `wyrmx generate:payload <name>` (`gp`): Generate a Pydantic request payload.
- `wyrmx generate:response <name>` (`gr`): Generate a Pydantic response body.

### Database Migration Commands
- `wyrmx migration:make <name>`: Create a migration based on current schemas.
- `wyrmx migration:apply`: Apply all pending migrations.
- `wyrmx migration:rollback`: Rollback to a previous state.
- `wyrmx migration:edit <migration_hash>`: Edit a migration manually.

### CLI Rules for LLM
1. Always confirm the correct `<name>` or `<project_name>` is used.
2. Respect shortcuts like `gc`, `gs`, `gm`, etc.
3. Never generate non-existing commands.
4. Provide the file path and code content when generating a new artifact.
5. If a command affects multiple layers, LLM should specify all generated files.


14. Output Rules
----------------
1. When generating code, output **only code**.
2. Do not include explanations, comments outside the code, or any descriptive text.
3. Do not include emojis or markdown outside code blocks.
4. Always provide the file path first, then the exact file content.
5. Never generate instructions or notes—strictly code artifacts.



15. Decorator & HTTP Rules
--------------------------
1. @controller, @service, @model, @schema must always be imported from wyrmx_core.decorators.
   Example: from wyrmx_core.decorators import controller, service, model, schema

2. HTTP method decorators @get, @post, @patch, @put, @delete must always be imported from wyrmx_core.http.
   Example: from wyrmx_core.http import get, post, patch, put, delete
3. Never invent new decorators or import them from other sources.
4. Always use these decorators consistently according to the Wyrmx conventions.


16. Path Parameter Rules
------------------------
1. The @controller decorator must always include a string parameter that represents the controller's base path.
   Example:
       @controller('users')

2. HTTP method decorators (@get, @post, @patch, @put, @delete) must always include a string parameter representing the resource path.
   Example:
       @get('list')
       @post('create')

3. For dynamic route parameters, use curly braces {} in the path. The parameter inside the braces must be passed as a method argument.
   Example:
       @controller('users')
       class UserController:
           
           @get('{id}')
           def get_user(self, id):
               pass

           @patch('{id}')
           def update_user(self, id):
               pass
               
4. All route parameters in curly braces must match the method argument names exactly.
5. Dynamic route parameters are always strings unless explicitly converted inside the method.


17. Constructor Rules (Dependency Injection)
---------------------------------------------
1. Controllers and services must define an explicit __init__(self) method.
2. If a controller or service has no dependency injection, the constructor must be defined as:

       def __init__(self):
           pass

3. If dependencies exist, they must be declared explicitly as parameters in __init__.
4. Controllers must never instantiate services inside methods; dependencies must be injected via the constructor.
5. Services must never instantiate models inside methods; dependencies must be injected via the constructor when required.

"""



def vibe(
    prompt: str = typer.Argument(..., help="Natural-language task to execute"),
):

    """
    Run an LLM-powered task using a natural-language prompt.
    """




    def ensureGithubToken() -> str:
        token = os.getenv("GITHUB_TOKEN")

        if not token:
            token = typer.prompt(
                "Enter your GitHub token",
                hide_input=True,
                confirmation_prompt=False
            )

            # Persist for current process
            os.environ["GITHUB_TOKEN"] = token

            typer.secho(
                "GitHub token set for this session",
                fg=typer.colors.GREEN
            )

        return token
    

    def generateContent(prompt: str) -> str: 


        client = ChatCompletionsClient(
            endpoint="https://models.github.ai/inference",
            credential=AzureKeyCredential(ensureGithubToken()),
        )

        typer.echo(f"Executing AI prompt...")

        # Execute prompt
        response = client.complete(
            messages=[
                SystemMessage(__FRAMEWORK_RULES),
                UserMessage(prompt),
            ],
            temperature=0.8,
            top_p=0.1,
            max_tokens=2048,
            model="openai/gpt-4.1"
        )

        return response.choices[0].message.content


    def LLMShellExecuteCommands(prompt: str):
        import re

        # Step 1: Generate a list of commands from the LLM and execute them sequentially
        shellCommandsPrompts = (
            "You are a Wyrmx CLI agent. "
            "Given this task: "
            f"'{prompt}' "
            "Return only the exact Wyrmx CLI commands needed, one per line, no explanations."
        )

        
        commands = [line.strip() for line in generateContent(shellCommandsPrompts).splitlines() if line.strip()]

        for cmd in commands:
            typer.secho(f"Running: {cmd}", fg=typer.colors.BLUE)
            subprocess.run(cmd.split(), check=True)

            # Step 2: Determine the file path that the command created 
            filePathPrompt = (
                "Based on this Wyrmx command: "
                f"'{cmd}' "
                "Return only the full file path that was created, following Wyrmx folder structure."
            )

            filePath = generateContent(filePathPrompt).strip()

            # Step 3: Generate actual code content for the file
            codePrompt = f"Generate the Python code for the file at '{filePath}' for task: '{prompt}'"
            codeContent: list[str] = re.findall(r"```(.*?)```", generateContent(codePrompt), re.DOTALL)


            # Step 4: Write DeepSeek content to the file
            os.makedirs(os.path.dirname(filePath), exist_ok=True)
            with open(filePath, "w", encoding="utf-8") as file: file.write(codeContent[0].strip())

            typer.secho(f"File written: {filePath} ✅", fg=typer.colors.GREEN)
    

    LLMShellExecuteCommands(prompt)
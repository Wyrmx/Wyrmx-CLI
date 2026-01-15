from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

import typer
import os



__FRAMEWORK_RULES = """






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
    

    # prepare environment
    endpoint = "https://models.github.ai/inference"
    model = "deepseek/DeepSeek-V3-0324"
    token = ensureGithubToken()

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )


    # Execute prompt
    response = client.complete(
        messages=[
            SystemMessage(""),
            UserMessage(prompt),
        ],
        temperature=0.8,
        top_p=0.1,
        max_tokens=2048,
        model=model
    )

    print(response.choices[0].message.content)

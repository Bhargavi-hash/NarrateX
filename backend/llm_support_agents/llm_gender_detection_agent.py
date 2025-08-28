import subprocess
import json
import textwrap

MODEL_NAME = "tinyllama"  # Change if you prefer mistral, gemma, etc.

def infer_gender_with_llm(name: str, context: str) -> str:
    """
    Use a local LLM (tinyllamavia Ollama) to guess gender based on context.
    Returns: "male", "female", or "unknown"
    """
    prompt = textwrap.dedent(f"""
    You are an assistant that identifies character genders.
    Character: {name}
    Context: {context}

    Based on the above, answer with ONLY one word:
    male, female, or unknown.
    """)

    try:
        # Call Ollama through subprocess
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        raw_output = result.stdout.decode("utf-8").strip().lower()

        print("LLM raw output:", raw_output)

        # Normalize output
        if "male" in raw_output and "female" not in raw_output:
            return "male"
        elif "female" in raw_output and "male" not in raw_output:
            return "female"
        else:
            return "unknown"

    except subprocess.CalledProcessError as e:
        print("Error running Ollama:", e.stderr.decode("utf-8"))
        return "unknown"

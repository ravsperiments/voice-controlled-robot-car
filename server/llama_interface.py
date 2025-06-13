import requests
import json

def parse_command(text):
    prompt = f"Convert this to JSON: {text}"

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "phi3:mini",  # or whichever model you're running
            "prompt": prompt,
            "stream": False
        })

        result = response.json()
        raw_output = result.get("response", "")

        # Try to extract the first JSON object from the response
        json_start = raw_output.find("{")
        json_end = raw_output.rfind("}") + 1
        json_block = raw_output[json_start:json_end]

        return json.loads(json_block)

    except Exception as e:
        return { "error": f"Could not parse model response: {e}" }

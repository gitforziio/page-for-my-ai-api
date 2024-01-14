import requests

backend_url = ""
password = ""

async def use_ai(query, task, req_format, res_format, model="gpt-3.5-turbo-1106"):
    try:
        if not query or not query.strip():
            raise ValueError("query is empty")
        if not task or not task.strip():
            raise ValueError("task is empty")
        
        payload = {
            "query": query,
            "task": task,
            "reqFormat": req_format,
            "resFormat": res_format,
            "model": model,
            "password": password,
        }
        
        response = requests.post(backend_url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        return response.json()
    except Exception as err:
        print(f"Error: {err}")
        return {"type": "error", "error": str(err)}

async def use_ai4(query, task, req_format, res_format):
    return await use_ai(query, task, req_format, res_format, "gpt-4-1106-preview")

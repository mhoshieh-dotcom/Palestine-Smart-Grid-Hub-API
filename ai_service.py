from google import genai
from fastapi import HTTPException

MY_RAW_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"

def analyze_power_grid_load(grid_data: str) -> str:
    try:
        client = genai.Client(api_key=MY_RAW_API_KEY)
        
        system_instruction = (
            "You are an expert Electrical Engineering AI Assistant for the Palestine Smart Grid system. "
            "Analyze the provided power consumption data, identify peak load times, detect anomalies, "
            "and provide 3 concise technical recommendations to optimize the grid and prevent blackouts."
        )
        
        full_prompt = f"{system_instruction}\n\nHere is the real-time load data:\n{grid_data}"
        
        clean_prompt = full_prompt.encode("utf-8", errors="ignore").decode("utf-8")
        
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=clean_prompt
        )
        
        return response.text
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Engine Error: {str(e)}")

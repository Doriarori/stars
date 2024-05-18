import uvicorn
from fastapi import FastAPI, HTTPException, status
import requests

app = FastAPI()

NASA_API_KEY = "IqUcYN3j1nIgoalQuZQaduBJe14v1sPV7M1ozFSE"


@app.get("/health", status_code=status.HTTP_200_OK)
async def service_alive():
    return {'message': 'Service alive'}


@app.get("/apod")
async def astronomy_picture_of_the_day():
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail="Error retrieving APOD from NASA API")


@app.get("/neo")
async def near_earth_objects(start_date: str, end_date: str):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={NASA_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=400, detail="Error retrieving NEO data from NASA API")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))

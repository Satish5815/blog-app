from fastapi import FastAPI;

app=FastAPI();

app = FastAPI(
    title="Blog API",
    version="1.0.0",
    description="Production-ready Blog API"
)

@app.get('/health')
def health_check():
    return {
        'status':'Ok'
    }
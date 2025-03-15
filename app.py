from fastapi import FastAPI, Query, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# تمكين CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ربط المجلدات الثابتة والقوالب
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# نموذج بيانات الإخراج
class BMIOutput(BaseModel):
    bmi: float
    message: str

# عرض صفحة HTML عند زيارة الموقع
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# حساب BMI API
@app.get("/calculate_bmi")
def calculate_bmi(
    weight: float = Query(..., gt=20, lt=200, description="الوزن بالكيلوغرام"),
    height: float = Query(..., gt=1, lt=3, description="الطول بالمتر")
):
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        message = "لديك نقص في الوزن، كُل أكثر."
    elif 18.5 <= bmi < 25:
        message = "لديك وزن طبيعي، حافظ عليه."
    elif 25 <= bmi < 30:
        message = "لديك زيادة في الوزن، تمرن أكثر."
    else:
        message = "أنت تعاني من السمنة، قم بمراجعة طبيب."

    return BMIOutput(bmi=bmi, message=message)
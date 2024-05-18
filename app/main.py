from uuid import UUID, uuid4
from fastapi import FastAPI, File, HTTPException, Form, Depends,UploadFile, status
from pydantic import BaseModel, Field
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

# from backendwork.app.mediaHandler import mediaSaver
from . import crud, models, schemas
from .database import SessionLocal, engine
# from backendwork.app import EmailSender


# from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

#dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
        
        
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount('/uploadedFiles', StaticFiles(directory='uploadedFiles'),'uploadedFiles')

class College(BaseModel):
    
    name: str= Form(...)
    address: str= Form(...)
    email: str= Form(...)
    phone: str= Form(...)
    signatory: str = Form(...) 
    # logo: UploadFile = File(...)

# class TestCollege(BaseModel):
#     name: str
    # logo: FilePath

@app.get("/all", response_model=list[schemas.CollegeBase])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.College).all()
    return users

@app.get("/")
async def root():
    return {"message": "Hello World"}
  
# @app.post("/register")
# async def register(college: College):
#     print(college)
    
#     return {"message":"Success"}

from .validators import validate_phone_number, validate_email
from .EmailSender import send_registration_email
from .mediaHandler import mediaSaver

# @app.post("/register", response_model=list[schemas.CollegeBase])
@app.post("/register")
async def register(logo: UploadFile = File(...), name: str=Form(...), address: str=Form(...), email: str = Form(...), phone: str = Form(...), signatory: str=Form(...), signature_style: str=Form(...), db: Session = Depends(get_db)):
    print("Hello, World!")
    if not validate_email(email):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid Email. Email must be like example@mail.com")
        
    if not validate_phone_number(phone):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid Phone number. Phone number must be like 1234567890.")
    
    db_college = crud.get_college_by_email(db,email)
    if db_college:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered!")
    else:
        new_filename= mediaSaver(logo)
        if new_filename:
            media_dict = {
                "filename":new_filename,
                "size":logo.size
            }
            media = crud.save_media(db=db, media=media_dict)
            
            college_dict = {
                "college_name":name,
                "address":address,
                "official_email":email,
                "official_phone":phone,
                "signatory":signatory,
                "signature_style": signature_style,
                "logo_id":media.media_id                
            }
            
            college = crud.create_college(db=db, college=college_dict)
            send_registration_email(username=name,user_id=college.college_id,recipient_email=email)
            return JSONResponse(content={"message":f"An email with College ID is send to your mail address: {email}."},status_code=status.HTTP_201_CREATED)             
                
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="There is problem in saving the given file.")
    

@app.post("/login")
async def login(clgid: str = Form(...), db: Session = Depends(get_db)):
    college = crud.get_college_by_id(db=db,clgid=clgid)
    if college:
        return JSONResponse(content={"id":clgid}, status_code=status.HTTP_202_ACCEPTED)
    else:
        return JSONResponse(content="ID not exists", status_code=status.HTTP_401_UNAUTHORIZED)

# to get all projects stored in DB
@app.get("/all-projects", response_model=list[schemas.GetProjectData])
async def getAllProjects(db: Session = Depends(get_db)):
    projects = crud.fetchAllProjects(db=db)
    return projects


# Not made completely
from datetime import datetime
@app.post("/generate-mou")
async def submitProjects_GenerateMoU(project_ids: str = Form(...), start_date: datetime = Form(...), duration: int = Form(...), db: Session = Depends(get_db)):
    # print(project_ids.split(","))
    ids = project_ids.split(",")
    ids = list(map(int, ids))
    # print(ids)
    
    classified_projects_by_company = dict()
    for i in ids:
        # company_id = crud.getCompanyIDByProjectID(db,i).associated_company_id
        company_id = crud.getCompanyIDByProjectID(db,i)
        if company_id not in classified_projects_by_company.keys():
            classified_projects_by_company[company_id] = list([i])
        else:
            classified_projects_by_company[company_id].append(i)
    print(classified_projects_by_company)
    
    
    
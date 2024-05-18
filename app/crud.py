from sqlalchemy.orm import Session

from . import models, schemas

def get_all_user(db: Session):
    return db.query(models.College).all()

def get_college_by_email(db:Session, email: str):
    return db.query(models.College).filter(models.College.official_email == email).first()
    # return does_exists

def get_college_by_id(db: Session, clgid: str):
    return db.query(models.College).filter(models.College.college_id == clgid).first()

def save_media(db: Session, media: dict):
    db_media = models.MediaFiles(filename=media["filename"], size=media["size"])
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media

def create_college(db: Session, college: dict):
    db_college = models.College(college_name=college["college_name"],address=college["address"], official_email=college["official_email"],official_phone=college["official_phone"],signature_style=college["signature_style"],signatory=college["signatory"],logo_id=college["logo_id"])
    db.add(db_college)
    db.commit()
    db.refresh(db_college)
    return db_college

def fetchAllProjects(db: Session):
    return db.query(models.Project).all()

def getCompanyIDByProjectID(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.project_id==project_id).first()
    
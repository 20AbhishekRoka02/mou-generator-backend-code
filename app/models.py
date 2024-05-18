
# import uuid
# from networkx import project
from sqlalchemy import Column, Float, Integer, String, Text, Boolean, DateTime, ForeignKey, null
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
# from sqlalchemy.sql.functions import func
# from sqlalchemy.orm import validates
# import re

# from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


from .database import Base

class College(Base):
    __tablename__ = 'TestCollege'

    # College ID (UUID) - Auto-generated using gen_random_uuid() in PostgreSQL
    college_id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))

    # College Name - Unique and not null
    college_name = Column(String, unique=True, nullable=False)

    # Address - Long text and not null
    address = Column(Text, nullable=False)

    # Official email - Unique, valid email format, and not null
    official_email = Column(String, unique=True, nullable=False)

    # Official phone - Unique, valid phone number format, and not null
    official_phone = Column(String, unique=True, nullable=False)

    # Signatory - Unique, string, and not null
    signatory = Column(String, unique=True, nullable=False)
    
    # logo id
    logo_id = Column(UUID(as_uuid=True), ForeignKey("Media.media_id"))

    # Verified - Boolean with default value of False
    verified = Column(Boolean, nullable=False, server_default=text('false') ) 
    
    signature_style = Column(String, nullable=False)
    
    
    
    
    
    

class MediaFiles(Base):
    __tablename__ = "Media"
    
    media_id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    filename = Column(String, nullable=False)
    size = Column(Float, nullable=False)
    upload_date = Column(DateTime,server_default=text('now()') , nullable=False)
    

class Company(Base):
    __tablename__="Company"
    company_id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String(length=255), unique=True, nullable=False)
    company_short_name = Column(String(length=255), unique=True, nullable=True)
    company_address = Column(String, nullable=False)
    company_email = Column(String(255), nullable=False)
    company_phone = Column(String, nullable=False)
    logo_id = Column(UUID(as_uuid=True), ForeignKey("Media.media_id"))
    
    
class Project(Base):
    __tablename__="Projects"
    
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(length=255), unique=True, nullable=False)
    purpose = Column(String)
    context = Column(String)
    associated_company_id = Column(Integer, ForeignKey("Company.company_id"))

class ProjectDescription(Base):
    __tablename__ = "Project_Description"
    
    desc_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("Projects.project_id"))
    desc = Column(String, nullable=False)
    rate = Column(String, nullable=False)
    
class MoU(Base):
    __tablename__ = "mous"
    mou_id = Column(Integer, primary_key=True, autoincrement=True)
    mou_name = Column(String)
    start_date  = Column(DateTime, nullable=False)
    start_date  = Column(DateTime, nullable=False)
    comapny_id = Column(Integer, ForeignKey("Company.company_id"))
    project_id = Column(Integer, ForeignKey("Projects.project_id"))
    
    
    
    

    

    
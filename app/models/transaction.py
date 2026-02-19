from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    dataset_version = Column(String, nullable=False, default="v1")

    pipeline_run_id = Column(Integer, ForeignKey("pipeline_runs.id"), nullable=True)
    pipeline_run = relationship("PipelineRun")

    user = relationship(
        "User",
        back_populates="transactions"
    )
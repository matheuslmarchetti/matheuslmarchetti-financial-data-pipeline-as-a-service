from sqlalchemy.orm import Session
from app.models.pipeline_run import PipelineRun
from app.services.pipeline_service import (
    start_pipeline,
    finish_pipeline,
)
from app.models.transaction import Transaction

class PipelineRunner:
    """
    Responsável por orquestrar execução do pipeline.
    """

    def __init__(self, db: Session, pipeline: PipelineRun):
        self.db = db
        self.pipeline = pipeline


    def run(self, collector):
        try:
            start_pipeline(self.db, self.pipeline)

            data = collector.collect()

            for item in data:
                transaction = Transaction(
                    description=item["description"],
                    amount=item["amount"],
                    user_id=self.pipeline.created_by_id,
                    dataset_version="v1",
                    pipeline_run_id=self.pipeline.id,
                )

                self.db.add(transaction)

            self.db.commit()

            finish_pipeline(self.db, self.pipeline, success=True)

            return data

        except Exception:
            self.db.rollback()
            finish_pipeline(self.db, self.pipeline, success=False)
            raise
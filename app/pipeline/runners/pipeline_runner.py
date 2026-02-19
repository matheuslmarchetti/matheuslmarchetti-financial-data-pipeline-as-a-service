from sqlalchemy.orm import Session
from app.models.pipeline_run import PipelineRun
from app.services.pipeline_service import (
    start_pipeline,
    finish_pipeline,
)


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

            # Aula 16 ainda NÃO salva no banco
            # Apenas estrutura de execução

            finish_pipeline(self.db, self.pipeline, success=True)

            return data

        except Exception:
            finish_pipeline(self.db, self.pipeline, success=False)
            raise
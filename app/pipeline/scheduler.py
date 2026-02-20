from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.pipeline_run import PipelineRun
from app.pipeline.runners.pipeline_runner import PipelineRunner
from app.pipeline.collectors.yfinance_collector import YFinanceCollector


def run_daily_simulation():
    """
    Simula execução diária do pipeline.
    """

    db: Session = SessionLocal()

    try:
        # cria registro de execução
        pipeline = PipelineRun(
            name="daily_yfinance_pipeline",
            created_by_id=1,  # usuário admin fixo para simulação
        )

        db.add(pipeline)
        db.commit()
        db.refresh(pipeline)

        # executa runner
        collector = YFinanceCollector(symbol="AAPL")
        runner = PipelineRunner(db, pipeline)
        runner.run(collector)

    finally:
        db.close()
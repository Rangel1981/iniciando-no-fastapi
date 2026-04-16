from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout.contrib.models import BaseModel

# O bloco abaixo só é lido por ferramentas de linting (VS Code)
# O Python ignora isso ao rodar o código, evitando erro circular
if TYPE_CHECKING:
    from workout.categorias.models import CategoriaModel
    from workout.centro_treinamento.models import CentroTreinamentoModel

class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    # Relacionamento com Categoria
    # Usamos a string "CategoriaModel" para o SQLAlchemy e a tipagem para o VS Code
    categoria: Mapped["CategoriaModel"] = relationship("CategoriaModel", back_populates="atletas")
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.pk_id"), nullable=False)

    # Relacionamento com Centro de Treinamento
    centro_treinamento: Mapped["CentroTreinamentoModel"] = relationship("CentroTreinamentoModel", back_populates="atletas")
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey("centros_treinamentos.pk_id"), nullable=False)
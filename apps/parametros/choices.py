from model_utils import Choices

TIPO_MOV_CHOICES = Choices(
    (1, "INGRESO", "Ingresos"),
    (2, "EGRESO", "Egresos"),
    (3, "TRANSFER", "Transferencias"),
    (5, "NOTACR", "Nota de crédito"),
    (6, "NOTADB", "Nota de débito"),
    )

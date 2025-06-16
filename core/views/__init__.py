from .user import UserViewSet
from .fornecedor import FornecedorViewSet
<<<<<<< HEAD
from .categoria import CategoriaViewSet
from .produto import ProdutoViewSet
from .cliente import ClienteViewSet
from .funcionario import FuncionarioViewSet
from .cargo import CargoViewSet
from .estoque import EstoqueViewSet, MovimentacaoEstoqueViewSet
from .compra import CompraViewSet
from .venda import VendaViewSet
from .pagamento import FormaPagamentoViewSet, PagamentoViewSet
from .promocao import PromocaoViewSet
from .relatorio import RelatorioVendaViewSet, RelatorioEstoqueViewSet

__all__ = [
    'UserViewSet',
    'FornecedorViewSet',
    'CategoriaViewSet', 
    'ProdutoViewSet',
    'ClienteViewSet',
    'FuncionarioViewSet',
    'CargoViewSet',
    'EstoqueViewSet',
    'MovimentacaoEstoqueViewSet',
    'CompraViewSet',
    'VendaViewSet',
    'FormaPagamentoViewSet',
    'PagamentoViewSet',
    'PromocaoViewSet',
    'RelatorioVendaViewSet',
    'RelatorioEstoqueViewSet'
]
=======
from .produto import ProdutoViewSet
>>>>>>> 71aa74115a60bcd504a86ba66b965479b4e1a650

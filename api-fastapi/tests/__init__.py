from src.repositories.cidadeRepository  import CidadeRepository
from src.repositories.clienteRepository import ClienteRepository
from src.repositories.freteRepository   import FreteRepository

from src.models.cidade                  import Cidade
from src.models.cliente                 import Cliente
from src.models.frete                   import Frete

from src.schemas.cidadeSchemas          import *
from src.schemas.clienteSchemas         import *
from src.schemas.freteSchemas           import *

from src.services.freteService          import FreteService
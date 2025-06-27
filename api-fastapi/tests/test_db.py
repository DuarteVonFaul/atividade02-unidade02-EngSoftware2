from . import *

def test_cliente_database_insert(session):
    
    with session:
        reposity = ClienteRepository(session)
        cidade = reposity.add('Guilherme',
                              'Sao Luis - MA', 
                              '(99)99100-0000')
        


        ...

    assert cidade.codigo_cliente == 1
    
    ...
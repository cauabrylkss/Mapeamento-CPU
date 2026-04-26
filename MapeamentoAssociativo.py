import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento

# Parametros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal
# Altere a funcao para fazer uso da tecnica de mapeamento associativo


tabelaMapeados = [-1 for _ in range(0, 8)]
def mapeamentoAssociativo(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas

    global enderecoCache
    
    paginaRequisitada = endereco >> 2
    conteudoRequisitado = endereco & 3
    
    for j in range(len(tabelaMapeados)):
        if tabelaMapeados[j] == paginaRequisitada:
            print(tabelaMapeados)
            print("cache hit")
            return j
            
    print(f"Pag req: {paginaRequisitada} \n Conteudo req {conteudoRequisitado}")
    if -1 not in tabelaMapeados:
        print("cache cheiop")
        exit()
        
    for i in range(len(tabelaMapeados)):
        if (tabelaMapeados[i] == -1):
            enderecoCache = i;
            break
        
    pagina = memoriaSecundaria.getPagina(paginaRequisitada)
    
    memoriaPrincipal.setPagina(pagina, enderecoCache)
    tabelaMapeados[enderecoCache] = paginaRequisitada
    
    print(tabelaMapeados)    

    #retorna endereco
    return enderecoCache

#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '__main__':

    #executa funcao de mapeamento com 20 enderecos em modo Debug
    testaMapeamento(nEnderecos=20, 
                               nPaginasMemoriaPrincipal=8, 
                               nPaginasMemoriaSecundaria=16, 
                               debug=True, 
                               funcaoMapeamento=mapeamentoAssociativo,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=30000, 
                               nPaginasMemoriaPrincipal=1028, 
                               nPaginasMemoriaSecundaria=4096, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoAssociativo, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)


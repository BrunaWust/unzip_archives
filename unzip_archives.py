import zipfile
import os

def descompactar_pasta_zip(caminho_arquivo_zip, caminho_destino):
    """
    Função para descompactar um arquivo ZIP em um diretório específico.
    
    :param caminho_arquivo_zip: Caminho do arquivo ZIP a ser descompactado.
    :param caminho_destino: Diretório onde os arquivos descompactados serão armazenados.
    """
    try:
        # Verifica se o diretório de destino existe, caso contrário, cria
        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)
        
        # Abre o arquivo ZIP
        with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_ref:
            # Extrai todos os arquivos para o diretório de destino
            zip_ref.extractall(caminho_destino)
        
        print(f"Arquivo {caminho_arquivo_zip} descompactado com sucesso em: {caminho_destino}")
    except Exception as e:
        print(f"Ocorreu um erro ao descompactar o arquivo {caminho_arquivo_zip}: {e}")

def descompactar_todos_zips(pasta_zip, caminho_destino_base, caminho_destino_comum):
    """
    Função para descompactar todos os arquivos ZIP em uma pasta específica e também em uma pasta comum.
    
    :param pasta_zip: Caminho da pasta contendo os arquivos ZIP.
    :param caminho_destino_base: Diretório base onde os arquivos descompactados serão armazenados.
    :param caminho_destino_comum: Diretório onde todos os arquivos descompactados serão armazenados.
    """
    # Verifica se o diretório comum existe, caso contrário, cria
    if not os.path.exists(caminho_destino_comum):
        os.makedirs(caminho_destino_comum)
    
    for item in os.listdir(pasta_zip):
        if item.endswith('.zip'):
            caminho_arquivo_zip = os.path.join(pasta_zip, item)
            nome_arquivo = os.path.splitext(item)[0]
            caminho_destino = os.path.join(caminho_destino_base, nome_arquivo)
            
            # Descompacta na pasta específica
            descompactar_pasta_zip(caminho_arquivo_zip, caminho_destino)
            
            # Descompacta na pasta comum
            descompactar_pasta_zip(caminho_arquivo_zip, caminho_destino_comum)

# Exemplo de uso
pasta_zip =   # Substitua pelo caminho da pasta contendo os arquivos ZIP
caminho_destino_base = # Substitua pelo caminho do diretório de destino base
caminho_destino_comum =   # Substitua pelo caminho do diretório comum

descompactar_todos_zips(pasta_zip, caminho_destino_base, caminho_destino_comum)

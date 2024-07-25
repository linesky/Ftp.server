from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
#pip install pyftpdlib
# Definindo o diretório de trabalho
FILES_DIR = 'files'
os.makedirs(FILES_DIR, exist_ok=True)

# Função principal para configurar e iniciar o servidor FTP
def main():
    # Cria um DummyAuthorizer para gerenciar os usuários
    authorizer = DummyAuthorizer()

    # Adiciona um usuário com permissões de leitura e escrita
    # Parâmetros: username, password, homedir, perm
    authorizer.add_user("user", "12345", FILES_DIR, perm="elradfmw")

    # Adiciona um usuário anônimo (opcional)
    # authorizer.add_anonymous(FILES_DIR)

    # Cria um handler personalizado para o servidor FTP
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define o endereço e a porta do servidor FTP
    address = ("0.0.0.0", 21)
    server = FTPServer(address, handler)

    # Inicia o servidor FTP
    server.serve_forever()
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()


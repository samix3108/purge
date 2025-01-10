### Descrição do Código

#### Objetivo
O script automatiza dois processos comuns para desenvolvedores ou administradores de sistemas que desejam redefinir ou limpar o ambiente Python:

1. **Desinstalar todos os pacotes Python instalados:**
   - Utiliza o comando `pip freeze` para listar os pacotes instalados e, em seguida, desinstala cada um deles.
   - A desinstalação é feita automaticamente, sem solicitar confirmações, graças ao uso do parâmetro `-y`.

2. **Limpar o cache do pip:**
   - Remove os arquivos temporários armazenados pelo pip, economizando espaço em disco e garantindo um ambiente mais limpo.

---

#### Componentes Principais

1. **Função `uninstall_all_packages`:**
   - Lista todos os pacotes instalados usando `pip freeze`.
   - Desinstala cada pacote identificado.
   - Trata erros que possam ocorrer durante a listagem ou desinstalação.

2. **Função `clear_pip_cache`:**
   - Executa o comando `pip cache purge` para limpar os arquivos em cache.
   - Exibe mensagens informando o sucesso ou falha na operação.

3. **Bloco Principal (`if __name__ == "__main__"`):**
   - Chama as funções em sequência: primeiro desinstala os pacotes, depois limpa o cache.
   - Exibe mensagens de status para informar o progresso.

---

#### Aplicação Prática
Este script é útil para:
- Redefinir ambientes Python em máquinas de desenvolvimento ou produção.
- Limpar o ambiente antes de configurar novos pacotes ou dependências.
- Economizar espaço em disco ao remover pacotes desnecessários e arquivos em cache.

#### Aviso
**Atenção:** Este código remove todos os pacotes instalados no ambiente Python, podendo causar impactos em sistemas configurados ou em desenvolvimento. Use-o com cautela e preferencialmente em ambientes isolados (como virtualenvs ou containers).

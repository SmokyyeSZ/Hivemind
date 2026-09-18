import sqlite3
from enum import Enum


#2. Cria a tabela para armazenar inteligência tática

class MotherMind:
    
    def __init__(self):
        #1. conecta ao arquivo do banco de dados (obviamente cria o arquivo caso não exista)
        self.conexao = sqlite3.connect("hivemind.db")
        self.cursor = self.conexao.cursor()
        self.memoria = {}
        self.tabela = self.cursor.execute("""    
            CREATE TABLE IF NOT EXISTS estrategias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria TEXT,
                nome TEXT,
                conteudo TEXT,
                data TEXT
            )
        """)
        self.conexao.commit()

    class Categoria(Enum):
        recon = 'recon'
        conhecimento = 'conhecimento'

    def processar_dado(self, dado_recebido):
        # 1. Primeira barreira: A chave "categoria" existe?
        if "categoria" in dado_recebido:
            categoria = dado_recebido["categoria"]
            
            # 2. Segunda barreira: A categoria é válida ("recon" ou "conhecimento")?
            categorias_validas = ["recon", "conhecimento"]
            
            if categoria not in categorias_validas:
                print("[-] Alerta: Dado descartado. Categoria desconhecida (lixo).")
                return False
            
            # Se passou pelos filtros, processa e guarda na memória!
            print(f"[+] Sucesso: Dado da categoria '{categoria}' aceito.")
            return True
        else:
            print("[-] Alerta: Dado descartado. Sem etiqueta de categoria.")
            return False

    def salvar_estrategia(self, nome, conteudo, categoria, data):
            self.cursor.execute("""
                INSERT INTO estrategias (nome, conteudo, categoria, data)
                VALUES (?, ?, ?, ?)
            """, (nome, conteudo, categoria, data))
            
            self.conexao.commit()

    def achar_dado(self, categoria_busca):

            try:
                # Tenta pegar o valor correspondente no Enum
                cat_valida = self.Categoria(categoria_busca).value
                sql = "SELECT nome, conteudo FROM estrategias WHERE categoria = ?"

                for nome, conteudo in self.conexao.execute(sql, (cat_valida,)):
                    print(f"Nome: {nome}, Conteúdo: {conteudo}")
            
            except ValueError:
                print(f"[-] Alerta: A categoria '{categoria_busca}' não é válida.")
                
    def del_memory(self, categoria_busca, info_del):
        try:
            cat_valida = self.Categoria(categoria_busca).value
            
            self.cursor.execute(
                "DELETE FROM estrategias WHERE categoria = ? AND nome = ?", 
                (cat_valida, info_del)
            )
            
            self.conexao.commit()
            print(f"Registros removidos: {self.cursor.rowcount}")

        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao deletar: {e}")

mente = MotherMind()
mente.salvar_estrategia("Nmap", "Porta 80 e 443 abertas", "recon", "18/09/2026")
mente.achar_dado('recon')
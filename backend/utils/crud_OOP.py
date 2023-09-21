import time
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session


class SQLconnect:
    """Classe para gerenciar a conexão com a base de dados"""

    def __init__(self) -> None:
        """Metodo para iniciar conexão com a base inmemory SQLite"""
        self.DB_PATH = "nia_oca_canal_cerc/utils/recimob.db"
        self.max_tentativas = 3
        self.retry_delay = 5

    def criar_db(self):
        """Criar conexão com a base de dados
        com mecanismo de retry e controle de pool
        utilizando base de dados in-memory para teste local de funcionalidades
        :return: Engine de conexão SQLAlchemy
        :rtype: <SQLAlchemy Engine>
        """
        for tentativa in range(1, self.max_tentativas + 1):
            try:
                SQLALCHEMY_DATABASE_URL = f"sqlite:///{self.DB_PATH}"
                db = create_engine(
                    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
                )
                print(
                    f"[{datetime.now()}] [OCA] [ORQUESTRADOR] DB CONECTADO: ",
                    SQLALCHEMY_DATABASE_URL,
                )
                return db
            except AttributeError as e:
                # Handle the exception
                print(
                    "Error de conexão com a base de dados"
                    + f"(tentativa {tentativa}/{self.max_tentativas}): {e}"
                )
                if tentativa < self.max_tentativas:
                    print(f"Tentando novamente em {self.retry_delay} segundos...")
                    time.sleep(self.retry_delay)
                else:
                    print("Número máximo de tentativas atingido. Saindo...")
                    raise SQLAlchemyError("Erro de conexão com Base de Dados" + f"{e}")

    def criar_cnx(self):
        """Metodo para criar engine e conexão
        :return:
            conn: objeto conexão
            db: db engine
        """
        try:
            db = self.criar_db()
        except SQLAlchemyError:
            return None, None
        try:
            conn = db.connect()
            return conn, db
        except AttributeError as e:
            raise SQLAlchemyError("Erro de conexão com Base de Dados" + f"{e}")

    def get_db_session(self, db) -> Session:
        """Metodo para criar session
        :return:
            session: SQLAlchemy.Session
        """
        try:
            session_maker = sessionmaker(autocommit=False, autoflush=True, bind=db)
            session = session_maker()
            return session
        except SQLAlchemyError as e:
            return {"Error:": str(e.orig)}
        finally:
            Session().rollback()

    def atualizando_obj(self, obj, database=False) -> None:
        """Metodo para atualizar entidades da base"""
        conn, db = self.criar_cnx()
        session = self.get_db_session(db)
        if not database:
            print(f"[{datetime.now()}] [OCA] [ORQUESTRADOR] Pulando atualização BD...")
        else:
            try:
                session.add(obj)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise SQLAlchemyError(f"Erro atualizando base de dados {e}")
            finally:
                session.close()
                db.dispose()
                conn.close()


class ObjetoSQL:
    """Classe para gerenciar as operações de CRUD nos objetos SQL"""

    def __init__(self):
        self.obj_connect = SQLconnect()
        self.conn, self.db = self.obj_connect.criar_cnx()
        self.session = self.obj_connect.get_db_session(self.db)

    def processar_query_select(self, tabela):
        """Metodo para aplicar select em uma tabela
        :return: retorno após rodar a query
        :rtype: <string>
        """
        try:
            output = self.session.query(tabela)
        except Exception:
            self.session.close()
            self.db.dispose()
            del self.obj_connect
            raise SQLAlchemyError
        return output

    def processar_query_insert(self, query, values):
        """Metodo para aplicar inserção de informações em uma tabela
        :return: retorno após rodar a query
        :rtype: <string>
        """
        try:
            output = self.conn.execute(query, values)
        except Exception:
            self.conn.close()
            self.db.dispose()
            del self.obj_connect
            raise SQLAlchemyError
        return output

    def encerrar(self):
        """Metodo para encerrrar conexão com base de dados e limpar os objetos em memória"""
        self.session.close()
        self.conn.close()
        self.db.dispose()
        del self.obj_connect

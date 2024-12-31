# services.py

from neo4j import GraphDatabase
from django.conf import settings

class Neo4jService:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI, 
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return result.data()

    def get_graph_data(self):
        query = """
        MATCH (n)-[r]->(m)
        RETURN n, r, m LIMIT 25
        """
        return self.execute_query(query)

# 使用时记得关闭连接
# neo4j_service = Neo4jService()
# graph_data = neo4j_service.get_graph_data()
# neo4j_service.close()

import sqlite3

class AgentState:
    def __init__(self, db_path='agent_states.db'):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS states (
                    agent_id INTEGER PRIMARY KEY,
                    state TEXT
                )
            ''')

    def save_state(self, agent_id, state):
        with self.conn:
            self.conn.execute('INSERT OR REPLACE INTO states (agent_id, state) VALUES (?, ?)', (agent_id, state))

    def load_state(self, agent_id):
        cursor = self.conn.execute('SELECT state FROM states WHERE agent_id=?', (agent_id,))
        result = cursor.fetchone()
        return result[0] if result else None

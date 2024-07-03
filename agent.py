from langchain.utilities import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType

# Create the MySQL connection URI
connection_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"

# Create the SQLDatabase object
db = SQLDatabase.from_uri(connection_uri)


# check that the database has been instantiated correctly

db.get_usable_table_names()

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run(
    "How many seconds are the total talktime in hours   ?"
)
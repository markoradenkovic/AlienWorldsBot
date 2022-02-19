# IMPORTS
from program_logic.program_initializer import ProgramInitializer
from program_logic.bot_runnable import BotRunnable

# START OF MAIN
# Program Initializer, read data, setup new Chrome Windows, and return prepared Bot_Runnable_Instances
program_initializer_instance = ProgramInitializer()
program_initializer_instance.initialize()
bot_runnables_list = program_initializer_instance.get_bot_runnables()

# BotRunnable LOGIC, loop through each runnable and start them up
for bot_runnable in bot_runnables_list:
    bot_runnable.prepare_bot_for_mining()


# Loop infinitely the mining process without stopping until person closes down the botting browsers

# IMPORTS
from program_logic.program_initializer import ProgramInitializer
import time

# START OF MAIN
# Program Initializer, read data, setup new Chrome Windows, and return prepared BotRunnable instances
program_initializer_instance = ProgramInitializer()
program_initializer_instance.initialize()
bot_runnables_list = program_initializer_instance.get_bot_runnables()

# BotRunnable LOGIC, loop through each runnable and start them up
for bot_runnable in bot_runnables_list:
    bot_runnable.prepare_bot_for_mining()

# Loop infinitely the mining process without stopping until person closes down the botting browsers
# while True:
#     for bot_runnable in bot_runnables_list:
#         bot_runnable.start_mining()
#     time.sleep(10)  # Sleep 10 seconds after trying to start_mining, hopefully next loop round some bots are ready again



"""
Welcome to your first Halite-II bot!

This bot's name is Settler. It's purpose is simple (don't expect it to win complex games :) ):
1. Initialize game
2. If a ship is not docked and there are unowned planets
2.a. Try to Dock in the planet if close enough
2.b If not, go towards the planet

Note: Please do not place print statements here as they are used to communicate with the Halite engine. If you need
to log anything use the logging module.
"""
# Let's start by importing the Halite Starter Kit so we can interface with the Halite engine
import hlt
# Then let's import the logging module so we can print out information
import logging
BOT_NAME = "STARTER"
# GAME START
# Here we define the bot's name as Settler and initialize the game, including communication with the Halite engine.
game = hlt.Game(f"{BOT_NAME}")
# Then we print our start message to the logs
logging.info(f"Starting my {BOT_NAME} bot!")

#Sorter for planet dist
def sorter(elem):
    return elem[1]

while True:
    # TURN START
    # Update the map for the new turn and get the latest version
    game_map = game.update_map()
    # Here we define the set of commands to be sent to the Halite engine at the end of the turn
    command_queue = []
    # For every ship that I control

    # logging.info(game_map._players.keys()) # outputs -> dict_keys([0, 1])
    
    #All the planets
    planets = [p for p in game_map.all_planets()]
    #enemy_ships = [e for e in game_map._players]
    
    for ship in game_map.get_me().all_ships():
        # If the ship is docked
        if ship.docking_status != ship.DockingStatus.UNDOCKED:
            # Skip this ship
            continue
        dist = [ship.calculate_distance_between(p) for p in planets]
        planets_dist = [[p,d]for p,d in zip(planets,dist)]
        planets_dist.sort(key=sorter)
        # For each planet in the game (only non-destroyed planets are included)
        for planet in planets_dist: #game_map.all_planets()
            
            # If the planet is owned
            if planet[0].is_owned():
                # Skip this planet
                if planet[0].owner.id != game_map.get_me().id:
                    logging.info(planet[0].owner.id) #returns string 'Player [num]'
                    #logging.info(game_map.get_me().id) 
                    navigate_command = ship.navigate(
                    ship.closest_point_to(planet[0]),
                    game_map,
                    speed=int(hlt.constants.MAX_SPEED/2),
                    ignore_ships=True)
                # If the move is possible, add it to the command_queue (if there are too many obstacles on the way
                # or we are trapped (or we reached our destination!), navigate_command will return null;
                # don't fret though, we can run the command again the next turn)
                    if navigate_command:
                        command_queue.append(navigate_command)
                        break
                continue
            
            # If we can dock, let's (try to) dock. If two ships try to dock at once, neither will be able to.
            if ship.can_dock(planet[0]):
                # We add the command by appending it to the command_queue
                command_queue.append(ship.dock(planet[0]))
           
            else:
                # If we can't dock, we move towards the closest empty point near this planet (by using closest_point_to)
                # with constant speed. Don't worry about pathfinding for now, as the command will do it for you.
                # We run this navigate command each turn until we arrive to get the latest move.
                # Here we move at half our maximum speed to better control the ships
                # In order to execute faster we also choose to ignore ship collision calculations during navigation.
                # This will mean that you have a higher probability of crashing into ships, but it also means you will
                # make move decisions much quicker. As your skill progresses and your moves turn more optimal you may
                # wish to turn that option off.
                navigate_command = ship.navigate(
                    ship.closest_point_to(planet[0]),
                    game_map,
                    speed=int(hlt.constants.MAX_SPEED/2),
                    ignore_ships=True)
                # If the move is possible, add it to the command_queue (if there are too many obstacles on the way
                # or we are trapped (or we reached our destination!), navigate_command will return null;
                # don't fret though, we can run the command again the next turn)
                if navigate_command:
                    command_queue.append(navigate_command)
            break

    # Send our set of commands to the Halite engine for this turn
    game.send_command_queue(command_queue)
    # TURN END
# GAME END
"""
            if not planet[0].is_owned():
                navigate_command = ship.navigate(
                    ship.closest_point_to(planet[0]),
                    game_map,
                    speed=int(hlt.constants.MAX_SPEED/2),
                    ignore_ships=True)
"""
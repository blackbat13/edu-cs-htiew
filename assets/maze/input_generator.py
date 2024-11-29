from random import randint

maze1 = """###########
#o        #
# #########
#     #   #
# ##### ###
#         #
# # # #####
# # #     #
# ### # # #
#   # # #x#
###########"""

maze2 = """###################################
#o                        #       #
# # ##### # ### ####### ### #######
# #     # #   #     # # #   #   # #
# ########### ### ### ### ### ### #
#           #   #         # #   # #
# ### ### ######### ### ### # ### #
#   #   #     # # #   #           #
# # ##### ### # # ####### #########
# #     #   # #         #         #
# # ##### ### # ### ######### # # #
# #     # #       #         # # # #
# # # ### ####### ##### ### # # ###
# # #   #       #     #   # # #   #
# # # # ########### ### ### # # ###
# # # #         # #   #   # # #   #
# ### # # # # # # ##### # ##### # #
# #   # # # # #       # #   #   # #
# # # # # # # ### # ### ##### # # #
# # # # # # #   # # # #   # # # # #
# # # # # ### ### ### ##### ##### #
# # # # #   #   #             #   #
# # ### # # ######### # # ##### # #
# #   # # #         # # #     # # #
# # ### # # # # # ######### ### # #
# # #   # # # # #         #   # # #
# # # # # # ### # # # # ### # ### #
# # # # # #   # # # # #   # #   # #
# # # # ### # ### ### # ##### # # #
# # # #   # # #     # #     # # # #
# # # # ### ### # ##### # ### # ###
# # # #   #   # #     # #   # #   #
# # ### ##### ### ### ####### #####
# # #       #   #   #       #    x#
###################################"""

def prepare_maze(maze):
    result = ""
    for el in maze:
        if el == "#":
            result += "0"
        elif el == "o":
            result += "1"
        elif el == "x":
            result += "9"
        elif el == " ":
            result += str(randint(2, 8))
        else:
            result += el

    return result

with open("maze.txt", "w") as file:
    maze_lines = maze2.split("\n")
    width = len(maze_lines[0])
    height = len(maze_lines)
    print(width, height, file=file)
    print(prepare_maze(maze2), file=file)

with open("maze_test.txt", "w") as file:
    maze_lines = maze1.split("\n")
    width = len(maze_lines[0])
    height = len(maze_lines)
    print(width, height, file=file)
    print(prepare_maze(maze1), file=file)
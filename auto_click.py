import pyautogui
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--number_click", required=True, help="number click when auto, no limit is 0", type=int)
ap.add_argument("-p", "--position", required=True, help="position will action click", type=str)
ap.add_argument("-s", "--second_delay", required=True, help="position y when click", type=float)
args = vars(ap.parse_args())

number_click = args["number_click"]
position = args["position"]
print(position)
dict_position = dict(position)
# s = args["second_delay"]
# print(l_position)
# for p in l_position:
#     print(p)
#     break

# if number_click == 0:
#     try:
#         while True:
#             pyautogui.moveTo(position_x, position_y, s, pyautogui.rightClick(x=position_x, y=position_y))
#     except KeyboardInterrupt:
#         print('\n')
# else:
#     try:
#         while number_click != 0:
#             pyautogui.moveTo(position_x, position_y, s, pyautogui.rightClick(x=position_x, y=position_y))
#             number_click = number_click - 1
#     except KeyboardInterrupt:
#         print('\n')

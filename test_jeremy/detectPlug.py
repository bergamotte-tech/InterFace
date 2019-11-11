# import os
# import time

# def detectPlug():
#     oldList = []
#     while True:
#         newList = os.popen("lsusb | awk '{print $6}'").read().split("\n")[:-1]
        
#         if len(oldList) == 0:
#             pass
#         elif len(newList)>len(oldList):
#             os.popen("machin.mp3")
#         elif len(newList)<len(oldList):
#             print("REMOVED")
        
#         oldList = newList

# detectPlug()

arr = ["coucou"]

print (arr)
print(arr[0])
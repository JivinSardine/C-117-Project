import os
import cv2

# set path for the Images folder
path = "/Users/michaes/Desktop/CodingSpace/WhiteHatJR Python/C-117/Project/images"

# create a list variable named Images
Images = []

# use for loop to check each file in the folder
for file in os.listdir(path):
    # separate the name and extension from a file name
    name, ext = os.path.splitext(file)
    # check if the extension of the file matches the image extension
    if ext == ".jpg" or ext == ".png":
        # create a variable file_name
        file_name = f"{path}/{file}"
        # add each file in the images list using .append()
        Images.append(file_name)

# create a variable count to store len(images)
count = len(Images)

# read the first image from the images list
frame = cv2.imread(Images[0])

# capture width, height & Channels using frame.shape
width, height, channels = frame.shape

# create a tuple variable size using width, height
size = (width, height)

# print size to check the result
print(size)

# create a variable out and assign with cv2.VideoWriter()
video_name = "Project.mp4"
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
out = cv2.VideoWriter(video_name, fourcc, fps, size)

# create a for loop to add images to a video writer
for i in range(count-1):
    # read each image
    img = cv2.imread(Images[i])
    # add the image in the video using out.write()
    out.write(img)

# print a message to know the video is complete
out.release()
print("Done")

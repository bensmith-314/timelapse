import os
from moviepy.editor import ImageSequenceClip

image_folder = './images'

fps = 24

output_file = 'newTimelapse.mov'

# Get the list of images and sort them by extracting the number from each filename
images = sorted(
    [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith('.png')],
    key=lambda x: int(x.split('frame')[-1].split('.')[0])  # Extract the number after 'frame' and before the extension
)

# Ensure the list is populated before creating the video
if not images:
    print("No images found in the directory.")
    exit(1)

clip = ImageSequenceClip(images, fps=fps)
clip.write_videofile(output_file, codec="libx264")
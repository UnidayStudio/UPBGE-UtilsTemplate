# Utils Component Templates
###### For UPBGE 0.2.3
This templates was created to help Blender Game Engine (UPBGE) users to create games or any kind of interactive things. Easy to use, easy to attach to your project.

To use, just download the files, open it on UPBGE (version 0.2.3 recommended) and you're done!
You can use this template in your projects, even for commercial projects. Just credit me for this.:)
It's very easy to use in your projects: Just load this script into your .blend file (or paste them in the same folder that your .blend is), select the object that you want, and attach the script into the object's components.

## Sound Speaker Component
This component will serve as an **sound Speaker** for your game. With this, you can easly control 3D sound, volume.
Unfortunatelly, **the sounds needs to be mono to make the 3D sound works**. You can convert to mono using windows CMD like this:
'> ffmpeg -i Sound.wav -ac 1 SoundMono.wav'
It's very simple to configure:
- **Sound File**: The file name, example: "Assets/DoorMono.wav".
- **Loop Sound**: If you want the sound to loop or just play once.
- **Volume**: The Volume.
- **Pitch**: The Pitch.
- **3D Sound**: If you want the sound to be 3D.
- **Min Distance**: If 3D Sound is enabled, the sound will have the max volume if the listener is this near.
- **Max Distance**: If 3D Sound is enabled, the sound will volume down until zero when the listener reach this distance.
- **Delete Object After End**: If enabled, the object will be deleted at the end of the sound (if Loop Sound equals to false).

## Minimap Component
This component will spawn a minimap based on the camera (which owns the component) view. Add this component to a camera and position it on top of your character.
To configure, take a look at the values:
- **Camera Type**: You can choose between Perspertive or Ortographic camera.
- **Camera Height**: Define the height that you want your minimap camera to be. If you don't want the component to modify this, just set to zero (0).
- **Minimap Position**: The position of the center of the minimap on the screen (values goes from 0 to 1).
- **Minimap Size**: The size of the minimap (values goes from 0 to 1).
- **Follow Object**: You can define an object for the minimap to follow (like the player). Leave it empty if you don't want.
- **Rotate on Z axis**: If you defined a Follow Object, you can also makes the minimap rotates on the Z axis according to the follow object's rotation.

Created by **Guilherme Teres Nunes**

Access my youtube channel:
## [Uniday Studio on Youtube](youtube.com/UnidayStudio)
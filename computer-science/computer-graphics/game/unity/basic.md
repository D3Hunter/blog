### asset
- Standard Assets: 2D, Cameras, Characters, CrossPlatformInput, Effects, Environment, ParticleSystems, Prototyping, Utility, Vehicles.
    - Unity transfers Standard Assets in and out of Projects using Asset packages.
- images
- FBX and model files
- meshes and animations
- audio files

### projection mode
- Perspective
- Orthographic (sometimes called ‘isometric’).

Click on the padlock on the top right of the Scene Gizmo to enable or disable rotation of the Scene.

Flythrough mode
Use Flythrough mode to navigate the Scene View by flying around in first-person, similar to how you would navigate in many games.
Click and hold the right mouse button.
Move the view around using the mouse, the WASD keys to move left/right/forward/backward, and the Q and E keys to move up and down.
Hold down Shift to move faster.

Centering the view on a GameObject
- Edit > Frame Selected
- Edit > Lock View to Selected

Unit snapping: 可快速按snap单位进行移动或旋转，可以以点、线为目标

`Scenes` contain the environments and menus of your game. Think of each unique Scene file as a unique level. It is possible to have multiple Scenes open for editing at one time.
To save changes to the scene, select Save Scene from the file menu, or hit `Ctrl/Cmd + S`. This saves current changes to the scene and Does a `“Save Project”` (below).

Every object in your game is a `GameObject`
GameObjects are the fundamental objects in Unity that represent characters, props and scenery. They do not accomplish much in themselves but they act as containers for Components, which implement the real functionality.
Fortunately, Unity has a `Prefab` asset type that allows you to store a GameObject object complete with components and properties.
Objects created as `prefab` instances will be shown in the hierarchy view in `blue` text. (Normal objects are shown in `black` text.). To make it clear when a property has been overridden, it is shown in the inspector with its name label in `boldface`.

There is also an additional option in Translate mode to lock movement to a particular plane. 原点附件的三个平面

Note that the Transform values in the Inspector for any child GameObject are displayed relative to the Parent’s Transform values. These values are referred to as local coordinates.

Non-uniform scaling is when the Scale in a Transform has different values for x, y, and z; Non-uniform scaling can be useful in a few specific cases but it introduces a few oddities that don’t occur with uniform scaling:

By default, the physics engine assumes that one unit in world space corresponds to one metre.
A Constraint component links the position, rotation, or scale of a GameObject to another GameObject. A constrained GameObject moves, rotates, or scales like the GameObject it is linked to.
A locked Constraint takes control of the relevant parts of the Transform of the GameObject. You cannot manually move, rotate, or scale a GameObject with a locked Constraint.
A GameObject can only contain one Constraint component of the same kind. For example, you cannot add more than one Position Constraint.
- An Aim Constraint `rotates` a GameObject to face its source GameObjects.
- A Parent Constraint `moves` and `rotates` a GameObject as if it is the child of another GameObject in the Hierarchy window. However, it offers certain advantages that are not possible when you make one GameObject the parent of another:
- A Position Constraint component `moves` a GameObject to follow its source GameObjects.
- A Rotation Constraint component `rotates` a GameObject to match the rotation of its source GameObjects.
- A Scale Constraint component `resizes` a GameObject to match the scale of its source GameObjects.

Rotations in 3D applications are usually represented in one of two ways, `Quaternions` or `Euler angles`. Each has its own uses and drawbacks. Unity uses Quaternions internally, but shows values of the equivalent Euler angles in the inspector to make it easy for you to edit. Euler angles suffer from `Gimbal Lock`.
When dealing with handling rotations in your scripts, you should use the Quaternion class and its functions to create and modify rotational values.

`File > Build Settings…` is the menu item to access the Build Settings window. The first time you view this window in a project, it will appear blank. If you build your game while this list is blank, only the currently open scene will be included in the build. If you want to quickly build a test player with only one scene file, just build a player with a blank scene list.

Preset 一些预设的参数值，可保存并付给别的GameObject

### random
In probability and statistics, the `quantile function`, associated with a probability distribution of a random variable, specifies the value of the random variable such that the probability of the variable being less than or equal to that value equals the given probability. It is also called the `percent-point function` or `inverse cumulative distribution function`. 可以用来计算`Continuous weighted random distribution`. 在unity里使用`AnimationCurve`


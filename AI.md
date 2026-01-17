Sure. Short. Clear. Feasible in **2–3 hours**.

---

## Game summary

You are in a **circular lake**.
You can move freely, but **water slows you down**.
A **goblin runs on land** around the lake.
It is **4× faster than you on land**.
It **cannot enter water**.

You survive by:

* Using water to slow yourself carefully.
* Controlling angles, not distance.
* Avoiding mistakes.

The goblin tries to **cut you off**, not follow directly.

---

## Core mechanics (minimal)

**Player**

* Position (Vector2)
* Speed
* Water slow factor
* Keyboard movement

**Goblin**

* Moves only on lake edge
* Speed = player_speed × 4
* Chases player angle
* Simple AI (no pathfinding)

**World**

* Circular map
* Radius
* Water everywhere except edge
* Distance-to-center decides speed

---

## Win / lose

* **Lose**: goblin reaches your angle and touches you.
* **Win**: survive for N seconds.

---

## OOP structure (simple)

```
game/
 ├─ core/
 │   ├─ game.py        # main loop
 │   └─ constants.py
 ├─ states/
 │   └─ play.py        # only one state
 ├─ world/
 │   └─ world.py       # lake + physics
 ├─ entities/
 │   ├─ entity.py
 │   ├─ player.py
 │   └─ goblin.py
 ├─ ai/
 │   └─ pursuit.py
 └─ main.py
```

Classes:

* `Game` → loop, update, draw
* `World` → radius, water check
* `Entity` → position, speed
* `Player(Entity)`
* `Goblin(Entity)`
* `GoblinAI`

No components. No states. Keep it small.

---

## Libraries to use (only these)

Required:

* `pygame`
* `pygame.math.Vector2`
* `math`
* `time`

Optional (skip if short on time):

* `dataclasses`

No tkinter. No pygame_gui.

---

## What to cut (important)

❌ Menus
❌ Settings
❌ Sound
❌ Stamina
❌ Fog
❌ Multiple states

---

## Time plan (realistic)

**30 min**

* Window, loop, circle map

**45 min**

* Player movement + water slow

**30 min**

* Goblin movement on edge

**30 min**

* Angle-based AI

**15 min**

* Collision + timer

Done.

---

## Key idea

This is a **geometry game**, not a graphics game.
If angles feel fair, the game works.

If you want next:

* tiny AI formula
* collision math
* minimal code skeleton

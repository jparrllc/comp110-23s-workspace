"""Checks Light, if green, says go."""

light: str = input("What color is the Light? ").lower()

if (light == "green"):
    print("GO!")
    print("Drive safe! Love, mom.")
else:
    if(light != "red"):
        if(light == "yellow"):
            print("slow down!")
        else:
            print("Go report this to the authorities.")
    else:
         print("Stop!")
print("Dont look at your phone!")
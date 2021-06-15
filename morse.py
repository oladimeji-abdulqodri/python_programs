text=input("enter a sentence or word")
for morse in text:
    if morse in(" "):
        print("space=  _")
    elif morse in(","):
        print(",=  --..--")
    elif morse in("."):
        print(".=  .-.-.-")
    elif morse in("?"):
        print("?=  ..--..")
    elif morse in("  0"):
        print("0=  -----")
    elif morse in("  1"):
        print("1=  .----")
    elif morse in("  2"):
        print("2=  ..---")
    elif morse in("  3"):
        print("3=  ...--")
    elif morse in("  4"):
        print("4=  ....-")
    elif morse in("  5"):
        print("5=  .....")
    elif morse in("  6"):
        print("6=  -....")
    elif morse in("  7"):
        print("7=  --...")
    elif morse in("  8"):
        print("8=  ---..")
    elif morse in("9"):
        print("9=  ----.")
    elif morse in("  A","a"):
        print("a =  .-")
    elif morse in ("  B","b"):
        print("b=  -...")
    elif morse in("  C","c"):
        print("c=  -.-.")
    elif morse in("  D","d"):
        print("d=  -..")
    elif morse in(" E","e"):
        print("e=  .")
    elif morse in("F","f"):
        print("f=  ..-.")
    elif morse in("  G","g"):
        print("g=  --..")
    elif morse in("  H","h"):
        print("h=  ....")
    elif morse in("  I","i"):
        print("i=  ..")
    elif morse in("  J","j"):
        print("j=  .---")
    elif morse in("  K","k"):
        print("k=  -.-")
    elif morse in("  L","l"):
        print("l=  .-..")
    elif morse in("  M","m"):
        print("m=  --")
    elif morse in("  N","n"):
        print("n=  -.")
    elif morse in("  O","o"):
        print("o=  ---")
    elif morse in("  P","p"):
        print("p=  .--.")
    elif morse in("  Q","q"):
        print("q=  .--.")
    elif morse in("  R","r"):
        print("r=  .-.")
    elif morse in("  S","s"):
        print("s=  ...")
    elif morse in("  T","t"):
        print("t=  -")
    elif morse in("  U","u"):
        print("u=  ..-")
    elif morse in("  V","v"):
        print("v=  ...-")
    elif morse in(" W",'w'):
        print("w=  .--")
    elif morse in("  X","x"):
        print("x=  -..-")
    elif morse in("Y","y"):
        print("y=  -.-")
    elif morse in("Z","z"):
        print("z=  --..")


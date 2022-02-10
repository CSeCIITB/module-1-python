def tux_say(to_print):
    print(f"""
     {to_print} 
        \\
        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/
    """)

while(True):
    inp = input("Enter expression : ")
    tux_say(inp + " = " + str(eval(inp)))

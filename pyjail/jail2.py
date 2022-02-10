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
    for keyword in ['eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write','process','socket','help']:
        if keyword in inp.lower():
            tux_say("Stop hacking !!")
            exit()
    tux_say(inp + " = " + str(eval(inp)))

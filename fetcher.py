import pyperclip; print("OpenRouter Token fetcher version 0.1 / write '1' to get first avabible token from 'tokens' file.")
def formatFl(unFormattedContent):
    formatted=[]; newFormatted=[]
    for i in unFormattedContent: formatted.append(i.strip("\n").split(" ")); return formatted
def read(fl): return formatFl(fl.readlines())
def token_Usage_loop(fl_contents,id,file):
    print(f"{fl_contents[id][0]} <- your token is already in your clipboard! Happy usage (👉ﾟヮﾟ)👉"); pyperclip.copy(fl_contents[id][0])
    while True:
        u_input = input("type (exit) if token Ended. ")
        if u_input.lower()=="exit": break
    save(id,"used",fl_contents,file)
def formatCMD(unFormattedcmd): return unFormattedcmd.split(" ")
def CMDProcess(CMD, fl_contents):
    if CMD[0] == "1":
        count=0
        try: 
            while fl_contents[count][1] != "available": count+=1; return [0,count]
        except: print("No un-used token available.")
def save(id_,status_,fl_content_,tokens_file):
    new_content = fl_content_; new_content[id_][1] = status_; newstring=""
    for i in new_content: newstring+=i[0]+" "+i[1]+"\n"
    with open(tokens_file,"w") as f: f.write(newstring); print(f"{id_} -> marked as 'used'")
def cmdProcessing(fl_contents):
    CMD = input("<. write command .> ... "); CMD = formatCMD(CMD); exit_code = CMDProcess(CMD,fl_contents)
    try:
        if exit_code[0] == 0: token_Usage_loop(fl_contents,exit_code[1],"tokens")
    except Exception as e: print(f"Problem occured while handling your command. {e}")
def _start(tokens_file):
    while True: 
        with open(tokens_file,"r") as f: f = read(f); cmdProcessing(f)
_start("tokens")

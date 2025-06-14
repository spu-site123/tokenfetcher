import pyperclip; print("OpenRouter Token fetcher version 0.1 / write '1' to get first avabible token from 'tokens' file.")
def formatFl(unFormattedContent):
    formatted=[]; newFormatted=[]
    for i in unFormattedContent:
        clearing=""
        for d in i:
            if d!="\n": clearing+=d
        formatted.append(clearing.split(" "));    
    return formatted
def read(fl_content):
    fl_content = fl_content.readlines(); fl_content = formatFl(fl_content)
    return fl_content
def token_Usage_loop(fl_contents,id,file):
    print(f"{fl_contents[id][0]} <- your token is already in your clipboard! Happy usage (👉ﾟヮﾟ)👉"); pyperclip.copy(fl_contents[id][0])
    while True:
        exit = input("type (exit) if token Ended. ")
        if exit=="exit": break
    save(id,"used",fl_contents,file)
def formatCMD(unFormattedcmd): return unFormattedcmd.split(" ")
def CMDProccess(CMD, fl_contents):
    if CMD[0] == "1":
        count=0
        while fl_contents[count][1] != "available": count+=1
        return [0,count]
def save(id_,status_,fl_content_,tokens_file):
    new_content = fl_content_; new_content[id_][1] = status_; newstring=""
    for i in new_content: newstring+=i[0]+" "+i[1]+"\n"
    print(newstring)
    fl = open(tokens_file,"w"); fl.write(newstring); fl_ = open(tokens_file,"r")
    return fl_
def cmdProcessing(fl_contents):
    CMD = input("<. write command .> ... "); CMD = formatCMD(CMD); exit_code = CMDProccess(CMD,fl_contents)
    if exit_code[0] == 0: token_Usage_loop(fl_contents,exit_code[1],"tokens")
def _start(tokens_file):
    while True:
        fl = open(tokens_file,"r"); fl = read(fl); cmdProcessing(fl)
_start("tokens")

import re
file1 = open(r'C:\Users\mail2\OneDrive\Desktop\html\mysites\gfg coppy\code.txt', 'r')
lines=file1.readlines()
m=[]
def c_cpp_to_html(i):
    a=["!","-","~~","~`","`~","[(]","[)]"]
    b=['<span class="colr2">!</span>','<span class="colr2">-</span>','<span class="colr2">=</span>','<span class="colr2">></span>',
    '<span class="colr2"><</span>','(',')']


    for ii,j in zip(a,b):
        try:i=re.sub(ii,j,i)
        except:pass
    i='<span>'+i+'</span>'



    a=[r"\bfor\b",r"\bprintf\b",r"\bscanf\b",r"\belse if\b",r"\belse\b",r"\bif\b",r"\bwhile\b",r"\busing\b",r"\bnamespace\b",r"\binclude\b",r"\breturn\b",
    r"\bcout\b",r"\bcin\b",r"\bvoid\b",r"\bstruct\b",r"\bunion\b",r"\bint\b",r"\bchar\b",r"\bstring\b",r"\bfloat\b",r"\bNULL\b",r"\blong\b",r"\bbyte\b",
    r"\bshort\b",r"\bdouble\b",r"\bbool\b","[!]","[,]","[;]","[#]","[*]","[+]","[-]","[&]","[|]","[(]","[)]","[[]","[]]","[{]","[}]",
    "< /span >","<  <",">  >","< span >","< span ","</span  >","<span  >"," ( "," ) ",r"%d",r"%f",r"%u",r"%s",r"%c",r"\\n",r"\\b","</span>  <span"
    ]



    b=['<span class="colr2">for</span>',"<span class='colr2'>printf</span>","<span class='colr2'>scanf</span>",'<span class="colr2">else if</span>',
    '<span class="colr2">else</span>','<span class="colr2">if</span>','<span class="colr2">while</span>','<span class="colr2">using</span>',
    '<span class="colr3">namespace</span>','<span class="colr3">include</span>','<span class="colr2">return</span>',
    '<span class="colr3">cout</span>','<span class="colr3">cin</span>','<span class="colr3">void</span>','<span class="colr3">struct</span>',
    '<span class="colr3">union</span>','<span class="colr3">int</span>','<span class="colr3">char</span>','<span class="colr2">string</span>',
    '<span class="colr3">float</span>','<span class="colr3">NULL</span>','<span class="colr3">long</span>','<span class="colr3">byte</span>','<span class="colr3">short</span>',
    '<span class="colr2">double</span>','<span class="colr3">bool</span>','<span class="colr2">!</span>','<span class="colr2">,</span>',
    '<span class="colr2">;</span>','<span class="colr3">#</span>','<span class="colr2">*</span>','<span class="colr2">+</span>',
    '<span class="colr2">-</span>','<span class="colr2">&</span>','<span class="colr2">|</span>','<span class="colr2">(</span>',
    '<span class="colr2">)</span>','<span class="colr5">[</span>','<span class="colr5">]</span>','<span class="colr5">{</span>',
    '<span class="colr5">}</span>','</span>','<span class="colr5"><<</span>','<span class="colr5">>></span>','<span>','<span ',
    '</span>','<span>','(',')',r'<span class="colr7">%d</span>',r'<span class="colr7">%f</span>',r'<span class="colr7">%u</span>',
    r'<span class="colr7">%s</span>',r'<span class="colr7">%c</span>',r'<span class="colr7">\\n</span>',r'<span class="colr7">\\b</span>',"</span><span"]

    for ii,j in zip(a,b):
        try:i=re.sub(ii,j,i)
        except:pass
    return i

def c_cpp_print_to_html(i):
    a=[r"%d",r"%f",r"%u",r"%s",r"%c",r"``n",r"\\b","~~","~`","`~","<  <",">  >","< /span >","<  <",">  >","< span >","< span ","</span  >","<span  >","</span>  <span"]
    b=[r'<span class="colr7">%d</span>',r'<span class="colr7">%f</span>',r'<span class="colr7">%u</span>',
    r'<span class="colr7">%s</span>',r'<span class="colr7">%c</span>',r'<span class="colr7">``n</span>',r'<span class="colr7">\\b</span>',
    '=','>','<',"<<",">>",'<span>','<span ',
    '</span>','<span>',"</span><span"]
    
    for ii,j in zip(a,b):
        try:i=re.sub(ii,j,i)
        except:pass
    
    return i

for j in range(len(lines)):
    i=lines[j]
    if "//" not in i:

        try:
            if(re.findall("->",i) ):
                pass
            else:
                i=re.sub("[>]",' > ',i)

        except:pass
        try:i=re.sub("[<]",' < ',i)
        except:pass
        try:i=re.sub("=",'~~',i)
        except:pass
        try:i=re.sub(">",'~`',i)
        except:pass
        try:i=re.sub("<",'`~',i)
        except:pass
        
        s=re.findall("\"[^<,^),^;]*\"",i)


        if len(s)==0:
            i=c_cpp_to_html(i)
        
        else:
            ss=[]
            for t in s:
                t=re.sub(r"\\n",'``n',t)
                i=re.sub(r"\\n",'``n',i)
                ss.append('<span class="colr6imp">'+t+"</span>")
                i=re.sub(t,"this text will change",i)
                print(t)

            i=c_cpp_to_html(i)
            
            for r in ss:
                r=c_cpp_print_to_html(r)
                i=re.sub("this text will change",r,i)
                i=re.sub('``n',r"\\n",i)
    else:
        i='<span class="colr4">'+lines[j]+'</span>'
    m.append(i)

file1.close()

file1 = open(r'C:\Users\mail2\OneDrive\Desktop\html\mysites\gfg coppy\html.txt', 'w')
file1.writelines(m)
file1.close()
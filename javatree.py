global counter
counter=0
def parser(a):
    global counter
    list1=[""]
    list2=[]
    list3=[]
    list4=[]
    l=0
    c="(),+-=/\\%&\""
    count=0;
    for b in a:
         if b in c:
             list1=list1+[""+b]
             list1=list1+[""]
             
         else:
             l=len(list1)-1
             list1[l]=list1[l]+""+b
    for b in list1:
        if len(b.strip())>0:
            list2=list2+[b.strip()]
    l=len(list2)
    t=False
    starts=False
    sstarts=False
    for b in range(len(list2)):
        lis=len(list2[b])
        if lis>0:
            ll=list2[b]
            s=""
            if len(ll)>0:
                s=ll[0]
            
            if b+1<l:
                if list2[b+1]=="(":
                    if (s>="A" or s>="a") and (s<="Z" or s<="z"):
                        
                        t=True
            if starts:
                if s=='\"':
                    sstarts=True
            if not(t):
                 if not(starts): 
                    if(s>="A" or s>="a") and (s<="Z" or s<="z"): 
                        pass
                    elif(s>="0" and s<="9"):
                        if "." in list2[b]:
                           pass
                        else:
                            pass
                    elif s=="\"":
                        
                        starts=not(starts)
                    elif s in c:
                        list3=list3+[b]
                        pass
                    else:
                        pass
            if s=="\"" and sstarts:
                starts=not(starts)
            t=False
    #counter=0
    counter2=0
    counter3=0
    counter4=0
    counter5=0
    vars0=0
    #counter=0
    ttrue=True
    for b in range(len(list3)):
        if list2[list3[b]]==")":
            counter2=b
            counter3=b
            counter4=0
            if 0==0:
                counter03=list3[b]
                counter4=0
                while(counter03>-1):
                     if (list2[counter03]=="(" or counter03==0) :
                         if 0==0:
                             tt=""
                             list4=list4+[tt+""]
                             xy=len(list4)-1
                             for counter5 in range(counter03-1,list3[b]+1):
                                 list4[xy]=list4[xy]+list2[counter5]
                                 if counter5==counter03-1:
                                     list2[counter5]=tt
                                 else:
                                     list2[counter5]=""
                                 counter03=-1
                                 
                             
                         
                         counter4=counter4+1
                     counter03=counter03-1
            counter=counter+1
    return list4

class TreeNode:
    def __init__(self, content=""):
        self.content = content.strip()
        self.children = []

    def __repr__(self, level=0):
        indent = " " * (level * 4)
        result=""
        bbb=self.content.split(";")
        for bb in bbb:
            aaa=parser(bb)
            if len(aaa)<1:
                result =result+indent+bb+"\n"
            else:
                for n in aaa:
                    result =result+indent+n+"\n"
        
        for child in self.children:
            result += child.__repr__(level + 1)
            
        return result


def parse_javatree_tree(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    stack = []
    root = TreeNode("root")
    current_node = root
    buffer = ""

    for char in data:
        if char == "{":
            # Cria um novo nó com o conteúdo atual do buffer
            if buffer.strip():
                new_node = TreeNode(buffer)
                current_node.children.append(new_node)
                stack.append(current_node)
                current_node = new_node
            buffer = ""
        elif char == "}":
            # Finaliza o conteúdo do nó atual
            if buffer.strip():
                current_node.children.append(TreeNode(buffer))
            buffer = ""
            if stack:
                current_node = stack.pop()
        elif char == ";":
            # Finaliza o buffer para criar nós no mesmo nível
            if buffer.strip():
                current_node.children.append(TreeNode(buffer))
            buffer = ""
        else:
            buffer += char

    return root


def main():
    file_name = input("Enter the name of the .java file to load: ")

    try:
        tree = parse_javatree_tree(file_name)
        print("\nParsed C Tree:")
        print(tree)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print("\033c\033[40;37m\n")
    main()


# 	ORG 	0x3C9
# ARG1:	WORD	0x0000
# ARG2:	WORD	0xFFFF
# ARG3:	WORD	0x1055
# ARG4:	WORD	0x2002
# CHECK:	WORD	0x0000
# RES1:	WORD	0x0000
# RES2:	WORD	0xFE01
# RES3:	WORD	0x00AA
# START:	CLA	
# 	CALL	TEST1
# 	HLT	
# 	CALL	TEST2
# 	HLT	
# 	CALL	TEST3
# 	HLT		
# 	LD	CHECK
#                 HLT
# TEST1:	CLA
#                 LD              ARG1
#                 PUSH            
#                 PUSH            
#                 WORD            0x0F20
#                 POP             
#                 CMP             RES1
#                 BEQ             OK
#                 BR              NOTOK
def init_block(n):
    string = ""
    for i in range(n):
        string+="ARG"+str(i)+":"+ " WORD " + "0x"+hex(i)[2:]+"\n"
        # string+="ARG"+str(i+1)+"0x"+hex(i+1)[2:]+"\n"
    # for i in range():
    # create loop with step 2
    for i in range(0, n-1):
        string+="RES"+str(i)+":"+ " WORD " + "0x"+hex(i*(i+1))[2:]+"\n"
    string+="CHECK:	WORD 0x0000\n"
    return string

def body_block(n):
    string = "START: CLA\n"
    for i in range(n-1):
        string+="\tCALL\tTEST"+str(i)+"\n"
    string+="\tLD\tCHECK\n"
    string+="\tHLT\n"
    return string

def test_block(n):
    string = ""
    for i in range(n-1):
        string+="TEST"+str(i)+":\tCLA\n"
        string+="\tLD\tARG"+str(i)+"\n"
        string+="\tPUSH\n"
        string+="\tLD\tARG"+str(i+1)+"\n"
        string+="\tPUSH\n"
        string+="\tWORD\t0x0F20\n"
        string+="\tPOP\n"
        string+="\tCMP\tRES"+str(i)+"\n"
        string+="\tBEQ\tOK\n"
        string+="\tBR\tNOTOK\n"
    return string

def test_former(n):
    print("ORG 0x3C9")
    print(init_block(n))
    print(body_block(n))
    print(test_block(n))
    ok_block = "OK:\tPOP\n\tPOP\n\tLD\t#0x1\n\tADD\tCHECK\n\tST\tCHECK\n\tCLA\n\tRET\n"
    notok_block = "NOTOK:\tPOP\n\tPOP\n\tLD\t#0x0\n\tADD\tCHECK\n\tST\tCHECK\n\tCLA\n\tRET\n"
    print(ok_block)
    print(notok_block)

test_former(10)
# maddress BB maddress BB mwrite 81F0014002 maddress F0 maddress F0 mwrite 0080009008 mwrite 0100000000 mwrite 0020000000 mwrite 0010A01001 mwrite 0080009408 mwrite 0100001000 mwrite 0001001001 mwrite 0010A80010 mwrite 80FA011040 mwrite 0020009021 mwrite 0001020001 mwrite 80F7041040 mwrite 0001E09020 mwrite 0088009208 mwrite 0200000000 mwrite 80C4101040 

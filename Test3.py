print('''
            ------------------------
            Tarun Mobile Shop
            ------------------------
            1) Readmi : 64 GB/128 GB/256 GB
            2) Mi : 64 GB/128 GB/256 GB
            3) Samsung : 64 GB/128 GB/256 GB
            4) iphone : 64 GB/128 GB/256 GB
            ------------------------
''')
ch=int(input('Choose Mobile Phone :'))
if  ch==1: 
          print('''
                    ----------------------
                      Readmi Phone
                    ----------------------
                    1) 64 GB: 12000
                    2) 128 GB: 23000
                    3) 256 GB: 32999
            ''') 
if ch==1:
         gb = 12000
         m_name = 'Readmi'
         cust_name=input('Customer Name :')
         pi =int(input('How Many Piece You Want :'))
         tb = gb * pi 
         print(f'''
                    ----------------------------
                           Bill Details
                    ----------------------------
                     Mobile Phone : {m_name}
                     Customer Name : {cust_name}
                     Piece : {pi}
                    -----------------------------
                        Total Bill : {tb}
                    -----------------------------
                       Thanks For Visiting Us
                    ----------------------------- 
           ''')
if ch==2:
         gb = 23000
         m_name = 'Readmi'
         cust_name = input('Customer name :')
         pi=int(input('How Mant Piece You Want :'))
         tb = gb * pi
         print(f'''
                     -----------------------------
                              Bill Detail
                     -----------------------------
                       Mobile Phone: {m_name}
                       Customer Name : {cust_name}
                       Piece : {pi}
                     -----------------------------
                          Total Bill : {tb}
                     -----------------------------
                        Thanks For Visiting Us
                     ----------------------------- 
          ''')
if ch==3:
        gb = 32999
        m_name = 'Readmi'
        cust_name = input('Customer Name :')
        pi = int(input('How Many Piece You Want :'))
        tb = gb * pi
        print(f'''
                    -----------------------------
                           Bill Detail
                    -----------------------------
                     Mobile Phone : {m_name}
                     Customer Name : {cust_name}
                     Piece : {pi}
                    -----------------------------
                        Total Bill : {tb}
                    -----------------------------
                       Thanks For Visiting Us
                    -----------------------------
          ''')
        print('''
                  ------------------------ 
                   MI Phone
                  ------------------------ 
                  1) 64 GB - 11000
                  2) 128 GB - 20000
                  3) 256 GB - 36000
          ''')
elif ch==2:
        int=int(input('Choice MI Moblie Phone :'))
        if ch==1:
         gb = 11000
         M_name = 'MI'
         cust_name = input('Customer Name :')
         pi=int(input('How many piece you want :'))
         tb = gb * pi
        print(f'''
                 ----------------------------
                  Detials
                 ----------------------------
                  Mobile Name : {M_name}
                  Customer Name : {cust_name}
                  Piece : {pi}
                 -----------------------------
                 Total Bill  : {tb}
                 -----------------------------
          ''')







    

     
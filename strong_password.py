def strong_password(password):
    c_l=0
    s_l=0
    n_d=0
    s_sc=0
    i=0
    while i<len(password):
        if password[i].isupper():
            c_l+=1
        elif password[i].islower():
            s_l+=1
        elif password[i].isdigit():
            n_d+=1
        else:
            s_sc+=1
        i+=1
    # print(c_l,s_l,n_d,s_sc)
    if c_l>=1 and s_l>=1 and n_d>=1 and s_sc>=1:
        print("it is strong password")
    else:
        print("it is not strong password")
password=input("enter password")
strong_password(password)

# strong password

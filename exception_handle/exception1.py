try:
    if '1'!=1:
        raise( "someError")
    else:
        print("someeroor has not occur")
except( "someError"):
    print("someError has occured")
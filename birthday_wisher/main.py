import pandas as pd
import datetime
def sendMail(to,sub,msg):
    print(f"Email to {to} sent with subject:{sub} and message{msg}")
if __name__=="__main__":
    df=pd.read_excel("data.xlsx")
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%d-%m")
    writeInd=[]
    for index,item in df.iterrows():
        bdy=item['Birthday'].strftime("%d-%m")
        if(today==bdy) and yearNow not in str(item['year']):
            sendMail(item['Email'],"Happy Birthday",item['Dialogue'])
            writeInd.append(index)
    # print(writeInd)
    for i in writeInd:
        yr=df.loc[i,'year']
        print(yr)
        df.loc[i,'year']=str(yr)+','+str(yearNow)
        print(df.loc[i,'year'])
    print(df)
    df.to_excel('data.xlsx')
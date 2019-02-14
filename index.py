from tkinter import*
import random
import time
import datetime

payroll=Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Payroll management system")

def exit():
    payroll.destroy()

def Reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    cityWeighting.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPaymentDue.set("")

def PayRef():

    PayDate.set(time.strftime("%x"))
    RefPay= random.randint(20000,709467)
    RefPaid=str("PR"+str(RefPay))
    Reference.set(RefPaid)

    NIPay = random.randint(4200, 9467)
    NIPaid = str("NI" + str(RefPay))
    NINumber.set(NIPaid)
def PayPeriod():
    i=datetime.datetime.now()
    TaxPeriod.set(i.month)

    NCode = random.randint(1200, 1467)
    CodeNI= str("NICode" + str(NCode))
    NICode.set(CodeNI)

def MonthlySalary():
    BS=float(BasicSalary.get())
    CW=float(cityWeighting.get())
    OT=float(OverTime.get())

    MTax=((BS+CW+OT)* 0.3)
    TTax="R", str('%.2f'%(MTax))


    Tax.set(TTax)

    MPension = ((BS + CW + OT) * 0.02)
    MMPension = "R", str('%.2f' % (MPension))

    Pension.set(MMPension)

    MStudentLoan = ((BS + CW + OT) * 0.012)
    MMStudentLoan = "R", str('%.2f' % (MStudentLoan))

    StudentLoan.set(MMStudentLoan)

    MNIPayment = ((BS + CW + OT) * 0.011)
    MMNIPayment = "R", str('%.2f' % (MNIPayment))

    NIPayment.set(MMNIPayment)



    Deduct= MTax +MPension+MStudentLoan+MNIPayment
    Deduct_Payment= "R",str('%.2f'%(Deduct))
    Deductions.set(Deduct_Payment)
    Gross_pay="R", str('%.2f' %(BS+CW+OT))
    GrossPay.set(Gross_pay)


    NetPayAfter=((BS+CW+OT)-Deduct)
    NetAfter="R",str('%.2f'%(NetPayAfter))

    TaxablePay.set(TTax)
    PensionablePay.set(MMPension)
    OtherPaymentDue.set("0.00")

    NetPay.set(NetAfter)








EmployeeName=StringVar()
Address=StringVar()
Reference=StringVar()
EmployerName=StringVar()
cityWeighting=StringVar()
BasicSalary=StringVar()
OverTime=StringVar()
GrossPay=StringVar()
NetPay=StringVar()
Tax=StringVar()
Pension=StringVar()
StudentLoan=StringVar()
NIPayment=StringVar()
Deductions=StringVar()
PostCode=StringVar()
Gender=StringVar()
PayDate=StringVar()
TaxPeriod=StringVar()
NINumber=StringVar()
NICode=StringVar()
TaxablePay=StringVar()
PensionablePay=StringVar()
OtherPaymentDue=StringVar()



Tops=Frame(payroll,width=1350, height=50, bd=3)
Tops.pack(side=TOP)
LF=Frame(payroll,width=700, height=650,bd=3,relief="raise")

LF.pack(side=LEFT)
RF=Frame(payroll,width=600, height=650, bd=3,relief="raise")
RF.pack(side=RIGHT)

lblInfo=Label(Tops, font=('arial',50,'bold'),text="Payroll Management System",fg="Red",bd=1)

lblInfo.grid(row=0,column=0)
LeftInsideLF=Frame(LF,width=700, height=100,bd=3,relief="raise" )
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=325,height=400,bd=3,relief="raise")
LeftInsideLFLF.pack(side=LEFT)

LeftInsideRFRF=Frame(LF, width=325,height=400,bd=3,relief="raise")
LeftInsideRFRF.pack(side=RIGHT)

RightInsideLF=Frame(RF,width=700, height=200,bd=3,relief="raise" )
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=300,height=400,bd=3,relief="raise" )
RightInsideLFLF.pack(side=LEFT)

RightInsideRFRF=Frame(RF, width=300,height=400,bd=3,relief="raise" )
RightInsideRFRF.pack(side=RIGHT)


lblEmployeeName=Label(LeftInsideLF, font=('arial',12,'bold'),text="Employee Name",fg="red",bd=10,anchor='w')

lblEmployeeName.grid(row=0,column=0)
txtEmployeeName= Entry(LeftInsideLF,justify='left',textvariable=EmployeeName,fg="red",font=('arial',12,'bold'),bd=3,width=54, bg="white")
txtEmployeeName.grid(row=0,column=1)
lblAddress=Label(LeftInsideLF, font=('arial',12,'bold'),text="Address",fg="red",bd=10,anchor='w')

lblAddress.grid(row=1,column=0)
txtAddress= Entry(LeftInsideLF,fg="red",justify='left',textvariable=Address,font=('arial',12,'bold'),bd=3,width=54, bg="white" )
txtAddress.grid(row=1,column=1)

lblReference=Label(LeftInsideLF,fg="red", font=('arial',12,'bold'),text="Reference",bd=10,anchor='w')

lblReference.grid(row=2,column=0)
txtReference= Entry(LeftInsideLF,fg="red",justify='left',textvariable=Reference,font=('arial',12,'bold'),bd=3,width=54, bg="white")
txtReference.grid(row=2,column=1)
lblEmployerName=Label(LeftInsideLF,fg="red", font=('arial',12,'bold'),text="Employer Name",bd=10,anchor='w')

lblEmployerName.grid(row=3,column=0)
txtEmployerName= Entry(LeftInsideLF,fg="red",justify='left',textvariable=EmployerName,font=('arial',12,'bold'),bd=3,width=54, bg="white" )
txtEmployerName.grid(row=3,column=1)

lblCity=Label(LeftInsideLFLF, font=('arial',12,'bold'),text="City Weighting ",fg="red",bd=10,anchor='w')

lblCity.grid(row=0,column=0)
txtCity= Entry(LeftInsideLFLF,fg="red",justify='left',textvariable=cityWeighting,font=('arial',12,'bold'),bd=3,width=18, bg="white")
txtCity.grid(row=0,column=1)


lblBasicSalary=Label(LeftInsideLFLF, font=('arial',12,'bold'),text="Basic Salary ",fg="red",bd=10,anchor='w')

lblBasicSalary.grid(row=1,column=0)
txtBasicSalary= Entry(LeftInsideLFLF,fg="red",textvariable=BasicSalary,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtBasicSalary.grid(row=1,column=1)

lblOvertime=Label(LeftInsideLFLF, font=('arial',12,'bold'),text="Over Time ",fg="red",bd=10,anchor='w')

lblOvertime.grid(row=2,column=0)
txtOvertime= Entry(LeftInsideLFLF,fg="red",font=('arial',12,'bold'),textvariable=OverTime,bd=3,width=18,justify='left', bg="white")
txtOvertime.grid(row=2,column=1)

lblGrossPay=Label(LeftInsideLFLF, font=('arial',12,'bold'),text="Gross Pay ",fg="red",bd=10,anchor='w')

lblGrossPay.grid(row=3,column=0)
txtGrossPay= Entry(LeftInsideLFLF,fg="red",textvariable=GrossPay,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtGrossPay.grid(row=3,column=1)


lblNetPay=Label(LeftInsideLFLF, font=('arial',12,'bold'),text="Net Pay ",fg="red",bd=10,anchor='w')

lblNetPay.grid(row=4,column=0)
txtNetPay= Entry(LeftInsideLFLF,fg="red",textvariable=NetPay,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtNetPay.grid(row=4,column=1)



##=============================================================================================

lblTax=Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Tax ",fg="red",bd=10,anchor='w')

lblTax.grid(row=0,column=0)
txtTax= Entry(LeftInsideRFRF,justify='left',fg="red",font=('arial',12,'bold'),textvariable=Tax,bd=3,width=18, bg="white")
txtTax.grid(row=0,column=1)


lblPension=Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Pension ",fg="red",bd=10,anchor='w')

lblPension.grid(row=1,column=0)
txtPension= Entry(LeftInsideRFRF,fg="red",textvariable=Pension,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtPension.grid(row=1,column=1)

lblStudentLoan=Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Student Loan ",fg="red",bd=10,anchor='w')

lblStudentLoan.grid(row=2,column=0)
txtStudentLoan= Entry(LeftInsideRFRF,fg="red",textvariable=StudentLoan,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtStudentLoan.grid(row=2,column=1)

lblNIPayment=Label(LeftInsideRFRF,font=('arial',12,'bold'),text="NI Payment ",fg="red",bd=10,anchor='w')

lblNIPayment.grid(row=3,column=0)
txtNIPayment= Entry(LeftInsideRFRF,fg="red",textvariable=NIPayment,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtNIPayment.grid(row=3,column=1)

lblDeductions=Label(LeftInsideRFRF, font=('arial',12,'bold'),text="Deductions ",fg="red",bd=10,anchor='w')

lblDeductions.grid(row=4,column=0)
txtDeductions= Entry(LeftInsideRFRF,fg="red",textvariable=Deductions,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtDeductions.grid(row=4,column=1)





##==============================Right side=====================



lblPostalCode=Label(RightInsideLF, font=('arial',12,'bold'),text="Postal Code",fg="red",bd=10,anchor='w')

lblPostalCode.grid(row=0,column=0)
txtPostalCode= Entry(RightInsideLF,fg="red",textvariable=PostCode,font=('arial',12,'bold'),bd=3,width=48,justify='left', bg="white")
txtPostalCode.grid(row=0,column=1)
lblGender=Label(RightInsideLF, font=('arial',12,'bold'),text="Gender",fg="red",bd=10,anchor='w')

lblGender.grid(row=1,column=0)
txtGender= Entry(RightInsideLF,fg="red",font=('arial',12,'bold'),textvariable=Gender,bd=3,width=48, bg="white" ,justify='left')
txtGender.grid(row=1,column=1)

#right inner side==========================================================
lblPayDate=Label(RightInsideLFLF, font=('arial',12,'bold'),text="Pay Date",fg="red",bd=10,anchor='w')

lblPayDate.grid(row=0,column=0)
txtPayDate= Entry(RightInsideLFLF,fg="red",font=('arial',12,'bold'),bd=3,width=18,textvariable=PayDate,justify='left', bg="white")
txtPayDate.grid(row=0,column=1)

lblTaxPeriod=Label(RightInsideLFLF, font=('arial',12,'bold'),text="Tax Period",fg="red",bd=10,anchor='w')

lblTaxPeriod.grid(row=1,column=0)
txtTaxPeriod= Entry(RightInsideLFLF,fg="red",textvariable=TaxPeriod,font=('arial',12,'bold'),bd=3,width=18,justify='left', bg="white")
txtTaxPeriod.grid(row=1,column=1)

lblNINumber=Label(RightInsideLFLF, font=('arial',12,'bold'),text="NI Number",fg="red",bd=10,anchor='w')

lblNINumber.grid(row=2,column=0)
txtNINumber= Entry(RightInsideLFLF,fg="red",font=('arial',12,'bold'),textvariable=NINumber,bd=3,width=18,justify='left', bg="white")
txtNINumber.grid(row=2,column=1)

lblNICode=Label(RightInsideLFLF, font=('arial',12,'bold'),text="NI Code",fg="red",bd=10,anchor='w')

lblNICode.grid(row=3,column=0)
txtNICode= Entry(RightInsideLFLF,fg="red",font=('arial',12,'bold'),bd=3,width=18,textvariable=NICode,justify='left', bg="white")
txtNICode.grid(row=3,column=1)

lblTaxablePay=Label(RightInsideLFLF, font=('arial',12,'bold'),text="Taxable Pay",fg="red",bd=10,anchor='w')

lblTaxablePay.grid(row=4,column=0)
txtTaxablePay= Entry(RightInsideLFLF,fg="red",font=('arial',12,'bold'),textvariable=TaxablePay,bd=3,width=18,justify='left', bg="white")
txtTaxablePay.grid(row=4,column=1)

lblPensionablePay=Label(RightInsideLFLF, font=('arial',12,'bold'),text="Pensionable Pay",fg="red",bd=10,anchor='w')

lblPensionablePay.grid(row=5,column=0)
txtPensionablePay= Entry(RightInsideLFLF,fg="red",font=('arial',12,'bold'),bd=3,width=18,textvariable=PensionablePay,justify='left', bg="white")
txtPensionablePay.grid(row=5,column=1)

lblOtherPaymentDue=Label(RightInsideLFLF, font=('arial',12,'bold'),text="Other Payment Due",fg="red",bd=10,anchor='w')

lblOtherPaymentDue.grid(row=6,column=0)
txtOtherPaymentDue= Entry(RightInsideLFLF,fg="red",font=('arial',12,'bold'),textvariable=OtherPaymentDue,bd=3,width=18,justify='left', bg="white")
txtOtherPaymentDue.grid(row=6,column=1)



btnWagePayment=Button(RightInsideRFRF,padx=8,bd=8,fg="red",font=('arial',16,'bold'),width=14,
                      command=MonthlySalary,text="Wage Payment",bg="white").grid(row=1,column=0)

btnReset=Button(RightInsideRFRF,padx=8,bd=8,fg="red",font=('arial',16,'bold'),width=14,
                      text="Reset System",bg="white",command=Reset).grid(row=2,column=0)

btnPayReference=Button(RightInsideRFRF,padx=8,bd=8,fg="red",font=('arial',16,'bold'),width=14,
                      text="Pay Reference",bg="white",command=PayRef).grid(row=3,column=0)
btnPayCode=Button(RightInsideRFRF,padx=8,bd=8,fg="red",font=('arial',16,'bold'),width=14,
                      text="Pay Code",bg="white",command=PayPeriod).grid(row=4,column=0)
btnExit=Button(RightInsideRFRF,padx=8,bd=8,fg="red",font=('arial',16,'bold'),width=14,
                      text="Exit",bg="white",command=exit).grid(row=5,column=0)


payroll.mainloop()

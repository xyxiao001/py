import decimal
print (decimal.Decimal('1.00') / decimal.Decimal('3.00'))
# 0.3333333333333333333333333
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
#0.33

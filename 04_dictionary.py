#Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini 
# lug'at ko'rinishida qaytaruvchi funksiya yozing >>python dictionary
while True:
   radius = int(input("iltimos aylananig radiusini kiriting: "))
   diameter= radius*2
   perimeter= radius*6.2832
   area = radius * 3.1416

   thisdict = {
      radius : "radius",
      diameter : "diametr",
      perimeter : "perametr",
      area : "yuzi"
   }
   print( thisdict  )
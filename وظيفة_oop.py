
import re
class Arabictextcleaner:
      def convert_letters(self,s):
          s1=re.sub("[أإآ]","ا",s) 
          return s1
      def delet_movement(self,s2) :
          s3=re.sub(r"[ًٌٍَُِّ]","",s2)
          return s3
      def delete_punktuation(self,s4):
          s5=re.sub(r"[!?؟>{}<._،‘,\[\]]","",s4) #\[ patternلكي يقبلها ال
          return s5
      def delete_c_words(self,s6):
          pattern = r"\b(في|من|إلى|على|عن|أن|إن|ما|لا|لن|لم|هل|قد|ثم|فقد|هذا|هذه|ذلك|تلك|هناك|هنا|كل|أي|أو|و|يا|إنه|أنها|كما|مع|كان|كانت|ليس|لكن|بل|حتى|إذ|إلا|بين|أمام|خلف|بعد|قبل|أكثر|أقل|أحد|كلما|حين|إذًا|أثناء|أصبح|بدون|بسبب|عند|لدى|إلي|منذ|مثل|بما|إما|أيضًا)\b"
          s7=re.sub(pattern,"",s6)
          return s7
      def divide_text(self,s8):
          s9=list(s8.split(" "))
          return s9
      def all_f(self ,x):
          x1=self.convert_letters(x)
          x1=self.delet_movement(x1)
          x1=self.delete_punktuation(x1)
          x1=self.delete_c_words(x1)
          return x1
k1= Arabictextcleaner()
print(k1.convert_letters("مرحبا بك حسأآإم"))

print(k1.delet_movement("أَحمِدً رافقَ رامزاٍ"))

print(k1.delete_punktuation("أحمد .؟رافق رامز[]"))

print (k1.delete_c_words("محمد من و جاسم صديقين بسبب منذ سنة"))

print(k1.divide_text("محمد جاسم فهد رولا بسمة"))

print (k1.all_f("أأحمدً! بسبب يتأخر عن الجلسة"))



class Keyboard_convert:
    def convert_a_to_e(self ,s):
        dict1={
    'ض': 'q', 'ص': 'w', 'ث': 'e', 'ق': 'r', 'ف': 't', 'غ': 'y', 'ع': 'u', 'ه': 'i', 'خ': 'o', 'ح': 'p',
    'ج': '[', 'د': ']', 'ش': 'a', 'س': 's', 'ي': 'd', 'ب': 'f', 'ل': 'g', 'ا': 'h', 'ت': 'j', 'ن': 'k',
    'م': 'l', 'ك': ';', 'ط': "'", 'ئ': 'z', 'ء': 'x', 'ؤ': 'c', 'ر': 'v', 'لا': 'b', 'ى': 'n', 'ة': 'm',
  " " : " " , 'و': ',', 'ز': '.', 'ظ': '/'
}
        s1=""
        for i in s:
            if i in dict1.keys():
                s1=s1+dict1[i]
        return s1
    def convert_e_to_a(self,s2):
        dict2={'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج'
               , ']': 'د', 'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل', 'h': 'ا', 'j': 'ت', 'k': 'ن', 'l': 'م', ';': 'ك', "'": 'ط'
               , 'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا', 'n': 'ى', 'm': 'ة', ' ': ' ', ',': 'و', '.': 'ز', '/': 'ظ'}
        s3=""
        for i1 in s2:
            if i1 in dict2.keys():
                s3=s3+dict2[i1]
        return s3
    def faumos_word(self,s4):
        dict3={"Oracle":"أوراكل","Python":"بايثون","Machine":"ماشين","Python": "بايثون", "Java": "جافا", "Scala": "سكالا", "Oracle": "أوراكل", "Machine": "ماشين", "Learning": "ليرننغ", "Deep": "ديب", "Data": "داتا", "Model": "موديل", "HTML": "إتش تي إم إل", "CSS": "سي إس إس", "Package": "باكيج", "Function": "فانكشن", "Class": "كلاس", "Object": "أوبجكت", "Code": "كود", "Index": "إندكس", "Method": "ميثود", "Input": "إنبوت", "Output": "أوتبوت", "Source": "سورس", "File": "فايل", "User": "يوزر", "Account": "أكونت", "Password": "باسورد", "Email": "إيميل", "Server": "سيرفر", "Cloud": "كلود"}

        if s4 in dict3:
            return dict3[s4]
    
k2=Keyboard_convert()
print (k2.convert_a_to_e("اثممخ هى سغقهش"))

print (k2.convert_e_to_a("lpl] hghwghk "))

print (k2.faumos_word("Machine"))



class MathUtils:
    def avge(self ,list1):
        s=0
        for i in list1:
            s=s+i
        l=0    
        for j in list1:
            l=l+1
        return s/l     
    def mediator(self,list2):
        list2.sort()
        l=0    
        for j in list2:
            l=l+1
        if l%2==0:
            return (list2[(l//2)-1]+list2[l//2])/2
        else:
            return list2[l//2]
        
    def Q1(self,list3):
        list3.sort()
        l1=0  
        for j in list3:
            l1=l1+1
        if l1%2==0:
            x=(list3[(l1//2)-1]+list3[l1//2])/2
            return x
        else:
            x= list3[l1//2]
            return x
        list4=list3[:x]   
        l2=0  
        for j in list4:
            l2=l2+1
        if l2%2==0:
            x1=(list4[(l2//2)-1]+list4[l2//2])/2
            return x1
        else:
            x1= list4[l2//2]
            return x1  
    def Q3(self,list5):
        list5.sort()
        l2 = len(list5)
        if l2 % 2 == 0:
            upper_half = list5[l2 // 2:]
        else:
            upper_half = list5[(l2 // 2) + 1:]
        long = len(upper_half)
        if long % 2 == 0:
            return (upper_half[long // 2 - 1] + upper_half[long // 2]) / 2
        else:
            return upper_half[long // 2]
    def min_value(self ,list6)    :
        min=list6[0]
        for i in list6:
            if i<min:
                min=i
        return min
    def max_value(self,list7):
        max=list7[0]
        for i in list7:
            if i>max:
                max=i
        return max
    def range_minmax(self,list8):
        return list8[min(list8):max(list8)]
    
    def tabaun(self,data):
        n = len(data)
        mean = sum(data) / n
        total = 0
        for x in data:
            total += (x - mean) ** 2
        return total / n 
    def enheraf(self,data):
        n = len(data)
        mean = sum(data) / n
        total = 0
        for x in data:
            total += (x - mean) ** 2
        variance = total / n
        std_dev = variance ** 0.5
        return std_dev
    def all_data(self, lisst):
        print("...........................")

        print(f"avge : {self.avge(lisst)}")
        print(f"mediator : {self.mediator(lisst)}")
        print(f"Q1 : {self.Q1(lisst)}")
        print(f"Q3 : {self.Q3(lisst)}")
        print(f"min_value : {self.min_value(lisst)}")
        print(f"max_value : {self.max_value(lisst)}")
        print(f"rang : {self.range_minmax(lisst)}")
        print(f"t : {self.tabaun(lisst)}")
        print(f"e : {self.enheraf(lisst)}") 
 
        

k3=MathUtils()
print (k3.avge([3,4,5,2,4]))

print(k3.mediator([9,11,12,20,3,1,5]))

print(k3.Q1([2,5,4,5]))
print(k3.Q3([2,5,4,8,6,8,5]))
print (k3.max_value([2,5,4,8,6,8,5]))
print (k3.min_value([2,5,4,8,6,8,5]))
print (k3.range_minmax([2,5,4,8,6,8,5]))
print (k3.tabaun([2,5,4,8,6,8,5]))
print (k3.enheraf([2,5,4,8,6,8,5]))


k3.all_data([2,5,4,8,6,8,5])
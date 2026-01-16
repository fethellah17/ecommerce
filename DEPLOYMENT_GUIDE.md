# دليل النشر على Vercel - موقع Django E-commerce

## ✅ تم الإعداد بنجاح!

### الملفات المحدثة:
- ✅ `vercel.json` - تكوين Vercel
- ✅ `settings.py` - إعدادات Django مع PostgreSQL و AWS S3
- ✅ `requirements.txt` - جميع الحزم المطلوبة
- ✅ `build.sh` - سكربت البناء
- ✅ `.env` - ملف البيئة المحلي
- ✅ `.env.example` - نموذج متغيرات البيئة
- ✅ `.vercelignore` - الملفات المستبعدة من النشر

---

## 🚀 خطوات النشر على Vercel

### 1. تثبيت Vercel CLI
```bash
npm install -g vercel
```

### 2. تسجيل الدخول
```bash
vercel login
```

### 3. إعداد قاعدة البيانات PostgreSQL

#### الخيار أ: Vercel Postgres (موصى به - $0.24/شهر)
1. افتح مشروعك على Vercel Dashboard
2. اذهب إلى: **Storage** → **Create Database** → **Postgres**
3. انسخ `POSTGRES_URL` من تبويب `.env.local`

#### الخيار ب: Neon (مجاني تمامًا)
1. سجل على: https://neon.tech
2. أنشئ مشروع جديد
3. انسخ رابط الاتصال (يبدأ بـ `postgresql://`)

#### الخيار ج: Supabase (مجاني)
1. سجل على: https://supabase.com
2. أنشئ مشروع
3. اذهب إلى: **Settings** → **Database** → انسخ **Connection String**

### 4. إضافة متغيرات البيئة

#### من Terminal:
```bash
cd test/ecommerce
vercel env add SECRET_KEY
# أدخل: مفتاح-سري-جديد-قوي-123456789

vercel env add DATABASE_URL
# أدخل: postgresql://user:pass@host/db

vercel env add DEBUG
# أدخل: False
```

#### أو من Dashboard:
1. افتح مشروعك على https://vercel.com
2. **Settings** → **Environment Variables**
3. أضف:
   - `SECRET_KEY` = مفتاح سري قوي
   - `DATABASE_URL` = رابط PostgreSQL
   - `DEBUG` = False

### 5. النشر!
```bash
cd test/ecommerce
vercel --prod
```

---

## 🎨 (اختياري) إعداد AWS S3 للصور

بدون S3، الصور المرفوعة ستُحذف بعد كل deployment.

### الخطوات:
1. **إنشاء حساب AWS**: https://aws.amazon.com
2. **إنشاء S3 Bucket**:
   - اذهب إلى S3 Console
   - Create bucket
   - اسم: `your-ecommerce-media`
   - Region: `us-east-1` (أو أقرب منطقة)
   - Uncheck "Block all public access"
   
3. **إنشاء IAM User**:
   - IAM → Users → Add user
   - Attach policy: `AmazonS3FullAccess`
   - احفظ: Access Key ID و Secret Access Key

4. **إضافة متغيرات البيئة**:
```bash
vercel env add USE_S3
# أدخل: True

vercel env add AWS_ACCESS_KEY_ID
# أدخل: AKIA...

vercel env add AWS_SECRET_ACCESS_KEY
# أدخل: secret-key

vercel env add AWS_STORAGE_BUCKET_NAME
# أدخل: your-ecommerce-media

vercel env add AWS_S3_REGION_NAME
# أدخل: us-east-1
```

5. **إعادة النشر**:
```bash
vercel --prod
```

---

## 🧪 اختبار محلي

```bash
# تفعيل البيئة الافتراضية
cd test
Scripts\activate

# تشغيل السيرفر
cd ecommerce
python manage.py runserver

# افتح: http://localhost:8000
```

---

## 📝 ملاحظات مهمة

### الأمان:
- ⚠️ لا ترفع ملف `.env` إلى Git
- ⚠️ استخدم `SECRET_KEY` قوي في الإنتاج
- ✅ `DEBUG=False` في الإنتاج دائمًا

### قاعدة البيانات:
- ✅ SQLite للتطوير المحلي فقط
- ✅ PostgreSQL للإنتاج (Vercel/Neon/Supabase)
- ⚠️ قم بعمل نسخ احتياطية دورية

### الملفات الثابتة:
- ✅ WhiteNoise يتعامل مع static files
- ✅ تُجمع تلقائيًا عند البناء

### الوسائط (Media):
- ⚠️ بدون S3: تُحذف بعد كل deployment
- ✅ مع S3: تُخزن بشكل دائم

---

## 🔧 استكشاف الأخطاء

### خطأ "Application Error":
```bash
vercel logs --follow
```

### خطأ في قاعدة البيانات:
- تحقق من `DATABASE_URL` في Environment Variables
- تأكد من أن قاعدة البيانات تقبل اتصالات من الخارج

### خطأ في الملفات الثابتة:
```bash
python manage.py collectstatic --noinput
```

---

## 📚 موارد مفيدة

- [Vercel Docs](https://vercel.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Neon Postgres](https://neon.tech)
- [AWS S3 Guide](https://aws.amazon.com/s3/getting-started/)

---

## 🎉 جاهز للنشر!

كل شيء معد الآن. فقط اتبع الخطوات أعلاه وموقعك سيكون على الهواء في دقائق!

```bash
cd test/ecommerce
vercel --prod
```

حظ موفق! 🚀

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, is_staff=False, is_active=True, is_admin=False, is_doctor=False, is_user=True):
        if not phone:
            raise ValueError('users must have a phone number')
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(phone=phone)
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.doctor = is_doctor
        user_obj.user = is_user
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,)
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
            is_staff=True,
            is_admin=True,) 
        return user
    
    
class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M','Man'),
        ('W','Woman'),
        ('T','Transgender'),
        ('N','Nonbinary'),
        ('GI','Gender identity'),
        ('GT','Gender transition')
    )
    GENDER_INTERESTED_IN = (
        ('M','Man'),
        ('W','Woman'),
        ('E','Everyone'),
    )
    LOOKING_CHOICES =(
        ('1','long-term dating'),
        ('2','short-term dating'),
        ('3',"don't know yet"),
        ('4','Hookups'),
        ('5','Friendship'),
        ('6','Other'),
    )
    INTEREST_CHOICES = (
        ('1','Dance'),
        ('2','Woodworking'),
        ('3','Music'),
        ('4','Drawing'),
        ('5','Fishing'),
        ('6','Video Game'),
        ('7','Hiking'),
        ('8','Computer Programming'),
        ('9','Blogging'),
        ('10','Swimming'),
        ('11','Running'),
        ('12','Chess'),
        ('13','Travel'),
        ('14','Singing'),
        ('15','Baking'),
        ('16','yoga'),
        ('17','Pottery'),
        ('18','Sports'),
        ('19','Cooking'),
        ('20','Writing'),
        ('21','Painting'),
        ('22','Reading'),
        ('23','Gardening'),
    )
    SEXUAL_CHOICES = (
        ('1','Allosexual'),
        ('2','Allosexism'),
        ('3','Andorsexual'),
        ('4','Asexual'),
        ('5','Bisexual'),
        ('6','Biromantic'),
        ('7','Coming out'),
        ('8','Cupiosexual'),
        ('9','Gay'),
        ('10','Closeted'),
        ('11','Gayromantic'),
        ('12','Fluid'),
        ('13','Gaysexual'),
        ('14','Demiromantic'),
        ('15','Heterosexual'),
        ('16','Homosexual'),
        ('17','Libidoist asexual'),
        ('18','Monosexual'),
        ('19','Omnisexual'),
        ('20','Pansexual'),
        ('21','Pomosexual'),
        ('22','Passing'),
        ('23','Questioning'),
        ('24','Queer'),
        ('25','Romantic orientation'),
        ('26','Sapiosexual'),
        ('27','Sexual attraction'),
        ('28','Sexual orientation or sexuality'),
        ('29','Spectrasexual'),
        ('30','Sex-averse'),)

    PROMPT_CHOICES = (
        ('1','You lokk like someone'),
        ('2',"What's your favourite pizza topping"),
        ('3','like first impression are really'),
        ('4','A lot of people can fake strength'),
        ('5','i find you very intriguing'),
        ('6','My friends would be jealous if you'),      
    )
    RELATION_CHOICES = (
        ('1',"Marriage"),
        ('2',"Friendship"),
        ('3',"Monogamous"),
        ('4',"Nonmonogamous"),
        ('5',"commitment"),
        ('6',"Polygamous"),
        ('7',"Engagement"),
        ('8',"Long distance"),
        ('9',"Polymorous"),
    )
    ZODIAC_CHOICES = (
        ("1","Capricorn"),
        ("2","Aquarius"),
        ("3","Pisces"),
        ("4","Aries"),
        ("5","Taurus"),
        ("6","Gemini"),
        ("7","Cancer"),
        ("8","Leo"),
        ("9","Virgo"),
        ("10","Libra"),
        ("11","Scorpio"),
        ("12","Sagittarius"),

    )
    DRINKING_CHOICES = (
        ("1","socially"),
        ("2","planing to quit"),
        ("3","socially at the weekend"),
        ("4","occasionally"),
        ("5","night"),
        ("6","Never"),
    )
    SMOKING_CHOICES = (
        ("1","socially"),
        ("2","Regularly"),
        ("3","try to quit"),
    )
    EDUCATION_CHOICES =(
        ("1","Secondary Education"),
        ("2","undergratuate"),
        ("3","at college"),
        ("4","postgraduate"),
        ("5","at university"),
    )

    STATUS_CHOICES = (
        ("1","single"),
        ("2","married"),
        ("3","unmarried"),
        ("4","Divorcee"),
        ("5","soul mate"),
    )
    DIETARY_CHOICE = (
        ("1","lactose intolerance"),
        ("2","Gluten intolerance or sensitivity"),
        ("3","Vegetarianism"),
        ("4","veganism"),
        ("5","Kosher"),
        ("6","Keto"),
        ("7","Diabetes"),
        ("8","Low carb"),
        ("9","Dairy-free"),
        ("10","Food allergies"),
    )
    WORKOUT_CHOICE = (
        ("1","daily"),
        ("2","Never"),
        ("3","sometimes"),
    )
    LANGUAGE_CHOICE = (
        ("ab","Abkhaz"),
        ("aa","Afar"),
        ("af","Afrikaans"),
        ("ak","Akan"),
        ("sq","Albanian"),
        ("am","Amharic"),
        ("ar","Arabic"),
        ("an","Aragonese"),
        ("hy","Armenian"),
        ("as","Assamese"),
        ("av","Avaric"),
        ("ae","Avestan"),
        ("ay","Aymara"),
        ("az","Azerbaijani"),
        ("bm","Bambara"),
        ("ba","Bashkir"),
        ("eu","Basque"),
        ("be","Belarusian"),
        ("bn","Bengali"),
        ("bh","Bihari"),
        ("bi","Bislama"),
        ("bs","Bosnian"),
        ("br","Breton"),
        ("bg","Bulgarian"),
        ("my","Burmese"),
        ("ca","Catalan"),
        ("ch","Chamorro"),
        ("ce","Chechen"),
        ("ny","Chichewa"),
        ("zh","Chinese"),
        ("cv","Chuvash"),
        ("kw","Cornish"),
        ("co","Corsican"),
        ("cr","Cree"),
        ("hr","Croatian"),
        ("cs","Czech"),
        ("da","Danish"),
        ("dv","Divehi"),
        ("nl","Dutch"),
        ("en","English"),
        ("eo","Esperanto"),
        ("et","Estonian"),
        ("ee","Ewe"),
        ("fo","Faroese"),
        ("fj","Fijian"),
        ("fi","Finnish"),
        ("fr","French"),
        ("ff","Fula"),
        ("gl","Galician"),
        ("ka","Georgian"),
        ("de","German"),
        ("el","Greek"),
        ("gn","Guaraní"),
        ("gu","Gujarati"),
        ("ht","Haitian"),
        ("ha","Hausa"),
        ("he","Hebrew "),
        ("hz","Herero"),
        ("hi","Hindi"),
        ("ho","Hiri Motu"),
        ("hu","Hungarian"),
        ("ia","Interlingua"),
        ("id","Indonesian"),
        ("ie","Interlingue"),
        ("ga","Irish"),
        ("ig","Igbo"),
        ("ik","Inupiaq"),
        ("io","Ido"),
        ("is","Icelandic"),
        ("it","Italian"),
        ("iu","Inuktitut"),
        ("ja","Japanese"),
        ("jv","Javanese"),
        ("kl","Kalaallisut"),
        ("kn","Kannada"),
        ("kr","Kanuri"),
        ("ks","Kashmiri"),
        ("kk","Kazakh"),
        ("km","Khmer"),
        ("ki","Kikuyu"),
        ("rw","Kinyarwanda"),
        ("ky","Kirghiz"),
        ("kv","Komi"),
        ("kg","Kongo"),
        ("ko","Korean"),
        ("ku","Kurdish"),
        ("kj","Kwanyama"),
        ("la","Latin"),
        ("lb","Luxembourgish"),
        ("lg","Luganda"),
        ("li","Limburgish"),
        ("ln","Lingala"),
        ("lo","Lao"),
        ("lt","Lithuanian"),
        ("lu","Luba-Katanga"),
        ("lv","Latvian"),
        ("gv","Manx"),
        ("mk","Macedonian"),
        ("mg","Malagasy"),
        ("ms","Malay"),
        ("ml","Malayalam"),
        ("mt","Maltese"),
        ("mi","Māori"),
        ("mr","Marathi"),
        ("mh","Marshallese"),
        ("mn","Mongolian"),
        ("na","Nauru"),
        ("nv","Navajo"),
        ("nb","Norwegian"),
        ("nd","North Ndebele"),
        ("ne","Nepali"),
        ("ng","Ndonga"),
        ("nn","Norwegian Nynorsk"),
        ("no","Norwegian"),
        ("ii","Nuosu"),
        ("nr","South Ndebele"),
        ("oc","Occitan"),
        ("oj","Ojibwe"),
        ("cu","Old Church Slavonic"),
        ("om","Oromo"),
        ("or","Oriya"),
        ("os","Ossetian"),
        ("pa","Panjabi"),
        ("pi","Pāli"),
        ("fa","Persian"),
        ("pl","Polish"),
        ("ps","Pashto"),
        ("pt","Portuguese"),
        ("qu","Quechua"),
        ("rm","Romansh"),
        ("rn","Kirundi"),
        ("ro","Romanian"),
        ("ru","Russian"),
        ("sa","Sanskrit "),
        ("sc","Sardinian"),
        ("sd","Sindhi"),
        ("se","Northern"),
        ("sm","Samoan"),
        ("sg","Sango"),
        ("sr","Serbian"),
        ("gd","Scottish Gaelic"),
        ("sn","Shona"),
        ("si","Sinhala"),
        ("sk","Slovak"),
        ("sl","Slovene"),
        ("so","Somali"),
        ("st","Southern Sotho"),
        ("es","Spanish"),
        ("su","Sundanese"),
        ("sw","Swahili"),
        ("ss","Swati"),
        ("sv","Swedish"),
        ("ta","Tamil"),
        ("te","Telugu"),
        ("tg","Tajik"),
        ("th","Thai"),
        ("ti","Tigrinya"),
        ("bo","Tibetan Standard"),
        ("tk","Turkmen"),
        ("tl","Tagalog"),
        ("tn","Tswana"),
        ("to","Tonga"),
        ("tr","Turkish"),
        ("ts","Tsonga"),
        ("tt","Tatar"),
        ("tw","Twi"),
        ("ty","Tahitian"),
        ("ug","Uighur"),
        ("uk","Ukrainian"),
        ("ur","Urdu"),
        ("uz","Uzbek"),
        ("ve","Venda"),
        ("vi","Vietnamese"),
        ("vo","Volapük"),
        ("wa","Walloon"),
        ("cy","Welsh"),
        ("wo","Wolof"),
        ("fy","Western Frisian"),
        ("xh","Xhosa"),
        ("yi","Yiddish"),
        ("yo","Yoruba"),
        ("za","Zhuang"),
    )
    phone_regex = RegexValidator(regex='^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    
    first_login = models.BooleanField(default=False)
    otp = models.CharField(max_length=9, blank=True, null=True)
    logged = models.BooleanField(default=False, help_text='If otp verification got successful')
    count = models.IntegerField(default=0, help_text='Number of otp sent')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.BooleanField(default=False)
    user = models.BooleanField(default=True)
    
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='M',blank=True, null=True)
    gender_intersted_in = models.CharField(max_length=50, choices=GENDER_INTERESTED_IN, default='M',blank=True, null=True)
    looking_for = models.CharField(max_length=50, choices = LOOKING_CHOICES, default='1',blank=True, null=True)
    interest_in = models.CharField(max_length=50, choices = INTEREST_CHOICES,blank=True, null=True)
    sexual_orientation_in = models.CharField(max_length=50, choices = SEXUAL_CHOICES,blank=True, null=True)
    user_dob=models.DateField(null=True)
    
    pick_prompt = models.CharField(max_length=50, choices=PROMPT_CHOICES, null=True, blank=True)
    relationship_type = models.CharField(max_length=50, choices=RELATION_CHOICES, blank=True,null= True)
    work_title = models.CharField(max_length=100, null=True,blank=True)
    company_industry_name = models.CharField(max_length=100,blank=True, null=True)
    university = models.CharField(max_length=100,blank=True,null=True)
    Height = models.CharField(max_length=10,blank=True,null=True)
    language_you_know = models.CharField(max_length=30, choices=LANGUAGE_CHOICE,blank=True,null=True)
    zodia_choices = models.CharField(max_length=20, choices=ZODIAC_CHOICES,blank=True,null=True)
    drinking_choices = models.CharField(max_length=50, choices=DRINKING_CHOICES,blank=True,null=True)
    smoking_choices = models.CharField(max_length=50,choices=SMOKING_CHOICES,blank=True,null=True)
    education_choices = models.CharField(max_length=50,choices=EDUCATION_CHOICES,blank=True,null=True)
    status_choices = models.CharField(max_length=20,choices=STATUS_CHOICES,blank=True,null=True)
    dietary_choices = models.CharField(max_length=50,choices=DIETARY_CHOICE,blank=True,null=True)
    work_out = models.CharField(max_length=50,choices= WORKOUT_CHOICE,blank=True,null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.phone
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin
    @property
    def is_doctor(self):
        return self.doctor
    @property
    def is_user(self):
        return self.user
    
class Upload_image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_model")
    upload_image = models.ImageField(upload_to='images',null=True,blank=True)
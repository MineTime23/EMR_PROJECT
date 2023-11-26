from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, password=None, **extra_fields):
        if not user_id:
            raise ValueError('The given user_id must be set')
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(user_id, password, **extra_fields)

# User 모델 정의
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=15, unique=True, primary_key=True)  # 사용자 ID
    name = models.CharField(max_length=50)  # 이름
    birth_date = models.DateField()  # 생년월일
    address = models.CharField(max_length=255)  # 주소
    gender = models.CharField(max_length=1, choices=[('M', '남성'), ('F', '여성')])  # 성별
    phone_num = models.CharField(max_length=15)  # 전화번호
    email = models.EmailField(unique=True)  # 이메일 (unique=True)
    department = models.CharField(max_length=50, blank=True)  # 부서
    position = models.CharField(max_length=50, blank=True)  # 직책
    role = models.CharField(max_length=10, choices=[  # 역할
        ('관리자', '관리자'),
        ('의사', '의사'),
        ('물리 치료사', '물리 치료사'),
        ('기타 의료진', '기타 의료진'),
        ('환자', '환자'),
        ('간호사', '간호사'),
    ])

    # Boolean fields
    is_staff = models.BooleanField(default=True)  # 스태프 여부
    is_superuser = models.BooleanField(default=False)  # 슈퍼유저 여부
    is_active = models.BooleanField(default=True)  # 활성 여부

    # Custom user manager
    objects = CustomUserManager()

    # Set the username field
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email', 'name', 'birth_date', 'address', 'gender', 'phone_num', 'role']

    # 호환성 문제로 코드 추가 (231121)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_user_permissions',
    )

    def __str__(self):
        return f"ID: {self.user_id} 이름: {self.name}"


# Patient 모델 정의
class Patient(models.Model):
    id = models.AutoField(primary_key=True)  # 환자 ID
    last_name = models.CharField(max_length=50, null=False)  # 성
    first_name = models.CharField(max_length=50, null=False)  # 이름
    birth_date = models.DateField(null=False)  # 생년월일
    address = models.CharField(max_length=255, null=False)  # 주소
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)  # 성별
    phone_num = models.CharField(max_length=15, null=False)  # 전화번호
    email = models.CharField(max_length=100, null=True)  # 이메일
    image = models.CharField(max_length=50, null=True)  # 이미지

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

# 검사데이터
class TestRecords(models.Model):
    test_code = models.AutoField(primary_key=True)  # 검사 코드
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True, blank=True)  # 환자
    MuscleMass = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 근육량
    BodyFatMass = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 체지방량
    Muscular_strength = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 근력
    cardio_endurance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 심폐지구력
    agility = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 민첩성
    flexibility = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 유연성
    # data_code = models.AutoField()
    date = models.DateField()  # 날짜

    def __str__(self):
        return f" 신체계측/바이탈 "

# 매체데이터
class MediaRecords(models.Model):
    MEDIA_TYPES = [
        ('XRAY', 'X-Ray'),
        ('VIDEO', 'Video'),
        ('INBODY', 'InBody'),
        ('OTHER', 'Other'),
    ]

    data_code = models.AutoField(primary_key=True)  # 미디어 코드
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True, blank=True)  # 환자
    test_code = models.ForeignKey(TestRecords, on_delete=models.DO_NOTHING, related_name='media', null=True, blank=True)  # 테스트 레코드
    field4 = models.CharField(max_length=255, null=True, blank=True)  # 필드4

    def __str__(self):
        media_type = None
        if self.xray_url:
            media_type = 'X-Ray'
        elif self.video_url:
            media_type = 'Video'
        elif self.inbody_url:
            media_type = 'InBody'
        else:
            media_type = 'Other'

        return f"Media Record - Date: {self.date}, Patient: {self.patient.patient_number}, Type: {media_type}"

# 진단데이터
class DiagnosticRecords(models.Model):
    diagnosis_code = models.AutoField(primary_key=True)  # 진단 코드
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True, blank=True)  # 환자
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)  # 사용자
    diagnosis_date = models.DateField(auto_now_add=True)  # 진단일
    symptoms = models.CharField(max_length=55, null=True, blank=True)  # 증상
    diagnosis = models.CharField(max_length=55, null=True, blank=True)  # 진단
    comments = models.CharField(max_length=55, null=True, blank=True)  # 코멘트

    def __str__(self):
        return f"진료 기록"

# 처방데이터
class Prescription(models.Model):
    prescription_code = models.AutoField(primary_key=True)  # 처방 코드, 자동 생성 필드
    medical_record = models.ForeignKey('DiagnosticRecords', on_delete=models.CASCADE)  # 진료 기록과의 외래키 관계
    medication_name = models.CharField(max_length=100)  # 처방 약 명, 문자열 필드
    total_dosage = models.DecimalField(max_digits=10, decimal_places=2)  # 총 투여량, 실수 필드
    frequency = models.IntegerField()  # 투여 횟수, 정수 필드
    duration_days = models.IntegerField()  # 투여 기간(일수), 정수 필드
    unit = models.CharField(max_length=20)  # 단위, 문자열 필드
    def __str__(self):
        return f" 처방 자료 "


# 치료데이터
class TreatmentRecords(models.Model):
    treatment_code = models.AutoField(primary_key=True)  # 치료 코드
    DiagnosticRecords.diagnosis_code = models.ForeignKey(DiagnosticRecords, on_delete=models.DO_NOTHING,
                                                         related_name='치료', null=True, blank=True)  # 진단 레코드
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='치료', null=True, blank=True)  # 환자
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='치료', null=True, blank=True)  # 사용자
    date = models.DateField(auto_now_add=True)  # 날짜
    treatment_type = models.CharField(max_length=30, null=True, blank=True)  # 치료 유형
    duration = models.IntegerField(null=True, blank=True)  # 기간
    time = models.IntegerField(null=True, blank=True)  # 시간

    def __str__(self):
        return f" 치료 "



# 운동데이터
class ExerciseRecords(models.Model):
    EXERCISE_TYPE_CHOICES = [
        ('strength', '무산소'),
        ('cardio', '유산소'),
    ]

    exercise_code = models.AutoField(primary_key=True)  # 운동 코드
    DiagnosticRecords.diagnosis_code = models.ForeignKey(DiagnosticRecords, on_delete=models.DO_NOTHING,
                                                         related_name='운동', null=True, blank=True)  # 진단 레코드
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, related_name='운동', null=True, blank=True)  # 환자
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='운동', null=True, blank=True)  # 사용자
    date = models.DateField(auto_now_add=True)  # 날짜
    iteration = models.IntegerField(null=True, blank=True)  # 반복 횟수
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 중량
    duration = models.IntegerField(null=True, blank=True)  # 기간
    speed = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 속도
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # 거리
    exercise_type = models.CharField(max_length=10, choices=EXERCISE_TYPE_CHOICES, null=True, blank=True)  # 운동 유형

    def __str__(self):
        return f" 운동 "




# 예약시스템
class Appointments(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')  # 의사
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_appointments')  # 환자
    appointment_date = models.DateField()  # 예약 날짜
    appointment_time = models.TimeField()  # 예약 시간
    symptoms = models.TextField()  # 증상
    purpose = models.TextField()  # 목적

    PENDING = 'pending'  # 대기 중
    IN_PROGRESS = 'in_progress'  # 진행 중
    COMPLETED = 'completed'  # 완료
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=PENDING)  # 상태

    def __str__(self):
        return f"{self.doctor.name} - {self.patient.last_name} {self.patient.first_name} - {self.appointment_date.strftime('%Y-%m-%d')} {self.appointment_time.strftime('%H:%M')}"

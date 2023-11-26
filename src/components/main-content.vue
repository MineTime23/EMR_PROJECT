<template>
  <main class="content">
    <div class="grid-frame">
      <div class="grid-container">

        <div class="grid-item-1">
          <p id="title">환자 정보</p>
          <div id="space">
            <p style="font-size: 20px; text-align: left"><strong>홍길동</strong></p>
          </div>
          <div class="patient-info-div">
            <table class="patient-info">
              <tr>
                <th>성별</th>
                <td>남</td>
              </tr>
              <tr>
                <th>생년월일</th>
                <td>2000년 1월 1일</td>
              </tr>
              <tr>
                <th>주소</th>
                <td>경기도 안산시 상록구 한양대학로 55</td>
              </tr>
            </table>
          </div>
          <div>
            <input type="text" v-model="searchTreatments" placeholder="날짜로 검색">
            <button @click="search" class="search-button">검색</button>
          </div>
          <table class="treatment-list" style="margin: 16px 0 0 0">
            <tr>
              <th width="96px">ID</th>
              <th width="64px">날짜</th>
              <th width="40px">종류</th>
              <th>담당직원</th>
            </tr>
          </table>
          <div class="treatment-list-div">
            <table id="trtlist" class="treatment-list">
              <tr v-for="trt in trtlist" :key="trt.id" @click="rowClickTrt(trt)">
                <td width="96px">{{ trt.id }}</td>
                <td width="64px">{{ trt.date }}</td>
                <td width="40px">{{ trt.type }}</td>
                <td>{{ trt.manager }}</td>
              </tr>
            </table>
          </div>
          <div style="margin: 24px 0 0 0;">
            <button @click="search" class="treat-button">검사 데이터 보기</button>
            <button @click="search" class="treat-button">매체 데이터 보기</button>
          </div>
        </div>
        <div class="grid-item-2">
          <p id="title">환자 검색</p>
          <div id="space">
            <input type="text" v-model="searchPatients" placeholder="날짜로 검색">
            <button @click="search" class="search-button">검색</button>
          </div>
          <table class="patient-list" style="margin: 16px 0 0 0">
            <tr>
              <th width="96px">환자ID</th>
              <th width="64px">성함</th>
              <th width="40px">성별</th>
              <th>생년월일</th>
            </tr>
          </table>
          <div class="patient-list-div" style="margin: 0">
            <table id="patlist" class="patient-list">
              <tr v-for="pat in patlist" :key="pat.id" @click="rowClickPat(pat)">
                <td width="96px">{{ pat.id }}</td>
                <td width="64px">{{ pat.name }}</td>
                <td width="40px">{{ pat.sex }}</td>
                <td>{{ pat.birth }}</td>
              </tr>
            </table>
          </div>
        </div>
      </div>
      <div class="grid-container">
        <div class="grid-item-3">
          <p id="title">환자 검사 데이터</p>
          <button id="x">✕</button>
        </div>
        <div class="grid-item-4">
          <p id="title">환자 진료 데이터</p>
          <button id="x">✕</button>
          <div id="patlist_result"></div>
          <div class="treatdata-div">
            <table class="treatdata">
              <tr>
                <th>일자</th>
                <td>2023년 10월 30일</td>
              </tr>
              <tr>
                <th>담당</th>
                <td>이상익</td>
              </tr>
              <tr>
                <th>증상</th>
                <td><textarea readonly>무릎이 뻣뻣 시린 느낌, 일주일 정도, 움직일 때 특히 아픔</textarea></td>
              </tr>
              <tr>
                <th>진단</th>
                <td><textarea readonly>퇴행성 관절염</textarea></td>
              </tr>
              <tr>
                <th>특이<br>사항</th>
                <td><textarea readonly>진행 초기</textarea></td>
              </tr>
            </table>
          </div>
        </div>
        <div class="grid-item-5">
          <p id="title">환자 치료 데이터</p>
          <button id="x">✕</button>
          <div class="treatdata-div">
            <table class="treatdata">
              <tr>
                <th>일자</th>
                <td>2023년 9월 26일</td>
              </tr>
              <tr>
                <th>담당</th>
                <td>홍인정</td>
              </tr>
              <tr>
                <th>치료<br>내역</th>
                <td><textarea readonly>양 무릎 온찜질 20분, 유연성 운동(스트레칭)</textarea></td>
              </tr>
            </table>
          </div>
        </div>
      </div>
      <div class="grid-container">
        <div class="grid-item-7">
          <p id="title2">작성</p>
          <button class="section-button"
                      @click="toggleSection('diagnosis', 'http://localhost:8000/api3/create_diagnosis/')">진료 데이터
              </button>
              <button class="section-button"
                      @click="toggleSection('prescription', 'http://localhost:8000/api4/create_prescription/')">처방 데이터
              </button>
              <button class="section-button"
                      @click="toggleSection('exercise', 'http://localhost:8000/api6/create_exercise/')">운동 데이터
              </button>
              <button class="section-button"
                      @click="toggleSection('treatment', 'http://localhost:8000/api5/create_treatment/')">치료 데이터
              </button>
          <div class="writedata-div">
            <template>
              <!-- Your existing HTML template goes here -->
              <div id="diagnosis-section" class="section-form">
                <h2>진료 데이터 입력 폼</h2>
                <form>
                  <label for="diagnosis-input">진료 내용:</label>
                  <input type="text" id="diagnosis-input" name="diagnosis-input">
                </form>
                <button class="save-button" @click="saveData('diagnosis')">저장</button>
              </div>

              <div id="prescription-section" class="section-form">
                <h2>처방 데이터 입력 폼</h2>
                <form>
                  <label for="prescription-input">처방 내용:</label>
                  <input type="text" id="prescription-input" name="prescription-input">
                </form>
                <button class="save-button" @click="saveData('prescription')">저장</button>
              </div>

              <div id="exercise-section" class="section-form">
                <h2>운동 데이터 입력 폼</h2>
                <form>
                  <label for="exercise-input">운동 내용:</label>
                  <input type="text" id="exercise-input" name="exercise-input">
                </form>
                <button class="save-button" @click="saveData('exercise')">저장</button>
              </div>

              <div id="treatment-section" class="section-form">
                <h2>치료 데이터 입력 폼</h2>
                <form>
                  <label for="treatment-input">치료 내용:</label>
                  <input type="text" id="treatment-input" name="treatment-input">
                </form>
                <button class="save-button" @click="saveData('treatment')">저장</button>
              </div>
              <div class="grid-item-6">
                <p id="title2">AI 진단</p>
              </div>

            </template>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      trtcont: false,
      patlist: [{
        "id": 23051116,
        "name": "배효민",
        "sex": "남",
        "birth": 891012
      }],
      trtlist: [{
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }, {
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }, {
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }, {
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }, {
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }, {
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }, {
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }, {
        "id": 23108978,
        "date": 231024,
        "type": "운동",
        "manager": "홍인정"
      }]
    };
  },
  methods: {
    submitForm() {
      console.log('검색: ' + this.searchPatients);
    },
    rowClickPat(pat) {
      alert(`환자 ID: ${pat.id}\n성함: ${pat.name}\n성별: ${pat.sex}\n생년월일: ${pat.birth}`);
    },
    rowClickTrt(trt) {
      alert(`치료 ID: ${trt.id}\n날짜: ${trt.date}\n종류: ${trt.type}\n담당직원: ${trt.manager}`);
    },
    openPopup(url) {
      var popup = window.open('', '_blank', 'width=600,height=400,scrollbars=yes,resizable=yes');
      popup.location.href = url;
    },

    async toggleSection(section, apiUrl) {
      const sections = document.querySelectorAll('.section-form');
      sections.forEach((sec) => {
        sec.style.display = 'none';
      });

      const selectedSection = document.getElementById(`${section}-section`);
      if (selectedSection) {
        selectedSection.style.display = 'block';
        document.querySelector('.save-button').style.display = 'block';

        // API 호출
        const response = await fetch(apiUrl);
        const data = await response.text();
        selectedSection.innerHTML = data;
      }
    },

    saveData(section) {
      const inputData = document.getElementById(`${section}-input`).value;
      alert(`저장되었습니다: ${inputData}`);
    }
  }
};
</script>


<style scoped>
.content {
  flex: 1;
  padding: 24px;
  background: #f0f0f0;
  min-height: 100vh;
}

.grid-frame {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  gap: 12px;
}

.invisible {
  visibility: hidden;
}

.grid-item-2 {
  background: #fff;
  padding: 24px;
  border: 1px solid #ddd;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 300px;
  height: 250px;
}

.grid-item-1 {
  background: #fff;
  padding: 24px;
  border: 1px solid #ddd;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 300px;
  height: 400px;
}

.grid-item-3 {
  background: #fff;
  padding: 24px;
  border: 1px solid #ddd;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 300px;
  height: 58px;
}

.grid-item-4 {
  background: #fff;
  padding: 24px;
  border: 1px solid #ddd;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 300px;
  height: 280px;
}

.grid-item-5 {
  background: #fff;
  padding: 24px;
  border: 1px solid #ddd;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 300px;
  height: 180px;
}

.grid-item-6 {
  position: absolute;
  top: 83%; /* 1/3 position */
  left: 50%; /* Center horizontally */
  transform: translate(-50%, -50%);
  background: #333540;
  padding: 24px;
  border: 1px solid #ddd;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 400px;
  height: 180px;
}

.grid-item-7 {
  position: relative;
  background: #fff;
  padding: 24px;
  border: 1px solid #ddd;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 448px;
  height: 700px;
}

p {
  padding-left: 36px;
}

#x {
  position: relative;
  border-color: white;
  background: white;
  color: red;
  top: -43px;
  right: -161px;
  margin: 0;
}

#title {
  position: relative;
  border-color: white;
  background: #bdbdbd;
  color: black;
  top: -24px;
  left: -24px;
  margin: 0;
  padding: 0;
  width: 50%;
}

#title2 {
  position: relative;
  border-color: white;
  background: #e1bee7;
  color: black;
  top: -24px;
  left: -24px;
  margin: 0;
  padding: 0;
  width: 33%;
}

#space {
  margin-top: -16px;
}

#patlist tr:hover {
  background-color: #e0e0e0;
}

#trtlist tr:hover {
  background-color: #e0e0e0;
}

.patient-list-div {
  align-items: center;
  height: 120px;
  overflow: auto;
}

.patient-list {
  border-collapse: collapse;
  width: 100%;
}

.patient-list tr {
  border-bottom: 1px solid #9e9e9e; /* Add white lines between rows */
}

.patient-list th {
  padding: 2px;
  text-align: left;
  background-color: #eeeeee;
}

.patient-list td {
  padding: 2px;
  text-align: left;
}

.patient-info-div {
  align-items: center;
  height: 96px;
}

.patient-info {
  border-collapse: collapse;
  width: 100%;
}

.patient-info tr {
  border-bottom: 1px solid #fff; /* Add white lines between rows */
}

.patient-info th {
  padding-right: 12px;
  text-align: right;
}

.patient-info td {
  padding: 0;
  text-align: left;
}

.treatment-list-div {
  align-items: center;
  height: 120px;
  overflow: auto;
}

.treatment-list {
  border-collapse: collapse;
  width: 100%;
}

.treatment-list tr {
  border-bottom: 1px solid #9e9e9e; /* Add white lines between rows */
}

.treatment-list th {
  padding: 2px;
  text-align: left;
  background-color: #eeeeee;
}

.treatment-list td {
  padding: 2px;
  text-align: left;
}

.treatdata-div {
  align-items: center;
  margin-top: -32px;
}

.treatdata {
  border-collapse: collapse;
  width: 100%;
}

.treatdata textarea {
  width: 100%;
  height: 4em;
  resize: none;
}

.treatdata tr {
  border-bottom: 1px solid #fff; /* Add white lines between rows */
}

.treatdata th {
  padding: 0 12px 12px 0;
  text-align: right;
  vertical-align: top;
}

.treatdata td {
  padding: 0 0 12px 0;
  text-align: left;
}

.writedata-div {
  align-items: center;
  background-color: #f5f5f5; /* 옅은 회색 배경색 */
  /* 다른 스타일 속성들을 필요에 따라 추가할 수 있습니다 */
  padding: 10px;
}


.writedata {
  border-collapse: collapse;
  width: 100%;
}

.writedata textarea {
  width: 100%;
  height: 5.4em;
  resize: none;
}

.writedata tr {
  border-bottom: 1px solid #fff; /* Add white lines between rows */
}

.writedata th {
  padding: 0 12px 12px 0;
  text-align: right;
  vertical-align: top;
}

.writedata td {
  padding: 0 0 12px 0;
  text-align: left;
}

.search-button {
  margin: 0 0 0 8px;
}

.treat-button {
  margin: 0 8px 0 8px;
  height: 32px;
}

.write-button {
  margin: 0 8px 0 8px;
  width: 80px;
  height: 32px;
}

.table-hover tbody tr:hover td, .table-hover tbody tr:hover th {
  background-color: #e0e0e0;
}

.section-button {
  padding: 10px;
  margin: 5px;
  cursor: pointer;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
}

.section-form {
  display: none;
  padding: 15px; /* Adjust padding as needed */
  margin-bottom: 20px; /* Add margin between sections */
}

.save-button {
  display: none;
  padding: 10px;
  margin-top: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

</style>
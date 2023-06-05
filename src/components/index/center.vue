<template>
  <div class="all">
    <div class="choose">
      <ul>
        <li>{{ $t("m.Classificationofworks") }}</li>
        <li>{{ $t("m.ranking") }}</li>
        <li>{{ $t("m.Endofbook") }}</li>
        <li>{{ $t("m.free") }}</li>
        <li>{{ $t("m.WritersSection") }}</li>
        <li>{{ $t("m.Recommendedzone") }}</li>
      </ul>
    </div>
    <div class="center">
      <el-carousel :interval="6000" arrow="always" height="50vh">
        <el-carousel-item v-for="(item, index) in imglist" :key="index">
          <h3><img :src="item" /></h3>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="reconmend">
      <h2>{{ $t("m.BookRecommendationList") }}</h2>
      <div class="content">
        <div class="week" v-if="this.books[0]">
          <ul>
            {{
              $t("m.Recommendedweekly")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                @click="intro1"
                :src="this.books[0][4]"
                height="200px"
                width="200px"
                alt=""
              />
            </li>
            <li>
              {{ $t("m.Novelid") }}:
              <span>{{ books[0][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[0][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[0][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}:
              <span>
                {{ books[0][3] }}
              </span>
            </li>
          </div>
        </div>
        <div class="week" v-if="this.books[1]">
          <ul>
            {{
              $t("m.Recommendedweekly")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                @click="intro2"
                :src="this.books[1][4]"
                height="200px"
                width="200px"
                alt=""
              />
            </li>
            <li>
              {{ $t("m.Novelid") }} :<span>{{ books[1][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[1][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[1][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}:
              <span>
                {{ books[1][3] }}
              </span>
            </li>
          </div>
        </div>
        <div class="week" v-if="this.books[2]">
          <ul>
            {{
              $t("m.Editorsrecommendation")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                v-if="books[2][4]"
                :src="this.books[2][4]"
                height="200px"
                width="200px"
                alt=""
                @click="intro3"
              />
            </li>
            <li>
              {{ $t("m.Novelid") }}:
              <span>{{ books[2][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[2][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[2][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}:
              <span>
                {{ books[2][3] }}
              </span>
            </li>
          </div>
        </div>
        <div class="week" v-if="this.books[3]">
          <ul>
            {{
              $t("m.Latestrecommendation")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                v-if="books[3][4]"
                :src="this.books[3][4]"
                height="200px"
                width="200px"
                alt=""
                @click="intro4"
              />
            </li>
            <li>
              {{ $t("m.Novelid") }}:
              <span>{{ books[3][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[3][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[3][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}
              <span>
                {{ books[3][3] }}
              </span>
            </li>
          </div>
        </div>
      </div>
    </div>
    <div class="share">
      <h2>{{ $t("m.Beautifulsentenceappreciation") }}</h2>
      <h4>
        {{ $t("m.sentence") }}
      </h4>
      <div class="box"><img src="@/assets/img/f.png" /></div>
    </div>
    <div id="hotbook">
      <h2 class="title">{{ $t("m.Popularbooks") }}</h2>
      <div id="book">
        <ul v-for="(item, index) in hotbooks" :key="index">
          <div class="img" v-if="item[4]">
            <img :src="item[4]" alt="" @click="watch(item[0])" />
          </div>
          <div class="right">
            <li class="name">{{ item[1] }}</li>
            <li class="bintro">{{ item[3] }}</li>

            <li class="el-icon-user">
              <span class="author">{{ item[2] }}</span>
              <span class="sort">{{ item[5] }}</span>
            </li>
          </div>
        </ul>
      </div>
    </div>
    <div class="readershare">
      <h2 class="title">读者分享</h2>
      <div class="dan">
        <div class="track">
          <div class="child child-1" v-if="barrages[0]">
            {{ barrages[0]["user_name"] }}:{{ barrages[0]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-2" v-if="barrages[1]">
            {{ barrages[1]["user_name"] }}:{{ barrages[1]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-3" v-if="barrages[2]">
            {{ barrages[2]["user_name"] }}:{{ barrages[2]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-4" v-if="barrages[3]">
            {{ barrages[3]["user_name"] }}:{{ barrages[3]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-5" v-if="barrages[4]">
            {{ barrages[4]["user_name"] }}:{{ barrages[4]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-6" v-if="barrages[5]">
            {{ barrages[5]["user_name"] }}:{{ barrages[5]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-7" v-if="barrages[6]">
            {{ barrages[6]["user_name"] }}:{{ barrages[6]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-8" v-if="barrages[7]">
            {{ barrages[7]["user_name"] }}:{{ barrages[7]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-9" v-if="barrages[8]">
            {{ barrages[8]["user_name"] }}:{{ barrages[8]["barrage"] }}
          </div>
        </div>
        <div class="track">
          <div class="child child-10" v-if="barrages[9]">
            {{ barrages[9]["user_name"] }}:{{ barrages[9]["barrage"] }}
          </div>
        </div>
      </div>
      <div class="bottom">
        <el-input
          type="text"
          :rows="2"
          placeholder="请输入弹幕内容"
          v-model="textarea"
          class="send"
        >
        </el-input>
        <el-button class="submit" @click="barrige">提交</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import request from "@/request";
import qs from "qs";
export default {
  name: "center",
  data() {
    return {
      input: "",
      imglist: [],
      books: [[]],
      hotbooks: [[]],
      flag: 1,
      textarea: "",
      barrages: [{}],
    };
  },
  methods: {
    intro1() {
      sessionStorage.setItem("bookid", this.books[0][0]);
      this.$router.push("/introbook");
    },
    intro2() {
      sessionStorage.setItem("bookid", this.books[1][0]);
      this.$router.push("/introbook");
    },
    intro3() {
      sessionStorage.setItem("bookid", this.books[2][0]);
      this.$router.push("/introbook");
    },
    intro4() {
      sessionStorage.setItem("bookid", this.books[3][0]);
      this.$router.push("/introbook");
    },
    watch(id) {
      sessionStorage.setItem("bookid", id);
      this.$router.push("/introbook");
    },
    barrige() {
      var data = {
        barrage: this.textarea,
      };
      request.post("/api/user/push_barrage", qs.stringify(data)).then((res) => {
        if (res.data.code == 200) {
          alert("发送成功");
          this.textarea = "";
          request.get("/api/user/get_barrage").then((res) => {
            console.log(res.data);
            this.barrages = res.data.barrages;
          });
        } else {
          alert("请登录后再发送弹幕哦~");
        }
      });
    },
  },

  mounted() {
    request.get("/api").then((res) => {
      this.hotbooks = res.data.hot_books;
      this.books = res.data.books;
      this.imglist = res.data.lun;
    }); //给首页发请求拿数据
    request.get("/api/user/get_barrage").then((res) => {
      this.barrages = res.data.barrages;
    });
  },
};
</script>
<style scoped>
.all {
  width: 90vw;
}

.choose {
  display: flex;
  justify-content: center;
  margin-top: 5vh;
}
.choose ul li {
  display: inline-block;
  margin-left: 100px;
  font-size: 15px;
}
.choose ul li:hover {
  cursor: pointer;
  color: red;
}
.center {
  margin-left: 10vw;
  width: 80vw;
  margin-top: 2vh;
}
.reconmend {
  margin-left: 5vw;
  margin-top: 10px;
  border-top: 1px solid black;
  margin-bottom: 20px;
  height: 70vh;
}

.box {
  height: 200px;
  width: 200px;
  overflow: hidden;
}

.reconmend img {
  transition: 0.6s;
  cursor: pointer;
}

.reconmend img:hover {
  transform: scale(1.2, 1.2);
}
.content {
  display: flex;
  justify-content: space-around;
  margin-top: 2vh;
}
.week {
  width: 20vw;
  margin-left: 50px;
}
.week li {
  margin-top: 10px;
  font-size: 15px;
}
.intro {
  height: 200px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 11;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
}
.share {
  margin-left: 5vw;
  border-top: 1px solid black;
  display: flex;
  justify-content: space-around;
  margin-bottom: 10px;
  padding-top: 10px;
}
.share img:hover {
  transform: scale(1.2, 1.2);
}
.share h4 {
  margin-top: 100px;
}
#hotbook {
  margin-left: 5vw;
  border-top: 1px solid black;
  padding-top: 10px;
  border-bottom: 1px solid black;
}
.title {
  margin-bottom: 10px;
}
#hotbook img:hover {
  transform: scale(1.2, 1.2);
}
#book {
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  flex-wrap: wrap;
}
#book img {
  width: 100px;
  height: 140px;
}
#book ul {
  margin-bottom: 20px;
  /* border-bottom: 1px solid black; */
}
.right {
  float: left;
  margin-left: 20px;
  width: 250px;
  position: relative;
}
.right li {
  margin-bottom: 10px;
}
.name {
  font-size: 18px;
  margin-top: 10px;
}
.bintro {
  font-size: 15px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  text-overflow: ellipsis;
}
.author {
  font-size: 10px;
  margin-left: 5px;
}
.sort {
  border: 1px solid black;
  display: inline-block;
  font-size: 15px;
  position: absolute;
  right: 10px;
  padding: 5px;
}

.img {
  height: 140px;
  width: 100px;
  overflow: hidden;
  transition: 0.6s;
  cursor: pointer;
  float: left;
}
.readershare {
  width: 85vw;
  margin: 10px auto 0;
  overflow: hidden;
  margin-left: 5vw;
  height: 400px;
  padding-bottom: 20px;
}
.dan {
  background-color: rgb(247, 247, 243);
}
.track {
  height: 20px;
  line-height: 40px;
  margin-bottom: 5px;
}

.child {
  line-height: 20px;
  margin-bottom: 10px;
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.1);
}

.child-1 {
  color: brown;
  text-shadow: 2px 2px 3px rgb(248, 81, 20);
  transform: translateX(1000px);
  animation: scrollTo linear 8s infinite;
}

.child-2 {
  color: rgb(127, 197, 35);
  text-shadow: 2px 2px 3px rgb(173, 255, 80);
  transform: translateX(1050px);
  animation: scrollTo linear 10s infinite;
}
.child-3 {
  color: coral;
  text-shadow: 2px 2px 3px coral;
  transform: translateX(800px);
  animation: scrollTo linear 7s infinite;
}
.child-4 {
  color: rgb(76, 140, 218);
  text-shadow: 2px 2px 3px rgb(76, 140, 218);
  transform: translateX(900px);
  animation: scrollTo linear 6s infinite;
}
.child-5 {
  color: rgb(234, 30, 118);
  text-shadow: 2px 2px 3px rgb(235, 84, 29);
  transform: translateX(1100px);
  animation: scrollTo linear 12s infinite;
}
.child-6 {
  color: rgb(144, 20, 169);
  text-shadow: 2px 2px 3px rgb(161, 27, 179);
  transform: translateX(1050px);
  animation: scrollTo linear 15s infinite;
}
.child-7 {
  color: rgb(47, 15, 145);
  text-shadow: 2px 2px 3px rgb(63, 29, 217);
  transform: translateX(1200px);
  animation: scrollTo linear 11s infinite;
}
.child-10 {
  color: rgb(107, 161, 119);
  text-shadow: 2px 2px 3px rgb(30, 190, 16);
  transform: translateX(1200px);
  animation: scrollTo linear 8s infinite;
}
.child-8 {
  color: rgb(219, 12, 12);
  text-shadow: 2px 2px 3px rgb(99, 10, 23);
  transform: translateX(1200px);
  animation: scrollTo linear 13s infinite;
}
.child-9 {
  color: rgb(128, 126, 134);
  text-shadow: 2px 2px 3px rgb(176, 19, 92);
  transform: translateX(1200px);
  animation: scrollTo linear 12s infinite;
}
@keyframes scrollTo {
  to {
    transform: translateX(-100px);
  }
}
.send {
  width: 400px;
  margin-top: 10px;
}
.submit {
  width: 100px;
  margin: auto;
  margin-left: 10px;
}
.bottom {
  margin-top: 20px;
  text-align: center;
}
</style>
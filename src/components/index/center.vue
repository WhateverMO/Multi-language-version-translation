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
        <div class="week">
          <ul>
            {{
              $t("m.Recommendedweekly")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                @click="intro1"
                :src="books[0][4]"
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
        <div class="week">
          <ul>
            {{
              $t("m.Recommendedweekly")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                @click="intro2"
                :src="books[1][4]"
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

        <div class="week">
          <ul>
            {{
              $t("m.Editorsrecommendation")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                :src="books[2][4]"
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
        <div class="week">
          <ul>
            {{
              $t("m.Latestrecommendation")
            }}
          </ul>
          <div class="onebook">
            <li class="box">
              <img
                :src="books[3][4]"
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
          <div class="img"><img :src="item[4]" alt="" /></div>
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
          <div class="child child-1">我是弹幕</div>
        </div>
        <div class="track">
          <div class="child child-2">我是弹幕</div>
        </div>
        <div class="track">
          <div class="child child-3">我是弹幕</div>
        </div>
        <div class="track">
          <div class="child child-4">我是弹幕</div>
        </div>
        <div class="track">
          <div class="child child-5">我是弹幕</div>
        </div>
        <div class="track">
          <div class="child child-6">我是弹幕</div>
        </div>
        <div class="track">
          <div class="child child-7">我是弹幕</div>
        </div>
      </div>
      <div class="bottom">
        <el-input
          type="textarea"
          :rows="2"
          placeholder="请输入弹幕内容"
          v-model="textarea"
          class="send"
        >
        </el-input>
        <el-button class="submit">提交</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import request from "@/request";
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
    };
  },
  methods: {
    intro1() {
      request
        .get("/api/user/read_book/introduce/" + this.books[0][0])
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("introduce", res.data);
            this.$bus.$emit("bookid", this.books[0][0]);
          }, 1000);
          this.$router.push("/introbook");
        }); //给首页发请求拿数据;
    },
    intro2() {
      request
        .get("/api/user/read_book/introduce/" + this.books[1][0])
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("introduce", res.data);
            this.$bus.$emit("bookid", this.books[1][0]);
          }, 1000);
          this.$router.push("/introbook");
        }); //给首页发请求拿数据
    },
    intro3() {
      axios
        .get("/api/user/read_book/introduce/" + this.books[2][0])
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("introduce", res.data);
            this.$bus.$emit("bookid", this.books[2][0]);
          }, 1000);
          this.$router.push("/introbook");
        }); //给首页发请求拿数据
    },
    intro4() {
      axios
        .get("/api/user/read_book/introduce/" + this.books[3][0])
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("introduce", res.data);
            this.$bus.$emit("bookid", this.books[3][0]);
          }, 1000);
          this.$router.push("/introbook");
        }); //给首页发请求拿数据
    },
  },

  mounted() {
    request.get("/api").then((res) => {
      this.hotbooks = res.data.hot_books;
      this.books = res.data.books;
      this.lun = res.data.lun;
    }); //给首页发请求拿数据
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
  height: 500px;
  padding-bottom: 20px;
}
.dan {
  background-color: rgb(244, 240, 235);
}
.track {
  height: 40px;
  line-height: 40px;
  margin-bottom: 5px;
}

.child {
  width: 80px;
  line-height: 20px;
  margin-bottom: 10px;
  text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.1);
}

.child-1 {
  color: brown;
  text-shadow: 2px 2px 3px rgb(248, 81, 20);
  transform: translateX(1000px);
  animation: scrollTo linear 4s infinite;
}

.child-2 {
  color: rgb(127, 197, 35);
  text-shadow: 2px 2px 3px rgb(173, 255, 80);
  transform: translateX(1050px);
  animation: scrollTo linear 7s infinite;
}
.child-3 {
  color: coral;
  text-shadow: 2px 2px 3px coral;
  transform: translateX(800px);
  animation: scrollTo linear 5s infinite;
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
  animation: scrollTo linear 4s infinite;
}
.child-6 {
  color: rgb(144, 20, 169);
  text-shadow: 2px 2px 3px rgb(161, 27, 179);
  transform: translateX(1050px);
  animation: scrollTo linear 4s infinite;
}
.child-7 {
  color: rgb(47, 15, 145);
  text-shadow: 2px 2px 3px rgb(30, 5, 143);
  transform: translateX(1200px);
  animation: scrollTo linear 5s infinite;
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
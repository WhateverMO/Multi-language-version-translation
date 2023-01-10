<template>
  <div class="all">
    <div>
      <el-input v-model="input" placeholder="请输入内容"></el-input>
      <el-button type="primary" plain @click="search">搜索</el-button>
    </div>
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
        <el-carousel-item v-for="item in imglist" :key="item.id">
          <h3><img :src="item.image" /></h3>
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
                src="@/assets/book/book_8.jpg"
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
              <span>{{ books[0][1] }}</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[0][2] }}</span>
            </li>
            <li>
              {{ $t("m.Briefintroduction") }}:
              <h6>
                {{ books[0][3] }}
              </h6>
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
                src="@/assets/book/book_1.jpg"
                height="200px"
                width="200px"
                alt=""
              />
            </li>
            <li>{{ $t("m.Novelid") }} :{{ books[1][0] }}</li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>{{ books[1][1] }}</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[1][2] }}</span>
            </li>
            <li>
              {{ $t("m.Briefintroduction") }}:
              <h6>
                {{ books[1][3] }}
              </h6>
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
                src="@/assets/book/book_5.jpg"
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
              <span>{{ books[2][1] }}</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[2][2] }}</span>
            </li>
            <li>
              {{ $t("m.Briefintroduction") }}:
              <h6>
                {{ books[2][3] }}
              </h6>
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
                src="@/assets/book/book_4.jpg"
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
              <span>{{ books[3][1] }}</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[3][2] }}</span>
            </li>
            <li>
              {{ $t("m.Briefintroduction") }}
              <h6>
                {{ books[3][3] }}
              </h6>
            </li>
          </div>
        </div>
      </div>
    </div>
    <div class="share">
      <h1>{{ $t("m.Beautifulsentenceappreciation") }}</h1>
      <h3>
        {{ $t("m.sentence") }}
      </h3>
      <img src="@/assets/img/f.png" />
    </div>
    <div id="hotbook">
      <h1>{{ $t("m.Popularbooks") }}</h1>
      <div id="book">
        <li><img src="@/assets/book/book_1.jpg" alt="" /></li>
        <li><img src="@/assets/book/book_2.jpg" alt="" /></li>
        <li><img src="@/assets/book/book_3.jpg" alt="" /></li>
        <li><img src="@/assets/book/book_4.jpg" alt="" /></li>
        <li><img src="@/assets/book/book_5.jpg" alt="" /></li>
        <li><img src="@/assets/book/book_6.jpg" alt="" /></li>
        <li><img src="@/assets/book/book_7.jpg" alt="" /></li>
        <li><img src="@/assets/book/book_8.jpg" alt="" /></li>
      </div>
    </div>
    <div id="readingfeel">
      <h1>{{ $t("m.Readersexperience") }}</h1>
      <span
        ><h3>
          {{ $t("m.readcontent") }}
          <br /></h3
      ></span>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "center",
  data() {
    return {
      input: "",
      imglist: [
        { id: 0, image: require("../../assets/img/lun1.jpg") },
        { id: 1, image: require("../../assets/img/lun2.jpg") },
        { id: 3, image: require("../../assets/img/lun4.jpg") },
      ],
      books: [[]],
      flag: 1,
    };
  },
  methods: {
    intro1() {
      axios
        .get(
          "http://localhost:5000/api/user/read_book/introduce/" +
            this.books[0][0]
        )
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("introduce", res.data);
            this.$bus.$emit("bookid", this.books[0][0]);
          }, 1000);
          this.$router.push("/introbook");
        }); //给首页发请求拿数据
    },
    intro2() {
      axios
        .get(
          "http://localhost:5000/api/user/read_book/introduce/" +
            this.books[1][0]
        )
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
        .get(
          "http://localhost:5000/api/user/read_book/introduce/" +
            this.books[2][0]
        )
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
        .get(
          "http://localhost:5000/api/user/read_book/introduce/" +
            this.books[3][0]
        )
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("introduce", res.data);
            this.$bus.$emit("bookid", this.books[3][0]);
          }, 1000);
          this.$router.push("/introbook");
        }); //给首页发请求拿数据
    },
    search() {
      axios
        .get("http://localhost:5000/api/user/book/search/" + this.input)
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("introduce", res.data);
            this.$bus.$emit("bookid", this.input);
          }, 1000);
          this.$router.push("/introbook");
        }); //给首页发请求拿数据
    },
  },

  mounted() {
    axios.get("http://localhost:5000/api").then((res) => {
      this.$bus.$emit("books", res.data.books);
    }); //给首页发请求拿数据
    this.$bus.$on("books", (books) => {
      this.books = books;
    });
  },
};
</script>
<style scoped>
.all {
  height: 335vh;
  width: 90vw;
}
.el-input {
  width: 300px;
  margin-left: 500px;
  margin-top: 5px;
}
.el-button {
  width: 100px;
  margin: auto;
}
.choose {
  display: flex;
  justify-content: center;
  margin-top: 1%;
}
.choose ul li {
  display: inline-block;
  margin-left: 100px;
}
.choose ul li:hover {
  cursor: pointer;
  color: red;
}
.center {
  margin-left: 10vw;
  width: 80vw;
  margin-top: 5vh;
}
.reconmend {
  font-size: larger;
  margin-left: 100px;
  margin-top: 10px;
  height: 100vh;
  border-top: 1px solid black;
  overflow: hidden;
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
}
.week {
  width: 1000px;
  margin-left: 50px;
}
.week li {
  margin-top: 10px;
}
.share {
  height: 30vh;
  margin-left: 5px;
  border-top: 1px solid black;
  display: flex;
  justify-content: space-around;
}
.share img:hover {
  transform: scale(1.2, 1.2);
}
.share h3 {
  margin-top: 100px;
}
#hotbook {
  margin-left: 50px;
  margin-right: 10px;
  border-top: 1px solid;
  height: 100vh;
  overflow: hidden;
}
#hotbook h1 {
  margin-bottom: 30px;
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
  width: 200px;
  height: 250px;
}
#book li {
  height: 250px;
  width: 200px;
  overflow: hidden;
  margin-left: 80px;
  margin-bottom: 20px;
  transition: 0.6s;
  cursor: pointer;
}
#readingfeel {
  margin-left: 100px;
  border-top: 1px solid;
  height: 30vh;
  border-bottom: 1px solid;
}
</style>
<template>
  <div>
    <div id="searchbook">
      <el-input
        v-model="input"
        placeholder="请输入你要翻译图书的名字"
      ></el-input>
      <el-button type="primary" plain>搜索</el-button>
    </div>
    <div id="translatebook">
      <div id="kind">
        <ul>
          <li><a href="#">玄幻</a></li>
          <li><a href="#">奇幻</a></li>
        </ul>
        <ul>
          <li><a href="#">武侠</a></li>
          <li><a href="#">仙侠</a></li>
        </ul>
        <ul>
          <li><a href="#">都市</a></li>
          <li><a href="#">现实</a></li>
        </ul>
        <ul>
          <li><a href="#">军事</a></li>
          <li><a href="#">历史</a></li>
        </ul>
        <ul>
          <li><a href="#">游戏</a></li>
          <li><a href="#">体育</a></li>
        </ul>
        <ul>
          <li><a href="#">科幻</a></li>
          <li><a href="#">悬疑</a></li>
        </ul>
      </div>
      <div class="book">
        <div class="week" v-if="this.books[0]">
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
        <div class="week" v-if="this.books[4]">
          <div class="onebook">
            <li class="box">
              <img
                @click="intro5"
                :src="this.books[4][4]"
                height="200px"
                width="200px"
                alt=""
              />
            </li>
            <li>
              {{ $t("m.Novelid") }}:
              <span>{{ books[4][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[4][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[4][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}:
              <span>
                {{ books[4][3] }}
              </span>
            </li>
          </div>
        </div>
        <div class="week" v-if="this.books[5]">
          <div class="onebook">
            <li class="box">
              <img
                @click="intro6"
                :src="this.books[5][4]"
                height="200px"
                width="200px"
                alt=""
              />
            </li>
            <li>
              {{ $t("m.Novelid") }} :<span>{{ books[5][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[5][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[5][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}:
              <span>
                {{ books[5][3] }}
              </span>
            </li>
          </div>
        </div>
        <div class="week" v-if="this.books[6]">
          <div class="onebook">
            <li class="box">
              <img
                v-if="books[6][4]"
                :src="this.books[6][4]"
                height="200px"
                width="200px"
                alt=""
                @click="intro7"
              />
            </li>
            <li>
              {{ $t("m.Novelid") }}:
              <span>{{ books[6][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[6][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[6][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}:
              <span>
                {{ books[6][3] }}
              </span>
            </li>
          </div>
        </div>
        <div class="week" v-if="this.books[7]">
          <div class="onebook">
            <li class="box">
              <img
                v-if="books[7][4]"
                :src="this.books[7][4]"
                height="200px"
                width="200px"
                alt=""
                @click="intro8"
              />
            </li>
            <li>
              {{ $t("m.Novelid") }}:
              <span>{{ books[7][0] }}</span>
            </li>
            <li>
              {{ $t("m.Novelname") }}:
              <span>《{{ books[7][1] }}》</span>
            </li>
            <li>
              {{ $t("m.author") }}:
              <span>{{ books[7][2] }}</span>
            </li>
            <li class="intro">
              {{ $t("m.Briefintroduction") }}
              <span>
                {{ books[7][3] }}
              </span>
            </li>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import request from "@/request";
export default {
  data() {
    return {
      bookid: "",
      input: "",
      books: [[]],
    };
  },
  methods: {
    intro1() {
      sessionStorage.setItem("transbook", this.books[0][0]);
      this.$router.push("/compare");
    },
    intro2() {
      sessionStorage.setItem("transbook", this.books[1][0]);
      this.$router.push("/compare");
    },
    intro3() {
      sessionStorage.setItem("transbook", this.books[2][0]);
      this.$router.push("/compare");
    },
    intro4() {
      sessionStorage.setItem("transbook", this.books[3][0]);
      this.$router.push("/compare");
    },
    intro5() {
      sessionStorage.setItem("transbook", this.books[4][0]);
      this.$router.push("/compare");
    },
    intro6() {
      sessionStorage.setItem("transbook", this.books[5][0]);
      this.$router.push("/compare");
    },
    intro7() {
      sessionStorage.setItem("transbook", this.books[6][0]);
      this.$router.push("/compare");
    },
    intro8() {
      sessionStorage.setItem("transbook", this.books[7][0]);
      this.$router.push("/compare");
    },
  },
  mounted() {
    request.get("/api/author/get_all_book").then((res) => {
      this.books = res.data.books;
    });
  },
};
</script>

<style scoped>
#searchbook {
  margin-left: 40vw;
  margin-top: 5vh;
}
#kind ul {
  display: inline-block;
  margin-left: 10vw;
}
#kind ul li {
  margin-bottom: 10vh;
}
#kind {
  margin-right: 10vw;
  margin-left: 10vw;
  margin-top: 10vh;
}

.box {
  height: 200px;
  width: 200px;
  overflow: hidden;
}

.week img {
  transition: 0.6s;
  cursor: pointer;
}

.week img:hover {
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
.book {
  margin-left: 5vw;
  margin-top: 2vh;
  display: flex;
  flex-wrap: wrap;
}
</style>
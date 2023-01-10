<template>
  <div>
    <div id="head">
      <div id="headl"><img src="@/assets/book/book_13.jpg" /></div>
      <div id="headr">
        <ul>
          <li>
            书名:<span>{{ bookname }}</span>
          </li>
          <li>
            作者:<span>{{ bookauthor }}</span>
          </li>
          <li>
            简介:<span>{{ bookintro }}</span>
          </li>
          <li>
            <el-button type="primary" plain @click="read">点击阅读</el-button>
            <el-button type="primary" plain>加入书架</el-button>
            <el-button type="primary" plain>投票互动</el-button>
          </li>
        </ul>
      </div>
    </div>
    <!-- 第三部分 -->
    <div id="back">
      <!-- 左边 -->
      <span id="l">
        <h4>
          <a href="#">作品信息</a>
          <a href="#">目录</a>
        </h4>
        <div id="newcontent">
          <span id="newl">
            <li v-for="(item, index) in list" :key="index">
              <h3>{{ item }}</h3>
            </li>
          </span>
        </div>
        <div id="fan">
          <div>粉丝互动</div>
          <el-table :data="tableData" border style="width: 100%">
            <el-table-column prop="user" label="用户" width="180">
            </el-table-column>
            <el-table-column prop="comment" label="评论" width="600">
            </el-table-column>
          </el-table>
          <el-input
            type="textarea"
            :rows="2"
            placeholder="发表你的评论"
            v-model="textarea"
            class="sendtext"
          >
          </el-input>
          <el-button type="primary" plain>点击发送</el-button>
        </div>
      </span>
      <!-- 右边 -->
      <span id="r">
        <div id="introduce">
          <h4>作者昵称</h4>
          <div class="name">
            <span> 作品总数 </span>
            <span> 累计字数 </span>
            <span> 创作天数 </span>
          </div>
          <div class="number">
            <span> 3 </span>
            <span> 4 </span>
            <span> 100 </span>
          </div>
          <div id="masterpiece">
            <h4 style="display: inline">其他作品</h4>
            <h4 style="display: inline; padding-left: 100px">更多</h4>
            <img src="@/assets/book/book_13.jpg" />
            <h5>
              李莫愁想要杀了陆展元，魔童哪吒想要<br />得到百姓认同，葫芦娃想要救出爷爷，<br />绯红女巫想要干掉灭霸，后羿想要射落十
            </h5>
            <el-button type="primary" plain>加入书架</el-button>
          </div>
          <div id="weekc">
            <ul>
              <h4>本周强推</h4>
              <li>
                <a href="">[古今传奇]</a>
              </li>
              <li>
                <a href="">[侦探推理]</a>
              </li>
              <li>
                <a href="">[诡秘悬疑]</a>
              </li>
              <li>
                <a href="">[奇妙时刻]</a>
              </li>
              <li>
                <a href="">[古今传奇]</a>
              </li>
              <li>
                <a href="">[侦探推理]</a>
              </li>
              <li>
                <a href="">[诡秘悬疑]</a>
              </li>
              <li>
                <a href="">[奇妙时刻]</a>
              </li>
            </ul>
          </div>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  data() {
    return {
      tableData: [
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
        {
          user: "猫咪酱",
          comment: "作者写的好好看啊期待下一次更新",
        },
      ],
      textarea: "",
      bookname: "",
      bookauthor: "",
      list: "[]",
      bookintro: "",
      bookid: "",
    };
  },
  methods: {
    read() {
      let date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      let h = date.getHours();
      let m = date.getMinutes();
      let s = date.getSeconds();
      let time =
        year +
        "年" +
        month +
        "月" +
        day +
        "日" +
        h +
        "时" +
        m +
        "分" +
        s +
        "秒";
      var data = {
        user_id: sessionStorage.getItem("id"),
        time: time,
      };
      axios
        .post(
          "http://localhost:5000/api/user/read_book/start_read/" +
            this.bookid +
            "/" +
            1,
          qs.stringify(data)
        )
        .then((res) => {
          setTimeout(() => {
            this.$bus.$emit("read", res.data);
          }, 1000);
          this.$router.push("/readbook");
        });
    },
  },
  mounted() {
    this.$bus.$on("introduce", (intro) => {
      this.bookauthor = intro.author_name;
      this.bookintro = intro.book_describe;
      this.bookname = intro.book_name;
      this.list = intro.content_list;
    });
    this.$bus.$on("bookid", (id) => {
      this.bookid = id;
      this.$store.commit("bookid", id);
    });
  },
};
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
#head {
  border-bottom: 1px solid black;
  margin-top: 10px;
  display: flex;
  justify-content: center;
  height: 50vh;
}
#headl {
  width: 300px;
  margin-top: 40px;
}
#headr {
  width: 500px;
}
#headr .el-button {
  width: 100px;
  height: 40px;
}
#head li {
  margin-top: 20px;
}
#back {
  border-bottom: solid 1px #000000;
  display: flex;
  justify-content: center;
  margin-top: 20px;
  height: 140vh;
}
#l {
  width: 850px;
  margin-left: 150px;
  margin-right: 100px;
}
#newcontent {
  border-bottom: 1px solid black;
  font-size: small;
  height: 30vh;
}
#newcontent li h5 {
  display: inline-block;
}
#newcontent li {
  margin-top: 10px;
}
#newr {
  margin-right: 150px;
  float: right;
}
#newl {
  float: left;
}
.sendtext {
  width: 400px;
  margin-top: 20px;
}
#fan {
  margin-top: 20px;
}
#r {
  float: right;
  padding-right: 50px;
}
#introduce div {
  margin-top: 30px;
}
.name span {
  margin-left: 10px;
}
.number span {
  margin-left: 50px;
}
</style>
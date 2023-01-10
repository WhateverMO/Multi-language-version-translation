<template>
  <div>
    <ul>
      <li>
        图书名字：<el-input
          v-model="bookname"
          placeholder="请输入图书名字"
        ></el-input>
      </li>
      <li>
        作品类型：<el-select
          v-model="bookclass"
          ref="bookclass"
          placeholder="请选择"
        >
          <el-option
            v-for="item in kind"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </li>
      <li>
        语言种类：<el-select
          v-model="booklang"
          ref="booklang"
          placeholder="请选择"
        >
          <el-option
            v-for="item in lang"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </li>
      <li>
        作品简介:<el-input
          type="textarea"
          :rows="2"
          placeholder="请输入内容"
          v-model="bookintro"
        >
        </el-input>
      </li>
      <li><el-button type="primary" @click="write">创建图书</el-button></li>
    </ul>
  </div>
</template>

<script>
import qs from "qs";
import axios from "axios";
export default {
  data() {
    return {
      kind: [
        {
          value: "1",
          label: "新闻",
        },
        {
          value: "2",
          label: "小说",
        },
        {
          value: "3",
          label: "历史",
        },
        {
          value: "4",
          label: "冒险",
        },
        {
          value: "5",
          label: "悬疑",
        },
        {
          value: "6",
          label: "爱情",
        },
        {
          value: "7",
          label: "恐怖",
        },
      ],
      lang: [
        {
          value: "1",
          label: "中文",
        },
        {
          value: "2",
          label: "英语",
        },
        {
          value: "3",
          label: "德语",
        },
        {
          value: "4",
          label: "法语",
        },
        {
          value: "5",
          label: "日语",
        },
        {
          value: "6",
          label: "韩语",
        },
      ],
      bookname: "",
      bookintro: "",
      bookclass: "",
      booklang: "",
    };
  },
  methods: {
    write() {
      var data = {
        name: this.bookname,
        lang_id: this.$refs.booklang.selected.value,
        book_desc: this.bookintro,
        bc_id: this.$refs.bookclass.selected.value,
      };
      const path = "http://localhost:5000/api/author/add_books_index";
      axios.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          alert("你的图书编号是" + res.data.book_id);
          setTimeout(() => {
            this.$bus.$emit("createid", res.data.book_id);
          }, 1000);
          this.$router.push("/write");
        }
      });
    },
  },
};
</script>

<style scoped>
ul {
  margin-top: 30px;
  margin-left: 40vw;
  height: 70vh;
}
ul li {
  /* display: flex;
    justify-content: center; */
  margin-bottom: 45px;
}
.el-input {
  width: 150px;
}
.el-button {
  margin-left: 5vw;
}

.el-textarea {
  width: 250px;
}
</style>

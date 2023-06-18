<template>
  <div class="all">
    <div class="first">
      <ul>
        <li>图书名字：{{ books.book_name }}</li>
        <li>作品类型：{{ books.book_class }}</li>
        <li>语言种类：{{ books.lang_name }}</li>
        <li>作品简介:{{ books.book_desc }}</li>
      </ul>
    </div>
    <div class="new">
      <ul>
        <li>
          图书名字：<el-input
            v-model="translatename"
            placeholder="请输入图书名字"
          ></el-input>
        </li>
        <li>
          作品类型：<el-select
            v-model="translateclass"
            ref="translateclass"
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
            v-model="translatelang"
            ref="translatelang"
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
            v-model="translateintro"
          >
          </el-input>
        </li>
        <li><el-button type="primary" @click="write">开始翻译</el-button></li>
      </ul>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import request from "@/request";
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
      translatename: "", //翻译之后
      translateintro: "",
      translateclass: "",
      translatelang: "",
      transbook: "", //翻译之前
      books: {},
    };
  },
  methods: {
    write() {
      var data = {
        name: this.translatename,
        //语言id
        new_lang_id: this.$refs.translatelang.selected.value,
        //简介
        book_describe: this.translateintro,
        //类型id
        bc_id: this.$refs.translateclass.selected.value,
      };
      const path = "api/author/translate_option/" + this.transbook;
      request.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          sessionStorage.setItem(
            "langid",
            this.$refs.translatelang.selected.value
          );
          sessionStorage.setItem("contentno", 1);
          sessionStorage.setItem("newstanslate", res.data.new_book_id);
          this.$router.push("/translation");
        }
      }); //post带参数
    },
  },
  mounted() {
    this.transbook = sessionStorage.getItem("transbook");
    request
      .get("/api/author/translate_option/" + this.transbook)
      .then((res) => {
        this.books = res.data;
      });
  },
};
</script>

<style scoped>
.all {
  display: flex;
  height: 60vh;
  margin-top: 10vh;
}
.new li {
  margin-bottom: 25px;
}
.new {
  margin-left: 10vw;
}
.first li {
  margin-bottom: 50px;
}
.first {
  margin-top: 20px;
  width: 400px;
  margin-left: 20vw;
  letter-spacing: 2px;
}
.el-input {
  width: 150px;
}
.el-textarea {
  width: 250px;
}
.el-button {
  width: 200px;
}
</style>

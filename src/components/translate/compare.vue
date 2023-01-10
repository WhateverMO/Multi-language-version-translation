<template>
  <div class="all">
    <div class="first">
      <ul>
        <li>图书名字：{{ firstname }}</li>
        <li>作品类型：{{ firstclass }}</li>
        <li>语言种类：{{ firstlang }}</li>
        <li>作品简介:{{ firstintro }}</li>
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
      translatename: "",
      translateintro: "",
      translateclass: "",
      translatelang: "", //翻译之后
      firstname: "",
      firstlang: "",
      firstintro: "",
      firstclass: "", //原始版本的书的信息
      firstlangid: "",
      firstbookid: "", //翻译之后
    };
  },
  methods: {
    write() {
      var data = {
        name: this.translatename,
        new_lang_id: this.$refs.translatelang.selected.value,
        book_desc: this.translateintro,
        bc_id: this.$refs.translateclass.selected.value,
        lang_id: this.fristlangid,
      };
      const path =
        "http://localhost:5000/api/author/translate_option/" +
        this.$store.state.firstbookid;
      axios.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
        if (res.data.code == 200) {
          this.$store.commit("translatebookid", res.data.new_book_id);
          this.$router.push("/translation");
        }
      }); //post带参数
    },
  },
  mounted() {
    this.$bus.$on("first", (first) => {
      this.firstname = first.book_name;
      this.firstclass = first.book_class;
      this.firstintro = first.book_desc;
      this.firstlang = first.lang_name;
      this.firstlangid = first.lang_id;
    });
  },
};
</script>

<style scoped>
.all {
  display: flex;
  justify-content: space-around;
  height: 60vh;
  margin-top: 10vh;
}
.new li {
  margin-bottom: 25px;
}
.first li {
  margin-bottom: 70px;
}
.first {
  width: 700px;
}
.el-input {
  width: 150px;
}
.el-textarea {
  width: 250px;
}
</style>

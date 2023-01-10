<template>
  <div class="all">
    <ul class="first">
      <li id="section">
        <el-select v-model="contentno" ref="contentno" placeholder="请选择">
          <el-option
            @click.native="change"
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </li>
      <li id="name">{{ title }}</li>

      <li id="content">
        <textarea rows="30" cols="70">{{ content }}</textarea>
      </li>
    </ul>
    <ul class="translate">
      <li>
        章节名字：<el-input
          v-model="translatetitle"
          placeholder="请输入图书名字"
        ></el-input>
      </li>
      <li id="content">
        <textarea rows="30" cols="70" v-model="translatecontent"></textarea>
      </li>
      <li id="button">
        <el-button type="primary" @click="hand">上传作品</el-button>
        <el-button type="primary">保存作品</el-button>
      </li>
    </ul>
  </div>
</template>

<script>
import qs from "qs";
import axios from "axios";
export default {
  data() {
    return {
      options: [
        {
          value: "1",
          label: "第一章",
        },
        {
          value: "2",
          label: "第二章",
        },
        {
          value: "3",
          label: "第三章",
        },
        {
          value: "4",
          label: "第四章",
        },
        {
          value: "5",
          label: "第五章",
        },
      ],
      content: "",
      title: "",
      contentno: "1",
      translatetitle: "",
      translatecontent: "",
    };
  },
  mounted() {
    axios
      .get(
        "http://localhost:5000/api/author/translate/" +
          this.$store.state.firstbookid +
          "/" +
          this.$store.state.translatebookid +
          "/" +
          1
      )
      .then((res) => {
        this.content = res.data.content;
        this.title = res.data.title;
      }); //拿最初版本书的第一章内容
  },
  methods: {
    hand() {
      var data = {
        text: this.translatecontent,
        title: this.translatetitle,
        contentnum: this.$refs.contentno.selected.value,
      };
      const path =
        "http://localhost:5000/api/author/translate/" +
        this.$store.state.firstbookid +
        "/" +
        this.$store.state.translatebookid +
        "/" +
        this.$refs.contentno.selected.value;
      axios.post(path, qs.stringify(data)).then((res) => {
        alert(res.data.msg);
      }); //post提交新翻译的内容
    },
    change() {
      axios
        .get(
          "http://localhost:5000/api/author/translate/" +
            this.$store.state.firstbookid +
            "/" +
            this.$store.state.translatebookid +
            "/" +
            this.$refs.contentno.selected.value
        )
        .then((res) => {
          this.content = res.data.content;
          this.title = res.data.title;
        }); //拿最初版本书的第一章内容
    },
  },
};
</script>

<style scoped>
.all {
  height: 80vh;
  display: flex;
  justify-content: space-around;
  margin-top: 5vh;
}
textarea {
  background-color: transparent;
}
#name {
  margin-left: 10vw;
}
#all2 {
  margin-top: 8vh;
}
.el-button {
  margin-left: 50px;
}
</style>
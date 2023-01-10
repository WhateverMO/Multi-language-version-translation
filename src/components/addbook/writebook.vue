<template>
  <div class="all">
    <div>
      <el-radio-group v-model="isCollapse" style="margin-bottom: 20px">
        <el-radio-button :label="false">展开</el-radio-button>
        <el-radio-button :label="true">收起</el-radio-button>
      </el-radio-group>
      <el-menu
        default-active="1-4-1"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        :collapse="isCollapse"
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-reading"></i>
            <span slot="title">已发布</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="1-1">选项1</el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-edit"></i>
            <span slot="title">草稿箱</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-delete-solid"></i>
            <span slot="title">回收站</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="3-1">选项1</el-menu-item>
            <el-menu-item index="3-2">选项2</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="4">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span slot="title">创建新章节</span>
          </template>
        </el-submenu>
      </el-menu>
    </div>
    <div>
      <el-drawer
        title="作家的话"
        :visible.sync="drawer"
        :direction="direction"
        :before-close="Close"
      >
        <textarea
          name=""
          id=""
          cols="60"
          rows="35"
          placeholder="在此输入正文"
        ></textarea>
        <el-button
          @click="drawer = true"
          type="primary"
          style="margin-left: 16px"
        >
          保存
        </el-button>
      </el-drawer>
    </div>

    <div class="center">
      <div>
        <el-input v-model="contentno" placeholder="请输入章节号"></el-input>
      </div>
      <div>
        <el-input v-model="title" placeholder="请输入章节名"></el-input>
      </div>
      <div>
        <textarea
          name=""
          id=""
          cols="120"
          rows="30"
          v-model="content"
          placeholder="在此输入正文"
        ></textarea>
      </div>
      <div class="choose">
        <el-button
          @click="drawer = true"
          type="primary"
          style="margin-left: 16px"
        >
          添加作家的话
        </el-button>
        <el-button type="primary" style="margin-left: 16px"> 保存 </el-button>
        <el-button type="primary" style="margin-left: 16px" @click="hand">
          发布
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import qs from "qs";
import axios from "axios";
export default {
  data() {
    return {
      drawer: false,
      direction: "rtl",
      isCollapse: true,
      title: "",
      content: "",
      contentno: "",
      newbookid: "",
    };
  },
  methods: {
    Close(done) {
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    hand() {
      var data = {
        content: this.content,
        title: this.title,
      };
      console.log(this.newbookid);
      axios
        .post(
          "http://localhost:5000/api/author/addbooks/" +
            this.newbookid +
            "/" +
            this.contentno,
          qs.stringify(data)
        )
        .then((res) => {
          alert(res.data.msg);
        }); //post带参数的登录请求
    },
  },
  mounted() {
    this.$bus.$on("createid", (newid) => {
      this.newbookid = newid;
    });
  },
};
</script>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.all {
  display: flex;
  justify-content: space-between;
}
.center {
  margin-right: 20vw;
}
.center div {
  margin-bottom: 10px;
}
</style>
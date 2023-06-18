<template>
  <div class="all">
    <div id="l">
      <img :src="$store.state.image" alt="" width="200px" height="200px" />
      <div class="intro">
        <span @click="attention">我的关注</span><span>我的喜欢</span
        ><span @click="collect">我的收藏</span>
      </div>
      <div class="num">
        <span>{{ this.attentionlength }}</span
        ><span>0</span><span>{{ this.collectlength }}</span>
      </div>
    </div>
    <div id="c">
      <div>
        用户名:<span>{{ $store.state.name }}</span>
      </div>
      <div>
        账号:<span>{{ $store.state.id }}</span>
      </div>
      <div>
        性别:<span>{{ $store.state.sex }}</span>
      </div>
      <div>
        年龄:<span>{{ $store.state.age }}</span>
      </div>
      <div>
        地区:<span>{{ $store.state.place }}</span>
      </div>
      <div>
        个人介绍: <span class="pintro">{{ $store.state.intro }}</span>
      </div>
      <el-button type="primary" @click="check" class="bt"
        >修改个人信息</el-button
      >
    </div>
  </div>
</template>

<script>
import request from "@/request";
export default {
  data() {
    return {
      collectlength: 0,
      attentionlength: 0,
    };
  },
  methods: {
    check() {
      this.$router.push("/checkinformation");
    },
    collect() {
      this.$router.push("/collect");
    },
    attention() {
      this.$router.push("/attention");
    },
  },
  mounted() {
    request.get("/api/user/information").then((res) => {
      console.log(res.data);
      this.attentionlength = res.data.following_count;
      this.collectlength = res.data.collect_count;
      this.$store.commit("name", res.data.username);
      this.$store.commit("sex", res.data.user_gender);
      this.$store.commit("place", res.data.user_area);
      this.$store.commit("intro", res.data.user_describe);
      this.$store.commit("age", res.data.user_age);
      this.$store.commit("id", res.data.user_id);
      this.$store.commit("image", res.data.user_avatar);
    }); //给session发请求拿用户信息
  },
};
</script>

<style scoped>
.all {
  display: flex;
  justify-content: center;
  margin-top: 50px;
  margin-bottom: 50px;
  margin-left: 200px;
}
#c {
  margin-left: 150px;
}
#c div {
  margin-bottom: 20px;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  font-size: 17px;
}
#c span {
  margin-left: 15px;
}
img {
  border-radius: 50%;
  border: black solid 1px;
  object-fit: cover;
}
.bt {
  width: 200px;
}
.intro {
  margin-top: 20px;
}
.num {
  margin-top: 10px;
}
.intro span {
  margin-right: 10px;
}
.intro :hover {
  cursor: pointer;
  color: red;
}
.num span {
  padding-left: 20px;
  padding-right: 50px;
}
.pintro {
  width: 400px;
  display: inline-block;
}
</style>
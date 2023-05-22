<template>
  <div>
    <div id="c3">
      <h2>我的作品</h2>
      <el-table :data="tableData" border style="width: 80%">
        <el-table-column prop="date" label="创作时间" width="180">
        </el-table-column>
        <el-table-column prop="name" label="书名" width="150">
        </el-table-column>
        <el-table-column prop="introduce" label="简介"> </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          name: "蘑菇圈",
          introduce:
            "包括《蘑菇圈》和《三只虫草》两部小说。作品延续阿来一贯擅长描写的主题：辽阔神秘的藏区、复杂闪光的人性、以及古老与现代的拉扯平衡。两部故事分别从藏区物产入手展开故事，将主角的命运与荒诞的时代连接，即使现实的压力从未停歇，人性中纯净的力量依然像蘑菇一样生机勃勃，随时破土而出。文字流畅易读，回味悠长。",
          date: "2016-05-02",
        },
        {
          name: "妖怪谈义",
          introduce:
            "柳田国男，日本现代民俗学奠基人，妖怪学者。其著作《远野物语》《妖怪谈义》《日本的传说》等对日本民俗学、妖怪学产生了深远影响。周作人曾深受柳田民俗学思想的影响，成为中国民俗学研究的开拓者。本书汇集柳田国男不同时期的妖怪研究学术著作，通过传说对比、分类神怪、探寻源流，深入分析了日本独特的妖怪文化，是柳田国男晚年集大成之作",
          date: "2016-05-02",
        },
      ],
    };
  },
};
</script > 

<style scoped>
#c3 h2 {
  text-align: center;
}

#c3 {
  margin-left: 45vh;
}
</style>